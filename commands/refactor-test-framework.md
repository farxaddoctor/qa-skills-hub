# Refactor Test Framework Command

## Purpose

Compatibility command for test framework refactor requests.

## When to use

- Use when older prompts ask to refactor a test framework.
- Prefer `commands/qa-audit.md` before any refactor.

## Inputs

- Refactor goal.
- Affected files or framework areas.
- Current behavior and verification constraints.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution, audit-before-edit, safe-refactor, and Human Gate policies.
3. Run audit before proposing edits.
4. Stop for approval before broad or risky refactor.

## Outputs

- Audit summary.
- Refactor scope.
- Risks and rollback thinking.
- Verification plan.

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion, destructive cleanup, or undocumented behavior assumptions.

## Related agents, workflows, policies, or skills

- `commands/qa-audit.md`
- `agents/qa-code-reviewer.md`
- `agents/automation-engineer.md`
- `workflows/automation-review.md`
- `policies/safe-refactor-policy.md`

## Application-agnostic constraints

- Do not add dependencies or runnable framework files to this repository.
- Do not use real project data.
