# QA Design Command

## Purpose

User-facing entry point for creating QA coverage from requirements, defects, workflows, or contracts.

## When to use

- Use when the user asks for test cases, test plan, coverage, or exploratory charters.
- Use before automation when scenarios are missing.

## Inputs

- Requirement, acceptance criteria, workflow, defect, incident, or contract.
- Expected behavior and constraints.
- Existing coverage if available.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution and policies.
3. Use routing rules to select `workflows/requirement-to-test-plan.md`.
4. Hand off to `agents/test-designer.md`.
5. Load reusable skills only through the selected workflow.
6. Stop at Human Gate if assumptions would become implementation decisions.

## Outputs

- Test design summary.
- Scenario matrix.
- Priorities and suggested test levels.
- Assumptions and open questions.

## Human Gate conditions

Human approval is required before treating undocumented behavior as confirmed or moving assumed scenarios into automation.

## Related agents, workflows, policies, or skills

- `agents/qa-orchestrator.md`
- `agents/test-designer.md`
- `workflows/requirement-to-test-plan.md`
- `routing/skill-routing-rules.md`
- `policies/human-gate-policy.md`

## Application-agnostic constraints

- Use placeholders only.
- Do not include real URLs, credentials, emails, selectors, roles, company names, or business flows.
- Do not write executable tests.
