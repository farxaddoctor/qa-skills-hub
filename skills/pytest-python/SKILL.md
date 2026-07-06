# Pytest Python Skill

## Purpose

Placeholder skill for Python automation with Pytest in a consuming project.

## When to use

- Use when scenarios are already defined and the consuming project uses Pytest.
- Combine with `skills/api-testing/SKILL.md` for API coverage or `skills/qa-test-design/SKILL.md` for scenario design.

## When not to use

- Do not use for browser-specific Playwright TypeScript work.
- Do not use when the consuming project does not use Python or Pytest.
- Do not add runnable framework examples to this repository.

## Required inputs

- Existing Pytest files, fixtures, helpers, or project conventions.
- Test scenarios, contracts, or failure logs.
- Data setup and cleanup constraints.

## Expected output

- Brief Pytest implementation or review guidance.
- Notes on fixtures, parametrization, assertions, data setup, and cleanup.

## Rules

- Keep fixtures explicit and scoped deliberately.
- Prefer clear assertions and deterministic data.
- Follow the consuming project's Python conventions.

## Anti-patterns

- Overusing autouse fixtures.
- Depending on test order or shared mutable state.
- Hiding unrelated cases inside one parametrized test.

## Review checklist

- Are fixtures understandable and scoped safely?
- Are assertions specific?
- Can tests run alone and in parallel?
- Is test data synthetic and deterministic?

## Example prompts

- "Use the Pytest Python placeholder skill to review this fixture design."
- "Suggest Pytest structure for these API scenarios using the consuming project's conventions."

## Related standards

- `standards/python-standards.md`
- `standards/api-testing-standards.md`
- `standards/automation-standards.md`
