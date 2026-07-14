# How To Use With Codex

Use the consumer repository's root `AGENTS.md` as the Codex entry point. It
must reference the immutable hub dependency through the relative path
`vendor/qa-skills-hub` and keep product-specific context in the consumer.

If the submodule is missing or uninitialized, stop and run from the consumer
root:

```text
python scripts/qa_hub.py bootstrap
```

## Required flow

Start each QA task with the applicable file under
`vendor/qa-skills-hub/commands/`, then route through
`vendor/qa-skills-hub/agents/qa-orchestrator.md`.

```text
Consumer root entry -> Hub command -> QA Orchestrator -> Constitution -> Policies -> Routing -> Workflow -> Agent -> Skills -> Audit -> Human Gate -> Output
```

Do not invoke a skill directly or bypass orchestration. Skills are selected
only after routing. Apply audit-before-edit and Human Gate requirements before
changes, and keep generated product artifacts in the consumer repository.

Codex should inspect and preserve consumer conventions, run the consumer's
normal verification commands, and report checks that could not be completed.

For clone, doctor, update, rollback, and CI details, see
[docs/consumer-integration.md](consumer-integration.md).
