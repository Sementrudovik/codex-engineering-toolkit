---
name: system-design
description: "Design a system boundary and responsibilities with C4-level views, interface/data decisions and key sequence or deployment diagrams."
license: MIT
metadata:
  origin: Toolkit-original
---

# System Design

Read required behavior, constraints and existing architecture. Start from the
decision the design must support, not a mandatory catalogue of diagrams.
Keep facts about the current system separate from proposed architecture.

## Views
- Context: people, in-scope system and directly connected external systems.
- Containers: applications/data stores and their responsibilities, technologies
  and communication. A C4 container need not be a Docker container.
- Components: add detail only for complex internal boundaries that need explanation.
- Sequences: show important success/failure, authorization and concurrency paths.
- Deployment: state runtime nodes, trust zones and persistence/recovery assumptions.
Label abstraction levels; a container view with implementation internals mixed in
is not a useful context diagram. Use a legend and consistent IDs/names.

## Decisions and trade-offs
Explain why the design fits scope/load/team constraints. Prefer existing/simple
architecture where adequate; do not impose microservices, queues or cloud services.
Define ownership, interfaces, contracts, consistency and failure behavior.
Tie data and state transitions to the same requirements as sequences and processes.
Separate latency/recovery targets from measured results.
Record a material decision as a proposed ADR or follow the project's approved
decision procedure; do not silently mark architectural choices accepted.

## Verify
Check every named operation/entity against contracts and data models.
Check trust boundaries, retries, idempotency and atomic updates where relevant.
Diagrams show intent, not deployed infrastructure or passing tests.
If no renderer is available, deliver diagram source and label rendering unverified.

## Deliver
Use [the design template](assets/design-template.md). Provide only relevant views,
trade-offs, unresolved questions and a justified implementation handoff.
Existing API/ADR/contract Skills may help, but are not mandatory dependencies.
No publication, deployment, agent spawning or external configuration is implied.

