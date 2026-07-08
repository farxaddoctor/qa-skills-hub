# QA Test Design Skill

## Purpose

Turn requirements, user stories, acceptance criteria, defects, incidents, API contracts, workflows, or risk areas into clear test coverage that can be used for manual testing, automation planning, exploratory testing, or review.

This skill defines what to test, why it matters, and how to structure coverage. It does not create runnable automation code.

## When to use

Use this skill when the task involves:

- Designing test cases from requirements, user stories, acceptance criteria, feature briefs, or API contracts.
- Expanding a happy path into positive, negative, edge, boundary, permission, state, data, integration, and regression coverage.
- Reviewing whether a feature has enough QA coverage.
- Creating exploratory testing charters.
- Turning a defect, incident, or production issue into regression scenarios.
- Identifying ambiguous behavior and missing requirements.
- Deciding which scenarios are suitable for manual testing, API automation, UI automation, unit testing, integration testing, or exploratory testing.
- Creating risk-based test coverage for limited testing time.

## When not to use

Do not use this skill when:

- The user needs framework-specific implementation details. Use a framework skill after test intent is clear.
- The task is only code review. Use `skills/qa-code-review/SKILL.md`.
- The task is root-cause analysis of a live failure. Use `skills/bug-analysis/SKILL.md`.
- The task is API implementation detail only. Combine with `skills/api-testing/SKILL.md`.
- No requirement, behavior, contract, defect, incident, or workflow context is available.
- The user explicitly asks for runnable automation code instead of test design.

## Required inputs

Collect or infer the following before designing coverage:

- Requirement, user story, acceptance criteria, feature brief, bug report, incident summary, API contract, or workflow description.
- Known expected behavior and business rules.
- Preconditions and entry points.
- Supported platforms, browsers, devices, roles, permissions, dependencies, and data rules when relevant.
- Validation rules, limits, field constraints, state transitions, and error handling rules.
- Existing coverage if the task is to review or improve coverage.
- Release priority, customer impact, business risk, or known defect history if risk-based prioritization is needed.

If inputs are incomplete, continue only with explicit assumptions and open questions. Do not invent product behavior.

## Operating mode

Follow this workflow unless the user explicitly requests a different format:

### 1. Understand the requirement

- Identify the feature, workflow, endpoint, rule, or defect under test.
- Separate confirmed behavior from assumptions.
- Identify missing or ambiguous requirements.
- Identify users, roles, permissions, states, data, and integrations involved.

### 2. Identify risk areas

Consider:

- Business-critical paths.
- Money, billing, payments, or irreversible actions.
- Security and permission boundaries.
- Data loss or data corruption.
- User onboarding, login, registration, or recovery flows.
- External integrations.
- High-traffic workflows.
- Complex validation or state transitions.
- Recent changes or known fragile areas.

### 3. Choose test design techniques

Use relevant techniques:

- Equivalence partitioning.
- Boundary value analysis.
- Decision table testing.
- State transition testing.
- Pairwise / combinatorial thinking.
- Negative testing.
- Error guessing.
- Role and permission matrix.
- CRUD coverage.
- Contract-based testing.
- Regression testing.
- Exploratory testing charters.

### 4. Build coverage

Group scenarios by behavior, workflow, rule, risk, or contract area.

Include where relevant:

- Positive scenarios.
- Negative scenarios.
- Edge cases.
- Boundary cases.
- Permission / RBAC cases.
- State transition cases.
- Data validation cases.
- Integration cases.
- Error handling cases.
- Regression cases.
- Exploratory charters.

### 5. Define expected results

Every scenario must have a clear expected result.

Avoid vague outcomes like:

- “works correctly”
- “system behaves as expected”
- “error is shown”

Prefer observable outcomes:

- specific validation message
- status change
- record created/updated/deleted
- permission denied
- no data persisted
- audit event created
- API response status/body/header matches contract
- UI remains on the same step
- notification is sent or not sent

### 6. Prioritize

Classify coverage as:

- Smoke
- Critical
- Regression
- Full
- Edge
- Exploratory
- Low priority

Explain priority when risk is high.

### 7. Recommend test level

When useful, classify the best level for each scenario:

- Unit
- API
- UI
- Integration
- Contract
- End-to-end
- Manual
- Exploratory
- Monitoring / production check

Do not force every scenario into UI automation.

## Test design techniques

### Equivalence partitioning

Use when inputs can be grouped into valid and invalid classes.

Example categories:

- valid email / invalid email
- supported file type / unsupported file type
- active user / blocked user
- valid token / invalid token

### Boundary value analysis

Use when fields have limits.

Check:

- minimum - 1
- minimum
- minimum + 1
- typical valid value
- maximum - 1
- maximum
- maximum + 1

Apply to:

- password length
- text fields
- numeric fields
- date ranges
- upload limits
- pagination limits
- rate limits

### Decision table testing

Use when behavior depends on multiple conditions.

Example conditions:

