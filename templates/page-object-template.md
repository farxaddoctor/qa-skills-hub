# Page Object Template

## Purpose

Describe the page, component, or workflow represented by this object.

## Responsibilities

- User actions.
- Meaningful state queries.
- Stable navigation or workflow helpers.

## Locators

Prefer role, label, placeholder, text, alt text, or approved test ids.

## Actions

Behavior-focused methods that match user intent.

## Assertions

Prefer assertions in tests unless a shared assertion represents a stable component contract.

## Avoid

- Mirroring every DOM element.
- Hiding unrelated setup.
- Exposing brittle selectors to tests.
