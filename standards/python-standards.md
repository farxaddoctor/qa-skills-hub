# Python Standards

## Core Standards

- Follow the consuming project's Python version, formatter, typing, import, and lint conventions.
- Keep fixtures explicit and scoped narrowly by default.
- Use parametrization for meaningful variations.
- Prefer direct assertions with useful failure output.
- Avoid hidden global state.
- Keep helpers small and behavior-revealing.

## Pytest Notes

- Use fixture cleanup patterns consistently.
- Avoid unrelated autouse fixtures.
- Use markers only when they have an established project meaning.
