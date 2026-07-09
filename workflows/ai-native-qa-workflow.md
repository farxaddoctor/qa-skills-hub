# AI-Native QA Workflow

## Purpose

Define the default end-to-end QA orchestration process for AI agents.

## When to use

- Use for any multi-step QA request.
- Use when the request needs more than one agent, workflow, or skill.
- Use when the agent must move from intake to design, automation strategy, review, and Human Gate approval.

## Inputs

- User request.
- Requirement, test plan, code, API contract, failure evidence, or bug report.
- Known constraints and requested output.

## Process

1. Intake: capture request, task mode, target artifact, and constraints.
2. Requirement clarification: separate confirmed behavior from assumptions and open questions.
3. Test design: create scenarios, priorities, and suggested test levels.
4. Automation strategy: identify framework, fixtures, data, locators, assertions, and cleanup.
5. Implementation plan: define scoped edits, affected files, validation, and risks.
6. Code generation or refactor: proceed only after audit-before-edit and required Human Gate approvals.
7. QA code review: review generated or changed automation for test value, reliability, maintainability, and leakage.
8. Human approval and verification: pause at Human Gate checkpoints and report validation results.

Every phase starts with Constitution and policy checks.

## Outputs

- Selected workflow path.
- Selected agents and skills.
- Assumptions and open questions.
- Human Gate decision.
- Verification or handoff notes.

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion of files, destructive cleanup, or assumptions about undocumented product behavior.

## Related agents, workflows, policies, or skills

- `constitution/qa-agent-constitution.md`
- `routing/skill-routing-rules.md`
- `policies/human-gate-policy.md`
- `policies/audit-before-edit.md`
- All agents in `agents/`
- All reusable skills in `skills/`

## Application-agnostic constraints

- Do not make the architecture Playwright-only.
- Do not use real URLs, credentials, emails, tokens, company names, selectors, or consumer-project roles.
- Use placeholders such as `<BASE_URL>`, `<USER_EMAIL>`, and `<RESOURCE_ID>`.
- Do not create executable automation tests or runnable frameworks.
