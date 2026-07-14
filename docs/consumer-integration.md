# Consumer Integration

Use a Git submodule as the recommended way to connect this hub to a consumer
repository. The consumer stores an immutable, full 40-character hub commit in
its gitlink, so every clone, agent, and CI runner resolves the same content.

This guide is application-agnostic. Keep product requirements, code, tests,
credentials, environment details, and other product-specific context in the
consumer repository. Treat the hub checkout as an immutable dependency.

## Integration contract

Use this standard relative path:

```text
vendor/qa-skills-hub
```

The consumer `.gitmodules` file records the reviewed hub origin and the path.
The consumer gitlink records the approved commit. Do not use a floating branch,
`--remote`, a local external checkout, an absolute filesystem path, or a
symlink as the integration source.

The consumer supplies these root entry instructions:

- `AGENTS.md` for Codex;
- `CLAUDE.md` for Claude Code;
- `.cursor/rules/qa-skills-hub.mdc` with `alwaysApply: true` for Cursor.

Each entry points to the hub through `vendor/qa-skills-hub`, keeps consumer
context in the consumer repository, and preserves this chain:

```text
Consumer root entry -> Hub command -> QA Orchestrator -> Constitution -> Policies -> Routing -> Workflow -> Agent -> Skills -> Audit -> Human Gate -> Output
```

QA requests must enter through a hub command and
`agents/qa-orchestrator.md`. Direct entry-to-skill or command-to-skill bypass is
forbidden.

## Clone and bootstrap

Clone a consumer repository and initialize its exact pinned hub commit with:

```text
git clone --recurse-submodules <consumer-repository-url>
```

If a consumer was cloned without submodules, or the hub is missing or
uninitialized, run the consumer-side bootstrap from the consumer root:

```text
python scripts/qa_hub.py bootstrap
```

Bootstrap validates the fixed `.gitmodules` path and origin, verifies gitlink
mode `160000`, and runs path-scoped submodule sync and update operations. It
does not select a branch or floating revision. After initialization it runs the
same strict doctor described below.

## Health checks

Run the dependency-free, read-only doctor from the consumer root:

```text
python scripts/qa_hub.py doctor
```

The doctor checks, in order:

1. the consumer Git repository;
2. the exact `.gitmodules` path and origin;
3. gitlink mode `160000`;
4. submodule initialization;
5. checkout SHA equality with the tracked gitlink;
6. a clean hub checkout;
7. required architecture anchors and the hub validator;
8. consumer-root agent entries;
9. native submodule integration without symlinks or external paths;
10. the hub static validator;
11. a clean consumer repository.

Common diagnostics are:

- missing or uninitialized hub: exit `22`; run bootstrap;
- stale checkout or checkout/gitlink mismatch: exit `23`; run bootstrap;
- dirty hub checkout: exit `24`; stop and inspect the hub changes;
- dirty consumer: exit `25`; review all reported changes before retrying;
- invalid configuration, gitlink, structure, or validator: exits `20`, `21`,
  `26`, or `27`; repair the reported defect before continuing.

## Immutable updates

Update only to a reviewed full SHA:

```text
python scripts/qa_hub.py update --commit <40-character-sha>
```

The update command runs the strict doctor before fetching anything, verifies
that the configured `origin` matches `.gitmodules`, fetches only the explicit
SHA, verifies a commit object, performs a detached checkout, and stages only
the `vendor/qa-skills-hub` gitlink. It runs the hub validator and post-update
integration checks before reporting success.

The command does not create a commit, push, pull request, or branch. Review the
single staged gitlink and commit it through the consumer repository's normal
reviewed workflow. If a post-checkout operation fails, the command attempts to
restore the previous detached checkout and gitlink automatically.

## Rollback

Before the staged gitlink is committed, restore it from `HEAD`, restore the
path-scoped checkout, and run the doctor:

```text
git restore --source=HEAD --staged -- vendor/qa-skills-hub
git submodule update --init --recursive -- vendor/qa-skills-hub
python scripts/qa_hub.py doctor
```

After an update has been committed, revert the corresponding consumer commit
through the normal reviewed workflow, then restore and validate the checkout:

```text
git revert <consumer-commit-sha>
git submodule update --init --recursive -- vendor/qa-skills-hub
python scripts/qa_hub.py doctor
```

Do not use force operations or destructive reset as an integration rollback.

## Consumer CI

Consumer CI should use one matrix job for Ubuntu and Windows. The workflow
checks out recursive submodules, sets up Python without installing packages,
and runs from the consumer root:

```text
python scripts/qa_hub.py doctor
```

In a separate step with `vendor/qa-skills-hub` as its working directory, run:

```text
python scripts/validate_repository.py
```

Use read-only repository permissions. Do not run canonical consumer scenarios
as part of this integration health workflow.
