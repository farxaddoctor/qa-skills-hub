# Playwright TypeScript Skill

## Purpose

Guide AI agents when designing, writing, refactoring, or reviewing Playwright TypeScript tests inside a consuming project.

This skill focuses on reliable browser automation, maintainable test architecture, locator strategy, assertions, fixtures, authentication setup, Page Object design, API-assisted setup, debugging, and flake prevention.

This repository is only a reusable skills library. Do not add runnable Playwright tests to this repository.

## When to use

Use this skill when the task involves:

- Creating Playwright TypeScript automation from defined test scenarios.
- Reviewing Playwright tests for flakiness, locator quality, assertions, and maintainability.
- Refactoring brittle Playwright tests, fixtures, helpers, or Page Objects.
- Designing browser automation structure for a consuming project.
- Improving authentication setup, storage state, fixtures, or test isolation.
- Investigating Playwright failures using traces, screenshots, videos, console logs, network logs, or CI logs.
- Improving test stability, parallel safety, and debugging quality.

## When not to use

Do not use this skill when:

- Test scenarios are not defined yet. Use `skills/qa-test-design/SKILL.md` first.
- The task is API-only and does not require browser automation. Use `skills/api-testing/SKILL.md`.
- The repository does not use Playwright with TypeScript.
- The user asks to add runnable examples to this skills hub.
- The task is mainly Java, Python, performance, security, or bug-report writing unless Playwright TypeScript is directly involved.

## Required inputs

Before making recommendations or changes, collect or infer:

- The test scenario or user behavior to automate.
- Existing test files, fixtures, helpers, Page Objects, and project conventions.
- Current locator strategy: role, label, text, test id, CSS, XPath, custom attributes.
- Authentication model: UI login, API login, storage state, token injection, session reuse.
- Test data setup and cleanup constraints.
- Browser/project configuration from `playwright.config.ts`.
- Failure artifacts when debugging: trace, screenshot, video, console output, network log, or CI log.
- Whether the task is audit-only, refactor-only, implementation, or debugging.

If required inputs are missing, state assumptions explicitly instead of inventing application behavior.

## Operating mode

Follow this workflow unless the user explicitly requests direct implementation:

1. **Audit first**
   - Read the relevant test, fixture, helper, Page Object, and config files.
   - Identify flake risks, weak selectors, timing assumptions, duplicated logic, and unclear assertions.

2. **Plan before editing**
   - Explain what should change and why.
   - Separate safe refactors from risky architectural changes.
   - Do not rewrite the whole framework unless asked.

3. **Apply scoped changes**
   - Modify only files needed for the requested task.
   - Preserve existing business behavior.
   - Keep changes small, reviewable, and reversible.

4. **Verify**
   - Suggest exact commands to run.
   - Include expected result and what to inspect if the run fails.

5. **Report**
   - Summarize changed files, reasons, risks, and remaining follow-up work.

## Locator strategy

Prefer locators in this order, adjusted to the consuming project's conventions:

1. `getByRole()` with accessible name.
2. `getByLabel()`.
3. `getByPlaceholder()`.
4. `getByText()` only when text is unique and user-observable.
5. `getByAltText()` / `getByTitle()` when appropriate.
6. `getByTestId()` when the project has stable test ids.
7. Scoped CSS locators only when accessible locators are not available.
8. XPath only as a last resort and only with justification.

Rules:

- Scope locators to a meaningful container when the page contains repeated elements.
- Avoid broad text locators that can match unrelated content.
- Avoid generated classes, DOM depth chains, visual position, and fragile `nth()` usage unless no better contract exists.
- Prefer asking for or recommending `data-testid` when the UI has no stable accessible contract.
- When using `nth()`, explain why it is safe or suggest a better frontend testability hook.

## Waiting and assertions

Rules:

- Use Playwright web-first assertions.
- Prefer waiting for user-observable state, URL changes, response completion, or specific UI state.
- Avoid `waitForTimeout()` as a stability mechanism.
- Avoid manual polling unless Playwright assertions are not enough.
- Register `waitForResponse`, `waitForRequest`, or `waitForURL` before triggering the action.
- Assertions should verify business outcomes, not only element visibility.

Good assertion targets:

- URL or route changed.
- Success/error message appears.
- Created entity appears in a specific table/list.
- API response status and payload match expected behavior.
- Button becomes enabled/disabled.
- Validation message appears.
- Wizard step changed or did not change.

Weak assertion targets:

- Element is visible but operation may still have failed.
- Generic page heading only.
- Toast appears but no persistent state is verified.
- Arbitrary timeout passed without checking state.

## Fixtures and setup

Use fixtures when they make setup reusable and test intent clearer.

Prefer:

- Role-based authentication fixtures.
- API login over repeated UI login when reliable.
- Storage state for stable authenticated sessions.
- API or fixture setup for expensive preconditions.
- Isolated data per test.
- Cleanup through API when possible.

Avoid:

- Hidden global mutable state.
- Shared test data that breaks parallel execution.
- Authentication logic duplicated across specs.
- Large fixture files that hide important behavior.
- Creating test dependencies through long UI flows when an API setup is available.

## Page Object guidance

Use Page Objects for reusable page behavior, not for hiding every single line of test code.

A good Page Object:

