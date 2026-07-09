# QA Review Command

## Purpose

User-facing entry point for reviewing QA automation code, diffs, generated tests, or framework changes.

## When to use

- Use when code, a diff, or generated tests exist.
- Use when the user requests PR-style review or QA risk analysis.

## Inputs

- Code, diff, changed files, generated tests, or review target.
- Purpose of the change or linked requirement/defect.
- Test results or evidence if available.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution and policies.
3. Use routing rules to select `workflows/automation-review.md`.
4. Hand off to `agents/qa-code-reviewer.md`.
5. Apply audit-before-edit before suggesting edits.
6. Stop at Human Gate before risky recommendations.

## Outputs

- Findings first, ordered by severity.
- Impact and fix direction.
- Missing coverage and residual risk.
- Verification notes.

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion, destructive cleanup, or undocumented behavior assumptions.

## Related agents, workflows, policies, or skills

- `agents/qa-orchestrator.md`
- `agents/qa-code-reviewer.md`
- `workflows/automation-review.md`
- `policies/audit-before-edit.md`
- `policies/human-gate-policy.md`

## Application-agnostic constraints

- Do not expose real URLs, credentials, emails, selectors, roles, company names, or business flows.
- Do not weaken assertions to hide failures.
