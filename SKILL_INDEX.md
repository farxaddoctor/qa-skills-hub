# Skill Index

Use this index to choose the smallest useful skill for the task. Combine skills only when the task naturally crosses boundaries.

| Skill | Use For | Primary Outputs |
| --- | --- | --- |
| `skills/qa-test-design/SKILL.md` | Turning requirements, user stories, incidents, or risk areas into test coverage | Test scenarios, edge cases, risk notes, coverage gaps |
| `skills/playwright-typescript/SKILL.md` | Designing or reviewing Playwright TypeScript automation | Test structure guidance, locator strategy, fixture/page-object recommendations |
| `skills/api-testing/SKILL.md` | Designing API test coverage independent of implementation language | Contract, status code, schema, auth, data, and negative test ideas |
| `skills/rest-assured-java/SKILL.md` | Creating or reviewing Java API automation with Rest Assured | Java API test guidance, request/response patterns, assertions |
| `skills/pytest-python/SKILL.md` | Creating or reviewing Python automation with Pytest | Fixture design, parametrization, assertions, maintainability guidance |
| `skills/qa-code-review/SKILL.md` | Reviewing automated tests and QA framework changes | Review findings, risks, maintainability comments, test gaps |
| `skills/bug-analysis/SKILL.md` | Analyzing failures, defects, flaky tests, or regression reports | Reproduction analysis, suspected cause, diagnostic next steps |
| `skills/test-data-generation/SKILL.md` | Designing synthetic, boundary, and negative test data | Data sets, equivalence classes, privacy-safe generation guidance |

## Recommended Combinations

- Test plan from requirements: `qa-test-design`
- Playwright test implementation review: `playwright-typescript` + `qa-code-review`
- API automation design: `api-testing` + either `rest-assured-java` or `pytest-python`
- Bug reproduction and report: `bug-analysis` + `test-data-generation`
- Framework refactor review: implementation skill + `qa-code-review`

## Selection Rules

- Start with the domain skill, then add a language/framework skill only if implementation guidance is needed.
- Use standards files as supporting context, not as replacements for skills.
- Keep project-specific facts outside this repository unless they are examples in a consuming project.
