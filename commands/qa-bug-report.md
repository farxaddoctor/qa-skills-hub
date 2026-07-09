# QA Bug Report Command

## Purpose

User-facing entry point for creating a structured bug report from evidence and analysis.

## When to use

- Use when a product defect appears likely.
- Use when reproduction steps and evidence need report-ready structure.
- Use after bug analysis identifies enough evidence.

## Inputs

- Expected behavior and actual behavior.
- Reproduction steps.
- Evidence such as logs, traces, screenshots, payloads, or videos.
- Environment context supplied by the consuming project, rewritten as placeholders if stored here.

## Process

1. Route through `agents/qa-orchestrator.md`.
2. Apply Constitution, evidence policy, and leakage policy.
3. Use routing rules to select `workflows/bug-to-regression.md`.
4. Hand off to `agents/bug-analyst.md`.
5. Produce a report with regression recommendation.
6. Stop at Human Gate before undocumented behavior assumptions.

## Outputs

- Bug title.
- Preconditions.
- Steps to reproduce.
- Expected and actual result.
- Evidence summary.
- Impact.
- Regression coverage recommendation.

## Human Gate conditions

Human approval is required before treating undocumented expected behavior as confirmed or including sensitive environment details.

## Related agents, workflows, policies, or skills

- `agents/qa-orchestrator.md`
- `agents/bug-analyst.md`
- `workflows/bug-to-regression.md`
- `policies/evidence-and-citation-policy.md`
- `policies/no-product-specific-leakage.md`
- `templates/bug-report-template.md`

## Application-agnostic constraints

- Use placeholders for URLs, users, ids, tokens, roles, and environment names.
- Do not include real credentials, emails, customer data, company names, or product-specific flows.
