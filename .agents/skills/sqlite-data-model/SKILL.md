---
name: sqlite-data-model
description: "Design ER models and SQLite tables, keys, indexes and migrations; verify constraints and lifecycle behavior on disposable databases."
license: MIT
metadata:
  origin: Toolkit-original
---

# ER and SQLite Data Model

Identify entities, ownership, identifiers, cardinality, lifecycle and query needs
from requirements/contracts. Distinguish conceptual entities from physical tables.
Do not expose storage-only fields in a public API merely because they exist in SQL.

## Design
Specify PK/FK, nullability, uniqueness, CHECK constraints, deletion behavior and
indexes justified by expected queries. Preserve opaque IDs as text.
For tenant-owned data, use composite keys/FKs or otherwise prove that child ownership
cannot cross tenant boundaries. Explicit NOT NULL avoids SQLite key/null surprises.
Do not assume SQLite has native row-level authorization; application queries must
scope identities and permissions correctly.
Document service-level invariants that row constraints cannot enforce, such as
route continuity or a minimum number of child rows at transaction completion.

## SQLite specifics
Enable PRAGMA foreign_keys=ON and verify it for each connection before beginning
transactions; do not assume a server-global setting or that changing it in a
transaction takes effect. Check SQLite version before relying on newer DDL features.
Consider actual storage/type affinity; type names alone are not strict validation.
Keep SQL values parameterized. Select monetary representation and time conventions
from explicit domain requirements.

## Migrations
Version migrations and define atomic execution, preconditions, verification and
rollback/restore expectations. Test a fresh database and upgrade of existing data.
A destructive down migration is not a safe production rollback strategy.
Do not disable FK checks, rebuild user tables or run migrations against real data
without the applicable authorization and backup/restore plan.

## Verify and deliver
Use a disposable DB to test positive and negative constraints, relevant indexes,
transaction rollback and foreign_key_check/integrity_check.
Report which invariants remain application responsibilities; schema success is
not proof of concurrency correctness or complete authorization.
Use [the model checklist](assets/model-checklist.md). Include ER, schema, migration
plan and actual test evidence. No external DB server or MCP is required.

