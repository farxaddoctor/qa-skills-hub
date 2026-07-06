Да, этот `qa-code-review/SKILL.md` хороший, но пока он тоже **слишком общий**. Он описывает правильные принципы, но агенту не хватает строгого review-протокола:

```text
1. что читать сначала
2. как классифицировать findings
3. как отличать blocker от minor
4. как не уходить в лишний refactor
5. как проверять, что тест реально ловит дефект
6. какой формат review возвращать
```

Я бы заменил файл на усиленную версию ниже.

````md
# QA Code Review Skill

## Purpose

Review QA automation changes for correctness, reliability, maintainability, test value, and risk.

This skill applies to automated tests, fixtures, helper code, Page Objects, API clients, test data utilities, CI test configuration, reporting setup, and QA framework changes.

The goal is not to enforce personal style preferences. The goal is to identify issues that can reduce test value, create false confidence, introduce flakiness, hide defects, or make the automation framework harder to maintain.

## When to use

Use this skill when the task involves:

- Reviewing a pull request, diff, or changed files that add or modify automated tests.
- Reviewing Playwright, API, Rest Assured Java, Pytest Python, or test utility code.
- Reviewing fixtures, Page Objects, API clients, test data builders, helpers, or framework configuration.
- Checking whether tests actually cover the intended behavior, requirement, or defect.
- Finding flaky waits, weak selectors, hidden dependencies, weak assertions, missing cleanup, or maintainability problems.
- Reviewing AI-generated tests before they are merged.
- Producing structured QA review comments.

## When not to use

Do not use this skill when:

- The user needs original test scenario design. Use `skills/qa-test-design/SKILL.md`.
- The user needs direct implementation and no review is requested.
- No code, diff, test output, requirement, bug report, or stated change intent is available.
- The task is pure production-code review and not related to tests, testability, quality risk, or automation architecture.
- The user asks for broad framework redesign without a concrete review target.

## Required inputs

Collect or infer the following before reviewing:

- Diff, pull request, changed files, code snippets, or relevant repository files.
- Purpose of the change: requirement, bug, risk area, feature, or refactor goal.
- Existing project conventions and relevant standards.
- Test run results, CI output, failure logs, traces, screenshots, or reports when available.
- Scope boundary: review only, suggest patch, or implement fixes.
- Target framework or layer: UI, API, integration, unit, contract, performance, or test infrastructure.

If the purpose of the change is unclear, ask or mark review findings as assumptions.

## Operating mode

Follow this workflow unless the user explicitly requests a different format:

### 1. Understand the change

- Identify what files changed.
- Identify the intended behavior, defect, or risk area.
- Identify whether the change is test-only, framework-level, or configuration-level.
- Separate confirmed facts from assumptions.

### 2. Review for test value first

Check whether the new or changed tests would actually fail if the intended behavior were broken.

Prioritize:

- Missing coverage.
- Weak assertions.
- False positives.
- False confidence.
- Tests that pass while not validating the intended behavior.

### 3. Review reliability

Check for flake risks:

- Arbitrary sleeps.
- Weak selectors.
- Race conditions.
- Shared mutable state.
- External dependencies.
- Order dependency.
- Environment coupling.
- Missing setup or cleanup.
- Uncontrolled test data.

### 4. Review maintainability

Check whether the change makes future testing easier or harder.

Look for:

- Duplication.
- Over-generalized helpers.
- Hidden behavior.
- Misplaced assertions.
- Page Object bloat.
- Fixtures with unclear responsibility.
- API clients with inconsistent request/response handling.

### 5. Review scope safety

Identify whether the change modifies more than needed.

Flag:

- Unrelated refactors.
- Global config changes without justification.
- New dependencies without clear value.
- Framework rewrites for a small test change.
- Risky auth, CI, or data changes mixed with simple tests.

### 6. Return findings first

Do not start with praise or long summaries. Return findings ordered by severity. Then provide a short summary.

### 7. Separate fixes by risk

