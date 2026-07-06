# API Testing Standards

## Core Standards

- Validate status, body, headers, schema, and important side effects.
- Test authentication and authorization paths.
- Cover missing, malformed, invalid, duplicate, expired, and out-of-range inputs.
- Include pagination, filtering, sorting, idempotency, concurrency, and rate limits when applicable.
- Keep API tests independent of execution order.
- Use deterministic synthetic data.
- Avoid logging secrets or sensitive payloads.

## Coverage Types

- Contract checks.
- Positive behavior checks.
- Negative validation checks.
- Authorization checks.
- State transition checks.
- Integration checks.
- Regression checks.
