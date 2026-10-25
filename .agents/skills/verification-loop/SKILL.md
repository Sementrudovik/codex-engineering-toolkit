---
name: verification-loop
description: "Verify a completed change with project-specific tests, static checks, security review and diff inspection; report gaps explicitly."
license: MIT
metadata:
  origin: ECC-adapted
---

# Verification Loop

## Scope the change
Identify the working tree, staged/unstaged and relevant untracked files.
Select a comparison base justified by the task/branch; never assume HEAD~1 is
the current task boundary. Preserve unrelated user work.
Read project-required checks and identify affected consumers/shared modules.

## Choose applicable gates
1. Build/package verification if the project has such an artifact.
2. Type checking using its established mypy/pyright or other checker.
3. Lint/format check mode before any fixing mode.
4. Focused behavior tests, then required broader regression/integration tests.
5. Security checks relevant to changed boundaries/dependencies.
6. Final diff review for unintended changes and unmet acceptance criteria.
A focused test does not waive mandatory project gates.

## Execute faithfully
Use the configured interpreter and commands. Python examples when installed:
python -m pytest, python -m mypy, ruff check. Select real targets from the project.
Missing tools are NOT RUN, not PASS, and do not authorize installation.
Capture original exit status and diagnostics. Prefer direct process execution.
If a shell pipeline is needed, use pipefail in a compatible shell; limiting
displayed output must not replace the command status with tail/head status.
Do not regenerate lockfiles or run dependency upgrades merely for verification.

## Interpret and repair
Use PASS / FAIL / NOT RUN / NOT APPLICABLE with scope, command and evidence.
No tests collected and skipped critical cases are gaps. Pattern search is not a
complete security scan; redact secret values rather than print matching payloads.
Static typing and schema checks do not prove authorization or runtime correctness.
A failed required gate blocks readiness. Diagnose and fix within authorized scope;
rerun affected gates after repair. Do not repeat unchanged commands or suppress
checks to obtain green. Distinguish unrelated baseline failures.

## Handoff
Review the final diff after repairs. Report requirements met and material gaps.
Use READY / NOT READY / PARTIAL only within the verified scope. Missing/failing
mandatory gates prevent a READY-for-release claim.
No timer-based reruns, hooks, dedicated agents or MCP are required.

