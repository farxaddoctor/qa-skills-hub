# Generate Bug Report Command

## Purpose

Compatibility command for creating a structured bug report.

## When to use

- Use when older prompts ask to generate a bug report.
- Prefer `commands/qa-bug-report.md` for new orchestration.

## Inputs

- Expected behavior and actual behavior.
- Reproduction steps.
- Evidence summary.
- Impact if known.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution, evidence policy, and leakage policy.
3. Delegate to `commands/qa-bug-report.md`.
4. Stop at Human Gate before undocumented expected behavior assumptions.

## Outputs

- Bug title.
- Preconditions.
- Steps to reproduce.
- Expected and actual result.
- Evidence summary.
- Regression recommendation.

## Human Gate conditions

Human approval is required before including sensitive environment details or treating undocumented behavior as confirmed.

## Related agents, workflows, policies, or skills

- `commands/qa-bug-report.md`
- `agents/bug-analyst.md`
- `workflows/bug-to-regression.md`
- `templates/bug-report-template.md`

## Application-agnostic constraints

- Use placeholders for URLs, users, ids, tokens, roles, and environment names.
- Do not store real credentials, emails, customer data, company names, product names, or business flows.
