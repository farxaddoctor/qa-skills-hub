# API Testing Skill

## Purpose

Design, review, and improve API test coverage for HTTP APIs and service contracts.

This skill is language-neutral. It focuses on API behavior, contracts, request validation, response validation, authentication, authorization, data, errors, idempotency, state transitions, side effects, and integration risk.

Use framework-specific skills only after API coverage is clear.

## When to use

Use this skill when the task involves:

- Designing API test scenarios from an endpoint contract, OpenAPI document, examples, user story, or written behavior.
- Reviewing API test coverage for missing contract, negative, auth, data, state, or schema checks.
- Translating API defects into regression coverage.
- Deciding which checks belong at API level versus UI, unit, integration, or end-to-end level.
- Preparing implementation guidance for Rest Assured, Pytest, Playwright APIRequestContext, Postman, Supertest, or another client.
- Auditing API tests for maintainability, independence, data isolation, and meaningful assertions.

## When not to use

Do not use this skill when:

- The task is browser-only UI automation. Use `skills/playwright-typescript/SKILL.md`.
- The API behavior is unknown and no contract, examples, logs, or requirements are provided.
- The user needs Java-specific Rest Assured implementation details. Combine with `skills/rest-assured-java/SKILL.md`.
- The user needs Python-specific implementation details. Combine with `skills/pytest-python/SKILL.md`.
- The task is only bug triage without designing coverage. Use `skills/bug-analysis/SKILL.md`.
- The task is performance or load testing only. Use a performance-specific skill.

## Required inputs

Collect or infer the following before designing or reviewing API coverage:

- Endpoint details: method, route, operation name, service, or contract section.
- Request structure: path parameters, query parameters, headers, cookies, and body schema.
- Response structure: status codes, body schema, headers, examples, and error format.
- Authentication rules: token type, session model, expiration, refresh behavior, required headers.
- Authorization rules: roles, permissions, ownership, tenant or account boundaries.
- Validation rules: required fields, formats, enums, min/max values, nullable fields, uniqueness, and field dependencies.
- State rules: persistence, transitions, lifecycle, idempotency, retry behavior, and side effects.
- Collection behavior: pagination, filtering, sorting, search, empty state, and limits.
- Data setup and cleanup constraints.
- Existing tests, defects, logs, or production incidents if reviewing or debugging.

If the contract is incomplete, list open questions instead of inventing expected behavior.

## Operating mode

Follow this workflow unless the user explicitly requests direct implementation:

### 1. Understand the contract

- Identify documented behavior.
- Separate confirmed rules from assumptions.
- Highlight missing or ambiguous requirements.
- Do not treat examples as the full contract unless stated.

### 2. Classify coverage

Group scenarios by:

- Positive behavior
- Negative validation
- Schema and contract
- Authentication
- Authorization / RBAC
- State transitions
- Idempotency
- Pagination / filtering / sorting
- Side effects
- Regression coverage

### 3. Build a coverage matrix

Return endpoint, scenario, request variation, expected status, expected body/header, side effect, and priority.

### 4. Define data strategy

Specify:

- Required setup
- Cleanup approach
- Unique data generation
- Reusable fixtures
- Isolation requirements
- Parallel execution risks

### 5. Choose implementation level

Explain whether each check belongs at:

- API level
- UI level
- Unit level
- Integration level
- Contract level
- Smoke suite
- Full regression suite
- End-to-end suite

### 6. Suggest implementation only after coverage is clear

Keep framework-specific code out unless the user asks for a target framework.

### 7. Verify

Provide execution or review steps appropriate to the consuming project.

## API coverage categories

Consider these categories when relevant.

### Contract checks

- Expected status codes.
- Required response fields.
- Field types.
- Nullable vs missing fields.
- Enum values.
- Date/time format.
- Numeric precision and ranges.
- Array structure and item schema.
- Important response headers.
- Error object shape.

### Positive checks

- Valid minimal request.
- Valid full request.
- Optional fields included.
- Optional fields omitted.
- Different supported enum values.
- Expected persistence or returned resource state.

### Negative validation checks

- Missing required fields.
- Invalid field type.
- Empty string when not allowed.
- Null when not allowed.
- Out-of-range values.
- Invalid enum values.
- Invalid date format.
- Duplicate unique fields.
- Unsupported content type.
- Malformed JSON.
- Unknown fields when contract defines strictness.

### Authentication checks

- No token or session.
- Invalid token.
- Expired token.
- Malformed authorization header.
- Token with missing scope.
- Revoked token if supported.

### Authorization / RBAC checks

- User without permission.
- Wrong role.
- Wrong owner.
- Wrong tenant, account, workspace, or organization.
- Cross-resource access attempt.
- Admin vs non-admin behavior.
- Read vs write permission difference.

### State transition checks

- Valid state transition.
- Invalid transition.
- Repeated transition.
- Operation on deleted or archived resource.
- Operation on already approved, rejected, completed, or cancelled resource.
- Side effect after transition.

### Collection checks

- Default pagination.
- Custom page size.
- Page boundary.
- Empty result.
- Filtering.
- Sorting.
- Search.
- Combined filters.
- Invalid filter or sort fields.

