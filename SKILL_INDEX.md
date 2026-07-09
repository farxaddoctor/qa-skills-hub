# Skill Index

Use this index to choose the smallest useful skill for the task.

This repository is a reusable QA Automation Skills Hub. Skills should be loaded selectively. Do not load every skill by default. Combine skills only when the task naturally crosses boundaries.

## Core Selection Rule

Choose the skill based on the current task stage:

```text
Requirement / idea / bug -> qa-test-design
API behavior / endpoint coverage -> api-testing
Playwright TypeScript automation -> playwright-typescript
Automation code or PR review -> qa-code-review
Failure / defect / flaky behavior -> bug-analysis
Test data design -> test-data-generation
Java API implementation -> rest-assured-java
Python automation implementation -> pytest-python
```

## Skill Catalog

| Skill | Use For | Primary Outputs | Do Not Use For |
|---|---|---|---|
| `skills/qa-test-design/SKILL.md` | Turning requirements, user stories, incidents, defects, API contracts, or risk areas into test coverage | Test scenarios, edge cases, risk notes, coverage gaps, exploratory charters, regression ideas | Writing framework-specific automation code |
| `skills/playwright-typescript/SKILL.md` | Designing, reviewing, debugging, or refactoring Playwright TypeScript automation | Locator strategy, assertion strategy, fixture guidance, Page Object recommendations, flake fixes | Pure API-only test design or Java/Python implementation |
| `skills/api-testing/SKILL.md` | Designing language-neutral API test coverage | Contract checks, status/body/schema/header assertions, auth/RBAC cases, negative cases, data strategy | Browser-only UI automation or framework-specific code by itself |
| `skills/rest-assured-java/SKILL.md` | Creating or reviewing Java API automation with Rest Assured | JUnit 5 + Rest Assured structure, request/response specs, assertions, client patterns | Language-neutral API coverage before behavior is clear |
| `skills/pytest-python/SKILL.md` | Creating or reviewing Python automation with Pytest | Fixture design, parametrization, assertions, maintainability guidance | Java-specific automation or browser-only Playwright TypeScript work |
| `skills/qa-code-review/SKILL.md` | Reviewing automated tests and QA framework changes | Findings by severity, risk analysis, missing coverage, maintainability comments, safe refactor notes | Original test design without code or diff |
| `skills/bug-analysis/SKILL.md` | Analyzing failures, defects, flaky tests, CI failures, or regression reports | Reproduction analysis, suspected cause, diagnostic next steps, product bug vs test issue judgment | Writing full test plans from requirements |
| `skills/test-data-generation/SKILL.md` | Designing synthetic, boundary, negative, and privacy-safe test data | Test data sets, equivalence classes, boundary values, invalid data, data isolation guidance | Full automation implementation by itself |

## Recommended Combinations

Use one skill when possible. Combine skills only when the task needs both perspectives.

| Task | Recommended Skills |
|---|---|
| Test plan from requirements | `qa-test-design` |
| Manual test cases from acceptance criteria | `qa-test-design` |
| API coverage from OpenAPI/contract | `api-testing` |
| API automation in Java | `api-testing` + `rest-assured-java` |
| API automation in Python | `api-testing` + `pytest-python` |
| Playwright E2E implementation | `qa-test-design` first if scenarios are unclear, then `playwright-typescript` |
| Playwright test review | `playwright-typescript` + `qa-code-review` |
| Framework refactor review | implementation skill + `qa-code-review` |
| Bug reproduction and regression ideas | `bug-analysis` + `qa-test-design` |
| Regression tests for an API bug | `bug-analysis` + `api-testing` |
| Test data for negative/boundary cases | `qa-test-design` + `test-data-generation` |
| Flaky Playwright test investigation | `bug-analysis` + `playwright-typescript` + `qa-code-review` |

## Skill Usage Workflow

### 1. Start with intent

Before choosing a skill, identify the task type:

- Design
- Implementation guidance
- Code review
- Debugging
- Refactoring
- Bug analysis
- Test data generation

### 2. Load the smallest useful skill set

Do not load unrelated skills. For example:

- Do not load `rest-assured-java` for Playwright-only work.
- Do not load `playwright-typescript` for API-only coverage.
- Do not load `bug-analysis` unless there is a failure, defect, flaky behavior, or regression report.
- Do not load `qa-code-review` unless there is code, a diff, or a framework change to review.

### 3. Keep project-specific context separate

This repository must stay application-agnostic.

Project-specific context belongs in the consuming project, such as:

- Application URL
- Test users and roles
- Environment variables
- API base URL
- Existing fixtures
- Existing Page Objects
- Existing API clients
- Domain entities
- Product-specific business rules

### 4. Use standards as support

Standards files support skills but do not replace them.

Examples:

