# Playwright Standards

## Core Standards

- Prefer user-facing locators such as role, label, placeholder, text, alt text, or approved test ids.
- Use web-first assertions.
- Avoid arbitrary sleeps.
- Keep tests focused and independent.
- Use fixtures for shared setup and authenticated state when appropriate.
- Prefer API setup for expensive preconditions when reliable.
- Keep page objects behavior-focused.
- Capture useful artifacts for debugging in CI when supported.

## Avoid

- DOM-depth CSS selectors.
- Generated class selectors.
- Broad text matching when a role or label is available.
- Long tests that combine unrelated workflows.
- Hidden setup that makes the test intent hard to follow.
