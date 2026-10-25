---
name: product-capability
description: "Translate product intent into actors, states, invariants, interface and data constraints ready for requirements or architecture review."
license: MIT
metadata:
  origin: ECC-adapted
---

# Product Capability

Use when a PRD/discussion exists but implementation-facing constraints are implicit.
Read relevant product context, current architecture and existing contracts.
Keep a single durable capability artifact in the project's established location.

## Analyze
State the actor, capability, user outcome and boundaries.
Separate user-visible promises from design preferences and policy decisions.
Define lifecycle states, allowed transitions, invariants, permissions and ownership.
Identify interfaces, input/output meaning, missing/null/default semantics, failure
paths, idempotency, migration and observability implications where relevant.
Expose data ownership, retention/deletion and recovery obligations.
Never invent product truth or silently resolve an approval-dependent business rule.

## Make it actionable
Use stable capability/requirement identifiers when the project has them.
For important constraints state how they can be verified and where enforcement lives.
Keep unresolved decisions with impact, owner if known, and next validation action.
Reconcile with existing schemas/workflows. State conflicts explicitly.
Include only relevant concerns; do not add billing, microservices or a new planning
stack when they do not belong to the capability.

## Deliver
Return capability, constraints, actors/surfaces, states, interface/data implications,
non-goals, open questions and handoff: ready / needs architecture / needs product input.
Use [the template](assets/capability-template.md) when no established artifact exists.
No external template path, MCP, agent, hook or command is required.
This is not a full SRS or a substitute for approval of unresolved product rules.

