# Playwright TypeScript Skill

## Purpose

Guide AI agents when designing, writing, refactoring, or reviewing Playwright tests in TypeScript inside a consuming project.

This skill focuses on reliable browser automation, test structure, locator strategy, assertions, fixtures, page objects, and maintainability. It does not add runnable tests to this repository.

## When to use

- Creating Playwright TypeScript automation from already defined test scenarios.
- Reviewing Playwright tests for flakiness, locator quality, assertions, and maintainability.
- Refactoring brittle tests, fixtures, helpers, or page objects.
- Designing browser automation structure for a consuming project.
- Investigating Playwright failure logs, traces, screenshots, or videos.
- Improving test isolation, setup, cleanup, and parallel safety.

## When not to use

- When test scenarios are not yet defined; start with `skills/qa-test-design/SKILL.md`.
- When the task is API-only and does not use browser automation; use `skills/api-testing/SKILL.md`.
- When the repository does not use Playwright TypeScript.
- When the request is to add runnable examples to this skills library.

## Required inputs

- Test scenario or behavior to automate.
- Existing Playwright files, fixtures, helpers, page objects, or project conventions when available.
- Relevant UI structure, accessibility information, stable test ids, or component contracts.
- Authentication, setup, data, and cleanup constraints.
- Failure artifacts such as trace, screenshot, video, console output, network log, or CI log for debugging tasks.

## Expected output

- Playwright TypeScript implementation guidance or scoped code changes in the consuming project.
- Recommended locator strategy and assertion strategy.
- Fixture, helper, page-object, and data setup recommendations.
- Flake risks and concrete fixes.
- Review findings with file and line references when reviewing code.
- Verification steps that fit the consuming project.

## Rules

- Prefer user-facing locators: role, label, placeholder, text, alt text, and approved test ids.
- Use Playwright web-first assertions for visible, enabled, URL, text, count, and state checks.
- Let Playwright auto-waiting work before adding custom waits.
- Avoid arbitrary sleeps and timing guesses.
- Keep tests independent, deterministic, and parallel-safe.
- Keep each test focused on one behavior or coherent workflow.
- Use fixtures for shared setup when they make intent clearer.
- Prefer API or fixture setup for expensive preconditions when reliable and consistent with project conventions.
- Keep page objects focused on meaningful user actions and state queries.
- Make assertions verify business-observable outcomes, not only element presence.
- Follow the consuming project's naming, folder layout, linting, and fixture patterns.
- Preserve useful debugging artifacts in CI when supported.

## Anti-patterns

- Using `waitForTimeout` as a stability strategy.
- Locating by brittle CSS chains, DOM depth, generated classes, or visual position when better locators exist.
- Overusing broad text locators that can match unrelated content.
- Combining unrelated workflows into one long test.
- Hiding important behavior inside generic helpers.
- Sharing mutable state across parallel tests.
- Treating element visibility as proof that the operation succeeded.
- Asserting implementation details unless the test level explicitly requires it.
- Adding runnable Playwright examples to this repository.

## Review checklist

- Would the test fail for the behavior it claims to verify?
- Are locators stable, accessible, and aligned with project conventions?
- Are assertions specific, web-first, and user-observable?
- Is setup isolated and cleanup-safe?
- Can the test run alone and in parallel?
- Are waits event-based or assertion-based rather than time-based?
- Are fixtures and page objects reducing real duplication without hiding intent?
- Are failure artifacts and error messages useful enough for CI triage?

## Example prompts

- "Use the Playwright TypeScript skill to review this test for flakiness and locator quality."
- "Refactor this Playwright flow using existing project fixtures and stable assertions."
- "Design a page object shape for this workflow without adding app-specific behavior to the skills repo."
- "Analyze this Playwright trace summary and suggest likely causes of failure."
- "Turn these QA scenarios into Playwright automation guidance for a TypeScript project."

## Related standards

- `standards/playwright-standards.md`
- `standards/typescript-standards.md`
- `standards/automation-standards.md`
- `templates/page-object-template.md`
