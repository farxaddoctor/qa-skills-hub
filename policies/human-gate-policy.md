# Human Gate Policy

## Purpose

Define mandatory approval checkpoints for AI QA agents.

## When to use

- Use before any risky edit, refactor, deletion, configuration change, or assumption about undocumented product behavior.
- Use when an agent is unsure whether the requested action changes shared behavior or trust boundaries.

## Inputs

- Proposed action.
- Files, workflows, or areas affected.
- Known risks and rollback options.
- Evidence supporting the action.

## Process

1. Classify the approval level.
2. State the proposed action and risk.
3. Provide a safer alternative when available.
4. Stop until approval is explicit.
5. Proceed only within the approved scope.

## Outputs

- Approval level.
- Risk statement.
- Approval request.
- Approved scope or stop decision.

## Human Gate conditions

Approval levels:

- Level 0: no approval needed for read-only analysis, routing, or documentation-only planning.
- Level 1: approval required for scoped file edits in a consumer project.
- Level 2: approval required for shared utilities, fixtures, Page Objects, API clients, or framework behavior.
- Level 3: approval required for broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion of files, destructive cleanup, or undocumented product assumptions.

The agent must stop and ask for approval before:

- Editing files when scope is unclear.
- Deleting files.
- Changing CI/CD.
- Adding or updating dependencies.
- Modifying shared utilities.
- Modifying auth/session behavior.
- Using real credentials or secrets.
- Treating undocumented behavior as confirmed.

## Related agents, workflows, policies, or skills

- `constitution/qa-agent-constitution.md`
- `policies/audit-before-edit.md`
- `policies/safe-refactor-policy.md`
- `routing/skill-routing-rules.md`
- `agents/qa-orchestrator.md`

## Application-agnostic constraints

- Approval requests must use generic placeholders only.
- Do not include real credentials, tokens, emails, URLs, company names, product names, selectors, or consumer-project roles.
- Do not use Human Gate approval to bypass this repository's no-leakage policy.
