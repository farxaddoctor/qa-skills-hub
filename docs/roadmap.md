# QA Skills Hub Roadmap

## Authority

This file is the authoritative roadmap for the QA Skills Hub project. It defines the planned stage order, scope, dependencies, acceptance criteria, and current status. Supporting reports and historical evidence may inform this roadmap, but they do not override it.

The governing forward sequence is:

```text
Stage 4.1 -> Stage 6 -> Stage 7
```

Stages must not be reordered or treated as complete without satisfying their stated acceptance criteria. Historical evidence collected ahead of schedule does not advance a stage status.

## Status vocabulary

- `COMPLETE`: all stated acceptance criteria are supported by repository evidence.
- `NOT STARTED`: implementation or controlled execution for the stage has not begun.
- `IN PROGRESS`: approved stage work has begun, but one or more acceptance criteria remain open.
- `BLOCKED`: the stage cannot progress without an identified dependency, decision, or Human Gate.

## Confirmed completed foundations

The following foundations are confirmed by the current repositories and Git history:

- The universal QA skills, standards, templates, agents, workflows, routing rules, Constitution, and policies are present in the Hub.
- The AI-native QA orchestration and repository validation layers are present.
- Stage 4 delivered deterministic static validation for the Hub at commit `81197bf84ed51913bc3a93ace41661ab80a8e3b9`.
- Stage 5 delivered reproducible Consumer integration and its Hub integration guide.
- The current Hub HEAD, `6dac377256c58830e937eb97f8c9fe3bcf3928c6`, contains the Stage 4 validator review fixes.

These completed foundations do not constitute Stage 6 or Stage 7 acceptance evidence.

## Stage 4.1 - Close static-validator review defects

### Goal

Close the confirmed review defects in the Stage 4 Hub validator without expanding validation into Consumer evidence execution or Consumer artifact validation.

### Scope

- Correct the reviewed defects in `scripts/validate_repository.py`.
- Preserve deterministic, read-only validation of the Hub repository.
- Preserve the Hub's application-agnostic and no-product-specific-leakage constraints.
- Keep Consumer evidence contracts, execution, and validation out of this stage.

### Dependencies

- Completed Stage 4 static validator at Hub commit `81197bf84ed51913bc3a93ace41661ab80a8e3b9`.
- Confirmed validator review findings.

### Acceptance criteria

- The reviewed Stage 4 validator defects are fixed in Hub history.
- `python scripts/validate_repository.py` exits successfully on the current Hub checkout.
- The validator remains deterministic and read-only.
- No Consumer evidence scenario is required to accept Stage 4.1.

### Current status

`COMPLETE`

Implementation evidence is present in commits `5e14c43` and `4bea1c33955df415b40eca2e0faae50836b7354d`. Completion does not imply that the Consumer pin has advanced to the current Hub HEAD.

## Stage 6 - Define machine-readable evidence contracts

### Goal

Define stable, machine-readable contracts for Consumer evidence before controlled evidence execution or acceptance claims.

### Scope

- Define a versioned payload schema for recorded simulation evidence.
- Define a versioned routing trace schema covering the required orchestration fields and canonical status vocabulary.
- Define canonical result identity, including the distinction between a canonical result and historical attempts.
- Define a machine-readable manifest structure that maps each scenario to exactly one canonical result and zero or more historical attempts.
- Define required provenance, including the Consumer revision, Hub pin, schema version, and evidence identity.
- Define compatibility and change rules for future contract versions.

Stage 6 defines contracts. It does not execute evidence scenarios and does not claim reproducibility or acceptance.

### Dependencies

- Stage 4.1 is `COMPLETE`.
- Existing Stage 5 Consumer integration remains reproducible and keeps the Hub as an immutable pinned dependency.
- Canonical status and routing-field sources are identified from the Consumer instructions and Hub validation rules.
- Human approval is obtained for any scoped Consumer edits required to introduce the contracts.

### Acceptance criteria

- Payload and routing trace schemas are machine-readable, versioned, and documented.
- The routing trace schema represents every required trace field and permits only the canonical statuses `PASS`, `FAIL`, `BLOCKED`, and `HUMAN_APPROVAL_REQUIRED`.
- Canonical result identity is deterministic and does not depend on filename inference or review judgment.
- The manifest structure represents exactly one canonical result per scenario, optional immutable historical attempts, evidence provenance, and schema versions.
- Positive and negative contract examples demonstrate unambiguous validation expectations without running evidence scenarios.
- Contract ownership, compatibility rules, and approval boundaries are documented.

### Current status

`IN PROGRESS`

No current manifest or payload/routing trace schema satisfies these criteria. The early baseline described below does not change this status.

## Stage 7 - Controlled evidence execution and acceptance

### Goal

Execute evidence under controlled conditions and produce reproducible, validator-backed acceptance evidence using the Stage 6 contracts.

### Scope

- Define and perform controlled evidence execution under an approved execution plan.
- Add a deterministic, read-only sandbox validator.
- Validate the manifest and all Stage 6 schemas.
- Validate evidence encoding, canonical statuses, required routing trace fields, and canonical-result mappings.
- Introduce oracle change-control for `expected/*`, including ownership, rationale, evidence, independent review, approval boundaries, immutable history, and rollback.
- Record execution provenance and demonstrate reproducibility against the approved Consumer pin and Hub revision.
- Produce acceptance evidence only after all Stage 7 controls pass.

### Dependencies

- Stage 6 is `COMPLETE` and its contracts are approved and versioned.
- The Consumer is pinned to the approved Hub revision under test.
- Human Gates are approved separately for Consumer evidence changes, shared validator behavior, CI changes, and oracle policy changes as applicable.
- The controlled execution plan defines the environment matrix, sample size, stop conditions, and acceptance thresholds before execution begins.

### Acceptance criteria

- Controlled evidence execution follows the pre-approved plan without modifying oracles during result generation or evaluation.
- The sandbox validator is deterministic, read-only, and passes on the complete acceptance evidence set.
- Manifest/schema, encoding, status, trace-field, and canonical-mapping checks all pass.
- Oracle change-control is documented, approved, and applied to every oracle change.
- Evidence provenance identifies the exact Consumer revision, Hub pin, schema versions, execution environment, and canonical artifacts.
- Reproduction under the approved plan yields results consistent with its predefined thresholds.
- The acceptance report distinguishes confirmed acceptance evidence from historical, exploratory, or superseded artifacts.

### Current status

`NOT STARTED`

No controlled Stage 7 evidence execution, sandbox validator, oracle change-control process, or reproducibility-backed acceptance set currently satisfies these criteria.

## Historical note - early baseline

> Early baseline evidence collection — COMPLETED AHEAD OF SCHEDULE (non-acceptance).
> One execution per canonical scenario was captured (N=1 per scenario; six canonical result artifacts total) and evaluated manually against the then-current expected/* oracles. The evidence was recorded against Hub commit f5dda9b45e1571c084aa70713f3730497bb10882. It has no machine-readable canonical-result manifest and no payload/trace schema. This is exploratory historical baseline evidence only. It does not satisfy Stage 6 or Stage 7 acceptance criteria, establish reproducibility or statistical confidence, or provide acceptance evidence for the current consumer pin or current Hub HEAD. The planned sequence remains Stage 4.1 → Stage 6 → Stage 7.

This historical note records evidence provenance and limitations only. It is not a completed Stage 6 or Stage 7 work item and must not be used to change their statuses.
