# Compatibility Test Cases

## Purpose

Validate that legacy commands and compatibility agents delegate to canonical orchestration.

These are architecture acceptance specifications, not executable product tests.

## Compatibility Rules

- Compatibility components may support older prompts.
- Compatibility components must not create an alternative workflow.
- Compatibility components must not become second canonical roles.
- Compatibility components must route through Constitution, policies, audit, and Human Gate.
- Compatibility components must not directly execute a skill before routing.

## CT-001 generate-test-cases Delegates To qa-design

ID: CT-001

Purpose: Validate legacy test-case generation command delegation.

Input: Use `commands/generate-test-cases.md` for generic test case generation.

Expected command: `commands/qa-design.md`

Expected workflow: `workflows/requirement-to-test-plan.md`

Expected primary agent: `agents/test-designer.md`

Expected skills: `skills/qa-test-design/SKILL.md`

Required policies: `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Not required for analysis-only design.

Expected output: Delegated design output from canonical command.

Forbidden behavior: Directly executing a skill; creating an alternate generation workflow; bypassing Constitution or policies.

Pass criteria: `commands/generate-test-cases.md` delegates to `commands/qa-design.md`.

## CT-002 generate-bug-report Delegates To qa-bug-report

ID: CT-002

Purpose: Validate legacy bug report command delegation.

Input: Use `commands/generate-bug-report.md` for sanitized defect evidence.

Expected command: `commands/qa-bug-report.md`

Expected workflow: `workflows/bug-to-regression.md`

Expected primary agent: `agents/bug-analyst.md`

Expected skills: `skills/bug-analysis/SKILL.md`

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before undocumented behavior assumptions.

Expected output: Delegated bug report output from canonical command.

Forbidden behavior: Creating a second bug-report workflow; bypassing leakage policy.

Pass criteria: `commands/generate-bug-report.md` delegates to `commands/qa-bug-report.md`.

## CT-003 analyze-bug Delegates To qa-debug

ID: CT-003

Purpose: Validate legacy bug analysis command delegation.

Input: Use `commands/analyze-bug.md` for generic failure evidence.

Expected command: `commands/qa-debug.md`

Expected workflow: `workflows/flaky-test-investigation.md` or `workflows/bug-to-regression.md`

Expected primary agent: `agents/bug-analyst.md`

Expected skills: `skills/bug-analysis/SKILL.md`

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before risky assumptions or changes.

Expected output: Delegated debug analysis from canonical command.

Forbidden behavior: Classifying root cause without evidence; bypassing evidence policy.

Pass criteria: `commands/analyze-bug.md` delegates to `commands/qa-debug.md`.

## CT-004 create-api-tests Delegates To qa-design Or qa-automate

ID: CT-004

Purpose: Validate legacy API test command delegation.

Input: Use `commands/create-api-tests.md` for generic API coverage or approved API implementation guidance.

Expected command: `commands/qa-design.md` for coverage or `commands/qa-automate.md` for approved implementation guidance.

Expected workflow: `workflows/api-contract-to-tests.md` for coverage or `workflows/test-plan-to-automation.md` for implementation guidance.

Expected primary agent: `agents/api-test-engineer.md`

Expected skills: `skills/api-testing/SKILL.md`; language skill only when implementation language is specified.

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before implementation or undocumented API behavior assumptions.

Expected output: Delegated API coverage or approved implementation guidance.

Forbidden behavior: Creating executable API tests in this repository; choosing language framework without context.

Pass criteria: `commands/create-api-tests.md` delegates to canonical API design or automation routing.

## CT-005 review-playwright-test Delegates To qa-review Or qa-audit

ID: CT-005

Purpose: Validate legacy Playwright review command delegation.

Input: Use `commands/review-playwright-test.md` for generic Playwright test review.

Expected command: `commands/qa-review.md` or `commands/qa-audit.md`

Expected workflow: `workflows/automation-review.md`

Expected primary agent: `agents/qa-code-reviewer.md`

Expected skills: `skills/qa-code-review/SKILL.md`; `skills/playwright-typescript/SKILL.md` only when needed.

Required policies: `policies/audit-before-edit.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before risky recommendations or changes.

Expected output: Delegated review or audit output.

Forbidden behavior: Treating Playwright as the architecture; applying fixes during review-only routing.

Pass criteria: `commands/review-playwright-test.md` delegates to canonical review or audit routing.

## CT-006 refactor-test-framework Delegates To qa-audit

ID: CT-006

