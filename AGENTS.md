# Agent Catalog

These files define reusable QA-oriented agent roles. Use them as role prompts or subagent briefs in tools that support specialized agents.

## Canonical Agents

| Agent | Purpose |
| --- | --- |
| `agents/qa-orchestrator.md` | Routes requests through Constitution, policies, routing, workflows, agents, skills, audit, and Human Gate. |
| `agents/test-designer.md` | Converts requirements and risks into test coverage. |
| `agents/automation-engineer.md` | Plans or implements automation through the selected framework skill after scenarios and strategy are clear. |
| `agents/api-test-engineer.md` | Designs API test coverage from contracts, endpoint behavior, and integration risks. |
| `agents/qa-code-reviewer.md` | Reviews QA automation code and test design quality. |
| `agents/bug-analyst.md` | Analyzes failures, defects, and flaky behavior before regression design or automation changes. |

## Compatibility Agents

These older role files remain for compatibility and should delegate to the canonical agents.

| Agent | Delegates to |
| --- | --- |
| `agents/playwright-engineer.md` | `agents/automation-engineer.md` with `skills/playwright-typescript/SKILL.md`. |
| `agents/api-automation-engineer.md` | `agents/api-test-engineer.md` with `skills/api-testing/SKILL.md`. |
| `agents/java-api-automation-engineer.md` | `agents/api-test-engineer.md` with `skills/rest-assured-java/SKILL.md`. |
| `agents/python-automation-engineer.md` | `agents/automation-engineer.md` with `skills/pytest-python/SKILL.md`. |

Agents should remain universal. Add project-specific context only in the consuming project or prompt.