### Idempotency and concurrency checks

- Repeated identical request.
- Retry after timeout if behavior is defined.
- Duplicate create request.
- Concurrent update or delete if relevant.
- Idempotency key behavior if supported.

### Regression checks

- API bug converted into a focused scenario.
- Previously missing validation.
- Previously broken permission boundary.
- Previously incorrect error or status code.
- Previously incorrect side effect.

## Expected output

### For design tasks

Return:

- Summary of understood API behavior.
- Assumptions and open questions.
- Coverage matrix.
- Recommended test data strategy.
- Priority: smoke, regression, full, or edge.
- Suggested implementation level.
- Framework-specific notes only if requested.

### For review tasks

Return:

- Existing coverage summary.
- Missing scenarios.
- Weak assertions.
- Data isolation risks.
- Auth/RBAC gaps.
- Contract gaps.
- Suggested fixes with priority.

### For implementation guidance

Return:

- Test structure.
- Setup and cleanup plan.
- Request builders or fixture suggestions.
- Assertion strategy.
- Negative test grouping.
- Verification commands or review steps.

## Rules

- Test the API contract, not only status codes.
- Validate status, body, headers, schema, errors, and side effects when defined.
- Include authentication and authorization paths for protected operations.
- Cover missing, malformed, invalid, duplicate, expired, unauthorized, unsupported, and out-of-range inputs where relevant.
- Include idempotency, pagination, filtering, sorting, concurrency, and rate-limit behavior when applicable.
- Verify important side effects, persistence, and no-op expectations.
- Keep tests isolated and independent of execution order.
- Use deterministic synthetic data and unique identifiers when needed.
- Keep secrets, tokens, personal data, and sensitive payloads out of examples and logs.
- Distinguish contract, integration, smoke, regression, and end-to-end coverage.
- Do not assume undocumented behavior is guaranteed.
- Do not hardcode environment-specific base URLs, credentials, account IDs, or tokens.
- Do not generate implementation code before the coverage and data strategy are clear.

## Anti-patterns

- Checking only that the response status is 200.
- Treating response presence as proof of correct behavior.
- Ignoring response schema, headers, error contract, and side effects.
- Ignoring negative, authorization, and validation scenarios.
- Hardcoding base URLs, tokens, account identifiers, or credentials.
- Reusing production-like personal data in examples.
- Depending on previous tests' side effects.
- Using shared mutable test data without cleanup.
- Treating generated sample payloads as authoritative when the contract says otherwise.
- Testing through the UI when an API-level check would be faster and more precise.
- Creating many low-value tests that do not map to contract rules or risks.
- Inventing expected behavior when the contract is silent.

## Review checklist

- Does each test map to a contract rule, risk, or meaningful behavior?
- Are status, body, headers, schema, errors, and side effects covered where applicable?
- Are auth and permission cases represented?
- Are invalid, missing, malformed, boundary, duplicate, and unsupported inputs covered?
- Are state transitions and no-op expectations tested where relevant?
- Are pagination, filtering, sorting, and empty-state cases covered for collection endpoints?
- Are data setup and cleanup deterministic and isolated?
- Are tests independent of execution order and safe for parallel runs?
- Are secrets and sensitive values excluded from code, logs, and examples?
- Are open questions documented instead of guessed?
- Is framework-specific implementation aligned with the consuming project's patterns?

## Coverage matrix format

Use this format for API test design tasks:

| Endpoint             | Scenario                       | Type          | Request variation           | Expected status           | Expected response/body                   | Side effect         | Priority   |
| -------------------- | ------------------------------ | ------------- | --------------------------- | ------------------------- | ---------------------------------------- | ------------------- | ---------- |
| `POST /resource`     | Create with valid minimal body | Positive      | Required fields only        | `201`                     | Resource id and expected fields returned | Resource persisted  | Smoke      |
| `POST /resource`     | Missing required field         | Negative      | Omit required field         | `400` or documented error | Error code/message matches contract      | No resource created | Regression |
| `GET /resource/{id}` | Read without permission        | Authorization | Valid id, insufficient role | `403`                     | Error shape matches contract             | No data leaked      | Smoke      |

## Example prompts

```text
Use the API testing skill.
Design API test coverage for this endpoint contract.
Return a coverage matrix with positive, negative, auth, schema, and state checks.
Do not write framework-specific code yet.
```

```text
Use the API testing skill.
Review these API tests and identify missing negative, authorization, schema, and side-effect assertions.
Return findings by priority.
```

```text
Use the API testing skill.
Convert this API bug into regression scenarios.
Include the original failure condition, expected behavior, and minimal regression coverage.
```

```text
Use the API testing skill.
Create a language-neutral API test plan for these CRUD operations.
Separate smoke, regression, and full coverage.
```

```text
Use the API testing skill with the Rest Assured Java skill.
Turn this coverage matrix into JUnit 5 + Rest Assured implementation guidance.
```

## Related standards

- `standards/api-testing-standards.md`
- `standards/testing-standards.md`
- `standards/automation-standards.md`
- `templates/api-test-template.md`
