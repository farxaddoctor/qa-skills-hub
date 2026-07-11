# Routing Test Cases

## Purpose

Validate command-to-workflow, command-to-agent, and command-to-skill routing.

These are architecture acceptance specifications, not executable product tests.

## Routing Rules Under Test

- Each case must have one primary workflow and one primary agent unless the workflow explicitly defines a sequential handoff.
- Supporting agents are allowed only when the expected workflow needs them.
- Framework and language skills are selected only after routing.
- Skills that must not be loaded are listed under forbidden behavior.

## RT-001 qa-design Requirement

ID: RT-001

Purpose: Validate standard requirement-to-coverage routing.

Input: Design QA coverage from generic requirements.

Expected command: `commands/qa-design.md`

Expected workflow: `workflows/requirement-to-test-plan.md`

Expected primary agent: `agents/test-designer.md`

Expected skills: `skills/qa-test-design/SKILL.md`

Required policies: `policies/no-product-specific-leakage.md`, `policies/evidence-and-citation-policy.md`, `policies/human-gate-policy.md`

Human Gate: Not required for analysis-only design.

Expected output: Scenario matrix, risks, assumptions, open questions, and suggested test levels.

Forbidden behavior: Loading implementation skills; writing executable tests; bypassing `agents/qa-orchestrator.md`.

Pass criteria: One primary workflow and one primary agent are selected, and the design skill is loaded only after routing.

## RT-002 qa-design API Contract

ID: RT-002

Purpose: Validate API contract routing.

Input: Design coverage from a generic API contract.

Expected command: `commands/qa-design.md`

Expected workflow: `workflows/api-contract-to-tests.md`

Expected primary agent: `agents/api-test-engineer.md`

Expected skills: `skills/api-testing/SKILL.md`

Required policies: `policies/no-product-specific-leakage.md`, `policies/evidence-and-citation-policy.md`, `policies/human-gate-policy.md`

Human Gate: Required before undocumented API behavior is treated as confirmed.

Expected output: API coverage matrix and open contract questions.

Forbidden behavior: Loading `skills/rest-assured-java/SKILL.md` or `skills/pytest-python/SKILL.md` without a framework requirement; inventing status codes, schemas, auth rules, or permissions.

Pass criteria: API design is selected as the lower and more precise path for contract coverage.

## RT-003 qa-automate Approved Scenarios

ID: RT-003

Purpose: Validate automation strategy routing after scenarios are approved.

Input: Create automation strategy from approved generic scenarios.

Expected command: `commands/qa-automate.md`

Expected workflow: `workflows/test-plan-to-automation.md`

Expected primary agent: `agents/automation-engineer.md`

Expected skills: Framework or language skill selected from consumer-project context.

Required policies: `policies/audit-before-edit.md`, `policies/no-product-specific-leakage.md`, `policies/safe-refactor-policy.md`, `policies/human-gate-policy.md`

Human Gate: Required before file modification.

Expected output: Automation strategy, scoped implementation plan, convention audit, and verification plan.

Forbidden behavior: Assuming Playwright; loading framework skill without context; editing before approval.

Pass criteria: Existing conventions are inspected before edits and implementation remains scoped to approved scenarios.

## RT-004 qa-review

ID: RT-004

Purpose: Validate code review routing.

Input: Review a generic automated test diff.

Expected command: `commands/qa-review.md`

Expected workflow: `workflows/automation-review.md`

Expected primary agent: `agents/qa-code-reviewer.md`

Expected skills: `skills/qa-code-review/SKILL.md`; framework skill only when needed.

Required policies: `policies/audit-before-edit.md`, `policies/no-product-specific-leakage.md`, `policies/safe-refactor-policy.md`, `policies/human-gate-policy.md`

Human Gate: Not required for read-only review. Required before broad refactor or implementation.

Expected output: Findings ordered by severity with evidence, impact, recommendations, and verification guidance.

Forbidden behavior: Applying fixes during review-only routing; suggesting broad refactor without evidence.

Pass criteria: Review stays read-only and returns findings first.

## RT-005 qa-audit

ID: RT-005

Purpose: Validate audit routing.

Input: Audit generic automation structure before edits.

Expected command: `commands/qa-audit.md`

Expected workflow: `workflows/automation-review.md`

Expected primary agent: `agents/qa-code-reviewer.md`

Expected skills: `skills/qa-code-review/SKILL.md`; framework skill only when needed.

Required policies: `policies/audit-before-edit.md`, `policies/safe-refactor-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before risky recommendations or changes.

Expected output: Current-state audit, risks, safe-to-edit status, Human Gate level, and validation plan.

Forbidden behavior: Editing files during audit; skipping safe-refactor policy.

Pass criteria: Audit produces safe-to-edit decision without implementation.

## RT-006 qa-debug

ID: RT-006

Purpose: Validate failure and flaky behavior routing.

Input: Analyze sanitized failure evidence.

Expected command: `commands/qa-debug.md`

Expected workflow: `workflows/flaky-test-investigation.md`

Expected primary agent: `agents/bug-analyst.md`

Expected skills: `skills/bug-analysis/SKILL.md`; framework skill only when evidence requires it.

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/audit-before-edit.md`, `policies/human-gate-policy.md`

Human Gate: Required before risky fixes, retry changes, CI/CD changes, or undocumented behavior assumptions.

Expected output: Evidence summary, hypotheses, diagnostics, likely cause classification, and next steps.

Forbidden behavior: Rewriting tests before investigation; increasing retries by default; treating hypotheses as facts.

Pass criteria: Root-cause investigation precedes any implementation recommendation.

## RT-007 qa-bug-report

