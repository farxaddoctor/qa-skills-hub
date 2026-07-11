# Validation Layer

## Purpose

The validation layer defines architecture acceptance specifications for `qa-skills-hub`.

It verifies that AI QA work follows:

```text
Command -> QA Orchestrator -> Constitution -> Policies -> Routing -> Workflow -> Agent -> Skill -> Audit -> Human Gate -> Output
```

Validation files check expected orchestration behavior for Claude Code, Codex, Cursor, and other compatible agents that can read repository instructions.

## What Validation Files Are

Validation files are architecture acceptance specifications. They are not executable product tests, automation suites, or consumer-project tests.

They describe:

- Expected command routing.
- Required policies.
- Expected workflows, agents, and skills.
- Human Gate behavior.
- Leakage prevention behavior.
- Compatibility delegation.
- Expected output and forbidden behavior.

## Result Definitions

PASS: routing, policies, output, and stop conditions match expectations.

FAIL: the agent bypasses orchestration, selects incorrect components, leaks product data, or performs forbidden actions.

BLOCKED: required input or evidence is missing and the workflow cannot safely proceed.

HUMAN_APPROVAL_REQUIRED: the route is correct, but the Human Gate prevents execution until explicit approval.

## Common Test-Case Format

Every validation case uses this format:

```text
ID:
Purpose:
Input:
Expected command:
Expected workflow:
Expected primary agent:
Expected skills:
Required policies:
Human Gate:
Expected output:
Forbidden behavior:
Pass criteria:
```

Use generic placeholders only. Do not include real URLs, credentials, emails, company names, product names, selectors, account data, or business-specific roles.

## How To Evaluate A Scenario

1. Read the user request or proposed agent behavior.
2. Identify the intended command.
3. Confirm the request routes through `agents/qa-orchestrator.md`.
4. Confirm Constitution and relevant policies are applied.
5. Confirm `routing/skill-routing-rules.md` selects one primary workflow and one primary agent unless a sequential handoff is explicitly required.
6. Confirm skills are selected only after routing.
7. Confirm audit-before-edit and leakage checks are applied when relevant.
8. Confirm Human Gate behavior matches `policies/human-gate-policy.md`.
9. Compare output and stop conditions with the validation case.
10. Assign `PASS`, `FAIL`, `BLOCKED`, or `HUMAN_APPROVAL_REQUIRED`.

## Validation Files

- `validation/orchestration-acceptance-tests.md`
- `validation/routing-test-cases.md`
- `validation/human-gate-test-cases.md`
- `validation/leakage-test-cases.md`
- `validation/compatibility-test-cases.md`

## Related Standard

- `standards/agent-handoff-standard.md`
