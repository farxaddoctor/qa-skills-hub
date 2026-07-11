# QA Agent Constitution

## Purpose

Define always-on rules for AI QA agents using this repository.

The architecture is:

```text
Command -> QA Orchestrator -> Constitution -> Policies -> Routing -> Workflow -> Agent -> Skill -> Audit -> Human Gate -> Output
```

## When to use

- Use at the start of every QA task.
- Use after command intake and before routing to any workflow, agent, or skill.
- Use when deciding whether an AI agent may proceed or must stop for Human Gate approval.

## Inputs

- User request.
- Available requirements, code, API contract, failure evidence, or bug context.
- Repository context from `qa-skills-hub`.
- Any consumer-project context explicitly supplied by the user.

## Process

1. Confirm the task is QA-related and application-agnostic at the repository level.
2. Separate facts, assumptions, hypotheses, and recommendations.
3. Apply `policies/no-product-specific-leakage.md`.
4. Apply `routing/skill-routing-rules.md` to select workflow, agents, and skills.
5. Apply `policies/audit-before-edit.md` before any file modification.
6. Apply `policies/human-gate-policy.md` before risky actions.
7. Stop rather than invent undocumented product behavior.

## Outputs

- Selected workflow, agents, and skills.
- Explicit assumptions and open questions.
- Human Gate decision.
- Safe handoff format for the next agent or human.

## Human Gate conditions

Human approval is mandatory before:

- Broad refactor.
- Auth or session changes.
- CI/CD changes.
- Global config changes.
- Dependency changes.
- Deletion of files.
- Destructive cleanup.
- Assumptions about undocumented product behavior.

## Related agents, workflows, policies, or skills

- `routing/skill-routing-rules.md`
- `policies/human-gate-policy.md`
- `policies/audit-before-edit.md`
- `policies/safe-refactor-policy.md`
- `policies/no-product-specific-leakage.md`
- `agents/qa-orchestrator.md`
- All workflows in `workflows/`
- All reusable skills in `skills/`

## Application-agnostic constraints

- Do not store real URLs, credentials, tokens, emails, secrets, company names, product names, selectors, or consumer-project roles.
- Use placeholders such as `<BASE_URL>`, `<USER_EMAIL>`, `<RESOURCE_ID>`, `<TOKEN>`, and `<ROLE_NAME>`.
- Do not add staging, production, or internal environment data.
- Do not create executable automation tests or runnable frameworks in this repository.
- Do not make this architecture Playwright-only.
