---
name: domain-modeling
description: "Clarify domain terminology, entities, relationships, boundaries, and invariants when designing or revising a domain model or glossary."
license: MIT
metadata:
  origin: mattpocock-adapted
---

# Domain Modeling

## 1. Locate the relevant language
If GLOSSARY-MAP.md exists, follow its context links; otherwise read the relevant existing
GLOSSARY.md and domain documents. Follow established paths before proposing new ones.
When no glossary exists, discuss a draft model; absence alone does not authorize creation.
Reading a glossary for ordinary code work is not itself a modeling task.

## 2. Sharpen and stress-test the model
Challenge ambiguous/conflicting terms with concrete examples. Mark invented cases as
hypothetical. A term may legitimately have different meanings across bounded contexts;
qualify it at boundaries rather than forcing one global definition. For important concepts
identify identity, relationships, cardinalities, ownership and lifecycle/invariants.
Separate domain meaning from tables, classes and infrastructure.

Compare stated rules with accessible code. A mismatch is a decision to resolve, not proof
that current implementation or a proposed rule is automatically authoritative. Record
alternatives and downstream impact; ask only for business decisions or facts unavailable
from accessible sources. Do not invent product approval.

## 3. Separate artifacts and permission
First establish whether recording changes is authorized. If not, return proposed terms,
relationships, invariants, conflicts and open questions in the response; no file is written.
If writing is authorized, select the existing project format; only if no suitable format
exists use [the glossary template](assets/glossary-template.md). For structure/routing
questions read [recording guidance](references/recording.md).

Keep glossary entries concise: meaning, context, domain-specific aliases and agreement
status. Store detailed identity rules, relationships, lifecycle and invariants in the
established capability/spec/domain-model artifact and link to it when needed. A glossary
is not a specification, scratchpad or implementation-design store. Record resolved terms
promptly within scope; keep unsettled proposals visibly separate from agreed vocabulary.

## 4. Offer decisions sparingly
Propose an ADR when all three apply: reversal is meaningfully costly, the choice would
surprise a future reader without context, and genuine alternatives were weighed. Otherwise
use a lighter note or the existing project convention. Read the ADR branch of recording
guidance only when a decision merits recording. Use the established ADR format or an
available ADR Skill; none is mandatory. Discussion alone does not authorize writing an
accepted ADR. Implementation/schema design remains a separate task unless requested.
