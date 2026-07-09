# QA Skills Hub

QA Skills Hub is a reusable AI skills library for QA automation work across projects and coding agents. It is designed for Claude Code, Codex, Cursor, and other agentic coding tools that can read repository instructions and task-specific skill files.

This repository is intentionally application-agnostic. It does not assume a company, product, staging URL, test account, user role, domain model, or existing test framework.

## What This Repository Provides

- Reusable QA automation skills for AI coding agents.
- Agent role prompts for planning, implementation, review, and bug analysis.
- Command prompts for common QA automation workflows.
- Workflow definitions for multi-step QA processes.
- Routing rules and safety policies for agent handoffs.
- Standards for test design, Playwright TypeScript, API testing, Rest Assured Java, Pytest Python, and review quality.
- Templates for test cases, bug reports, API tests, page objects, and PR reviews.
- Placeholder areas for attributed third-party material.

## Primary Focus Areas

- QA test design
- Playwright TypeScript
- API testing
- Rest Assured Java
- Pytest Python
- QA code review
- Bug analysis
- Test data generation

Selenium is intentionally out of scope for now.

## Repository Layout

```text
qa-skills-hub/
  constitution/ Always-on rules for AI QA agents
  skills/       Reusable skill instructions for AI agents
  agents/       Role-oriented agent prompts
  commands/     Task-oriented command prompts
  workflows/    Multi-step QA processes and handoff formats
  routing/      Decision rules for selecting agents and skills
  policies/     Safety and evidence policies for agent behavior
  standards/    General engineering and QA standards
  templates/    Reusable markdown templates
  third-party/  Placeholder directories for copied or adapted external material
  docs/         Usage and attribution documentation
```

## Orchestration Layers

- Constitution layer: always-on rules for AI QA agents.
- Policies layer: safety, approval, no-leakage, audit, and refactor constraints.
- Routing layer: selection of workflow, agent, and reusable skills.
- Workflows layer: ordered execution processes.
- Agents layer: reusable QA execution roles.
- Skills layer: reusable capability modules.
- Human Gate layer: stop and approval checkpoints.
- Commands layer: user-facing entry points.

## AI-Native QA Architecture

```text
Constitution -> Policies -> Routing -> Workflows -> Agents -> Skills -> Human Gate -> Commands
```

- Constitution: always-on rules for safety, evidence-based QA reasoning, audit-before-edit, human approval, and no product-specific leakage.
- Policies: safety and approval constraints that protect against unsafe edits, leakage, and risky refactors.
- Routing: selection of the workflow, agent, and skills for the user request.
- Workflows: ordered QA processes from intake through clarification, test design, automation strategy, implementation planning, review, and verification.
- Agents: reusable QA execution roles with responsibilities and handoffs.
- Skills: reusable capabilities selected by routing rules; Playwright TypeScript is only one possible automation skill.
- Human Gate: mandatory approval before broad refactor, auth/session changes, CI/CD changes, global config changes, dependency changes, file deletion, destructive cleanup, or assumptions about undocumented product behavior.
- Commands: user-facing entry points that route through the orchestrator instead of directly calling skills.

## How To Use

1. Pick the skill that matches the task from `SKILL_INDEX.md`.
2. For multi-step work, select a command or workflow from `commands/` or `workflows/`.
3. Apply routing rules from `routing/skill-routing-rules.md`.
4. Provide project-specific context separately, such as framework conventions, existing fixtures, API contracts, or coding standards.
5. Ask the agent to follow the selected skill, workflow, and relevant policies.
6. Review the generated work before using it in a real project.

## Design Principles

- Keep skills universal and portable.
- Prefer clear test intent over clever implementation.
- Separate test design from test automation.
- Make assumptions explicit.
- Do not invent product behavior when requirements are missing.
- Prefer stable contracts, accessible locators, deterministic data, and isolated tests.
- Treat AI output as a draft that must be reviewed.

## What This Is Not

This is not an application test framework. It does not include runnable Playwright, Rest Assured, or Pytest examples. It is a reusable instruction and standards library for agents that will work inside other repositories.

## Third-Party Material

Do not paste third-party content into this repository without attribution. Use `docs/source-attribution.md` and the placeholders in `third-party/` to record source name, URL, license, retrieval date, and adaptation notes.
