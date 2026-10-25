---
name: requirements-traceability
description: "Check consistency and evidence links across requirements, stories, acceptance cases, interfaces, processes, data models and tests."
license: MIT
metadata:
  origin: Toolkit-original
---

# Requirements Traceability and Consistency

Locate authoritative artifacts and their versions. Preserve stable IDs.
Use a graph of evidence links, not repeated copies of requirement prose.

## Map
Link source -> requirement -> story/acceptance case -> implementation boundary
(operation/process/entity) -> validation case -> evidence.
NFRs may use cross-cutting verification cases instead of a user story.
Track assumptions and decisions separately from verified facts.
Use meaningful relation types (implements, verifies, realizes, depends_on), not
a flat claim that every linked artifact proves every other one.

## Check
Detect broken links, duplicate IDs, contradictory states/field names, orphan FRs,
missing acceptance cases, tests that check the wrong boundary and stale evidence.
State coverage denominator and exclusions. A linked test is planned coverage;
a PASS requires actual result evidence tied to a version/run.
An illustrative DB test must not be labelled full HTTP authorization/E2E verification.
Check API/business/schema/diagram semantics manually as well as link syntax.

## Machine-readable option
Use [the graph format](assets/traceability-format.md) and the bundled
[scripts/check_traceability.py](scripts/check_traceability.py) for JSON ID/ref/evidence
checks. Run it on trusted local files; it does not execute tests or prove semantics.
Do not mark approved/accepted merely because the checker passes.
Keep source artifacts authoritative; a generated coverage table is a projection.

## Deliver
Report inconsistencies first, with affected IDs and proposed resolution.
Then provide planned vs executed/verified coverage and remaining blockers.
Do not invent test results, owners, dates or a completeness percentage without a
defined denominator. No tracker/MCP integration or file mutation is required
unless the task authorizes writing the reviewed artifacts.

