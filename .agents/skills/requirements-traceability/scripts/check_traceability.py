#!/usr/bin/env python3
"""Validate local traceability links/evidence records, not business semantics."""
import json
from pathlib import Path
import sys

TYPES = {'source', 'requirement', 'story', 'acceptance', 'operation', 'process', 'entity', 'verification'}
RELATIONS = {'derived_from', 'implements', 'verifies', 'realizes', 'depends_on'}


def local_file(base, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError('Expected a relative local file path')
    target = (base / relative.split('#', 1)[0]).resolve()
    if base not in target.parents or not target.is_file():
        raise ValueError('Missing or out-of-root file: ' + relative)
    return target


def check(path):
    path = Path(path).resolve()
    base = path.parent
    graph = json.loads(path.read_text(encoding='utf-8'))
    nodes = {}
    for node in graph['artifacts']:
        key = node['id']
        if not isinstance(key, str) or not key or key in nodes:
            raise ValueError('Empty or duplicate artifact ID')
        if node['type'] not in TYPES:
            raise ValueError('Unknown artifact type: ' + str(node['type']))
        if node.get('path'):
            local_file(base, node['path'])
        nodes[key] = node
    for edge in graph['links']:
        if edge['from'] not in nodes or edge['to'] not in nodes:
            raise ValueError('Broken artifact reference')
        relation = edge['relation']
        if relation not in RELATIONS:
            raise ValueError('Unknown relation')
        left, right = nodes[edge['from']]['type'], nodes[edge['to']]['type']
        allowed = (relation == 'depends_on'
                   or relation == 'derived_from' and left == 'requirement' and right == 'source'
                   or relation == 'implements' and left == 'story' and right == 'requirement'
                   or relation == 'verifies' and ((left == 'acceptance' and right == 'requirement')
                                                or (left == 'verification' and right in {'acceptance', 'requirement'}))
                   or relation == 'realizes' and left in {'operation', 'process', 'entity'} and right == 'requirement')
        if not allowed:
            raise ValueError('Relation incompatible with artifact types')
    results = {}
    for entry in graph.get('evidence', []):
        key, result = entry['verification_id'], entry['result']
        if key not in nodes or nodes[key]['type'] != 'verification' or key in results:
            raise ValueError('Unknown or duplicate verification evidence')
        if result not in {'PASS', 'FAIL', 'NOT_RUN'}:
            raise ValueError('Unsupported result')
        if result != 'NOT_RUN':
            evidence = json.loads(local_file(base, entry['artifact']).read_text(encoding='utf-8'))
            if evidence.get('checks', {}).get(key) != result:
                raise ValueError('Result not supported by recorded evidence: ' + key)
        results[key] = result
    frs = {key for key, node in nodes.items() if node['type'] == 'requirement' and node.get('requirement_kind') == 'FR'}
    planned = {edge['to'] for edge in graph['links'] if edge['relation'] == 'verifies'
               and nodes[edge['from']]['type'] == 'acceptance' and edge['to'] in frs}
    uncovered = sorted(frs - planned)
    verifications = {key for key, node in nodes.items() if node['type'] == 'verification'}
    return {'graph_valid': True, 'artifact_count': len(nodes), 'link_count': len(graph['links']),
            'fr_total': len(frs), 'fr_with_planned_acceptance': len(planned), 'uncovered_fr': uncovered,
            'recorded_pass': sorted(key for key, value in results.items() if value == 'PASS'),
            'recorded_fail': sorted(key for key, value in results.items() if value == 'FAIL'),
            'not_run': sorted(verifications - {key for key, value in results.items() if value in {'PASS', 'FAIL'}}),
            'semantic_validation': 'NOT PERFORMED by this checker'}


def main():
    if len(sys.argv) != 2:
        print('Usage: check_traceability.py graph.json', file=sys.stderr)
        return 2
    try:
        result = check(sys.argv[1])
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result['uncovered_fr'] else 0
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(json.dumps({'graph_valid': False, 'error': str(exc)}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
