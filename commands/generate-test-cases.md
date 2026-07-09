# Generate Test Cases Command

## Purpose

Compatibility command for QA design requests.

## When to use

- Use when older prompts ask to generate test cases.
- Prefer `commands/qa-design.md` for new orchestration.

## Inputs

- Requirement, acceptance criteria, defect, workflow, or contract.
- Expected behavior and constraints.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution, routing, and policies.
3. Delegate to `commands/qa-design.md`.

## Outputs

- Scenario matrix.
- Expected results.
- Assumptions and open questions.

## Human Gate conditions

Human approval is required before undocumented behavior assumptions or implementation handoff.

## Related agents, workflows, policies, or skills

- `commands/qa-design.md`
- `agents/test-designer.md`
- `workflows/requirement-to-test-plan.md`
- `policies/human-gate-policy.md`

## Application-agnostic constraints

- Use placeholders only.
- Do not create executable tests.
