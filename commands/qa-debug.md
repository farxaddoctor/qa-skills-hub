# QA Debug Command

## Purpose

User-facing entry point for analyzing failures, flaky behavior, CI failures, logs, traces, or bug evidence.

## When to use

- Use when failure or flaky behavior is reported.
- Use before changing tests to make failures pass.
- Use when the user asks whether the cause is test, data, environment, dependency, or product behavior.

## Inputs

- Failure log, trace summary, screenshot, video, network log, stack trace, or CI output.
- Expected behavior and actual behavior.
- Reproduction steps and frequency if available.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution, evidence policy, and leakage policy.
3. Use routing rules to select `workflows/flaky-test-investigation.md` or `workflows/bug-to-regression.md`.
4. Hand off to `agents/bug-analyst.md`.
5. Recommend diagnostics before edits.
6. Stop at Human Gate before risky assumptions or changes.

## Outputs

- Failure summary.
- Evidence and hypotheses.
- Likely cause classification.
- Diagnostic next steps.
- Regression or bug-report handoff.

## Human Gate conditions

Human approval is required before assuming undocumented behavior, destructive cleanup, deletion, auth/session changes, CI/CD changes, global config changes, or dependency changes.

## Related agents, workflows, policies, or skills

- `agents/qa-orchestrator.md`
- `agents/bug-analyst.md`
- `workflows/flaky-test-investigation.md`
- `workflows/bug-to-regression.md`
- `policies/evidence-and-citation-policy.md`

## Application-agnostic constraints

- Do not store real logs containing credentials, tokens, emails, URLs, or customer data.
- Use placeholders such as `<RESOURCE_ID>`, `<USER_EMAIL>`, and `<TOKEN>`.
