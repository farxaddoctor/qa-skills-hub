# QA Code Review Skill

## Purpose

Review QA automation changes for correctness, reliability, maintainability, test value, and risk.

This skill applies to automated tests, fixtures, helper code, page objects, API clients, test data utilities, and QA framework changes.

## When to use

- Reviewing a pull request or diff that adds or changes automated tests.
- Reviewing Playwright, API, Rest Assured Java, or Pytest Python code.
- Reviewing fixture, helper, page-object, API-client, or test-data changes.
- Checking whether tests actually cover the intended behavior or defect.
- Finding flake risks, hidden dependencies, weak assertions, or maintainability problems.
- Producing a structured QA review comment.

## When not to use

- When the user needs original test scenario design; start with `skills/qa-test-design/SKILL.md`.
- When the user asks for implementation only and no review is needed.
- When no code, diff, test output, requirement, or stated change intent is available.
- When reviewing non-QA production code unless the focus is testability or quality risk.

## Required inputs

- Diff, pull request, changed files, or code snippets.
- Purpose of the change, linked requirement, bug, or risk area when available.
- Existing project conventions and relevant standards.
- Test run results, CI output, or failure logs if available.
- Scope boundary: review only, suggest patch, or implement fixes.

## Expected output

- Findings first, ordered by severity.
- File and line references when available.
- Impact explanation and concrete fix direction.
- Missing coverage and regression risk notes.
- Questions for unclear requirements or assumptions.
- Brief summary only after findings.
- Clear statement when no material issues are found.

## Rules

- Prioritize bugs, behavioral gaps, reliability risks, and missing tests over style comments.
- Verify that each test would fail for the intended defect or behavior.
- Check assertions for specificity and meaningful outcomes.
- Check setup, cleanup, and data generation for isolation and determinism.
- Check selectors, waits, retries, parallelism, and external dependencies for flake risk.
- Check helper abstractions for hidden behavior, over-generalization, or unclear responsibility.
- Respect the consuming project's conventions.
- Avoid requesting unrelated refactors.
- Distinguish confirmed issues from questions.
- If implementing fixes, keep changes narrowly scoped.

## Anti-patterns

- Approving tests that only verify implementation details or weak status checks.
- Focusing on formatting while missing coverage or flake risks.
- Requesting broad refactors unrelated to the change.
- Ignoring test independence, cleanup, or parallel execution.
- Assuming missing requirements instead of labeling them as questions.
- Giving vague comments without impact or fix direction.
- Treating AI-generated tests as correct without checking behavior.
- Rewriting unrelated code during review.

## Review checklist

- Does the change test the intended behavior or defect?
- Would the tests fail for the right reason?
- Are assertions specific enough to catch regressions?
- Are setup, cleanup, and test data isolated and deterministic?
- Are locators, waits, retries, fixtures, and external dependencies reliable?
- Are negative, boundary, permission, and regression cases covered when relevant?
- Are helper abstractions clear and worth their complexity?
- Are secrets, credentials, product-specific assumptions, and environment-specific values absent?
- Are verification commands or CI results available and meaningful?

## Example prompts

- "Use the QA code review skill to review this Playwright test diff. Findings first."
- "Review this API test PR for missing assertions, data isolation, and flake risk."
- "Use this skill to check whether these regression tests cover the reported bug."
- "Review this test framework refactor and identify behavioral risks."
- "Generate a PR review using `templates/pr-review-template.md`."

## Related standards

- `standards/testing-standards.md`
- `standards/automation-standards.md`
- `standards/playwright-standards.md`
- `standards/api-testing-standards.md`
- `templates/pr-review-template.md`