ID: RT-007

Purpose: Validate bug report routing.

Input: Create a bug report from sanitized defect evidence.

Expected command: `commands/qa-bug-report.md`

Expected workflow: `workflows/bug-to-regression.md`

Expected primary agent: `agents/bug-analyst.md`

Expected skills: `skills/bug-analysis/SKILL.md`; `skills/qa-test-design/SKILL.md` only when regression coverage is requested.

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before undocumented expected behavior is confirmed.

Expected output: Structured bug report with evidence and regression recommendation.

Forbidden behavior: Including real project data; inventing expected behavior.

Pass criteria: Report is evidence-backed, sanitized, and does not imply unconfirmed behavior.

## RT-008 Requirement Plus API Contract

ID: RT-008

Purpose: Validate ambiguous design routing when both requirement and API contract are supplied.

Input: Create coverage from generic acceptance criteria and a generic API contract.

Expected command: `commands/qa-design.md`

Expected workflow: `workflows/api-contract-to-tests.md` for API-specific coverage, with `workflows/requirement-to-test-plan.md` only as a sequential design handoff when non-API behavior also needs coverage.

Expected primary agent: `agents/api-test-engineer.md`

Expected skills: `skills/api-testing/SKILL.md`; `skills/qa-test-design/SKILL.md` only for broader scenario design.

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before undocumented behavior is treated as confirmed.

Expected output: Primary API coverage plus clearly separated broader scenario gaps when needed.

Forbidden behavior: Selecting multiple primary workflows at once; loading framework implementation skills without implementation context.

Pass criteria: One primary workflow is selected, and any broader design work is explicitly a sequential handoff.

## RT-009 Bug Report Plus Flaky Automated Test

ID: RT-009

Purpose: Validate routing when defect report and flaky test evidence are both present.

Input: Analyze a sanitized defect report and flaky automated test evidence.

Expected command: `commands/qa-debug.md`

Expected workflow: `workflows/flaky-test-investigation.md` first, then `workflows/bug-to-regression.md` only if evidence supports defect reporting.

Expected primary agent: `agents/bug-analyst.md`

Expected skills: `skills/bug-analysis/SKILL.md`

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/audit-before-edit.md`, `policies/human-gate-policy.md`

Human Gate: Required before test changes or undocumented expected behavior assumptions.

Expected output: Classification of test issue, environment issue, data issue, or product defect with evidence.

Forbidden behavior: Treating flake as product defect without evidence; editing the test immediately.

Pass criteria: Flaky investigation is primary and bug report handoff is sequential only when supported.

## RT-010 Code Review Plus Requested Refactor

ID: RT-010

Purpose: Validate routing when review and refactor are requested together.

Input: Review generic automation code and refactor issues found.

Expected command: `commands/qa-review.md`

Expected workflow: `workflows/automation-review.md`

Expected primary agent: `agents/qa-code-reviewer.md`

Expected skills: `skills/qa-code-review/SKILL.md`; framework skill only when needed.

Required policies: `policies/audit-before-edit.md`, `policies/safe-refactor-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: HUMAN_APPROVAL_REQUIRED before refactor implementation.

Expected output: Review findings first, refactor scope, risks, and approval request for implementation.

Forbidden behavior: Combining review and refactor into immediate edits; broad refactor without evidence.

Pass criteria: Review remains primary and implementation waits for audit and approval.

## RT-011 Automation Request With No Approved Scenarios

ID: RT-011

Purpose: Validate automation request handling when scenarios are missing.

Input: Automate a generic feature with no approved scenarios.

Expected command: `commands/qa-design.md`

Expected workflow: `workflows/requirement-to-test-plan.md`

Expected primary agent: `agents/test-designer.md`

Expected skills: `skills/qa-test-design/SKILL.md`

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Not required for clarification. Required before assumed scenarios become implementation.

Expected output: BLOCKED or clarification output with required inputs.

Forbidden behavior: Creating automation; loading framework skill; inventing behavior.

Pass criteria: The route stops before automation and asks for scenarios or expected behavior.

## RT-012 API Automation Request With No Language Specified

ID: RT-012

Purpose: Validate API automation routing when implementation language is not specified.

Input: Automate generic API tests without specifying language or framework.

Expected command: `commands/qa-design.md`

Expected workflow: `workflows/api-contract-to-tests.md`

Expected primary agent: `agents/api-test-engineer.md`

Expected skills: `skills/api-testing/SKILL.md`

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before implementation assumptions are made.

Expected output: API coverage and open question asking for target framework or language before implementation.

Forbidden behavior: Loading `skills/rest-assured-java/SKILL.md` or `skills/pytest-python/SKILL.md`; creating implementation guidance in an assumed language.

Pass criteria: Language-neutral coverage is produced and implementation is blocked pending framework context.

## RT-013 Playwright Request Where API Is Lower Test Level

ID: RT-013

Purpose: Validate that Playwright is not selected when API testing is the lower and more reliable level.

Input: Create Playwright coverage for behavior that can be validated through a generic API contract.

Expected command: `commands/qa-design.md`

Expected workflow: `workflows/api-contract-to-tests.md`

Expected primary agent: `agents/api-test-engineer.md`

Expected skills: `skills/api-testing/SKILL.md`

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before overriding lower-level test strategy without justification.

Expected output: Recommendation to cover behavior at API level, with Playwright reserved for user-facing integration gaps.

Forbidden behavior: Loading `skills/playwright-typescript/SKILL.md` as primary skill by default; treating Playwright as the architecture.

Pass criteria: API testing is selected as the primary lower-level route and Playwright remains optional supporting capability only when justified.
