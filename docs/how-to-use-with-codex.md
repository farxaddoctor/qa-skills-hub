# How To Use With Codex

Use this repository as supporting context when Codex is working inside a real application or test framework repository.

## Basic Flow

1. Ask Codex to read `SKILL_INDEX.md`.
2. Name the relevant skill file.
3. Provide the consuming project's code or requirements.
4. Ask Codex to follow the skill and relevant standards.
5. Let Codex inspect the consuming repository before editing.
6. Run the consuming project's normal verification commands.

## Example Prompts

```text
Use qa-skills-hub/skills/qa-code-review/SKILL.md to review this PR.
Focus on test value, flake risk, isolation, and missing assertions.
```

```text
Use qa-skills-hub/skills/playwright-typescript/SKILL.md.
Refactor this Playwright test in the current project using existing fixtures and locator conventions.
```

```text
Use qa-skills-hub/skills/bug-analysis/SKILL.md.
Analyze this CI failure and suggest diagnostics before changing code.
```

## Codex-Specific Notes

- Codex should inspect the target project before implementation.
- Codex should preserve existing project conventions.
- Codex should avoid changing this skills repository when the requested work belongs in the consuming project.
- Codex should verify changes with available tests, lint, or typecheck commands.
- Codex should report any verification that could not be run.
