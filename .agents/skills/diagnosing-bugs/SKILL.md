---
name: diagnosing-bugs
description: "Diagnose reported software failures or performance regressions through reproducible evidence and falsifiable hypotheses before fixing."
license: MIT
metadata:
  origin: mattpocock-adapted
---

# Diagnosing Bugs

Confirm the symptom, expected behavior, environment and scope: diagnosis only or a fix
as well. Read relevant code and domain records when available. Preliminary read-only
hypotheses can guide reproduction; distinguish them from established causes. Redact
secrets and minimize captured payloads in every phase. Production probes, stress,
trace capture and new instrumentation require applicable authorization.

## 1. Build a symptom-specific feedback loop
Locate the existing test/command nearest the real failure boundary. If it is insufficient,
read [reproduction approaches](references/reproduction.md) for alternatives; load the
intermittent/performance branch there only for those symptoms.
Record the command, input/version and actual result. Completion: a runnable observation
that can distinguish the reported symptom from success, or an explicit missing-access/
evidence blocker. An import/setup error alone does not reproduce the user's bug.
If blocked, list attempts and needed access/redacted artifacts; offer tentative ranked
hypotheses with predictions if useful. Do not present a cause or fix as verified, or retry
indefinitely. Continue only work independent of the missing evidence.

## 2. Reproduce and minimize
Observe the reported failure; capture its specific output or measured regression.
For intermittent failures record attempts, failures, seed/timing and workload.
Remove one input/caller/config element at a time and rerun; retain the conditions carrying
the failure. Completion: the smallest practical scenario still reproduces the same symptom;
explain limits to further minimization. Do not shrink away a second caller in a shared-state bug.

## 3. Rank falsifiable explanations
For each plausible hypothesis state its evidence, prediction and discriminating check.
Use the number warranted by evidence, not a fixed quota. Surface the ranking for useful
user context, while continuing authorized read-only probes that do not depend on an answer.
Completion: predictions separate alternatives; label causes, contributing conditions and
incidental errors distinctly. No reproduction means the ranking remains unverified.

## 4. Instrument the discriminating boundary
Prefer debugger/REPL inspection when it is available and suitable; otherwise use narrow
logs tied to a prediction. Change one relevant variable at a time where feasible.
Tag newly introduced diagnostic logs with a unique prefix and record the locations for
cleanup. Preserve pre-existing logs. For latency/throughput, use comparable workloads,
timings/profiles/query plans and variability, rather than treating extra logging as a
measurement strategy. Completion: evidence supports/refutes the prediction, or the probe
is explicitly inconclusive. Avoid broad logging of sensitive data.

## 5. Fix and regression-test when authorized
Diagnosis-only stops at findings/proposed next checks. For an authorized fix, exercise the
real caller seam with a regression check before the change when feasible. Observe RED,
apply the smallest justified fix, observe GREEN, then rerun the original unminimized
scenario. If reproduction required modifying a fixture, compare with a pristine copy
and identify what changed. A test at the wrong seam is not proof of regression protection.
If no adequate seam/environment exists, report that limitation; do not fabricate results.
Existing testing/TDD tools are optional aids, not required Skills. Completion: the original
symptom is addressed by observed evidence, or readiness is explicitly limited.

## 6. Clean up and report
- Account for original-repro and regression-check results, including NOT_RUN reasons.
- Remove only instrumentation/prototypes introduced for this diagnosis, or retain clearly
  identified evidence in an agreed debug location; verify tagged logs were handled.
- Preserve user changes and state the supported cause, confidence, fix and remaining risks.
- Include the causal explanation in a requested commit/PR description when applicable.

Completion is evidence-backed readiness, not merely a plausible patch. Commit, deployment
and external writes need applicable authorization and are not mandatory debugging steps.
