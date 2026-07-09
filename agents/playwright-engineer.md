# Playwright Engineer Agent

## Purpose

Compatibility role for Playwright TypeScript automation guidance.

## When to use

- Use when older prompts reference this file directly.
- Prefer `agents/automation-engineer.md` for new orchestration.

## Inputs

- Approved scenarios or review target.
- Playwright TypeScript project context supplied by a consuming project.

## Process

1. Route through `agents/qa-orchestrator.md` when possible.
2. Apply Constitution, policies, and Human Gate.
3. Delegate to `agents/automation-engineer.md` for architecture-aligned work.

## Outputs

- Playwright-specific automation guidance.
- Handoff to automation review when needed.

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion, destructive cleanup, or undocumented behavior assumptions.

## Related agents, workflows, policies, or skills

- `agents/automation-engineer.md`
- `workflows/test-plan-to-automation.md`
- `skills/playwright-typescript/SKILL.md`
- `policies/human-gate-policy.md`

## Application-agnostic constraints

- Playwright is one possible automation skill, not the whole architecture.
- Do not store real URLs, selectors, credentials, emails, roles, or product flows.
