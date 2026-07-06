# QA Test Design Skill

## Purpose

Turn requirements, user stories, defects, incidents, API contracts, or risk areas into clear test coverage that can be used for manual testing, automation planning, or review.

This skill defines what to test and why. It does not create runnable tests.

## When to use

- Designing test cases from requirements or acceptance criteria.
- Expanding a happy path into negative, edge, boundary, permission, state, and regression coverage.
- Reviewing whether a feature has enough QA coverage.
- Creating exploratory testing charters.
- Turning a defect or incident into regression scenarios.
- Identifying ambiguous behavior and missing requirements.

## When not to use

- When the user needs framework-specific implementation details; use a framework skill after test intent is clear.
- When the task is only code review; use `skills/qa-code-review/SKILL.md`.
- When the task is root-cause analysis of a live failure; use `skills/bug-analysis/SKILL.md`.
- When no requirement, behavior, contract, or defect context is available.

## Required inputs

- Requirement, feature brief, acceptance criteria, bug report, incident summary, API contract, or workflow description.
- Known expected behavior and constraints.
- Supported platforms, permissions, dependencies, and data rules when relevant.
- Existing coverage if the task is to review or improve coverage.
- Release priority, risk area, or customer impact if risk-based prioritization is needed.

If inputs are incomplete, continue only with explicit assumptions and open questions.

## Expected output

- Test scenarios grouped by behavior, workflow, contract, or risk area.
- Positive, negative, edge, boundary, permission, data, integration, state, and regression cases where relevant.
- Clear expected results.
- Priority or risk notes when useful.
- Coverage gaps, assumptions, and open questions.
- Optional automation suitability notes.

## Rules

- Separate test design from implementation.
- Derive scenarios from stated behavior, not imagined product details.
- Make all assumptions visible.
- Prefer observable behavior, contract outcomes, and user-relevant risk.
- Cover both valid and invalid paths.
- Include boundaries for required fields, optional fields, limits, dates, timezones, numeric ranges, state transitions, and permissions where applicable.
- Consider setup, cleanup, data isolation, dependencies, and repeatability.
- Avoid combining unrelated behaviors into one large scenario.
- Keep terminology generic unless the consuming project provides domain terms.
- Identify what is best verified at unit, API, UI, integration, exploratory, or monitoring level when asked.

## Anti-patterns

- Writing automation before the test intent is clear.
- Producing only happy-path cases.
- Inventing URLs, roles, credentials, selectors, business rules, or domain entities.
- Treating acceptance criteria as complete when obvious risks are missing.
- Using vague expected results such as "works correctly".
- Ignoring permissions, invalid states, cleanup, retries, concurrency, or auditability when relevant.
- Creating order-dependent scenarios without a workflow reason.

## Review checklist

- Does each scenario map to a stated behavior, risk, or defect?
- Are expected results specific and observable?
- Are positive, negative, edge, boundary, and regression paths represented?
- Are permissions, data setup, state transitions, and cleanup considered?
- Are assumptions and open questions clearly separated from facts?
- Is automation suitability noted without forcing everything into UI automation?
- Is the output free of project-specific names, URLs, credentials, and roles?

## Example prompts

- "Use the QA test design skill to create test scenarios from these acceptance criteria. Include edge cases and open questions."
- "Review this feature brief for missing test coverage and organize scenarios by risk."
- "Turn this defect into regression test ideas without writing automation code."
- "Create exploratory charters for this workflow using universal QA test design practices."
- "Given this API contract, identify behavior-level test cases before implementation."

## Related standards

- `standards/testing-standards.md`
- `standards/automation-standards.md`
- `templates/test-case-template.md`
