# Review Playwright Test Command

## Purpose

Compatibility command for Playwright TypeScript test review.

## When to use

- Use when older prompts ask to review a Playwright test.
- Prefer `commands/qa-review.md` or `commands/qa-audit.md` for new orchestration.

## Inputs

- Test file, Page Object, fixture, diff, failure evidence, or review scope.
- Expected behavior if available.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution, policies, and audit-before-edit.
3. Route to `agents/qa-code-reviewer.md`.
4. Use Playwright-specific capability only through routing.
5. Stop at Human Gate before risky recommendations.

## Outputs

- Findings by severity.
- Flake, locator, assertion, setup, and coverage risks.
- Verification recommendations.

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion, destructive cleanup, or undocumented behavior assumptions.

## Related agents, workflows, policies, or skills

- `commands/qa-review.md`
- `agents/qa-code-reviewer.md`
- `workflows/automation-review.md`
- `policies/audit-before-edit.md`

## Application-agnostic constraints

- Playwright is one skill, not the architecture.
- Do not store real selectors, URLs, credentials, emails, roles, or business flows.
