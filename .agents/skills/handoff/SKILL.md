---
name: handoff
description: "Prepare a concise, source-linked handoff of the current task so another session can continue with decisions, state, checks, and open work."
license: MIT
metadata:
  origin: mattpocock-adapted
---

# Handoff

## 1. Choose the deliverable
Identify the recipient's next task and access constraints. Honor an explicit output mode
and destination. A request to create/save a handoff document or file produces a file;
use the requested or established location, otherwise the OS temporary directory and
report its path and limited persistence. A request for a handoff summary in chat produces
a response, not an unsolicited file. For an unspecified "handoff", default to a document
in the response and state that no file was saved. Do not silently substitute a chat
response for an explicitly requested file or overwrite an unrelated existing artifact.

## 2. Capture resumable state
Use the current task's relevant context and artifacts, not unrelated session history.
Use [the handoff template](assets/handoff-template.md) when no project format is established;
omit non-applicable sections rather than inventing content. Include the objective, scope,
authorization, state/version, decisions, changes, actual checks, blockers and next action.
Label user decisions, proposals and assumptions separately. A suggested command is not
a completed action; NOT_RUN remains NOT_RUN.

## 3. Link and protect evidence
Reference authoritative specs, patches, logs and commits rather than copying them.
Carry the essential continuation state if a referenced item is unavailable; mark access
and path verification gaps. Explain which local paths/data do not travel to another machine.
Suggested Skills are optional names whose availability must be checked by the recipient.
Omit secrets and minimize personal data in content, URLs, filenames and command arguments.
Use safe placeholders without copying secret values. Describe omitted relevant evidence
and the normal authorized access route when needed.

## 4. Check the handoff
Check that a recipient can identify the current state, what is established, what remains
unverified and the next permitted action. Report the chosen output mode and destination.
Producing a handoff does not authorize sending it to another session, pushing code or
continuing implementation there. Finish with unresolved acceptance/authorization gates.
