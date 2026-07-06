# API Testing Skill

## Purpose

Design language-neutral API test coverage for HTTP APIs and service contracts.

This skill focuses on behavior, contracts, request validation, response validation, authentication, authorization, data, errors, idempotency, and integration risk. It does not require a specific automation library.

## When to use

- Designing API test scenarios from an endpoint contract, OpenAPI document, examples, or written behavior.
- Reviewing API coverage for missing contract, negative, auth, data, or state checks.
- Translating API defects into regression coverage.
- Deciding which checks belong at API level versus UI, unit, or integration level.
- Preparing implementation guidance for Rest Assured, Pytest, Playwright APIRequestContext, or another client.

## When not to use

- When the task is browser-only UI automation; use `skills/playwright-typescript/SKILL.md`.
- When the API behavior is unknown and no contract or examples are provided.
- When the user needs Java-specific Rest Assured implementation details; combine with `skills/rest-assured-java/SKILL.md`.
- When the user needs Python-specific implementation details; combine with `skills/pytest-python/SKILL.md`.
- When the task is only a bug triage without designing coverage; use `skills/bug-analysis/SKILL.md`.

## Required inputs

- Endpoint or operation details: method, route, operation name, or contract section.
- Request fields, path parameters, query parameters, headers, and body schema.
- Response examples, schema, headers, status codes, and error format.
- Authentication and authorization rules, if relevant.
- State transition, persistence, idempotency, pagination, filtering, sorting, and rate-limit rules when applicable.
- Data setup and cleanup constraints.
- Existing coverage or failure reports if reviewing or debugging.

## Expected output

- API test scenarios grouped by endpoint, behavior, contract, or risk.
- Positive, negative, boundary, schema, auth, permission, state transition, idempotency, and regression checks where relevant.
- Suggested setup, cleanup, and data isolation strategy.
- Contract assertions for status, body, headers, error shape, and side effects.
- Coverage gaps and open questions.
- Optional implementation notes for the consuming project's chosen framework.

## Rules

- Test the API contract, not only status codes.
- Validate required response fields, field types, important headers, and error format when defined.
- Include authentication and authorization paths for protected operations.
- Cover missing, malformed, invalid, duplicate, expired, unauthorized, unsupported, and out-of-range inputs where relevant.
- Include idempotency, pagination, filtering, sorting, concurrency, and rate-limit behavior when applicable.
- Verify important side effects, persistence, and no-op expectations.
- Keep tests isolated and independent of execution order.
- Use deterministic synthetic data and unique identifiers when needed.
- Keep secrets, tokens, personal data, and sensitive payloads out of examples and logs.
- Distinguish contract, integration, smoke, regression, and end-to-end coverage.
- Do not assume undocumented behavior is guaranteed.

## Anti-patterns

- Checking only that the response status is 200.
- Hardcoding environment-specific base URLs, tokens, account identifiers, or credentials.
- Reusing production-like personal data in examples.
- Depending on previous tests' side effects.
- Ignoring negative, authorization, and validation scenarios.
- Ignoring schema, headers, error contract, and side effects.
- Treating generated sample payloads as authoritative when the contract says otherwise.
- Testing through the UI when an API-level check would be faster and more precise.

## Review checklist

- Does each test map to a contract rule or meaningful behavior?
- Are status, body, headers, schema, errors, and side effects covered where applicable?
- Are auth and permission cases represented?
- Are invalid, missing, malformed, boundary, and duplicate inputs covered?
- Are data setup and cleanup deterministic and isolated?
- Are tests independent of execution order and safe for parallel runs?
- Are secrets and sensitive values excluded from code, logs, and examples?
- Are open questions documented instead of guessed?

## Example prompts

- "Use the API testing skill to design coverage for this endpoint contract."
- "Review these API tests and identify missing negative, auth, and schema cases."
- "Convert this API bug into regression test scenarios."
- "Create a language-neutral API test plan for these CRUD-like operations."
- "Given these response examples, identify contract assertions and open questions."

## Related standards

- `standards/api-testing-standards.md`
- `standards/testing-standards.md`
- `standards/automation-standards.md`
- `templates/api-test-template.md`
