---
name: python-testing
description: "Design and run Python tests with pytest fixtures, parametrization, mocks and optional async or coverage support."
license: MIT
metadata:
  origin: ECC-adapted
---

# Python Testing

## Discover the runner
Read relevant tests, pyproject.toml and pytest.ini/tox.ini/setup.cfg.
Resolve the project interpreter and plugins. Retain unittest if established;
do not migrate a suite merely because pytest is common.
A missing runner/plugin is a limitation, not permission for a silent installation.

## Select observable cases
Translate acceptance criteria or a regression into behavior assertions.
Cover relevant success/failure paths, boundaries, null/empty inputs and tenant/auth
boundaries. Test outputs and side effects rather than private names or exact prose.
Use parametrization for genuinely parallel cases with individually useful failures.
An import/setup error does not reproduce a business regression.
Use temporary files/disposable databases; clean resources deterministically.
Do not touch production/user data to make a test realistic.

## Fixtures and mocks
Use the narrowest sensible fixture scope. Avoid hidden state in autouse fixtures.
Patch where the symbol is looked up; use autospec/spec when an interface matters.
Mock external nondeterminism, not the behavior under test. A valid fixture does not
prove a real provider returns it. Control clocks/randomness; avoid arbitrary sleeps.

## Async
Inspect installed pytest-asyncio/anyio versions and configuration before choosing syntax.
In pytest-asyncio strict mode, async tests need the asyncio mark and async fixtures
need the plugin's fixture decorator. Match fixture lifetime with event-loop scope.
Do not assume fixtures work identically across plugin versions or modes.
Test cleanup/cancellation when relevant. If the async runner is missing, report
async tests NOT RUN rather than imply synchronous tests cover those paths.

## Run and interpret
Example commands when the configured environment contains pytest:
- python -m pytest tests/test_shipments.py -q
- python -m pytest tests/test_shipments.py::test_rejects_transition -q
Coverage flags require the configured coverage tool/plugin and a real package target.
Use project coverage thresholds; do not invent universal 80%/100% requirements.
Capture the command, exit status and actual passed/failed/skipped counts.
No tests collected (pytest exit 5) is not a successful test suite.
Keep complete diagnostics even when summarizing output.

## Complete
Run focused tests before broader required gates. Repeat passed checks only after
relevant changes/new evidence. Never weaken assertions to obtain green.
Report limitations and flakiness. No mandatory MCP, agent or package-manager script.

