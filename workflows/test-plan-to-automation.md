# Test Plan To Automation Workflow

## Purpose

Turn an approved test plan into automation strategy or scoped implementation guidance.

## When to use

- Use after test scenarios are approved.
- Use when automation is requested and the target framework is known.
- Use when fixture, data, locator, assertion, and validation strategy are needed.

## Inputs

- Approved scenarios or test plan.
- Target framework and language.
- Existing project conventions supplied by the consuming project.
- Data setup, cleanup, authentication, and verification constraints.

## Process

1. Apply Constitution, routing, audit-before-edit, safe-refactor, and leakage policies.
2. Confirm scenarios are complete enough to automate.
3. Identify fixtures, data setup, cleanup, locator strategy, assertions, and validation.
4. Select reusable skills through routing.
5. Prepare scoped implementation guidance.
6. Stop for Human Gate approval before risky implementation.

## Outputs

- Automation strategy.
- Data and fixture plan.
- Assertion and validation plan.
- Scoped implementation plan.
- Verification plan and Human Gate decision.

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion of files, destructive cleanup, or undocumented behavior assumptions.

## Related agents, workflows, policies, or skills

- `agents/automation-engineer.md`
- `agents/api-test-engineer.md`
- `agents/qa-code-reviewer.md`
- `workflows/automation-review.md`
- `policies/audit-before-edit.md`
- `policies/safe-refactor-policy.md`
- `skills/playwright-typescript/SKILL.md`
- `skills/api-testing/SKILL.md`

## Application-agnostic constraints

- Do not add runnable tests to this repository.
- Do not make Playwright the only automation path.
- Use placeholders for URLs, users, resource ids, tokens, and roles.
