# Flaky Test Investigation Workflow

## Purpose

Analyze flaky or intermittent test behavior before changing tests.

## When to use

- Use when a test passes and fails intermittently.
- Use when CI output, trace, video, log, or screenshot suggests unstable behavior.
- Use before refactoring waits, locators, fixtures, setup, or cleanup.

## Inputs

- Failure logs, trace summary, screenshots, videos, network logs, or CI output.
- Test name and failure frequency if known.
- Recent changes and environment details supplied by the consuming project.

## Process

1. Apply Constitution, evidence policy, audit-before-edit, and Human Gate policy.
2. Separate facts from hypotheses.
3. Classify likely cause as timing, locator, data, environment, dependency, product bug, or unclear.
4. Inspect whether waits and assertions target observable behavior.
5. Recommend diagnostics or minimal safe fix.
6. Hand off to review or automation only after cause category is clear.

## Outputs

- Likely cause classification.
- Evidence and alternative causes.
- Diagnostic steps.
- Test issue versus product bug recommendation.
- Human Gate decision for any risky fix.

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, file deletion, destructive cleanup, or undocumented behavior assumptions.

## Related agents, workflows, policies, or skills

- `agents/bug-analyst.md`
- `agents/qa-code-reviewer.md`
- `agents/automation-engineer.md`
- `policies/audit-before-edit.md`
- `skills/bug-analysis/SKILL.md`
- `skills/playwright-typescript/SKILL.md`
- `skills/qa-code-review/SKILL.md`

## Application-agnostic constraints

- Do not include real traces, URLs, credentials, emails, selectors, or consumer-project roles in this repository.
- Do not make flake handling Playwright-only.
- Do not weaken assertions to hide failures.
