# Skill packaging for this Toolkit

A Skill has name/description frontmatter and a standalone SKILL.md. Bundle only
resources actually used by its procedure. Link conditional references with the
condition for reading them. Avoid nested archived SKILL.md entrypoints.

Keep normal automatic selection unless the user requests explicit-only invocation
or an existing explicit-only policy is being preserved. Codex metadata for that is
agents/openai.yaml with policy.allow_implicit_invocation: false. Other hosts may
use different fields; do not copy Claude-specific frontmatter as Codex settings.
The policy does not itself grant or revoke authorization for filesystem/external actions.

Verify names, resource paths, declared dependencies, licensing and real task behavior.
A smaller file count or a passed YAML parser does not prove better task performance.
