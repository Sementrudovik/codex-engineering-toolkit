---
name: requirements-spec
description: "Create or revise a short technical specification with sourced functional and measurable nonfunctional requirements and explicit acceptance status."
license: MIT
metadata:
  origin: Toolkit-original
---

# Requirements Specification

Identify purpose, actors, system boundary, existing sources and requested depth.
Retain established requirement IDs; never renumber a referenced requirement silently.
A small task may need a short spec, not a full enterprise document.

## Define requirements
For each requirement record ID, type (FR/NFR/constraint), one testable statement,
source, rationale, priority, acceptance method and status (draft/proposed/approved).
Separate requirement, design decision, assumption and unresolved question.
Use observable inputs, preconditions, outputs and failure behavior rather than
vague phrases such as fast, secure or user-friendly.
Include relevant negative/authorization cases and data/error semantics.

## Nonfunctional requirements
State metric/unit, workload and environment, threshold and validation method.
If load, target or recovery window is unknown, label it proposed/unknown and name
what must be measured. Do not present a target as observed performance.
Treat security, availability, audit, privacy and recovery as scoped requirements,
not a universal checklist promising compliance.

## Consistency
Link FRs to stories/acceptance cases, interface operations and relevant entities.
NFRs may instead map to a cross-cutting verification scenario.
Do not mark an item verified because a diagram or schema exists.
Check duplicates, contradictions, hidden dependencies and scope creep.
Record ownership and unresolved approvals without inventing stakeholder names.

## Deliver
Use [the specification template](assets/spec-template.md) or the project format.
Return the short spec and explicit unresolved questions that block implementation.
Preserve history of changed semantics. No legal/regulatory certification is implied.
No code execution, MCP, agent or external system is required.

