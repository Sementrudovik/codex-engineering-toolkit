---
name: retro
description: "Review a completed coding session and propose evidence-backed improvements to the agent environment, checks, navigation, and instructions."
license: MIT
metadata:
  origin: mattpocock-adapted
---

# Session Retrospective

## 1. Establish the evidence
Use the session named by the user, or the current session. Read its relevant artifacts,
commands and outcomes; scope log inspection to that session. Separate observed events,
inferred causes and proposed improvements. Completion: the session boundary and evidence
gaps are explicit. Missing logs are not evidence that an event did or did not occur.

## 2. Inspect existing feedback and instructions
Locate the project's actual check commands, CI and relevant instruction files before
proposing additions. Distinguish a missing check from one skipped, unwired, failing to
execute, or passing while missing the regression. When a placement/role decision is
needed, read [instruction placement](references/instruction-placement.md).
Completion: each relevant existing mechanism and its observed failure are identified,
or access is reported unavailable. No second agent or Skill is mandatory.

## 3. Examine applicable categories
Scan all seven categories; deepen those supported by session evidence. Mark categories
not applicable or unknown rather than inventing findings to fill the list.

| Category | Use when | Investigate |
|---|---|---|
| Navigation | Repeated search, wrong files or hidden dependencies delayed work | Existing index/pointer, its read condition and whether it was actually followed |
| Automated checks | An error escaped available feedback, or a relevant check could not run | Existing command, coverage boundary and execution evidence; then the smallest missing check |
| Coding standards | A review missed a concrete violation or a rule conflicted with project practice | Mechanical failure suitable for a deterministic check versus a judgment requiring context |
| Global/project instructions | Relevant steering is large, contradictory or outside its proper scope | The rule's owner, applicability and whether project-only guidance leaked into global scope |
| Tool economy | Repeated or expensive calls are evidenced | Redundant work, avoidable output, caching and maintenance cost; distinguish usage from estimates |
| No-ops/stale rules | Instructions appear redundant or no longer match the environment | Whether removal changes behavior on the affected task; uncertainty is not proof of a no-op |
| Information access | Missing information blocked a conclusion or check | Minimum authorized read access or redacted evidence needed, not broad new privileges |

No CI or hook is not by itself a defect: relate the gap to project risk and workflow.
A single incident may justify a local repair, not a universal rule.

## 4. Present and verify recommendations
For each supported finding give evidence, consequence, likely mechanism, smallest useful
intervention and verification criterion. Rank by impact and strength of evidence. Prefer
an existing deterministic check for mechanical errors when practical; keep judgment and
non-discoverable context in instructions. Compare maintenance/execution cost before
proposing another hook, MCP server or agent. Report data gaps and applicable categories
with no supported finding. Completion is an actionable recommendation, not a list of
mandatory infrastructure additions.

A retrospective authorizes analysis, not automatic changes to global settings, standards,
hooks or CI. Implement only within already authorized scope or after approval of a concrete
proposal. Do not invent savings, usage, owners or agreement. If writing instructions is
part of the authorized follow-up, use an available writing workflow or existing conventions;
loading writing-for-agents is optional and does not itself guarantee writing quality.
