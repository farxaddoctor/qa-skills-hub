# Analyze Bug Command

## Purpose

Compatibility command for bug, failure, or flaky behavior analysis.

## When to use

- Use when older prompts ask to analyze a bug.
- Prefer `commands/qa-debug.md` for new orchestration.

## Inputs

- Expected behavior and actual behavior.
- Failure log, trace, screenshot, video, stack trace, API payload, or CI output.
- Reproduction steps and frequency if available.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution, evidence policy, and leakage policy.
3. Delegate to `commands/qa-debug.md`.
4. Stop at Human Gate before risky assumptions or changes.

## Outputs

- Failure summary.
- Evidence and hypotheses.
- Likely cause classification.
- Diagnostic next steps.

## Human Gate conditions

Human approval is required before undocumented behavior assumptions, destructive cleanup, deletion, auth/session changes, CI/CD changes, global config changes, or dependency changes.

## Related agents, workflows, policies, or skills

- `commands/qa-debug.md`
- `agents/bug-analyst.md`
- `workflows/flaky-test-investigation.md`
- `workflows/bug-to-regression.md`

## Application-agnostic constraints

- Do not store real logs with secrets, URLs, emails, customer data, company names, or internal environment details.