Classify each recommendation as:

- Safe now
- Safe after verification
- Needs design decision
- Risky / do not change without approval

## Severity levels

Use these severity levels.

### Blocker

The change should not be merged because it can break the suite, hide a real defect, corrupt data, expose secrets, or invalidate the test result.

Examples:

- Test always passes even when behavior is broken.
- Real credentials or tokens committed.
- Destructive cleanup can delete shared or production-like data.
- Global config disables important checks.
- Test depends on execution order.

### Major

The change can create false confidence, recurring flakiness, missing critical coverage, or significant maintenance risk.

Examples:

- Weak assertion only checks visibility or status code.
- Missing auth/RBAC coverage for protected API.
- `waitForTimeout` used as synchronization.
- Test data is shared and not isolated.
- Page Object duplicates an existing flow.

### Minor

The issue is worth fixing but does not seriously affect correctness.

Examples:

- Missing diagnostic assertion message.
- Slightly unclear test name.
- Small duplication.
- Low-risk selector improvement.
- Missing comment for a non-obvious workaround.

### Question

The reviewer needs clarification before deciding whether it is an issue.

Examples:

- Requirement is ambiguous.
- Expected error status is undocumented.
- Cleanup endpoint availability is unknown.
- Test environment rule is not documented.

### Nit

Very small style or readability improvement. Use sparingly.

## Evidence rules

- Do not claim something is the only occurrence unless confirmed by search.
- Include file paths and line references when available.
- Separate confirmed issues from suspected issues.
- Explain why the issue matters.
- Provide concrete fix direction.
- Do not make broad claims without evidence.
- Do not recommend broad refactors before identifying quick wins.
- Do not invent project conventions; use existing repository patterns when available.

## Review focus areas

### Test value

Check:

- Does the test verify the intended requirement or bug?
- Would it fail for the right reason?
- Does it verify an observable outcome?
- Does it check persistence, state, response, or user-visible behavior?
- Does it avoid testing only implementation details?
- Is the expected behavior documented or clearly stated?

### Assertions

Check:

- Are assertions specific?
- Do they verify meaningful outcomes?
- Do they include status, body, schema, side effects, or UI state where relevant?
- Are negative assertions safe from false passes?
- Are assertion messages useful for CI triage when the project standard requires them?

### UI automation reliability

Check:

- Locator stability.
- Accessible locators or stable test ids.
- Scoped locators for repeated elements.
- Avoidance of brittle CSS, XPath, generated classes, and positional selectors.
- Avoidance of arbitrary waits.
- Proper use of Playwright web-first assertions.
- Correct registration of waits before triggering actions.

### API automation reliability

Check:

- Status code plus body/schema assertions.
- Error contract validation.
- Auth and authorization coverage.
- Request builders or clients do not hide important behavior.
- Test data is isolated.
- Cleanup is safe.
- No hardcoded tokens, accounts, credentials, or environment-specific values.

### Fixtures and setup

Check:

- Setup is clear and deterministic.
- Fixtures reduce real duplication.
- Fixtures do not hide important behavior.
- Authentication setup follows project convention.
- Tests can run alone.
- Tests can run in parallel when the project supports parallelism.
- Cleanup does not fail the test for unrelated reasons unless cleanup is part of the behavior.

### Page Objects and helpers

Check:

- Page Objects represent meaningful user actions or page/component behavior.
- Page Objects do not become huge application-wide objects.
- Helpers are not overly generic.
- Assertions are placed intentionally.
- Existing Page Objects are reused before creating new ones.
- There is no duplicated flow across multiple helper layers.

### Test data

Check:

- Data is unique where needed.
- Tests do not rely on stale shared data unless explicitly seeded.
- Created data is cleaned up or documented as acceptable debt.
- Data dependencies fail fast with useful messages.
- Sensitive or production-like personal data is not used.

### Tags and test suite slicing

Check:

- Tags match project conventions.
- Smoke tests are fast and high-value.
- Full/regression tests are not pretending to test unfinished flows.
- Skipped or fixme tests include reasons.
- Test names are unique and behavior-focused.

