# Test Data Generation Skill

## Purpose

Placeholder skill for designing safe synthetic test data.

## When to use

- Use when scenarios need valid, invalid, boundary, negative, or regression data.
- Use when reviewing whether data is deterministic, isolated, and privacy-safe.

## When not to use

- Do not use to create production-like personal data.
- Do not use when validation rules or schema are completely unknown.
- Do not add runnable data factories to this repository.

## Required inputs

- Field definitions, schema, validation rules, or constraints.
- Data relationships, uniqueness requirements, and cleanup needs.
- Locale, timezone, length, numeric, or encoding concerns if relevant.

## Expected output

- Brief data sets or data categories.
- Boundary and negative values.
- Uniqueness, determinism, and cleanup notes.

## Rules

- Use synthetic data only.
- Avoid real personal, customer, production, or secret data.
- Prefer deterministic data unless randomness is explicitly useful and traceable.

## Anti-patterns

- Copying production data into tests.
- Generating random values that are hard to debug.
- Ignoring uniqueness in parallel execution.

## Review checklist

- Is the data synthetic and privacy-safe?
- Are boundary and invalid cases represented?
- Is uniqueness handled?
- Is cleanup possible?

## Example prompts

- "Use the test data generation placeholder skill to create boundary data for this schema."
- "Review this test data for privacy and determinism risks."

## Related standards

- `standards/testing-standards.md`
- `standards/automation-standards.md`
