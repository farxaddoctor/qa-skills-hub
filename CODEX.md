# Codex Usage Guide

Use this repository as a portable QA automation orchestration pack when working inside other codebases.

## How Codex Should Use This Repository

- Start with `constitution/qa-agent-constitution.md`, then apply `policies/`, `routing/`, `workflows/`, `agents/`, and selected `skills/`.
- Treat `skills/*/SKILL.md` files as reusable capability modules, not the default entry point.
- Treat `standards/*.md` files as quality bars.
- Treat `templates/*.md` files as output shapes, not mandatory forms.
- Keep generated code and examples in the consuming project, not in this repository.
- Avoid project-specific assumptions unless they are provided by the user or discovered in the target repository.

## Suggested Workflow

1. Read `SKILL_INDEX.md` and the Constitution.
2. Use `routing/skill-routing-rules.md` to select a workflow and agent.
3. Read the selected workflow, agent brief, and skills.
4. Inspect the consuming project before suggesting edits.
5. Apply audit-before-edit and Human Gate policies before risky changes.
6. Implement, review, or report according to the selected workflow.
7. Verify with the consuming project's normal test, lint, and typecheck commands when available.

## Boundaries

- This repository is not a runnable automation framework.
- Do not add real application tests here.
- Do not store credentials, URLs, account data, customer data, or product-specific behavior here.
- Do not introduce Selenium unless scope changes explicitly.

## Good Codex Prompts

- "Use `commands/qa-design.md` to turn these requirements into QA coverage."
- "Use `commands/qa-automate.md` to plan automation after test scenarios are clear."
- "Use `commands/qa-review.md` to review this QA automation change."
- "Use `commands/qa-debug.md` to analyze this failure log and propose next diagnostics."
