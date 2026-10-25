---
name: security-review
description: "Review changed code for exploitable trust-boundary failures, sensitive-data handling and dependency risks; lead with evidence."
license: MIT
metadata:
  origin: ECC-adapted
---

# Security Review

## Scope and authorization
Identify affected actors, entrypoints, protected data/resources, dependencies and
trust boundaries. Inspect reachable code paths before attributing an exploit.
Review is diagnostic by default. Keep findings separate from user-authorized fixes;
do not mutate dependencies, credentials or cloud resources just to review them.

## Inspect relevant boundaries
- Verify server-side object/tenant authorization across read/list/filter/export
  and update paths, alternate identifiers and feature flags.
- Use parameterized SQL and validated inputs; avoid unsafe deserialization or
  evaluating untrusted data as code.
- For subprocesses avoid shell interpolation and validate arguments.
- For user-controlled URL fetching inspect redirects, private addresses, credentials
  and egress policy when SSRF is relevant; hostname strings alone are insufficient.
- Follow established secret storage. Redact tokens/passwords/private payloads in
  diagnostics; client errors must not leak stack traces or SQL.
- For authentication/session changes review expiry, revocation, cookie and CSRF
  model. Do not impose a generic JWT recipe without knowing the architecture.
- Escape/sanitize browser output appropriately. Do not default CSP to unsafe-inline
  or unsafe-eval to make an example work.
- For uploads/files check intended size/type/ownership, symlinks and race conditions
  as applicable. Extension-only checks are insufficient.
- For concurrency/money inspect atomic invariants, retries and stale updates when
  important behavior depends on them.
- Inspect dependency/lockfile provenance and pinned execution. A scanner's output
  is evidence with a scope, not proof that the product is secure.

## Python and tooling
Check subprocess, pickle/unsafe YAML, eval/exec, SQL construction, broad exceptions,
async blocking/cancellation and repr/log leakage when affected.
Type annotations do not validate a request body.
Use existing Bandit/pip-audit or other scanners only if available and suitable.
Inspect scanner commands when project tooling might execute untrusted code.
No automatic pip upgrade, npm audit fix, npm update or fetch-and-run installers.

## Findings and completion
Report severity, file/line, trigger, affected asset, plausible impact and correction.
Label hypotheses and confidence; a suspicious pattern without a reachable path is
not a confirmed vulnerability. Use negative boundary tests for authorized fixes.
Explain what was and was not reviewed. No production scan, attack, credential
rotation or third-party mutation is implied. No mandatory reviewer agent/MCP/hook.

