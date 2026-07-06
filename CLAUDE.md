# Claude Code Orchestration

Use this repository as a universal QA automation skills library.

## Operating Rules

- Start with `SKILL_INDEX.md` and select the smallest relevant skill.
- Read the selected `skills/*/SKILL.md` before generating plans, tests, reviews, or bug analysis.
- Add relevant files from `standards/` only when they improve the answer.
- Keep all output project-neutral unless the consuming project provides specific context.
- Do not invent application behavior, URLs, roles, credentials, selectors, or domain rules.
- Do not add Selenium guidance unless the user explicitly expands scope later.

## Default Flow

1. Identify task type: design, automation, review, bug analysis, or data generation.
2. Load the matching skill.
3. Ask for missing critical inputs only when assumptions would be risky.
4. Produce concise, actionable QA output.
5. Call out risks, assumptions, and gaps clearly.
