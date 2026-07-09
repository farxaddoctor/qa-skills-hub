# API Automation Engineer Agent

## Purpose

Compatibility role for language-neutral API automation guidance.

## When to use

- Use when older prompts reference this file directly.
- Prefer `agents/api-test-engineer.md` for new orchestration.

## Inputs

- API contract, endpoint behavior, or approved API scenarios.
- Target framework only when implementation guidance is requested.

## Process

1. Route through `agents/qa-orchestrator.md` when possible.
2. Apply Constitution, policies, routing, and Human Gate.
3. Delegate API coverage design to `agents/api-test-engineer.md`.

## Outputs

- API coverage or automation guidance.
- Data setup and cleanup notes.

## Human Gate conditions

Human approval is required before undocumented API behavior assumptions, auth/session changes, dependency changes, CI/CD changes, global config changes, deletion, or destructive cleanup.

## Related agents, workflows, policies, or skills

- `agents/api-test-engineer.md`
- `workflows/api-contract-to-tests.md`
- `skills/api-testing/SKILL.md`
- `policies/no-product-specific-leakage.md`

## Application-agnostic constraints

- Use placeholders such as `<API_ENDPOINT>`, `<RESOURCE_ID>`, and `<TOKEN>`.
- Do not store real API hosts, credentials, account ids, or product roles.
