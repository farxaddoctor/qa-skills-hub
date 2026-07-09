# API Contract To Tests Workflow

## Purpose

Convert an API contract or endpoint description into API test coverage and implementation-ready guidance.

## When to use

- Use when an API contract, endpoint behavior, or request/response examples are provided.
- Use when API coverage or API automation guidance is requested.

## Inputs

- Endpoint method, route placeholder, operation, or contract section.
- Request and response schema or examples.
- Auth, authorization, validation, state, side-effect, pagination, filtering, and cleanup rules when applicable.

## Process

1. Apply Constitution, leakage policy, routing rules, and Human Gate policy.
2. Identify documented contract rules and open questions.
3. Build coverage by positive, negative, schema, auth, authorization, state, side-effect, and regression categories.
4. Define data setup, cleanup, and isolation.
5. Produce a coverage matrix.
6. Apply `policies/audit-before-edit.md` before any file modification or implementation handoff.
7. Hand off to implementation only if target framework is requested and approved.

## Outputs

- API coverage matrix.
- Contract questions.
- Data strategy.
- Suggested test level.
- Framework handoff only when requested.

## Human Gate conditions

Human approval is required before assuming undocumented status codes, response shapes, permission behavior, auth/session changes, dependency changes, CI/CD changes, global config changes, deletion, or destructive cleanup.

## Related agents, workflows, policies, or skills

- `agents/api-test-engineer.md`
- `agents/test-designer.md`
- `workflows/test-plan-to-automation.md`
- `policies/no-product-specific-leakage.md`
- `skills/api-testing/SKILL.md`
- `skills/test-data-generation/SKILL.md`

## Application-agnostic constraints

- Use placeholders such as `<API_ENDPOINT>`, `<RESOURCE_ID>`, `<TOKEN>`, and `<ROLE_NAME>`.
- Do not include real base URLs, tokens, payloads with customer data, or product-specific roles.
- Do not assume one API framework.
