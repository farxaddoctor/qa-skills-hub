# QA Skills Hub

QA Skills Hub is an AI-native QA Agent Orchestration Architecture for reusable QA work across projects and coding agents. It coordinates commands, QA orchestration, constitution rules, policies, routing, workflows, agents, skills, audit checkpoints, and Human Gate approval before producing QA outputs.

Skills are part of this architecture, but they are not the starting point. User intent enters through commands, then routing selects the workflow, agent, and reusable capability modules needed for the task.

This repository is intentionally application-agnostic. It does not assume a company, product, staging URL, test account, user role, domain model, or existing test framework.

## What This Repository Provides

- AI-native QA orchestration for command-driven QA work.
- Reusable QA capability modules for AI coding agents.
- Agent role prompts for planning, implementation, review, and bug analysis.
- Command prompts for common QA automation workflows.
- Workflow definitions for multi-step QA processes.
- Routing rules and safety policies for agent handoffs.
- Standards for test design, Playwright TypeScript, API testing, Rest Assured Java, Pytest Python, and review quality.
- Architecture validation specifications for orchestration acceptance, routing, Human Gate, leakage, and compatibility behavior.
- Templates for test cases, bug reports, API tests, page objects, and PR reviews.
- Placeholder areas for attributed third-party material.

## Primary Focus Areas

- QA test design
- Playwright TypeScript
- API testing
- Rest Assured Java
- Pytest Python
- QA code review
- Bug analysis
- Test data generation

Selenium is intentionally out of scope for now.

## Repository Layout

```text
qa-skills-hub/
  constitution/ Always-on rules for AI QA agents
  skills/       Reusable skill instructions for AI agents
  agents/       Role-oriented agent prompts
  commands/     Task-oriented command prompts
  workflows/    Multi-step QA processes and handoff formats
  routing/      Decision rules for selecting agents and skills
  policies/     Safety and evidence policies for agent behavior
  standards/    General engineering and QA standards
  validation/   Architecture acceptance specifications
  templates/    Reusable markdown templates
  third-party/  Placeholder directories for copied or adapted external material
  docs/         Usage and attribution documentation
```

## Orchestration Layers

- Commands layer: user-facing entry points.
- QA Orchestrator layer: central router for intent, evidence, constraints, and handoffs.
- Constitution layer: always-on rules for AI QA agents.
- Policies layer: safety, approval, no-leakage, audit, and refactor constraints.
- Routing layer: selection of workflow, agent, and reusable skills.
- Workflows layer: ordered execution processes.
- Agents layer: reusable QA execution roles.
- Skills layer: reusable capability modules.
- Audit layer: evidence and edit-readiness checks before changes or recommendations.
- Human Gate layer: stop and approval checkpoints.
- Output layer: reviewed QA artifact, recommendation, or handoff.

## AI-Native QA Architecture

```text
Command -> QA Orchestrator -> Constitution -> Policies -> Routing -> Workflow -> Agent -> Skill -> Audit -> Human Gate -> Output
```

- Command: user-facing entry point for intent such as design, automate, review, audit, debug, or bug report.
- QA Orchestrator: first agent handoff that applies the architecture in order.
- Constitution: always-on rules for safety, evidence-based QA reasoning, audit-before-edit, human approval, and no product-specific leakage.
- Policies: safety and approval constraints that protect against unsafe edits, leakage, and risky refactors.
- Routing: selection of the workflow, agent, and skills for the user request.
- Workflows: ordered QA processes from intake through clarification, test design, automation strategy, implementation planning, review, and verification.
- Agents: reusable QA execution roles with responsibilities and handoffs.
- Skills: reusable capabilities selected by routing rules; Playwright TypeScript is only one possible automation skill.
- Audit: evidence, scope, leakage, and edit-readiness checks before output or changes.
- Human Gate: mandatory approval before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, file deletion, destructive cleanup, or assumptions about undocumented product behavior.
- Output: final QA design, review, audit, diagnostic analysis, bug report, implementation plan, or handoff.

## Validation

The `validation/` directory defines architecture acceptance specifications, not executable product tests. Use it to check expected orchestration behavior, routing, Human Gate decisions, leakage prevention, and compatibility delegation across Claude Code, Codex, Cursor, and other compatible agents.

Agent handoffs should follow `standards/agent-handoff-standard.md`.

### Static validation

Run the repository's deterministic static checks locally with:

```text
python scripts/validate_repository.py
```

The validator uses only the Python standard library, performs no network access, and does not mutate the repository. Exit code `0` means all required checks passed, `1` means repository validation failures were found, and `2` means an internal or validator-configuration failure occurred. Errors use the sanitized form `[ERROR] <CHECK_ID> <path>:<line> <message>`; use the check ID, path, and line to correct the source without expecting a sensitive matched value to appear in output.

The same command runs in CI on Windows and Linux for every push, pull request, and manual dispatch. The workflow is defined in `.github/workflows/static-validation.yml`.

## How To Use

For a reproducible, cross-agent consumer setup, see the
[consumer integration guide](docs/consumer-integration.md).

Start from the command or user intent, then follow the orchestration path:

```text
Command -> QA Orchestrator -> Constitution -> Policies -> Routing -> Workflow -> Agent -> Skill -> Audit -> Human Gate -> Output
```

1. Identify the command or intent, such as `qa-design`, `qa-automate`, `qa-review`, `qa-audit`, `qa-debug`, or `qa-bug-report`.
2. Route the request through `agents/qa-orchestrator.md`.
3. Apply `constitution/qa-agent-constitution.md`.
4. Apply relevant policies from `policies/`.
5. Use `routing/skill-routing-rules.md` to select the workflow, responsible agent, and reusable skills.
6. Follow the selected workflow from `workflows/`.
7. Load only the skills selected by routing.
8. Run audit checks before edits, recommendations, or final handoff.
9. Stop at Human Gate when approval is required.
10. Produce the requested QA output for review in the consuming project.

## Design Principles

- Keep skills universal and portable.
- Prefer clear test intent over clever implementation.
- Separate test design from test automation.
- Make assumptions explicit.
- Do not invent product behavior when requirements are missing.
- Prefer stable contracts, accessible locators, deterministic data, and isolated tests.
- Treat AI output as a draft that must be reviewed.

## What This Is Not

This is not an application test framework. It does not include runnable Playwright, Rest Assured, or Pytest examples. It is a reusable instruction and standards library for agents that will work inside other repositories.

## Third-Party Material

Do not paste third-party content into this repository without attribution. Use `docs/source-attribution.md` and the placeholders in `third-party/` to record source name, URL, license, retrieval date, and adaptation notes.
