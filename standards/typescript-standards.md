# TypeScript Standards

## Core Standards

- Follow the consuming project's TypeScript version, formatter, lint rules, and module conventions.
- Prefer explicit types where they clarify contracts.
- Avoid `any` unless the project has a clear reason.
- Keep helpers small and typed.
- Avoid hidden shared mutable state.
- Keep async behavior explicit.

## Test Code Notes

- Test code should be as readable as production code.
- Prefer behavior-named helpers over generic utilities.
- Keep data builders deterministic and easy to debug.
