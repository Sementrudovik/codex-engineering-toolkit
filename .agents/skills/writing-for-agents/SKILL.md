---
name: writing-for-agents
description: "Write or audit agent-facing instructions, Skills, and AGENTS.md for clear activation, scoped dependencies, and verifiable completion."
license: MIT
metadata:
  origin: mattpocock-adapted
---

# Writing for Agents

## 1. Establish the contract
Identify the document's consumers, authorized task, existing conventions and constraints.
Distinguish a requested audit from permission to edit. Preserve material permissions,
exceptions and failure behavior. Completion: you can explain what behavior the document
must change and what must remain true; a shorter file is not itself success.

## 2. Arrange the work
Keep guidance needed by every branch visible in the entrypoint. Move substantial
branch-specific material behind a pointer that states what it contains and when to read
it. Verify its target exists. Keep a definition, its rule and caveat together. A mandatory
guardrail must not depend on an optional or unbundled resource.

Consider both context load (metadata and instructions the agent reads) and human load
(what the user must remember, select and maintain). A split can improve one and worsen
the other. Use one authoritative location for shared meaning where practical; retain a
small local repetition if removing it would break standalone use or reliable activation.
Use project configuration as the source of discoverable facts; preserve reasons and
exceptions that cannot be recovered from it.

## 3. Apply the relevant editing techniques
When auditing pointers, splitting a document, pruning text, or repairing vague completion
criteria, read [editing techniques](references/editing-techniques.md). For a narrow edit
that does not affect these, the entrypoint is sufficient. When creating or changing a
Skill's packaging or invocation, also read [Skill packaging](references/skill-packaging.md).
Do not load that branch merely to edit a human-facing document.

For ordered work, define observable completion of each consequential stage. Flat reference
material is valid when it serves the task; numbering does not by itself improve a document.
Do not split work into extra agents merely to create context boundaries.

## 4. Check meaning and activation
Compare before/after semantics, especially authorization, required checks and stopping
conditions. Try a relevant request and a near-miss; distinguish inspecting a description
from observing actual activation. For a claimed no-op, compare with/without it on the
relevant task when feasible; otherwise mark the judgment tentative. Report moved/removed
rules, resource dependencies and unresolved ambiguity. Completion requires preserved
mandatory behavior and resolved references, not just a YAML parse or smaller character count.
Claim lower task cost only with comparable usage evidence including retries and failures.
Apply only authorized edits; an audit does not authorize rewriting unrelated/global rules.
