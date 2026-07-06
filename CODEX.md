# Codex Usage Guide

Use this repository as a portable QA automation instruction pack when working inside other codebases.

## How Codex Should Use This Repository

- Treat `skills/*/SKILL.md` files as task instructions.
- Treat `standards/*.md` files as quality bars.
- Treat `templates/*.md` files as output shapes, not mandatory forms.
- Keep generated code and examples in the consuming project, not in this repository.
- Avoid project-specific assumptions unless they are provided by the user or discovered in the target repository.

## Suggested Workflow

1. Read `SKILL_INDEX.md`.
2. Select the relevant skill.
3. Read any matching standards file.
4. Inspect the consuming project before suggesting edits.
5. Implement or review according to the selected skill.
6. Verify with the consuming project's normal test, lint, and typecheck commands when available.

## Boundaries

- This repository is not a runnable automation framework.
- Do not add real application tests here.
- Do not store credentials, URLs, account data, customer data, or product-specific behavior here.
- Do not introduce Selenium unless scope changes explicitly.

## Good Codex Prompts

- "Use `skills/playwright-typescript/SKILL.md` to review this Playwright test for reliability."
- "Use `skills/api-testing/SKILL.md` to design API coverage for this endpoint contract."
- "Use `skills/qa-code-review/SKILL.md` and `standards/automation-standards.md` to review this PR."
- "Use `skills/bug-analysis/SKILL.md` to analyze this failure log and propose next diagnostics."
