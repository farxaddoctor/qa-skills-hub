# Agent Catalog

These files define reusable QA-oriented agent roles. Use them as role prompts or subagent briefs in tools that support specialized agents.

| Agent | Purpose |
| --- | --- |
| `agents/qa-orchestrator.md` | Routes QA work to the right skill, agent, or standard. |
| `agents/test-designer.md` | Converts requirements and risks into test coverage. |
| `agents/playwright-engineer.md` | Handles Playwright TypeScript automation guidance. |
| `agents/api-automation-engineer.md` | Handles language-neutral API testing strategy. |
| `agents/java-api-automation-engineer.md` | Handles Rest Assured Java API automation guidance. |
| `agents/python-automation-engineer.md` | Handles Pytest Python automation guidance. |
| `agents/qa-code-reviewer.md` | Reviews QA automation code and test design quality. |

Agents should remain universal. Add project-specific context only in the consuming project or prompt.
