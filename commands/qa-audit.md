# QA Audit Command

## Purpose

User-facing entry point for auditing existing QA automation, framework structure, or generated tests before edits.

## When to use

- Use when the user wants a quality assessment before refactor.
- Use when flake risk, weak assertions, weak selectors, or framework drift are suspected.

## Inputs

- Files, diff, generated tests, logs, traces, or review scope.
- Known concerns or failure history.
- Relevant constraints supplied by the consuming project.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution and policies.
3. Use routing rules to select `workflows/automation-review.md`.
4. Hand off to `agents/qa-code-reviewer.md`.
5. Apply audit-before-edit.
6. Stop at Human Gate before risky recommendations or changes.

## Outputs

- Findings by severity.
- Evidence and risk level.
- Safe-to-refactor decision.
- Recommended next workflow.

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion, destructive cleanup, or undocumented behavior assumptions.

## Related agents, workflows, policies, or skills

- `agents/qa-orchestrator.md`
- `agents/qa-code-reviewer.md`
- `workflows/automation-review.md`
- `policies/audit-before-edit.md`
- `policies/safe-refactor-policy.md`

## Application-agnostic constraints

- Do not include real URLs, credentials, emails, selectors, roles, company names, or internal environment data.
- Do not edit files during audit unless explicitly routed to implementation.
