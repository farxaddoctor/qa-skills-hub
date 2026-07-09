# Safe Refactor Policy

## Purpose

Define safe refactoring rules for QA automation work.

## When to use

- Use before changing test structure, fixtures, helpers, Page Objects, API clients, or framework utilities.
- Use when a requested change may preserve behavior but alter implementation shape.

## Inputs

- Current behavior and intended behavior.
- Refactor scope.
- Affected files or components.
- Existing verification commands.
- Rollback or revert strategy.

## Process

1. Confirm behavior to preserve.
2. Keep changes small and scoped.
3. Prefer reliability, clarity, and maintainability improvements.
4. Avoid broad rewrites unless Human Gate approval is granted.
5. Validate after change with relevant checks.
6. Record residual risks.

## Outputs

- Refactor scope.
- Behavior preservation statement.
- Risk level.
- Verification plan.
- Human Gate decision.

## Human Gate conditions

Human approval is required before:

- Broad refactor.
- Shared utility changes with multiple downstream users.
- Auth/session, CI/CD, global config, or dependency changes.
- File deletion or destructive cleanup.
- Changes based on undocumented product behavior.

## Related agents, workflows, policies, or skills

- `policies/audit-before-edit.md`
- `policies/human-gate-policy.md`
- `agents/automation-engineer.md`
- `agents/qa-code-reviewer.md`
- `workflows/test-plan-to-automation.md`
- `workflows/automation-review.md`

## Application-agnostic constraints

- Do not refactor around a specific product domain in this repository.
- Do not add runnable frameworks or executable tests here.
- Use generic examples and placeholders only.
