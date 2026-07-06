# Automation Standards

## Core Standards

- Automate stable, valuable behavior.
- Keep tests independent and parallel-safe.
- Use clear assertions that verify meaningful outcomes.
- Put reusable setup in fixtures or helpers without hiding test intent.
- Keep configuration, secrets, and environment details outside test logic.
- Prefer fast setup paths when they are faithful to the behavior under test.
- Clean up persisted data or generate safely disposable data.
- Treat retries as diagnostic signals, not proof of stability.

## Review Questions

- Would this test fail for the right reason?
- Can it run alone and in parallel?
- Is the failure message useful?
- Is the setup minimal and understandable?
- Does the abstraction reduce real duplication?
