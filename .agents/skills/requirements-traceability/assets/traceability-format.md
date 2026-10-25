# Traceability JSON format
Root object:
- artifacts: list of {id, type, status?, path?, requirement_kind?}
- links: list of {from, to, relation}
- evidence: list of {verification_id, result, artifact?}
Artifact types: source, requirement, story, acceptance, operation, process, entity, verification.
Relation: derived_from, implements, verifies, realizes, depends_on.
Requirement kind: FR or NFR where coverage is reported.

Directions:
- requirement -> source: derived_from
- story -> requirement: implements
- acceptance -> requirement: verifies
- verification -> acceptance/requirement: verifies
- operation/process/entity -> requirement: realizes

PASS/FAIL evidence requires a local JSON file inside the graph's directory tree:
{"checks": {"verification-ID": "PASS"}}
The checker verifies file identity/path confinement and recorded status, not the truth
of an arbitrary author's claims. NOT_RUN needs no fabricated evidence file.
Paths are relative to the graph file. No remote fetch, test execution or mutation.
Planned FR coverage counts FRs with at least one acceptance link, not completed tests.