- user role
- account status
- feature flag
- payment status
- resource ownership
- item state

### State transition testing

Use when an object moves between statuses.

Check:

- valid transitions
- invalid transitions
- repeated transitions
- transition from deleted/archived state
- side effects after transition

Example:

```text
Draft → Submitted → Approved → Published
Draft → Cancelled
Approved → Rejected should be invalid unless documented
```

### Permission matrix

Use when roles or ownership affect behavior.

Check:

- unauthenticated user
- authenticated user without permission
- owner
- non-owner
- admin
- manager
- viewer
- wrong tenant/account/workspace

### Regression design

For each defect, create regression coverage that includes:

- original failure condition
- minimal reproduction path
- expected fixed behavior
- negative/edge variant if relevant
- best test level for regression
- whether it should be smoke or regression

## Expected output

### For test case design tasks

Return:

```text
## Test design summary

Feature / area:
Scope:
Assumptions:
Open questions:

## Test scenarios

| ID | Scenario | Type | Preconditions | Steps / Action | Expected result | Priority | Suggested level |
|---|---|---|---|---|---|---|---|

## Coverage notes

## Automation suitability

## Open questions
```

### For coverage review tasks

Return:

```text
## Coverage review

Current coverage summary:
Missing coverage:
High-risk gaps:
Low-value or duplicate coverage:
Recommended additions:
Open questions:
```

### For defect-to-regression tasks

Return:

```text
## Regression design

Defect summary:
Original failure condition:
Expected fixed behavior:

| ID | Regression scenario | Preconditions | Action | Expected result | Priority | Suggested level |
|---|---|---|---|---|---|---|

Additional edge cases:
Open questions:
```

### For exploratory testing tasks

Return:

```text
## Exploratory charters

| Charter | Goal | Data / Setup | Areas to explore | Risks | Notes |
|---|---|---|---|---|---|
```

## Rules

- Separate test design from implementation.
- Derive scenarios from stated behavior, not imagined product details.
- Make all assumptions visible.
- Prefer observable behavior, contract outcomes, and user-relevant risk.
- Cover both valid and invalid paths.
- Include boundaries for required fields, optional fields, limits, dates, timezones, numeric ranges, state transitions, and permissions where applicable.
- Consider setup, cleanup, data isolation, dependencies, and repeatability.
- Avoid combining unrelated behaviors into one large scenario.
- Keep terminology generic unless the consuming project provides domain terms.
- Identify what is best verified at unit, API, UI, integration, exploratory, or monitoring level when asked.
- Do not create runnable automation code unless another framework-specific skill is explicitly used.
- Do not invent URLs, roles, credentials, selectors, field rules, status codes, or domain entities.
- If requirements are incomplete, produce open questions and assumption-based scenarios separately.

## Anti-patterns

- Writing automation before the test intent is clear.
- Producing only happy-path cases.
- Inventing URLs, roles, credentials, selectors, business rules, or domain entities.
- Treating acceptance criteria as complete when obvious risks are missing.
- Using vague expected results such as “works correctly”.
- Ignoring permissions, invalid states, cleanup, retries, concurrency, or auditability when relevant.
- Creating order-dependent scenarios without a workflow reason.
- Testing every scenario at UI level when API, unit, or integration level would be better.
- Mixing multiple unrelated behaviors into one test case.
- Creating too many low-value cases that do not map to risk or behavior.
- Treating exploratory testing as random clicking instead of charter-based investigation.

## Review checklist

- Does each scenario map to a stated behavior, risk, requirement, or defect?
- Are expected results specific and observable?
- Are positive, negative, edge, boundary, and regression paths represented?
- Are permissions, data setup, state transitions, and cleanup considered?
- Are assumptions and open questions clearly separated from facts?
- Is automation suitability noted without forcing everything into UI automation?
- Is the output free of project-specific names, URLs, credentials, and roles unless provided by the consuming project?
- Are high-risk scenarios prioritized?
- Are ambiguous requirements flagged?
- Are test levels chosen logically?
- Are scenarios independent and repeatable?

## Example prompts

```text
Use the QA test design skill.
Create test scenarios from these acceptance criteria.
Include positive, negative, boundary, permission, regression cases, assumptions, and open questions.
Do not write automation code.
```

```text
Use the QA test design skill.
Review this feature brief for missing coverage.
Organize gaps by risk and suggest which checks should be API, UI, manual, or exploratory.
```

```text
Use the QA test design skill.
Turn this defect into regression test scenarios.
Include the original failure condition, expected fixed behavior, priority, and suggested test level.
```

```text
Use the QA test design skill.
Create exploratory testing charters for this workflow.
Focus on data, permissions, state transitions, errors, and integration risks.
```

```text
Use the QA test design skill together with the API testing skill.
Given this API contract, identify behavior-level test cases before implementation.
Return a coverage matrix and open questions.
```

## Related standards

- `standards/testing-standards.md`
- `standards/automation-standards.md`
- `templates/test-case-template.md`
