# Audit Before Edit Policy

## Purpose

Require agents to inspect context and define risk before modifying files.

## When to use

- Use before modifying tests, fixtures, helpers, Page Objects, API clients, workflows, policies, commands, or shared utilities.
- Use before refactoring or generating code in a consumer project.

## Inputs

- Requested change.
- Relevant files or artifact paths.
- Expected behavior and current behavior.
- Existing conventions and verification commands.

## Process

1. Inspect relevant files before proposing edits.
2. Identify current pattern, scope, and behavior under test.
3. List risks, assumptions, and rollback considerations.
4. Decide whether Human Gate approval is required.
5. Define post-change validation.
6. Edit only within approved scope.

## Outputs

```text
Reviewed scope:
Current behavior:
Proposed change:
Risks:
Rollback thinking:
Validation:
Human Gate required:
```

## Human Gate conditions

Human approval is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, deletion of files, destructive cleanup, or assumptions about undocumented behavior.

## Related agents, workflows, policies, or skills

- `constitution/qa-agent-constitution.md`
- `policies/human-gate-policy.md`
- `policies/safe-refactor-policy.md`
- `agents/qa-code-reviewer.md`
- `workflows/automation-review.md`

## Application-agnostic constraints

- Do not inspect or copy real secrets into this repository.
- Do not store consumer-project URLs, selectors, roles, or business flows here.
- Use placeholders such as `<BASE_URL>`, `<USER_EMAIL>`, and `<RESOURCE_ID>` in examples.