- `standards/testing-standards.md`
- `standards/automation-standards.md`
- `standards/playwright-standards.md`
- `standards/api-testing-standards.md`
- `standards/typescript-standards.md`
- `standards/java-standards.md`
- `standards/python-standards.md`

### 5. Ask for confirmation when required context is missing

If the task lacks requirements, expected behavior, API contract, code, or failure evidence, the agent must state assumptions and open questions instead of inventing product behavior.

## Orchestration Layers

Use the orchestration layer when the work needs more than one skill.

| Layer | Location | Purpose |
|---|---|---|
| Skills | `skills/` | Reusable QA capabilities. |
| Agents | `agents/` | Role definitions with responsibilities, inputs, outputs, and handoffs. |
| Commands | `commands/` | User-facing entry points such as design, automate, audit, review, debug, and bug report. |
| Workflows | `workflows/` | Multi-step QA processes with stop conditions and handoff formats. |
| Routing | `routing/skill-routing-rules.md` | Decision rules for choosing agents, workflows, and skills. |
| Policies | `policies/` | Safety rules for editing, leakage prevention, refactoring, and evidence. |

### Agent routing quick map

| Situation | Agent | Primary skill |
|---|---|---|
| Requirements unclear | `agents/test-designer.md` | `skills/qa-test-design/SKILL.md` |
| API contract provided | `agents/api-test-engineer.md` | `skills/api-testing/SKILL.md` |
| Playwright TypeScript automation requested | `agents/automation-engineer.md` | `skills/playwright-typescript/SKILL.md` |
| Code or generated tests need review | `agents/qa-code-reviewer.md` | `skills/qa-code-review/SKILL.md` |
| Failure or flaky behavior reported | `agents/bug-analyst.md` | `skills/bug-analysis/SKILL.md` |

## Skill Resolution Check

When a user asks an agent to use a skill, the agent should first confirm:

```text
Skill files read:
- path/to/skill/SKILL.md

Supporting standards read:
- path/to/standard.md

Task mode:
- design / implementation / review / debugging / refactor

Scope:
- files or feature area being analyzed
```

If the requested skill file cannot be found in the consuming project, the agent should stop and report that the skill is not linked or not available.

## Common Usage Examples

### Test design

```text
Use the QA test design skill.
Create test scenarios from these acceptance criteria.
Include positive, negative, boundary, permission, regression cases, assumptions, and open questions.
Do not write automation code.
```

### Playwright audit

```text
Use the Playwright TypeScript and QA code review skills.

Before auditing, confirm the exact skill file paths you read.

Audit this Playwright project for:
1. waitForTimeout usage
2. weak selectors
3. Page Object quality
4. fixture usage
5. API login/auth pattern
6. test independence
7. smoke/full tagging

Do not edit files yet.
Return findings with risk level and safe-to-refactor status.
```

### API coverage

```text
Use the API testing skill.
Design API test coverage for this endpoint contract.
Return a coverage matrix with positive, negative, auth, authorization, schema, state, and regression checks.
Do not write framework-specific code yet.
```

### API implementation in Java

```text
Use the API testing skill with the Rest Assured Java skill.
Turn this API coverage matrix into JUnit 5 + Rest Assured implementation guidance.
Follow the consuming project's existing client and fixture patterns.
```

### Code review

```text
Use the QA code review skill.
Review this automated test diff.
Return findings first, ordered by severity.
Focus on test value, weak assertions, flake risk, data isolation, and maintainability.
Do not suggest broad refactors unless they directly affect reliability or test value.
```

### Bug to regression

```text
Use the bug analysis and QA test design skills.
Analyze this defect report and create regression scenarios.
Include the original failure condition, expected fixed behavior, suggested test level, and priority.
```

## Selection Rules

- Start with the domain skill.
- Add a framework or language skill only if implementation guidance is needed.
- Add `qa-code-review` only when reviewing code, diffs, framework changes, or generated tests.
- Add `bug-analysis` only when there is a defect, failure, flaky behavior, CI failure, or regression report.
- Add `test-data-generation` when the main challenge is valid, invalid, boundary, synthetic, or privacy-safe data.
- Do not use framework skills to invent requirements.
- Do not use this skills hub as a place for product-specific context.
- Do not add Selenium-related skills yet unless the project scope changes.

## Current Priority Skills

The strongest and most actively maintained skills are:

1. `skills/qa-test-design/SKILL.md`
2. `skills/playwright-typescript/SKILL.md`
3. `skills/api-testing/SKILL.md`
4. `skills/qa-code-review/SKILL.md`

The following skills are currently lightweight placeholders and should be expanded only when needed:

- `skills/rest-assured-java/SKILL.md`
- `skills/pytest-python/SKILL.md`
- `skills/bug-analysis/SKILL.md`
- `skills/test-data-generation/SKILL.md`