### Framework/config changes

Check:

- Global config changes are justified.
- Reporter, retry, timeout, worker, and trace changes are safe.
- New dependencies are necessary.
- CI impact is understood.
- Debug artifacts remain available for triage.

## Expected output

### For review-only tasks

Return:

```text
## Review findings

### Blocker
- Finding:
- Evidence:
- Why it matters:
- Suggested fix:
- Risk:
- Safe to change now:

### Major
...

### Minor
...

### Questions
...

## Summary
- Overall risk:
- Strong parts:
- Highest-priority fixes:
- Suggested verification:
```
````

### For audit tasks

Return:

```text
## Audit summary

Scope:
Files reviewed:
Standards or skills used:

## Findings table

| Severity | Area | Finding | Evidence | Why it matters | Suggested fix | Safe now |
|---|---|---|---|---|---|---|

## Quick wins

## Larger refactors

## Verification commands
```

### For patch-suggestion tasks

Return:

- Files to change.
- Minimal change plan.
- Risk level.
- Verification command.
- Rollback note if relevant.

Do not edit files unless the user explicitly asks to implement changes.

## Rules

- Prioritize correctness, test value, reliability, and missing coverage over style.
- Verify that each test would fail for the intended defect or behavior.
- Check assertions for specificity and meaningful outcomes.
- Check setup, cleanup, and data generation for isolation and determinism.
- Check selectors, waits, retries, parallelism, and external dependencies for flake risk.
- Check helper abstractions for hidden behavior, over-generalization, or unclear responsibility.
- Respect the consuming project's conventions.
- Avoid requesting unrelated refactors.
- Distinguish confirmed issues from questions.
- If implementing fixes, keep changes narrowly scoped.
- Do not approve AI-generated tests without checking behavior and assertions.
- Do not recommend deleting working code unless the risk and replacement plan are clear.
- Do not mix large architecture refactors with small test fixes unless requested.

## Anti-patterns

- Approving tests that only verify implementation details or weak status checks.
- Approving tests that would pass even if the target behavior were broken.
- Focusing on formatting while missing coverage or flake risks.
- Requesting broad refactors unrelated to the change.
- Ignoring test independence, cleanup, or parallel execution.
- Assuming missing requirements instead of labeling them as questions.
- Giving vague comments without impact or fix direction.
- Treating AI-generated tests as correct without checking behavior.
- Rewriting unrelated code during review.
- Suggesting new abstractions before checking existing project patterns.
- Treating element visibility or HTTP 200 as enough proof by itself.
- Hiding product bugs by weakening tests.

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
- Are changes scoped to the stated purpose?
- Are quick wins separated from larger refactors?
- Are confirmed issues separated from questions?

## Example prompts

```text
Use the QA code review skill.
Review this Playwright test diff.
Return findings first, ordered by severity.
Do not suggest broad refactors unless they directly affect reliability or test value.
```

```text
Use the QA code review skill.
Review this API test PR for missing assertions, data isolation, authorization gaps, and flake risk.
Return blocker/major/minor/questions sections.
```

```text
Use the QA code review skill.
Check whether these regression tests actually cover the reported bug.
Explain whether each test would fail before the fix.
```

```text
Use the QA code review skill.
Review this test framework refactor.
Identify behavioral risks, hidden dependencies, and verification steps.
Do not edit files.
```

```text
Use the QA code review skill.
Audit this repository's automated tests.
Focus on false positives, flaky waits, weak selectors, duplicated helpers, and missing cleanup.
Return a findings table and quick wins.
```

## Related standards

- `standards/testing-standards.md`
- `standards/automation-standards.md`
- `standards/playwright-standards.md`
- `standards/api-testing-standards.md`
- `templates/pr-review-template.md`

````

После замены:

```powershell
git add skills/qa-code-review/SKILL.md
git commit -m "Strengthen QA code review skill"
````
