# Claude Code Orchestration

Use this repository as a universal QA automation orchestration library.

## Operating Rules

- Start with `constitution/qa-agent-constitution.md` for always-on AI QA rules.
- Use `routing/skill-routing-rules.md` to choose the workflow, agent, and skills.
- Treat `workflows/` as the ordered process and `agents/` as role responsibilities.
- Read selected `skills/*/SKILL.md` files only after routing identifies the needed capability.
- Apply `policies/audit-before-edit.md` before file changes and `policies/human-gate-policy.md` before risky actions.
- Keep all output project-neutral unless the consuming project provides specific context.
- Do not invent application behavior, URLs, roles, credentials, selectors, or domain rules.
- Do not add Selenium guidance unless the user explicitly expands scope later.

## Default Flow

1. Apply the Constitution and relevant policies.
2. Classify the request and route it through the orchestrator.
3. Select the workflow, agent, and skill set.
4. Ask for missing critical inputs only when assumptions would be risky.
5. Follow audit and Human Gate requirements before edits or risky recommendations.
6. Produce concise QA output with assumptions, gaps, handoffs, and verification notes.
