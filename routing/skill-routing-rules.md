# Skill Routing Rules

## Purpose

Map user intent to workflow, agent, and reusable skills.

## When to use

- Use after applying `constitution/qa-agent-constitution.md`.
- Use before loading skills or selecting an agent.
- Use whenever a user request includes design, automation, review, debugging, bug reporting, audit, or refactor intent.

## Inputs

- User request.
- Available artifacts: requirement, test plan, code, diff, API contract, failure log, trace, or bug report.
- Known constraints and requested output.

## Process

1. Apply Constitution and policies.
2. Classify user intent.
3. Select one primary workflow.
4. Select one primary agent.
5. Load only the required skills.
6. Apply audit-before-edit when file changes may happen.
7. Apply Human Gate before risky actions.

## Outputs

```text
Intent:
Workflow:
Primary agent:
Skills:
Policies:
Human Gate required:
Stop condition:
Expected output:
```

## Human Gate conditions

Human Gate is required before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, file deletion, destructive cleanup, or assumptions about undocumented product behavior.

## Related agents, workflows, policies, or skills

| User intent              | Workflow                                                          | Agent                                                  | Skills                                                           |
| ------------------------ | ----------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------- |
| Test design              | `workflows/requirement-to-test-plan.md`                           | `agents/test-designer.md`                              | `skills/qa-test-design/SKILL.md`                                 |
| Automation planning      | `workflows/test-plan-to-automation.md`                            | `agents/automation-engineer.md`                        | Framework skill selected by context                              |
| API testing              | `workflows/test-plan-to-automation.md` or API-focused design path | `agents/api-test-engineer.md`                          | `skills/api-testing/SKILL.md`                                    |
| Code review              | `workflows/automation-review.md`                                  | `agents/qa-code-reviewer.md`                           | `skills/qa-code-review/SKILL.md`                                 |
| Bug regression           | `workflows/bug-to-regression.md`                                  | `agents/bug-analyst.md` then `agents/test-designer.md` | `skills/bug-analysis/SKILL.md`, `skills/qa-test-design/SKILL.md` |
| Flaky test investigation | `workflows/flaky-test-investigation.md`                           | `agents/bug-analyst.md`                                | `skills/bug-analysis/SKILL.md`, framework skill if needed        |
| QA audit                 | `workflows/automation-review.md`                                  | `agents/qa-code-reviewer.md`                           | `skills/qa-code-review/SKILL.md`                                 |

Routing examples:

- Unclear requirements -> `agents/test-designer.md`.
- Implementation requested but scenarios missing -> stop and run `workflows/requirement-to-test-plan.md`.
- Existing code review requested -> `agents/qa-code-reviewer.md`.
- Failure or flaky behavior reported -> `agents/bug-analyst.md`.
- API contract provided -> `agents/api-test-engineer.md`.
- Playwright TypeScript implementation requested -> `agents/automation-engineer.md` with `skills/playwright-typescript/SKILL.md`.

## Application-agnostic constraints

- Do not route based on product-specific role names, URLs, selectors, or domains.
- Playwright is one possible automation skill, not the architecture.
- Use placeholders only when examples are needed.

# Skill status

This skill is reserved for future implementation.

Do not route active tasks to this skill yet.
Use it only as a placeholder until the skill is fully defined.

Performance and security testing skills are reserved capabilities unless their SKILL.md files are fully implemented.
