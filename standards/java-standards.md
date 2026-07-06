# Java Standards

## Core Standards

- Follow the consuming project's Java version, formatter, imports, and test framework conventions.
- Keep test names descriptive.
- Prefer clear typed models when they improve request or response readability.
- Keep environment configuration outside test logic.
- Use assertions that explain behavior, not only raw values.
- Avoid broad utility layers that obscure test intent.

## Rest Assured Notes

- Reuse request specifications for stable shared setup.
- Reuse response specifications only for stable shared expectations.
- Keep endpoint-specific behavior visible in the test or focused helper.
