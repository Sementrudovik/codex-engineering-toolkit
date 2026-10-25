---
name: user-stories-ac
description: "Decompose an agreed capability into vertical user stories and observable acceptance criteria, including failure and authorization scenarios."
license: MIT
metadata:
  origin: ECC-adapted
---

# User Stories and Acceptance Criteria

Read agreed product/capability requirements and preserve their identifiers.
Split into thin vertical user outcomes, not separate database/backend/frontend chores.
A story describes actor, intent and benefit; a technical enabler is labelled as such.

## Write
For each story include ID, parent requirement IDs, context, scope, dependencies and
observable acceptance cases. Use Given/When/Then when it clarifies preconditions.
Include the happy path, meaningful boundaries, errors, retries/stale updates and
authorization behavior appropriate to the story.
Assign stable IDs to acceptance cases so they can link to tests and evidence.
Avoid acceptance criteria that merely prescribe internal method names.

## Estimate and state
Do not invent velocity, story points, sprint dates or business approval.
Distinguish proposed/planned/implemented/verified/accepted; use existing team status
definitions. A checked box does not prove a test or merge occurred.
Keep Definition of Done separate from acceptance of the user-visible behavior.
Readiness requires sufficient decisions to implement, not necessarily all nice-to-haves.

## Handoff
Use [the story template](assets/story-template.md).
Show requirement -> story -> acceptance case links and unresolved conflicts.
Do not create .stories state, reserve IDs in .git, run a ledger script, open issues
or synchronize Jira/Linear without a specifically authorized integration.
No mandatory TDD/reviewer agent is required; tests should target the acceptance cases.
This adaptation retains planning/AC concepts of ECC story-lifecycle, not its
transactional ledger, sprint automation or implementation-state authority.

