# Instruction placement and review

Use existing project conventions first; these are placement choices, not mandatory files.

| Material | Appropriate home and reading condition |
|---|---|
| Project/global steering | AGENTS.md: short applicable rules and precise navigation pointers; global scope only for genuinely cross-project guidance |
| Mechanical rule | Existing linter/type/test checks when a deterministic pattern can enforce it economically |
| Judgment, rationale, exceptions | Established coding standards; read when implementing or reviewing affected behavior |
| Detailed explanation | Existing docs/reference reached under an explicit task condition |
| Reusable discipline | A scoped Skill when it has an independent use case; no mandatory Skill chain |

Separate implementation from review as stages even when one agent performs both.
Implementation carries exploration and execution context; review checks the resulting diff
against requirements, relevant standards and evidence. A reviewer may need more than a diff
to understand semantics, so do not assume review requires no exploration. Both stages must
honor required checks; putting a rule in review is not permission to ignore it in implementation.
Suggest a pointer only when existing navigation is missing or ineffective. A new standards
file, hook or additional reviewer is a proposal requiring its own value and applicable scope.
