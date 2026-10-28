# Codex Engineering Toolkit

Version **1.0.1-rc.2**, a release candidate dated 2026-10-28.
26 Skills: **4 Reuse / 17 Adapt / 5 Build**. The ECC source is pinned
to commit `90606c8315ee09cafc303515c5f33024db6b9882`.

The six additions adapt [mattpocock/skills](https://github.com/mattpocock/skills)
at commit `59db609eb1e18aaf59b63284d0e52255aff0c63c`.
See [release notes](RELEASE-NOTES.md) for acceptance and validation limits.

## Project installation

Open this folder as a Codex project. Skills are located in `.agents/skills/`.
For another existing or new project, copy the selected Skill directories into
`<project>/.agents/skills/`, preserving their resources and licenses.
Check for name collisions before copying; review existing Skills before replacing
them. Restart your Codex session if the new Skills do not appear.
Review project-specific AGENTS.md instructions and configuration separately:
this toolkit does not replace your project's rules. For local use across projects, copy the selected directories into
`~/.agents/skills/`. Check for duplicates between user and project locations;
keep one active copy per name. Updates to this repository do not automatically
update independent user installations.

## Usage

Within the project, request a Skill explicitly, for example:
`$system-design design a file-processing system` or
`$requirements-spec prepare a specification based on the agreed PRD`.
Codex can also select a suitable Skill based on the task description.
Skills apply to subsequent requests in sessions with access to this project;
earlier chat history is not automatically reprocessed.
Copying this folder does not make local Skills available in ordinary ChatGPT chats.

| Skill | Purpose | Status |
|---|---|---|
| `api-design` | REST API resources, errors, and pagination | Reuse |
| `architecture-decision-records` | Architectural decisions and alternatives | Reuse |
| `contract-first` | A shared contract for consumers and providers | Reuse |
| `scientific-thinking-literature-review` | Literature search, screening, and synthesis | Reuse |
| `python-patterns` | Python typing, errors, resource management, and concurrency | Adapt |
| `python-testing` | Python tests, fixtures, mocks, and async testing | Adapt |
| `tdd-workflow` | An observed RED-to-GREEN development cycle | Adapt |
| `verification-loop` | Applicable checks and explicit reporting of gaps | Adapt |
| `security-review` | Trust boundaries and vulnerability review | Adapt |
| `search-first` | Finding existing solutions before building | Adapt |
| `documentation-lookup` | Verifying behavior against version-specific documentation | Adapt |
| `deep-research` | Investigating a question using primary sources | Adapt |
| `product-prd` | Product problems, goals, MVP, and scope | Adapt |
| `product-capability` | Actors, states, constraints, and invariants | Adapt |
| `requirements-spec` | Functional and nonfunctional requirements | Build |
| `user-stories-ac` | User stories and observable acceptance criteria | Adapt |
| `bpmn-modeling` | As-is/to-be processes and BPMN XML | Build |
| `sqlite-data-model` | SQLite data models, keys, and migrations | Build |
| `system-design` | System architecture, context, and interactions | Build |
| `requirements-traceability` | Links between requirements and verification evidence | Build |
| `writing-for-agents` | Agent instructions, conditional references, completion criteria | Adapt |
| `grilling` | Stress-test plans through dependent questions | Adapt |
| `diagnosing-bugs` | Reproduce failures and test explanations before fixing | Adapt |
| `retro` | Evidence-backed session retrospective (explicit invocation) | Adapt |
| `handoff` | Transfer task state with verified status and redaction (explicit invocation) | Adapt |
| `domain-modeling` | Domain terminology, contexts, relationships, and invariants | Adapt |

## Dependencies and limitations

No new MCP servers, hooks, additional agents, or model settings are included.
The original Reuse instructions are preserved in full and may mention tools
unavailable in your session. Check available capabilities and report gaps explicitly.
Project tools such as pytest, Ruff, and mypy are not installed automatically.
The only executable Skill helper is
`.agents/skills/requirements-traceability/scripts/check_traceability.py`.
It uses the Python standard library to validate links and evidence records;
it does not establish whether recorded test results or business requirements are true.

Previous pilots covered synthetic data and selected scenarios.
Packaging checks do not establish reliable automatic selection of every Skill,
compatibility with every project, BPMN XSD compliance or execution, or full
end-to-end behavior. Full v1.0 acceptance is still pending; token savings have
not been measured. Historical reports and private pilot code are not included
in this distribution.

## Bundle checks

Requires Python 3.9+. No network requests or dependency installation are needed:

```sh
python3 -B -m unittest discover -s tests -v
```

These checks cover file hashes and inventory, preservation of the four upstream
originals, path portability, and traceability checker regressions. They do not
provide behavioral acceptance testing of all Skills. YAML frontmatter can also
be validated with Ruby Psych; Ruby is required only for this additional check:

```sh
ruby tests/check_frontmatter.rb
```

`manifest.json` records relative paths and SHA-256 hashes for all distribution
files except the manifest itself. After intentional file changes, update the
manifest as part of review. Tests do not rewrite the expected hashes automatically.

## Publication and maintenance

Publish only the contents of this folder, not its parent workspace.
Repository: [Sementrudovik/codex-engineering-toolkit](https://github.com/Sementrudovik/codex-engineering-toolkit).
The initial release candidate is tagged
[`v1.0.0-rc.1`](https://github.com/Sementrudovik/codex-engineering-toolkit/tree/v1.0.0-rc.1).
This tag marks a release candidate, not a completed v1.0 acceptance review.
Before a release, review the diff, licenses, file hashes, absence of private data,
and applicable tests.
Sources and attribution are documented in [NOTICE.md](NOTICE.md);
license terms are in [LICENSE](LICENSE).
Codex documentation: https://learn.chatgpt.com/docs/build-skills
