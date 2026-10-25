# Provenance and adaptation

Source: https://github.com/affaan-m/ECC/blob/90606c8315ee09cafc303515c5f33024db6b9882/skills/security-review/SKILL.md
Commit: `90606c8315ee09cafc303515c5f33024db6b9882`.
Upstream Git blob SHA: `3f26b0df65661425de4e5c40c295e04edcad7a83`.

Status: Adapt; installed project-local on 2026-10-25.
The main SKILL.md is a complete standalone Toolkit workflow, not a routing wrapper
or byte-identical upstream copy. No upstream file needs to be loaded to execute it.
The unchanged original is retained at upstream/ecc-source.md for audit and attribution,
not as extra governing instructions. Review the generated UPSTREAM.diff for the rewrite.

Changes: Diagnostic vs mutation boundary; Python inputs/authorization/process concerns; no automatic dependency upgrades; redact evidence; scope and exploit confidence.

No executable scripts, lifecycle hooks, MCP config, agent roles or model overrides
are bundled in this skill. Mentioned project tools remain optional/existing tools.
The upstream root MIT license is included as LICENSE. Upstream origin/attribution
metadata remains intact in the archived original. Behavioral validation is limited;
consult ../../../README.md for this distribution's validation limits.

