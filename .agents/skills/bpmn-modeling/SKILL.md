---
name: bpmn-modeling
description: "Model as-is or to-be business processes with BPMN events, tasks, gateways and responsibility boundaries; produce BPMN XML when requested."
license: MIT
metadata:
  origin: Toolkit-original
---

# BPMN Process Modeling

Clarify process goal, start/end conditions, actors, artifacts and scope.
Separate observed as-is facts from hypothetical/proposed flows. Never invent a
current process or improvement percentage to complete an as-is/to-be comparison.

## Model semantics
Use tasks for work, events for occurrence/waiting, and gateways for branching/joining.
Sequence flows stay inside a process/pool. Use message flows across pools; lanes
allocate responsibility and do not replace collaboration boundaries.
Make exclusive conditions mutually understandable, with a default branch where useful.
Do not use parallel joins unless every active path can reach them correctly.
Model relevant rejection, timeout/retry, cancellation and recovery outcomes.
Do not equate BPMN business orchestration with an API call sequence.

## Artifacts
For a business discussion provide a process narrative/table plus a diagram.
For BPMN interchange produce .bpmn XML with correct namespaces, unique IDs,
valid references and, when a visual editor is the target, BPMN DI coordinates.
Mermaid flowcharts may accompany a model but are not BPMN XML.
Mark isExecutable=false unless a specific engine/runtime contract is implemented.

## Verify
Check all flow endpoints, incoming/outgoing links, lane membership and reachability
from starts to ends. Review split/join semantics and termination paths.
Run a trusted local BPMN XSD/engine validator if available; distinguish XML parsing,
structural checks, XSD validation and actual process execution.
A structurally valid graph does not prove correct token semantics.
Do not download or execute arbitrary referenced schemas. Report unperformed checks.

## Deliver
Keep requirements and process element IDs aligned using [the process checklist](assets/process-checklist.md).
Provide proposed vs approved status, assumptions and validation evidence.
No BPMN engine, MCP, plugin installation or external publication is required.

