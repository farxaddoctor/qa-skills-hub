# Testing Standards

## Core Standards

- Test behavior that matters to users, systems, or contracts.
- Keep expected results explicit.
- Include positive, negative, boundary, and regression coverage where relevant.
- Make assumptions and unresolved questions visible.
- Avoid order-dependent tests unless sequence is the behavior under test.
- Keep test data synthetic and privacy-safe.
- Prefer deterministic tests over broad randomization.
- Separate setup, action, assertion, and cleanup clearly.

## Quality Bar

A good test should be understandable, repeatable, isolated, and capable of failing for the behavior it claims to verify.
