# How To Use With Claude Code

Use the consumer repository's root `CLAUDE.md` as the Claude Code entry point.
That file must direct Claude Code to
`vendor/qa-skills-hub/CLAUDE.md`, using the immutable hub dependency at the
standard relative path `vendor/qa-skills-hub`.

If the submodule is missing or uninitialized, stop and run from the consumer
root:

```text
python scripts/qa_hub.py bootstrap
```

## Required flow

After reading both Claude entry files, start the QA task with the applicable
hub command and route it through
`vendor/qa-skills-hub/agents/qa-orchestrator.md`.

```text
Consumer root entry -> Hub command -> QA Orchestrator -> Constitution -> Policies -> Routing -> Workflow -> Agent -> Skills -> Audit -> Human Gate -> Output
```

Do not invoke a skill directly or bypass orchestration. Skills are selected
only after routing, and audit-before-edit and Human Gate requirements remain in
force.

Keep product-specific context and generated artifacts in the consumer. Do not
replace the pinned submodule with copied files, symlinks, a local external
path, or separately installed skills.

For clone, doctor, update, rollback, and CI details, see
[docs/consumer-integration.md](consumer-integration.md).
