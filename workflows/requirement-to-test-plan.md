# Requirement To Test Plan Workflow

## Purpose

Convert requirements, acceptance criteria, workflows, incidents, or defects into a clear QA test plan.

## When to use

- Use when requirements are unclear or incomplete.
- Use before automation when scenarios are missing.
- Use when a user asks for test cases, coverage, or test design.

## Inputs

- Requirement, acceptance criteria, workflow, incident, or defect summary.
- Expected behavior and constraints.
- Known risks, supported surfaces, or existing coverage.

## Process

1. Apply Constitution and leakage policy.
2. Clarify confirmed behavior, assumptions, and open questions.
3. Group coverage by workflow, rule, risk, or contract area.
4. Add positive, negative, boundary, permission, data, state, integration, and regression cases where relevant.
5. Assign priority and suggested test level.
6. Apply `policies/audit-before-edit.md` before any file modification or implementation handoff.
7. Produce a handoff for automation, API testing, review, or bug analysis.

## Outputs

- Test design summary.
- Scenario matrix.
- Risk and priority notes.
- Suggested test levels.
- Open questions.

## Human Gate conditions

Human approval is required before treating undocumented behavior as confirmed, moving from assumed scenarios to implementation, or storing consumer-project details in this repository.

## Related agents, workflows, policies, or skills

- `agents/test-designer.md`
- `agents/qa-orchestrator.md`
- `workflows/test-plan-to-automation.md`
- `policies/no-product-specific-leakage.md`
- `skills/qa-test-design/SKILL.md`
- `skills/test-data-generation/SKILL.md`

## Application-agnostic constraints

- Do not use real product names, URLs, credentials, emails, selectors, or consumer-project roles.
- Use placeholders only.
- Do not write automation code in this workflow.
