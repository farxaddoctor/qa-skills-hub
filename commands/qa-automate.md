# QA Automate Command

## Purpose

User-facing entry point for turning approved scenarios into automation strategy or scoped implementation guidance.

## When to use

- Use after scenarios are approved.
- Use when automation guidance is requested for a known framework.
- Use when fixture, data, locator, assertion, or validation strategy is needed.

## Inputs

- Approved test scenarios or test plan.
- Target framework and language.
- Existing conventions supplied by the consuming project.
- Data setup, cleanup, auth, and verification constraints.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution and policies.
3. Use routing rules to select `workflows/test-plan-to-automation.md`.
4. Hand off to `agents/automation-engineer.md`.
5. Apply audit-before-edit if files may change.
6. Stop at Human Gate before risky implementation.

## Outputs

- Automation strategy.
- Scoped implementation plan.
- Data, fixture, assertion, and validation plan.
- Verification plan.

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion, destructive cleanup, or undocumented behavior assumptions.

## Related agents, workflows, policies, or skills

- `agents/qa-orchestrator.md`
- `agents/automation-engineer.md`
- `workflows/test-plan-to-automation.md`
- `policies/audit-before-edit.md`
- `policies/human-gate-policy.md`

## Application-agnostic constraints

- Do not create runnable frameworks in this repository.
- Do not make Playwright the only automation path.
- Use placeholders such as `<BASE_URL>`, `<USER_EMAIL>`, and `<RESOURCE_ID>`.
