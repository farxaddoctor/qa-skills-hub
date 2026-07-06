# Rest Assured Java Skill

## Purpose

Placeholder skill for Java API automation with Rest Assured in a consuming project.

## When to use

- Use when API scenarios are already defined and the consuming project uses Java with Rest Assured.
- Combine with `skills/api-testing/SKILL.md` for coverage design.

## When not to use

- Do not use for language-neutral API coverage by itself.
- Do not use when the consuming project does not use Java or Rest Assured.
- Do not add runnable framework examples to this repository.

## Required inputs

- Existing Java test conventions.
- API scenarios or contract.
- Current Rest Assured helpers, specs, models, or failure logs if available.

## Expected output

- Brief Java/Rest Assured implementation or review guidance.
- Notes on request specs, response specs, assertions, data setup, and cleanup.

## Rules

- Keep environment configuration and secrets outside test code.
- Follow the consuming project's Java and test framework conventions.
- Keep tests independent and contract-focused.

## Anti-patterns

- Hardcoding base URLs, credentials, or environment-specific identifiers.
- Asserting only status codes.
- Hiding behavior under broad generic helpers.

## Review checklist

- Are assertions meaningful beyond status code?
- Are request and response helpers clear?
- Is data setup isolated and cleanup-safe?
- Are secrets absent from code and logs?

## Example prompts

- "Use the Rest Assured Java placeholder skill with the API testing skill to review these Java API tests."
- "Suggest Rest Assured structure for these API scenarios using the consuming project's conventions."

## Related standards

- `standards/java-standards.md`
- `standards/api-testing-standards.md`
- `standards/automation-standards.md`
