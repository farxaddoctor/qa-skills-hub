# Agent Handoff Standard

## Purpose

Define the mandatory handoff payload used between commands, the QA Orchestrator, workflows, agents, skills, audit, Human Gate, and output.

The handoff must remain application-agnostic. It must not include real URLs, credentials, emails, company names, product names, selectors, account data, customer data, or business-specific roles.

## Mandatory Handoff Structure

```yaml
task:
  id: "<TASK_ID>"
  intent: "<INTENT>"
  mode: "<DESIGN|AUTOMATE|REVIEW|AUDIT|DEBUG|BUG_REPORT>"
  requested_output: "<OUTPUT_TYPE>"

routing:
  command: "<COMMAND_PATH>"
  workflow: "<WORKFLOW_PATH>"
  primary_agent: "<AGENT_PATH>"
  supporting_agents: []
  skills: []

inputs:
  artifacts: []
  confirmed_facts: []
  assumptions: []
  hypotheses: []
  open_questions: []
  evidence: []

policies:
  applied: []
  audit_before_edit: false
  leakage_check_required: true

human_gate:
  required: false
  level: 0
  reason: null
  approval_scope: null

scope:
  included: []
  excluded: []
  affected_files: []

output:
  artifact_type: "<TYPE>"
  status: "<PASS|FAIL|BLOCKED|HUMAN_APPROVAL_REQUIRED>"
  verification_required: true
  verification_steps: []

handoff:
  next_agent: null
  stop_condition: null
  notes: []
```

## Required Fields

- `task.id`
- `task.intent`
- `task.mode`
- `task.requested_output`
- `routing.command`
- `routing.workflow`
- `routing.primary_agent`
- `routing.skills`
- `inputs.confirmed_facts`
- `inputs.assumptions`
- `inputs.hypotheses`
- `inputs.open_questions`
- `inputs.evidence`
- `policies.applied`
- `policies.audit_before_edit`
- `policies.leakage_check_required`
- `human_gate.required`
- `human_gate.level`
- `scope.included`
- `scope.excluded`
- `scope.affected_files`
- `output.artifact_type`
- `output.status`
- `output.verification_required`
- `output.verification_steps`
- `handoff.stop_condition`

## Optional Fields

- `routing.supporting_agents`
- `inputs.artifacts`
- `human_gate.reason`
- `human_gate.approval_scope`
- `handoff.next_agent`
- `handoff.notes`

Optional fields must be present in the structure and may be empty, `null`, or an empty list when not used.

## Creator And Consumer

- The command or `agents/qa-orchestrator.md` creates the initial handoff after command intake.
- The selected workflow consumes the routing fields and updates workflow-specific status.
- The primary agent consumes the workflow handoff and adds facts, assumptions, hypotheses, evidence, skill selection, audit status, and output shape.
- Supporting agents consume only the scoped fields assigned to them.
- The final agent closes the handoff by setting `output.status`, `verification_steps`, `handoff.next_agent`, and `handoff.stop_condition`.

## Facts, Assumptions, And Hypotheses

- Confirmed facts are evidence-backed statements from supplied artifacts, user-confirmed behavior, or inspected code.
- Assumptions are unverified statements needed to explain reasoning or identify gaps.
- Hypotheses are possible explanations for failures, flaky behavior, or defects.
- Assumptions and hypotheses must never be written as confirmed facts.
- If a required fact is missing, the handoff status must be `BLOCKED` or `HUMAN_APPROVAL_REQUIRED`.

## Human Gate Recording

- `human_gate.required` is `true` when approval is needed before proceeding.
- `human_gate.level` uses the levels defined in `policies/human-gate-policy.md`.
- `human_gate.reason` explains why approval is required.
- `human_gate.approval_scope` records the exact approved scope after explicit approval.
- If approval is required but not granted, `output.status` must be `HUMAN_APPROVAL_REQUIRED`.
- If the action is forbidden even with approval, such as storing real secrets in this repository, `output.status` must be `BLOCKED`.

## Scope Changes

Any scope change requires a new routing and Human Gate decision when it:

- Adds files or directories to `scope.affected_files`.
- Changes the selected command, workflow, primary agent, or skills.
- Expands from read-only analysis to edits.
- Touches shared utilities, fixtures, Page Objects, API clients, auth/session behavior, CI/CD, dependencies, deletion, or destructive cleanup.
- Turns undocumented assumptions into implementation decisions.

## Closing The Handoff

The final agent closes the handoff by:

1. Setting `output.status` to `PASS`, `FAIL`, `BLOCKED`, or `HUMAN_APPROVAL_REQUIRED`.
2. Recording verification requirements and steps.
3. Recording any remaining stop condition.
4. Setting `handoff.next_agent` to `null` when no further handoff is required.
5. Keeping all output application-agnostic and placeholder-safe.

## Pass Conditions

- The handoff follows the mandatory YAML structure.
- Required fields are present and filled with generic or placeholder-safe values.
- Routing fields match `routing/skill-routing-rules.md`.
- Human Gate state matches `policies/human-gate-policy.md`.
- Leakage checks are represented in `policies.leakage_check_required` and `policies.applied`.

## Fail Conditions

- Required fields are missing.
- Skills appear without command, workflow, and agent routing.
- Scope expands without new approval decision.
- Real product data or secrets appear in the payload.
- `output.status` hides a blocked or approval-required condition.
