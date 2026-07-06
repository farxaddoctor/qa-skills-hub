# Bug Analysis Skill

## Purpose

Placeholder skill for analyzing defects, failed tests, flaky behavior, and regression reports.

## When to use

- Use when the user provides failure evidence, reproduction steps, logs, screenshots, traces, or error messages.
- Use before creating regression coverage when root cause or failure type is unclear.

## When not to use

- Do not use as a replacement for test design when behavior is already clear.
- Do not invent root cause without evidence.
- Do not add runnable reproduction tests to this repository.

## Required inputs

- Expected behavior and actual behavior.
- Reproduction steps or failure frequency.
- Logs, traces, screenshots, payloads, stack traces, or CI output when available.

## Expected output

- Brief failure summary.
- Evidence-based hypotheses.
- Diagnostic next steps.
- Regression coverage ideas when appropriate.

## Rules

- Separate facts from hypotheses.
- Preserve useful error details.
- Consider product, test, data, environment, dependency, and timing causes.

## Anti-patterns

- Declaring root cause without evidence.
- Treating every failure as either product defect or test flake by default.
- Losing reproduction details.

## Review checklist

- Is expected versus actual behavior clear?
- Is the evidence sufficient?
- Are hypotheses labeled as hypotheses?
- Are next diagnostics concrete?

## Example prompts

- "Use the bug analysis placeholder skill to analyze this CI failure log."
- "Turn these reproduction notes into likely cause categories and next diagnostics."

## Related standards

- `standards/testing-standards.md`
- `templates/bug-report-template.md`