- Models a meaningful page, component, or workflow step.
- Exposes user-intent methods such as `openCampaign`, `createPlacement`, `submitForm`.
- Keeps locators close to the page/component they belong to.
- Uses assertions only when they represent stable page/component expectations.
- Does not contain unrelated test scenario logic.

Avoid:

- Huge Page Objects that represent the entire application.
- Generic helpers like `clickButton(name)` when they hide test intent.
- Putting assertions everywhere without clear ownership.
- Duplicating the same page behavior across multiple Page Objects.
- Creating a new Page Object before checking whether one already exists.

## Test structure

Prefer:

- Clear test names describing behavior and expected outcome.
- `test.step()` for long workflows.
- Arrange / Act / Assert structure when useful.
- One coherent behavior or workflow per test.
- Explicit tags according to the consuming project convention.
- Independent tests that can run alone.

Avoid:

- Long tests combining unrelated features.
- Copy-pasted specs with only small data changes.
- Tests depending on execution order.
- Test names that describe implementation instead of behavior.
- Duplicate test titles.

## API-assisted browser testing

When browser tests depend on backend state:

- Prefer API setup when the API is stable and project-approved.
- Use API login or storage state to avoid repeated UI login.
- Validate important API responses used for setup.
- Do not mix API and UI assertions randomly; keep the purpose clear.
- Use API cleanup when created data affects future runs.

## Debugging workflow

When investigating a failure:

1. Identify whether failure is caused by locator, timing, test data, environment, authentication, application bug, or test design.
2. Use trace, screenshot, video, console logs, and network logs when available.
3. Check whether the test has hidden dependencies or shared data.
4. Check whether the assertion verifies the correct outcome.
5. Recommend the smallest reliable fix.
6. If the product appears broken, suggest a bug report instead of forcing test changes.

## Expected output

For audit/review tasks, return:

- Summary
- Findings by severity
- Affected files and lines when available
- Why each issue matters
- Suggested fix
- Risk level
- Safe-to-refactor-now: yes/no
- Verification commands

For implementation/refactor tasks, return:

- Files changed
- What changed
- Why it changed
- Behavior preserved
- Verification steps
- Remaining risks

For debugging tasks, return:

- Most likely root cause
- Evidence
- Alternative causes
- Recommended fix
- Whether this looks like a test issue or product bug

## Rules

- Prefer user-facing locators and stable test ids.
- Use web-first assertions.
- Let Playwright auto-waiting work before adding custom waits.
- Avoid arbitrary sleeps and timing guesses.
- Keep tests independent, deterministic, and parallel-safe.
- Keep each test focused on one behavior or coherent workflow.
- Use fixtures for shared setup when they improve clarity.
- Prefer API or fixture setup for expensive preconditions when reliable.
- Keep Page Objects focused on meaningful user actions and state queries.
- Make assertions verify business-observable outcomes.
- Follow the consuming project's naming, folder layout, linting, and fixture patterns.
- Preserve useful debugging artifacts in CI when supported.
- Do not modify `playwright.config.ts`, global fixtures, authentication, CI, or reporting configuration without explaining the impact.
- Do not introduce new dependencies without justification.
- Do not invent application behavior when requirements are missing.

## Anti-patterns

- Using `waitForTimeout()` as a stability strategy.
- Locating by brittle CSS chains, DOM depth, generated classes, or visual position.
- Overusing broad text locators.
- Using XPath without justification.
- Combining unrelated workflows into one long test.
- Hiding important behavior inside generic helpers.
- Sharing mutable state across parallel tests.
- Treating element visibility as proof that an operation succeeded.
- Asserting implementation details unless the test level explicitly requires it.
- Creating duplicate Page Objects or duplicate helper methods.
- Rewriting working tests only for style preference.
- Adding runnable Playwright examples to this skills repository.

## Review checklist

- Would the test fail for the behavior it claims to verify?
- Are locators stable, accessible, scoped, and aligned with project conventions?
- Are assertions specific, web-first, and user-observable?
- Is setup isolated and cleanup-safe?
- Can the test run alone and in parallel?
- Are waits event-based or assertion-based rather than time-based?
- Are fixtures and Page Objects reducing real duplication without hiding intent?
- Are test names unique and behavior-focused?
- Are API-assisted setup steps reliable and validated?
- Are failure artifacts and error messages useful enough for CI triage?
- Are changes scoped and safe?

## Example prompts

```text
Use the Playwright TypeScript skill.
Audit this spec for flaky waits, weak selectors, and unclear assertions.
Do not edit yet. Return findings with risk levels and safe refactor suggestions.
```

```text
Use the Playwright TypeScript skill.
Refactor this Playwright test to remove waitForTimeout, improve assertions, and preserve existing behavior.
Modify only the relevant test and Page Object files.
```

```text
Use the Playwright TypeScript skill.
Review this Page Object. Check whether methods represent meaningful user actions, whether locators are stable, and whether assertions belong here.
```

```text
Use the Playwright TypeScript skill.
Analyze this trace summary and failure log. Decide whether the failure is caused by test flakiness, bad test data, environment instability, or a product bug.
```

```text
Use the Playwright TypeScript skill.
Design automation guidance for these QA scenarios. Do not write code until you identify fixtures, data setup, locator strategy, and assertions.
```

## Related standards

- `standards/playwright-standards.md`
- `standards/typescript-standards.md`
- `standards/automation-standards.md`
- `standards/api-testing-standards.md`
- `templates/page-object-template.md`