Purpose: Validate legacy refactor command delegation before implementation.

Input: Use `commands/refactor-test-framework.md` for generic test framework refactor.

Expected command: `commands/qa-audit.md`

Expected workflow: `workflows/automation-review.md`

Expected primary agent: `agents/qa-code-reviewer.md`

Expected skills: `skills/qa-code-review/SKILL.md`; framework skill only when needed.

Required policies: `policies/audit-before-edit.md`, `policies/safe-refactor-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: HUMAN_APPROVAL_REQUIRED, Level 3 before implementation path.

Expected output: Audit, risk, safe-to-edit status, and approval request.

Forbidden behavior: Starting refactor before audit and Human Gate approval.

Pass criteria: `commands/refactor-test-framework.md` delegates to `commands/qa-audit.md` before implementation.

## CT-007 playwright-engineer Delegates To automation-engineer

ID: CT-007

Purpose: Validate Playwright compatibility agent delegation.

Input: Use `agents/playwright-engineer.md` for approved Playwright automation guidance.

Expected command: `commands/qa-automate.md`

Expected workflow: `workflows/test-plan-to-automation.md`

Expected primary agent: `agents/automation-engineer.md`

Expected skills: `skills/playwright-typescript/SKILL.md` only when routing selects Playwright.

Required policies: `policies/audit-before-edit.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before file modification or risky recommendations.

Expected output: Delegated automation guidance from canonical automation agent.

Forbidden behavior: Compatibility agent directly executing the Playwright skill; becoming a second canonical automation role.

Pass criteria: `agents/playwright-engineer.md` delegates to `agents/automation-engineer.md`.

## CT-008 api-automation-engineer Delegates To api-test-engineer

ID: CT-008

Purpose: Validate API automation compatibility agent delegation.

Input: Use `agents/api-automation-engineer.md` for generic API automation guidance.

Expected command: `commands/qa-design.md` or `commands/qa-automate.md`

Expected workflow: `workflows/api-contract-to-tests.md` or `workflows/test-plan-to-automation.md`

Expected primary agent: `agents/api-test-engineer.md`

Expected skills: `skills/api-testing/SKILL.md`

Required policies: `policies/evidence-and-citation-policy.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before implementation or undocumented API behavior assumptions.

Expected output: Delegated API coverage decision from canonical API test agent.

Forbidden behavior: Creating alternative API automation workflow; bypassing API coverage design.

Pass criteria: `agents/api-automation-engineer.md` delegates to `agents/api-test-engineer.md`.

## CT-009 java-api-automation-engineer Delegates To api-test-engineer

ID: CT-009

Purpose: Validate Java API compatibility agent delegation.

Input: Use `agents/java-api-automation-engineer.md` for Java API automation guidance.

Expected command: `commands/qa-automate.md`

Expected workflow: `workflows/test-plan-to-automation.md`

Expected primary agent: `agents/api-test-engineer.md`

Expected skills: `skills/api-testing/SKILL.md`; `skills/rest-assured-java/SKILL.md` only after API coverage and Java context are clear.

Required policies: `policies/audit-before-edit.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before file modification, dependency changes, or undocumented API assumptions.

Expected output: Delegated API coverage decision before Java implementation planning.

Forbidden behavior: Java implementation planning before API coverage is clear; becoming a second canonical API role.

Pass criteria: `agents/java-api-automation-engineer.md` delegates canonical API decisions to `agents/api-test-engineer.md`.

## CT-010 python-automation-engineer Delegates To automation-engineer

ID: CT-010

Purpose: Validate Python compatibility agent delegation.

Input: Use `agents/python-automation-engineer.md` for Python automation guidance.

Expected command: `commands/qa-automate.md`

Expected workflow: `workflows/test-plan-to-automation.md`

Expected primary agent: `agents/automation-engineer.md`

Expected skills: `skills/pytest-python/SKILL.md`; `skills/api-testing/SKILL.md` only when API behavior is primary.

Required policies: `policies/audit-before-edit.md`, `policies/no-product-specific-leakage.md`, `policies/human-gate-policy.md`

Human Gate: Required before file modification, dependency changes, or risky implementation.

Expected output: Delegated automation guidance from canonical automation agent.

Forbidden behavior: Python implementation planning before scenarios are clear; becoming a second canonical automation role.

Pass criteria: `agents/python-automation-engineer.md` delegates to `agents/automation-engineer.md` or `agents/api-test-engineer.md` when API behavior is primary.
