#!/usr/bin/env python3
"""Deterministic, read-only static validation for QA Skills Hub."""
from __future__ import annotations

import fnmatch
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

STATUSES = {"PASS", "FAIL", "BLOCKED", "HUMAN_APPROVAL_REQUIRED"}
NAMESPACES = {"agents", "commands", "constitution", "docs", "policies", "routing", "skills", "standards", "templates", "third-party", "validation", "workflows", "scripts", ".github"}
ROOT_DOCS = {"AGENTS.md", "CLAUDE.md", "CODEX.md", "README.md", "SKILL_INDEX.md"}
CASE_FILES = (
    "validation/compatibility-test-cases.md",
    "validation/human-gate-test-cases.md",
    "validation/leakage-test-cases.md",
    "validation/orchestration-acceptance-tests.md",
    "validation/routing-test-cases.md",
)
APPROVED_INFRA = {"scripts/validate_repository.py", ".github/workflows/static-validation.yml"}
EXECUTABLE_CASE_FIELDS = ("Input",)

class ConfigError(RuntimeError):
    pass

@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    check_id: str
    severity: str
    message: str
    def render(self) -> str:
        return f"[{self.severity}] {self.check_id} {self.path}:{self.line} {self.message}"

@dataclass
class Case:
    path: str
    heading: str
    heading_line: int
    fields: dict[str, str]
    lines: dict[str, int]

