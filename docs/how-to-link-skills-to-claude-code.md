# How To Link Skills To Claude Code

This repository can be used as a local instruction library for Claude Code. The safest pattern is to reference the relevant files from the consuming project rather than copying product-specific context back into this repository.

## Recommended Setup

1. Keep `qa-skills-hub` in a stable local path.
2. In the consuming project, tell Claude Code which skill to use.
3. Provide the relevant skill file and standards file as context.
4. Keep project-specific details in the consuming project prompt, issue, or repository files.

## Example Prompts

```text
Use the QA skill at ../qa-skills-hub/skills/qa-test-design/SKILL.md.
Create test scenarios for this requirement. Do not write automation yet.
```

```text
Use:
- ../qa-skills-hub/skills/playwright-typescript/SKILL.md
- ../qa-skills-hub/standards/playwright-standards.md

Review this Playwright test for flakiness, selector quality, assertions, and maintainability.
```

```text
Use:
- ../qa-skills-hub/skills/api-testing/SKILL.md
- ../qa-skills-hub/templates/api-test-template.md

Design API coverage for this endpoint contract. Include negative and authorization scenarios.
```

## Suggested Claude Code Workflow

1. Start from `SKILL_INDEX.md`.
2. Select one skill.
3. Add a standard file only if it is relevant.
4. Give Claude Code the task and the consuming project's actual files.
5. Ask Claude Code to list assumptions and open questions.
6. Review generated test cases, code, or comments before merging.

## What Not To Do

- Do not paste staging URLs, credentials, account names, or company-specific rules into this repository.
- Do not store generated application tests in this repository.
- Do not copy third-party material without filling in `docs/source-attribution.md`.
- Do not use this repository as a replacement for project-level QA strategy.

## Keeping Skills Universal

When a project needs custom behavior, add that context to the consuming project. If a lesson is broadly useful, generalize it before adding it here.
