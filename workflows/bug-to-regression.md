# Bug To Regression Workflow

## Purpose

Turn a defect, incident, or failure analysis into evidence-based regression coverage.

## When to use

- Use when a bug report or incident needs regression scenarios.
- Use after failure analysis identifies a likely defect or behavior gap.
- Use when a fix needs targeted regression coverage.

## Inputs

- Defect summary.
- Expected behavior and actual behavior.
- Reproduction steps or failure evidence.
- Known fixed behavior, if available.

## Process

1. Apply Constitution, evidence policy, leakage policy, and Human Gate policy.
2. Separate evidence from hypotheses.
3. Identify original failure condition and expected fixed behavior.
4. Classify likely cause or mark it unknown.
5. Design minimal regression scenarios.
6. Apply `policies/audit-before-edit.md` before any file modification or implementation handoff.
7. Recommend test level and automation handoff.

## Outputs

- Failure summary.
- Evidence-based regression scenario matrix.
- Suggested test level and priority.
- Open questions and diagnostics.
- Handoff to test design, API testing, or automation.

## Human Gate conditions

Human approval is required before assuming undocumented expected behavior, treating unclear evidence as root cause, destructive cleanup, deletion, or auth/session, CI/CD, config, or dependency changes.

## Related agents, workflows, policies, or skills

- `agents/bug-analyst.md`
- `agents/test-designer.md`
- `workflows/flaky-test-investigation.md`
- `workflows/requirement-to-test-plan.md`
- `policies/evidence-and-citation-policy.md`
- `skills/bug-analysis/SKILL.md`
- `skills/qa-test-design/SKILL.md`

## Application-agnostic constraints

- Do not store real logs containing secrets or customer data.
- Use placeholders for identifiers, URLs, users, and resources.
- Do not invent product rules from incomplete evidence.