class Validator:
    def __init__(self) -> None:
        self.root = Path(__file__).resolve().parents[1]
        self.findings: list[Finding] = []
        self.cache: dict[str, str] = {}
        self.tracked = self.git_files()
        self.markdown = tuple(p for p in self.tracked if p.lower().endswith(".md"))
        self.cases: list[Case] = []
        self.required_fields: tuple[str, ...] = ()
        self.gate_levels: set[int] = set()

    @staticmethod
    def norm(value: str) -> str:
        value = value.replace("\\", "/")
        while value.startswith("./"):
            value = value[2:]
        return str(PurePosixPath(value))

    def git_files(self) -> tuple[str, ...]:
        try:
            proc = subprocess.run(["git", "ls-files", "-z"], cwd=self.root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            raw = proc.stdout.decode("utf-8")
        except (OSError, subprocess.CalledProcessError, UnicodeError) as exc:
            raise ConfigError("unable to enumerate tracked repository files") from exc
        return tuple(sorted({self.norm(p) for p in raw.split("\0") if p}))

    def text(self, path: str) -> str:
        path = self.norm(path)
        if path not in self.cache:
            target = self.root.joinpath(*PurePosixPath(path).parts)
            try:
                with target.open("r", encoding="utf-8", newline=None) as handle:
                    self.cache[path] = handle.read()
            except (OSError, UnicodeError) as exc:
                raise ConfigError(f"unable to read required UTF-8 text file: {path}") from exc
        return self.cache[path]

    def tracked_text(self, path: str) -> str | None:
        path = self.norm(path)
        if path in self.cache:
            return self.cache[path]
        target = self.root.joinpath(*PurePosixPath(path).parts)
        try:
            data = target.read_bytes()
        except OSError as exc:
            raise ConfigError(f"unable to read tracked file: {path}") from exc
        if b"\0" in data:
            return None
        try:
            value = data.decode("utf-8")
        except UnicodeError:
            return None
        if any(ord(char) < 32 and char not in "\t\n\r\f" for char in value):
            return None
        value = value.replace("\r\n", "\n").replace("\r", "\n")
        self.cache[path] = value
        return value

    def add(self, check: str, path: str, line: int, message: str, severity: str = "ERROR") -> None:
        self.findings.append(Finding(self.norm(path), max(1, line), check, severity, message))

    @staticmethod
    def line(text: str, offset: int) -> int:
        return text.count("\n", 0, offset) + 1

    @staticmethod
    def section(text: str, heading: str) -> tuple[str, int]:
        match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE | re.IGNORECASE)
        if not match:
            return "", 1
        start = match.end()
        next_heading = re.search(r"^## ", text[start:], re.MULTILINE)
        end = start + next_heading.start() if next_heading else len(text)
        return text[start:end], text.count("\n", 0, start) + 1

    @staticmethod
    def refs(value: str) -> list[str]:
        return re.findall(r"`((?:commands|workflows|agents|skills|policies|constitution|routing|standards|validation|templates|docs|third-party|scripts|\.github)/[^`]+)`", value)

    def load_config(self) -> None:
        readme = self.text("validation/README.md")
        schema = re.search(r"Every validation case uses this format:\s*```text\s*(.*?)```", readme, re.DOTALL)
        if not schema:
            raise ConfigError("validation case schema is missing from validation/README.md")
        fields = re.findall(r"^([A-Za-z][A-Za-z -]+):\s*$", schema.group(1), re.MULTILINE)
        if not fields:
            raise ConfigError("validation case schema has no required fields")
        self.required_fields = tuple(fields)
        policy = self.text("policies/human-gate-policy.md")
        self.gate_levels = {int(n) for n in re.findall(r"^- Level (\d+):", policy, re.MULTILINE)}
        if not self.gate_levels:
            raise ConfigError("Human Gate policy defines no numeric levels")
        for path in CASE_FILES:
            text = self.text(path)
            headings = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
            for index, heading in enumerate(headings):
                start = heading.end()
                end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
                block = text[start:end]
                if not re.search(r"^ID:\s*\S+", block, re.MULTILINE):
                    continue
                values: dict[str, str] = {}
                lines: dict[str, int] = {}
                for field in re.finditer(r"^([A-Za-z][A-Za-z -]+):\s*(.*?)\s*$", block, re.MULTILINE):
                    values[field.group(1)] = field.group(2)
                    lines[field.group(1)] = self.line(text, start + field.start())
                self.cases.append(Case(path, heading.group(1), self.line(text, heading.start()), values, lines))
        if not self.cases:
            raise ConfigError("no validation cases were discovered")

    def path_exists(self, reference: str, source: str) -> bool:
        raw = reference.strip().replace("\\", "/").split("#", 1)[0].split("?", 1)[0].rstrip(".,;:")
        if not raw or "<" in raw or ">" in raw:
            return True
        parent = PurePosixPath(source).parent
        if raw in ROOT_DOCS:
            candidate = PurePosixPath(raw)
        else:
            candidate = parent.joinpath(PurePosixPath(raw)) if raw.startswith(("./", "../")) or "/" not in raw else PurePosixPath(raw)
        normalized = self.norm(str(candidate))
        if normalized.startswith("../"):
            return False
        if any(char in normalized for char in "*?["):
            return any(fnmatch.fnmatch(path, normalized) for path in self.tracked)
        return self.root.joinpath(*PurePosixPath(normalized).parts).exists()

    def recognized(self, reference: str) -> bool:
        raw = reference.strip().replace("\\", "/")
        if not raw or "<" in raw or ">" in raw or " " in raw:
            return False
        first = raw.lstrip("./").split("/", 1)[0]
        return first in NAMESPACES or raw in ROOT_DOCS or ("/" not in raw and raw.endswith(".md"))

    @staticmethod
    def cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    def routing_rows(self) -> list[tuple[int, list[str]]]:
        text = self.text("routing/skill-routing-rules.md")
        section, start = self.section(text, "Command routing map")
        rows = []
        for number, raw in enumerate(section.splitlines(), start=start):
            if not raw.strip().startswith("|"):
                continue
            cells = self.cells(raw)
            if len(cells) != 4 or cells[0] == "Command" or set(cells[0]) <= {"-", ":"}:
                continue
            rows.append((number, cells))
        return rows

    def canonical_commands(self) -> list[str]:
        return sorted(p for p in self.tracked if re.fullmatch(r"commands/qa-[a-z0-9-]+\.md", p, re.IGNORECASE))

    def canonical_agents(self) -> list[str]:
        section, _ = self.section(self.text("AGENTS.md"), "Canonical Agents")
        return sorted({self.norm(p) for p in re.findall(r"`(agents/[^`]+\.md)`", section)})

    def process(self, path: str) -> tuple[str, int]:
        return self.section(self.text(path), "Process")

    def compatibility_commands(self) -> list[str]:
        canonical = set(self.canonical_commands())
        return sorted(p for p in self.tracked if p.startswith("commands/") and p.endswith(".md") and p not in canonical)

    def compatibility_agents(self) -> list[str]:
        canonical = set(self.canonical_agents())
        return sorted(p for p in self.tracked if p.startswith("agents/") and p.endswith(".md") and p not in canonical)

    def s4_001(self) -> None:
        for path in self.markdown:
            text = self.text(path)
            for match in re.finditer(r"`([^`\n]+)`", text):
                ref = match.group(1)
                if self.recognized(ref) and not self.path_exists(ref, path):
                    self.add("S4-001", path, self.line(text, match.start()), "recognized repository reference does not resolve")

    def s4_002(self) -> None:
        seen: dict[str, int] = {}
        actual: set[str] = set()
        for line, cells in self.routing_rows():
            command_refs = self.refs(cells[0])
            if len(command_refs) != 1:
                self.add("S4-002", "routing/skill-routing-rules.md", line, "routing row must contain one canonical command path")
                continue
            command = self.norm(command_refs[0])
            key = command.casefold()
            actual.add(key)
            if key in seen:
                self.add("S4-002", "routing/skill-routing-rules.md", line, "canonical command has more than one routing row")
            seen[key] = line
            for index, namespace in ((1, "workflows/"), (2, "agents/"), (3, "skills/")):
                refs = [ref for ref in self.refs(cells[index]) if ref.startswith(namespace)]
                if not refs and index != 3:
                    self.add("S4-002", "routing/skill-routing-rules.md", line, f"routing row is missing a {namespace[:-1]} path")
                for ref in refs:
                    if not self.path_exists(ref, "routing/skill-routing-rules.md"):
                        self.add("S4-002", "routing/skill-routing-rules.md", line, f"routing row contains an unresolved {namespace[:-1]} path")
        expected = {p.casefold() for p in self.canonical_commands()}
        for missing in sorted(expected - actual):
            self.add("S4-002", "routing/skill-routing-rules.md", 1, f"canonical command is missing from routing table: {missing}")
        for extra in sorted(actual - expected):
            self.add("S4-002", "routing/skill-routing-rules.md", seen.get(extra, 1), f"routing table command is not canonical: {extra}")

    def s4_003(self) -> None:
        for path in self.compatibility_commands():
            process, start = self.process(path)
            orchestrator = process.find("`agents/qa-orchestrator.md`")
            if orchestrator < 0:
                self.add("S4-003", path, start, "compatibility command process does not route through the QA Orchestrator")
                continue
            for match in re.finditer(r"`((?:commands/qa-|workflows/|agents/|skills/)[^`]+)`", process):
                if match.group(1) != "agents/qa-orchestrator.md" and match.start() < orchestrator:
                    self.add("S4-003", path, start + process.count("\n", 0, match.start()), "compatibility execution precedes QA Orchestrator routing")

    def s4_004(self) -> None:
        canonical_agents = set(self.canonical_agents())
        for path in self.compatibility_commands() + self.compatibility_agents():
            process, start = self.process(path)
            skills = list(re.finditer(r"`skills/[^`]+`", process))
            if not skills:
                continue
            delegations = [m.start() for m in re.finditer(r"`((?:workflows|agents)/[^`]+)`", process) if m.group(1).startswith("workflows/") or m.group(1) in canonical_agents]
            first = min(delegations) if delegations else None
            for skill in skills:
                if first is None or skill.start() < first:
                    self.add("S4-004", path, start + process.count("\n", 0, skill.start()), "compatibility process invokes a skill before workflow or canonical-agent delegation")

    def s4_005(self) -> None:
        path = "validation/README.md"
        text = self.text(path)
        definitions_section, _ = self.section(text, "Result Definitions")
        definitions = {m.group(1) for m in re.finditer(r"^([A-Z][A-Z_]+):\s+", definitions_section, re.MULTILINE)}
        if definitions != STATUSES:
            self.add("S4-005", path, 1, "terminal status definitions do not match the allowed vocabulary")
        handoff_path = "standards/agent-handoff-standard.md"
        handoff = self.text(handoff_path)
        match = re.search(r"status:\s*\"<([^\"]+)>\"", handoff)
        values = set(match.group(1).split("|")) if match else set()
        if values != STATUSES:
            self.add("S4-005", handoff_path, 1, "handoff terminal status vocabulary is incomplete or unsupported")
        for case in self.cases:
            for field in ("Human Gate", "Expected output"):
                value = re.sub(r"<[^>]+>", "", case.fields.get(field, ""))
                for token in re.findall(r"\b[A-Z][A-Z_]{3,}\b", value):
                    if token not in STATUSES:
                        self.add("S4-005", case.path, case.lines.get(field, case.heading_line), "explicit terminal status is not supported")
    def s4_006(self) -> None:
        exact: dict[str, tuple[str, int]] = {}
        folded: dict[str, str] = {}
        for case in self.cases:
            case_id = case.fields.get("ID", "").strip()
            for field in self.required_fields:
                if not case.fields.get(field, "").strip():
                    self.add("S4-006", case.path, case.heading_line, f"validation case is missing required field: {field}")
            if not case_id:
                continue
            if case_id not in case.heading:
                self.add("S4-006", case.path, case.heading_line, "validation case heading does not contain its ID")
            if case_id in exact:
                self.add("S4-006", case.path, case.lines.get("ID", case.heading_line), "validation case ID is duplicated")
            exact[case_id] = (case.path, case.heading_line)
            key = case_id.casefold()
            if key in folded and folded[key] != case_id:
                self.add("S4-006", case.path, case.lines.get("ID", case.heading_line), "validation case ID collides case-insensitively")
            folded[key] = case_id

    def s4_007(self) -> None:
        baseline = "policies/no-product-specific-leakage.md"
        for case in self.cases:
            value = case.fields.get("Required policies", "")
            line = case.lines.get("Required policies", case.heading_line)
            policies = [self.norm(p) for p in self.refs(value) if p.startswith("policies/")]
            if not policies:
                self.add("S4-007", case.path, line, "required-policy declaration is empty")
                continue
            keys = [p.casefold() for p in policies]
            if len(keys) != len(set(keys)):
                self.add("S4-007", case.path, line, "required-policy declaration contains a duplicate path")
            if baseline not in policies:
                self.add("S4-007", case.path, line, "required-policy declaration omits the product-leakage baseline")
            for policy in policies:
                if not self.path_exists(policy, case.path):
                    self.add("S4-007", case.path, line, "required-policy declaration contains an unresolved policy path")

    def s4_008(self) -> None:
        paths = set(CASE_FILES) | {"standards/agent-handoff-standard.md", "policies/human-gate-policy.md"}
        for path in sorted(paths):
            text = self.text(path)
            for match in re.finditer(r"\bLevel\s+(\d+)\b", text):
                if int(match.group(1)) not in self.gate_levels:
                    self.add("S4-008", path, self.line(text, match.start()), "Human Gate decision uses an undocumented numeric level")
        handoff = self.text("standards/agent-handoff-standard.md")
        for match in re.finditer(r"^\s*level:\s*(\d+)\s*$", handoff, re.MULTILINE):
            if int(match.group(1)) not in self.gate_levels:
                self.add("S4-008", "standards/agent-handoff-standard.md", self.line(handoff, match.start()), "handoff uses an undocumented Human Gate level")

    def s4_009(self) -> None:
        edit_capable = re.compile(
            r"\b(?:"
            r"implement(?:s|ed|ing|ation|ations)?|"
            r"modif(?:y|ies|ied|ying|ication|ications)|"
            r"edit(?:s|ed|ing)?|"
            r"updat(?:e|es|ed|ing)|"
            r"chang(?:e|es|ed|ing)|"
            r"refactor(?:s|ed|ing)?|"
            r"delet(?:e|es|ed|ing|ion|ions)|"
            r"remov(?:e|es|ed|ing|al|als)|"
            r"dependenc(?:y|ies)|packages?|"
            r"install(?:s|ed|ing|ation|ations)?|"
            r"configur(?:e|es|ed|ing)|"
            r"configurations?|"
            r"(?:ci(?:/cd)?|workflows?)\s+(?:changes?|updates?|edits?|modifications?|configuration)"
            r")\b",
            re.IGNORECASE,
        )
        documentation_only = re.compile(
            r"\b(?:(?:implementation|dependenc(?:y|ies)|packages?|configuration|ci(?:/cd)?|workflows?)\s+"
            r"(?:documentation|examples?|guidance|overview|plans?|planning|decisions?|recommendations?|references?|context)|configuration\s+details?)\b",
            re.IGNORECASE,
        )
        audit = "policies/audit-before-edit.md"
        for case in self.cases:
            executable = " ".join(case.fields.get(field, "") for field in EXECUTABLE_CASE_FIELDS)
            executable = documentation_only.sub("", executable)
            if edit_capable.search(executable) and audit not in self.refs(case.fields.get("Required policies", "")):
                self.add("S4-009", case.path, case.lines.get("Required policies", case.heading_line), "edit-capable validation case omits audit-before-edit policy")

    @staticmethod
    def heading(text: str, suffix: str) -> str:
        match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        value = match.group(1) if match else ""
        value = re.sub(rf"\s+{re.escape(suffix)}$", "", value, flags=re.IGNORECASE)
        return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")

    def s4_010(self) -> None:
        stems: dict[str, str] = {}
        headings: dict[str, str] = {}
        routes: dict[str, int] = {}
        for path in self.canonical_commands():
            stem = PurePosixPath(path).stem.casefold()
            if stem in stems:
                self.add("S4-010", path, 1, "canonical command filename stem collides case-insensitively")
            stems[stem] = path
            heading = self.heading(self.text(path), "Command")
            if not heading:
                self.add("S4-010", path, 1, "canonical command heading is missing")
            elif heading in headings:
                self.add("S4-010", path, 1, "canonical command heading collides case-insensitively")
            headings[heading] = path
        for line, cells in self.routing_rows():
            refs = self.refs(cells[0])
            if not refs:
                continue
            identity = PurePosixPath(refs[0]).stem.casefold()
            if identity in routes:
                self.add("S4-010", "routing/skill-routing-rules.md", line, "routing-table command identity is duplicated")
            routes[identity] = line

    def s4_011(self) -> None:
        paths: dict[str, str] = {}
        headings: dict[str, str] = {}
        for path in self.canonical_agents():
            key = path.casefold()
            if key in paths:
                self.add("S4-011", "AGENTS.md", 1, "canonical agent path collides case-insensitively")
            paths[key] = path
            if not self.path_exists(path, "AGENTS.md"):
                self.add("S4-011", "AGENTS.md", 1, "canonical agent path does not resolve")
                continue
            heading = self.heading(self.text(path), "Agent")
            if not heading:
                self.add("S4-011", path, 1, "canonical agent heading is missing")
            elif heading in headings:
                self.add("S4-011", path, 1, "canonical agent heading collides case-insensitively")
            headings[heading] = path
        for path in self.compatibility_agents():
            if self.heading(self.text(path), "Agent") in headings:
                self.add("S4-011", path, 1, "compatibility agent collides with a canonical agent heading")

    def s4_012(self) -> None:
        pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
        for path in self.markdown:
            text = self.text(path)
            for match in pattern.finditer(text):
                target = match.group(1).strip().split()[0].strip("<>")
                if target.startswith(("http" + "://", "https" + "://", "mailto:", "#")):
                    continue
                if self.recognized(target) and not self.path_exists(target, path):
                    self.add("S4-012", path, self.line(text, match.start()), "recognized local Markdown link does not resolve")
    def s4_013(self) -> None:
        patterns = (
            ("real URL", re.compile(r"https?://[^\s<>)\]`]+", re.IGNORECASE)),
            ("personal email-like value", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)),
            ("credential or secret assignment", re.compile(r"\b(?:password|token|api[_ -]?key|secret|credential)\b\s*[:=]\s*(?![<\[])['\"]?[A-Za-z0-9][^\s,;]*", re.IGNORECASE)),
            ("private-key marker", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----")),
            ("non-placeholder IPv4 value", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
            ("real selector assignment", re.compile(r"\b(?:selector|locator)\b\s*[:=]\s*['\"](?:#|\.)[A-Za-z][^'\"]+['\"]", re.IGNORECASE)),
            ("customer-specific identifier assignment", re.compile(r"\bcustomer[_ -]?id\b\s*[:=]\s*(?!<)['\"]?[A-Za-z0-9][A-Za-z0-9_-]{5,}", re.IGNORECASE)),
        )
        for path in self.tracked:
            text = self.tracked_text(path)
            if text is None:
                continue
            for category, pattern in patterns:
                for match in pattern.finditer(text):
                    self.add("S4-013", path, self.line(text, match.start()), f"prohibited {category} detected; matched value redacted")

    @staticmethod
    def chain(value: str) -> str:
        return " -> ".join(part.strip().rstrip(".") for part in value.strip().split("->"))

    def s4_014(self) -> None:
        constitution_path = "constitution/qa-agent-constitution.md"
        constitution = self.text(constitution_path)
        chain_pattern = re.compile(r"^\s*(Command\s*->.+?)\s*$", re.MULTILINE)
        chains = [self.chain(match.group(1)) for match in chain_pattern.finditer(constitution)]
        if len(chains) != 1:
            self.add("S4-014", constitution_path, 1, "Constitution must contain exactly one authoritative architecture chain")
            return
        authoritative = chains[0]
        authoritative_parts = authoritative.split(" -> ")
        normative_paths = (
            "README.md",
            "SKILL_INDEX.md",
            "validation/README.md",
            "validation/orchestration-acceptance-tests.md",
        )
        for path in normative_paths:
            text = self.text(path)
            declarations = list(chain_pattern.finditer(text))
            normalized = [self.chain(match.group(1)) for match in declarations]
            if authoritative not in normalized:
                self.add("S4-014", path, 1, "normative architecture declaration is missing")
            for match, declaration in zip(declarations, normalized):
                parts = declaration.split(" -> ")
                if parts != authoritative_parts[:len(parts)]:
                    self.add("S4-014", path, self.line(text, match.start()), "normative architecture declaration differs from the Constitution")
        for path in self.canonical_commands():
            process, start = self.process(path)
            orchestrator = process.find("`agents/qa-orchestrator.md`")
            if orchestrator < 0:
                self.add("S4-014", path, start, "canonical command process does not start through the QA Orchestrator")
                continue
            for match in re.finditer(r"`((?:workflows|agents|skills)/[^`]+)`", process):
                if match.group(1) != "agents/qa-orchestrator.md" and match.start() < orchestrator:
                    self.add("S4-014", path, start + process.count("\n", 0, match.start()), "workflow, agent, or skill execution precedes the QA Orchestrator")

    def s4_015(self) -> None:
        names = {"package.json", "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock", "pipfile.lock", "playwright.config.ts", "playwright.config.js", "pytest.ini", "tox.ini", "pyproject.toml", "requirements.txt"}
        directories = {"test", "tests", "e2e", "integration-tests", "consumer-tests"}
        binaries = {".exe", ".dll", ".so", ".dylib", ".jar", ".class", ".pyc", ".zip", ".png", ".jpg", ".jpeg", ".gif", ".pdf"}
        executable = ("*.spec.ts", "*.spec.js", "*.test.ts", "*.test.js", "test_*.py", "*_test.py")
        for path in self.tracked:
            if path in APPROVED_INFRA:
                continue
            pure = PurePosixPath(path)
            if {part.casefold() for part in pure.parts[:-1]} & directories:
                self.add("S4-015", path, 1, "tracked consumer test directory is prohibited in the hub")
            if pure.name.casefold() in names:
                self.add("S4-015", path, 1, "tracked framework configuration, manifest, or lockfile is prohibited in the hub")
            if pure.suffix.casefold() in binaries:
                self.add("S4-015", path, 1, "tracked binary artifact is unsupported in the hub")
            if any(fnmatch.fnmatch(pure.name.casefold(), pattern) for pattern in executable):
                self.add("S4-015", path, 1, "tracked runnable consumer test file is prohibited in the hub")

    def s4_016(self) -> None:
        validation_path = "validation/README.md"
        handoff_path = "standards/agent-handoff-standard.md"
        policy_path = "policies/human-gate-policy.md"
        validation = self.text(validation_path)
        handoff = self.text(handoff_path)
        policy = self.text(policy_path)
        requirements = (
            ("audit-before-edit", validation_path, validation),
            ("leakage checks", validation_path, validation),
            ("skills are selected only after routing", validation_path, validation),
            ("policies.audit_before_edit", handoff_path, handoff),
            ("policies.leakage_check_required", handoff_path, handoff),
            ("human_gate.level", handoff_path, handoff),
        )
        for phrase, path, text in requirements:
            if phrase.casefold() not in text.casefold():
                self.add("S4-016", path, 1, "shared validation/handoff concept is missing or inconsistent")
        levels = {int(n) for n in re.findall(r"^\s*level:\s*(\d+)\s*$", handoff, re.MULTILINE)}
        if not levels.issubset(self.gate_levels):
            self.add("S4-016", handoff_path, 1, "handoff Human Gate semantics differ from policy levels")
        if "BLOCKED" not in policy and "BLOCKED" not in handoff:
            self.add("S4-016", policy_path, 1, "prohibited-action BLOCKED semantics are not represented")

    def run(self) -> int:
        self.load_config()
        for check in (self.s4_001, self.s4_002, self.s4_003, self.s4_004, self.s4_005, self.s4_006, self.s4_007, self.s4_008, self.s4_009, self.s4_010, self.s4_011, self.s4_012, self.s4_013, self.s4_014, self.s4_015, self.s4_016):
            check()
        findings = sorted(set(self.findings))
        for finding in findings:
            print(finding.render())
        if findings:
            print(f"Repository validation failed with {len(findings)} finding(s).")
            return 1
        print("Repository validation passed.")
        return 0

def main() -> int:
    try:
        return Validator().run()
    except ConfigError as exc:
        print(f"[ERROR] INTERNAL <repository>:1 {exc}")
        return 2
    except Exception as exc:
        print(f"[ERROR] INTERNAL <validator>:1 internal failure ({type(exc).__name__})")
        return 2

if __name__ == "__main__":
    sys.exit(main())
