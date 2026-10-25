# ER/SQLite checklist
- List entities, ownership, cardinality and business key vs surrogate key.
- Define PK/FK, NOT NULL, UNIQUE, CHECK and ON DELETE/UPDATE.
- Show tenant-scoped composite references and application authorization boundaries.
- Justify indexes by query shape; avoid duplicating a PK/UNIQUE index without reason.
- Enable and verify PRAGMA foreign_keys for every connection outside a transaction.
- Pin required SQLite features to a checked minimum version.
- Separate row/database constraints from aggregate/service invariants.
- Version migration, test fresh DB and data-preserving upgrade.
- Describe backup/restore and destructive rollback limits.
- Test invalid rows, relationship integrity, rollback and consistency checks on disposable data.

