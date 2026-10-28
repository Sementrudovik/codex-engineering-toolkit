# Reproduction approaches

Choose the cheapest authorized approach that exercises the actual symptom. The list is
an escalation menu, not ten mandatory steps. Reuse project infrastructure where possible.

1. Existing failing unit/integration/E2E test at the real caller seam.
2. HTTP request against an authorized development/staging service, asserting the symptom.
3. CLI with a fixed fixture and expected output or exit behavior.
4. Browser automation with narrow DOM/console/network assertions where available.
5. Redacted replay of a captured request/event through the relevant path.
6. Disposable minimal harness retaining failure-bearing services and callers.
7. Property/fuzz exploration with controlled input bounds, seed and failure capture.
8. Bisection across known commits, datasets or configurations on a safe isolated checkout.
9. Differential execution on old/new versions under comparable inputs/environment.
10. Human-assisted steps with an explicit observation checklist when automation is unavailable.

For human assistance, specify steps, the symptom and how observations are returned; keep
credentials out of captures. No active HITL shell helper is bundled. The archived upstream
shell text is provenance, not a ready-to-run tool. A helper would require separate adaptation
and validation. Do not install browser/fuzz/network tooling automatically.

Tighten a valid loop by reducing unrelated setup, making the assertion symptom-specific and
controlling time/randomness/filesystem/network where relevant. Record the trade-off if a
faster loop no longer exercises the actual failure. Do not turn production capture/load into
an implicit permission from a debugging request.

## Intermittent failures
Record trials and failures with relevant seeds/concurrency/timing. Controlled repetition or
stress may increase observability only in an authorized bounded environment. There is no
universal frequency threshold for a debuggable bug; an observed rate is not a guarantee.
State the trial budget/stop condition and retain the exact failing case where possible.

## Performance regressions
Keep workload, environment and warm/cold-cache conditions comparable. Collect timings,
variability, profiles/query plans or queue/downstream boundaries as available. Bisect only
when there are comparable known states and a reliable measurement. A logging change can
alter latency; distinguish diagnostic perturbation from a demonstrated performance fix.
