# Create API Tests Command

## Purpose

Compatibility command for API coverage or API automation guidance.

## When to use

- Use when older prompts ask to create API tests.
- Prefer `commands/qa-design.md` for API coverage or `commands/qa-automate.md` for approved implementation guidance.

## Inputs

- API contract, endpoint behavior, examples, or approved API scenarios.
- Target framework only when implementation guidance is requested.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution, routing, and policies.
3. Hand off to `agents/api-test-engineer.md`.
4. Stop at Human Gate before risky changes.

## Outputs

- API coverage matrix.
- Data strategy.
- Framework handoff if requested.

## Human Gate conditions

Human approval is required before undocumented API behavior assumptions, auth/session changes, dependency changes, CI/CD changes, global config changes, deletion, or destructive cleanup.

## Related agents, workflows, policies, or skills

- `agents/api-test-engineer.md`
- `workflows/api-contract-to-tests.md`
- `commands/qa-design.md`
- `commands/qa-automate.md`

## Application-agnostic constraints

- Use placeholders such as `<API_ENDPOINT>`, `<RESOURCE_ID>`, and `<TOKEN>`.
- Do not store real hosts, credentials, payloads with customer data, or product roles.
