# Evidence And Citation Policy

## Purpose

Require QA conclusions, bug analysis, reviews, and source references to be evidence-based.

## When to use

- Use when analyzing failures, reviewing code, creating bug reports, or citing external material.
- Use before claiming root cause or adapting third-party content.

## Inputs

- Logs, traces, screenshots, code, diffs, API contracts, bug reports, or user-provided evidence.
- External source details when content is referenced, copied, adapted, or summarized.

## Process

1. Separate confirmed facts, assumptions, hypotheses, and unknowns.
2. Cite local files, evidence artifacts, or user-provided context when making findings.
3. Preserve exact error messages only when useful and safe.
4. Mark root cause as confirmed only when evidence supports it.
5. Update `docs/source-attribution.md` before storing copied or adapted external material.

## Outputs

- Evidence level: confirmed, likely, possible, or unknown.
- Cited source or artifact.
- Assumptions and open questions.
- Attribution requirement when external material is used.

## Human Gate conditions

Human approval is required before using ambiguous evidence as root cause, storing external material, or making assumptions about undocumented product behavior.

## Related agents, workflows, policies, or skills

- `agents/bug-analyst.md`
- `agents/qa-code-reviewer.md`
- `workflows/flaky-test-investigation.md`
- `workflows/bug-to-regression.md`
- `policies/no-product-specific-leakage.md`
- `docs/source-attribution.md`

## Application-agnostic constraints

- Do not store real logs with secrets, tokens, emails, URLs, customer data, product names, or internal environment details.
- Use placeholders such as `<ERROR_MESSAGE>`, `<RESOURCE_ID>`, and `<TRACE_ID>`.
