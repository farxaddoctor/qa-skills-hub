# No Product-Specific Leakage Policy

## Purpose

Define what must never be stored in this repository.

## When to use

- Use before adding or updating any markdown, prompt, skill, workflow, command, agent, policy, or template.
- Use when copying context from a consumer project.

## Inputs

- Proposed content.
- Source of content.
- Any examples, placeholders, logs, URLs, credentials, users, selectors, or domain terms.

## Process

1. Scan proposed content for real project data.
2. Replace allowed generic examples with placeholders.
3. Remove forbidden data rather than masking it poorly.
4. Attribute external material if copied, adapted, or summarized.
5. Stop if secrets or real project data are present.

## Outputs

- Leakage check result.
- Replaced placeholders.
- Attribution requirement, if any.
- Stop decision when unsafe content is found.

## Human Gate conditions

Human approval is required before using any consumer-project example that may reveal internal behavior. Approval does not allow storing secrets, credentials, tokens, real URLs, or customer data in this repository.

## Related agents, workflows, policies, or skills

- `constitution/qa-agent-constitution.md`
- `policies/evidence-and-citation-policy.md`
- `docs/source-attribution.md`
- `agents/qa-orchestrator.md`

## Application-agnostic constraints

Forbidden:

- Real URLs, hosts, staging names, production names, or internal environment names.
- Credentials, tokens, emails, secrets, keys, or customer data.
- Real company names, product names, user names, consumer-project roles, selectors, business flows, or account identifiers.

Allowed placeholders:

- `<BASE_URL>`
- `<USER_EMAIL>`
- `<RESOURCE_ID>`
- `<TOKEN>`
- `<ROLE_NAME>`
- `<API_ENDPOINT>`
- `<TEST_DATA_ID>`
