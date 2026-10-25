---
name: python-patterns
description: "Write or review Python application code with project-compatible typing, explicit errors, resource management and concurrency."
license: MIT
metadata:
  origin: ECC-adapted
---

# Python Development Patterns

## Establish scope
Read the affected package, pyproject.toml and relevant dependency/config files.
Respect the supported Python versions and existing architecture. Do not migrate
frameworks or add dependencies to illustrate a pattern. Use built-in generics on
Python 3.9+; use union syntax only with a compatible minimum version/annotation policy.

## Implement
- Annotate public boundaries with specific types. Use Protocol when structural
  interfaces help; annotations do not replace runtime input validation.
- Keep domain logic independent of I/O where this improves testability. Avoid
  imposing layers on a small module without an actual boundary to protect.
- Treat opaque IDs as strings. Choose Decimal or minor units for exact monetary
  arithmetic only with explicit domain rounding rules.
- Decide whether bool is valid for integer business inputs: bool subclasses int.
- Catch expected specific exceptions and preserve cause with raise ... from exc.
  Do not place secrets or personal payloads in exception messages.
- Use context managers for resources and transactions. A generator context manager
  must put cleanup in finally to handle exceptions inside the with block.
- Avoid mutable defaults and hidden global state; use explicit text encodings
  when persisting text. Reuse existing project conventions.
- Stream large inputs when useful. Do not claim a performance improvement from
  stylistic changes without measuring the relevant workload.

## Concurrency
Keep blocking calls out of the event loop. Reuse existing clients when appropriate;
set timeouts and concurrency bounds from requirements, not invented universal values.
Handle cancellation and resource cleanup. Threads may help blocking I/O; process
pools require suitable serialization and platform entrypoint handling.
With gather(return_exceptions=True), exceptions are possible results: narrow them
before returning values declared as strings. Never silently return exceptions
under an incompatible type annotation.

## Verification and delivery
Use installed project Ruff, mypy/pyright and tests; avoid duplicate formatters.
Run focused checks and broaden for shared boundaries, serialization or concurrency.
Unavailable tools are NOT RUN; do not install them implicitly.
For reviews, lead with concrete findings. For changes, report behavior, important
trade-offs, evidence and limits. No dedicated MCP, scripts or agents are required.

