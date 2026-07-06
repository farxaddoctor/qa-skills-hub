# QA Skills Hub

QA Skills Hub is a reusable AI skills library for QA automation work across projects and coding agents. It is designed for Claude Code, Codex, Cursor, and other agentic coding tools that can read repository instructions and task-specific skill files.

This repository is intentionally application-agnostic. It does not assume a company, product, staging URL, test account, user role, domain model, or existing test framework.

## What This Repository Provides

- Reusable QA automation skills for AI coding agents.
- Agent role prompts for planning, implementation, review, and bug analysis.
- Command prompts for common QA automation workflows.
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
  skills/       Reusable skill instructions for AI agents
  agents/       Role-oriented agent prompts
  commands/     Task-oriented command prompts
  standards/    General engineering and QA standards
  templates/    Reusable markdown templates
  third-party/  Placeholder directories for copied or adapted external material
  docs/         Usage and attribution documentation
```

## How To Use

1. Pick the skill that matches the task from `SKILL_INDEX.md`.
2. Provide the selected skill file to the AI agent as context.
3. Add project-specific context separately, such as framework conventions, existing fixtures, API contracts, or coding standards.
4. Ask the agent to follow the selected skill and the relevant standards.
5. Review the generated work before using it in a real project.

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
