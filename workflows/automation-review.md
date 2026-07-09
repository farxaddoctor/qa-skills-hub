# Automation Review Workflow

## Purpose

Review automated tests, generated tests, QA framework changes, or automation plans before merge or refactor.

## When to use

- Use when code, a diff, generated tests, or framework changes exist.
- Use for QA audit, PR review, or risk assessment.
- Use after code generation or refactor in the AI-native workflow.

## Inputs

- Code, diff, changed files, generated tests, or review target.
- Purpose of the change or linked requirement/defect.
- Test results, logs, traces, screenshots, or CI output if available.

## Process

1. Apply Constitution, leakage, audit-before-edit, and Human Gate policies.
2. Inspect the review target before judging.
3. Identify intended behavior and changed surface.
4. Review assertions, setup, cleanup, data isolation, flake risk, and coverage.
5. Classify findings by severity.
6. Recommend fixes only when tied to reliability, correctness, or test value.

## Outputs

- Findings first, ordered by severity.
- Evidence and affected files when available.
- Impact and fix direction.
- Missing coverage and residual risk.
- Verification recommendations.

## Human Gate conditions

Human approval is required before recommending or applying broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion, destructive cleanup, or undocumented behavior assumptions.

## Related agents, workflows, policies, or skills

- `agents/qa-code-reviewer.md`
- `agents/automation-engineer.md`
- `workflows/test-plan-to-automation.md`
- `policies/audit-before-edit.md`
- `policies/safe-refactor-policy.md`
- `skills/qa-code-review/SKILL.md`

## Application-agnostic constraints

- Do not include real product names, URLs, credentials, selectors, emails, or consumer-project roles.
- Do not weaken assertions to hide failures.
- Do not request broad style refactors unrelated to QA value.
