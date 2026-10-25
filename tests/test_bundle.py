from pathlib import Path
import hashlib
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))

class BundleTests(unittest.TestCase):
    def test_file_integrity_and_inventory(self):
        actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
                  if p.is_file() and '.git' not in p.relative_to(ROOT).parts
                  and '__pycache__' not in p.parts and p.name != '.DS_Store'
                  and p != ROOT / 'manifest.json'}
        self.assertEqual(actual, set(MANIFEST['files_sha256']))
        for relative, digest in MANIFEST['files_sha256'].items():
            p = ROOT / relative
            self.assertFalse(Path(relative).is_absolute())
            self.assertIn(ROOT, p.resolve().parents)
            self.assertFalse(p.is_symlink())
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(), digest, relative)

    def test_twenty_unique_skills_and_resources(self):
        skills = MANIFEST['skills']
        self.assertEqual(len(skills), 20)
        self.assertEqual(len({s['name'] for s in skills}), 20)
        self.assertEqual(sorted(s['status'] for s in skills).count('Reuse'), 4)
        self.assertEqual(sorted(s['status'] for s in skills).count('Adapt'), 11)
        self.assertEqual(sorted(s['status'] for s in skills).count('Build'), 5)
        for skill in skills:
            folder = ROOT / skill['path']
            for name in ('SKILL.md', 'LICENSE', 'PROVENANCE.md'):
                self.assertTrue((folder / name).is_file())
        self.assertEqual(len(list((ROOT / '.agents/skills').rglob('SKILL.md'))), 20)

    def test_reuse_upstream_git_blobs(self):
        for skill in MANIFEST['skills']:
            if skill['status'] == 'Reuse':
                raw = (ROOT / skill['path'] / 'SKILL.md').read_bytes()
                blob = b'blob ' + str(len(raw)).encode() + b'\0' + raw
                self.assertEqual(hashlib.sha1(blob).hexdigest(), skill['upstream_git_blob_sha1'])

    def test_no_local_paths_or_private_project_names(self):
        forbidden = ('/Users/', '/private/var/', 'ag_fin_report', 'arthur-consalting-case')
        for relative in MANIFEST['files_sha256']:
            text = (ROOT / relative).read_text(encoding='utf-8')
            # The checker itself contains these search patterns, not private data.
            if relative == 'tests/test_bundle.py':
                continue
            for item in forbidden:
                self.assertNotIn(item, text, relative)

    def test_local_markdown_resources(self):
        for skill in MANIFEST['skills']:
            entry = ROOT / skill['path'] / 'SKILL.md'
            text = re.sub(r'```.*?```', '', entry.read_text(encoding='utf-8'), flags=re.S)
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                target = target.split('#', 1)[0]
                if not target or re.match(r'[a-z]+:', target) or target.startswith('/'):
                    continue
                self.assertTrue((entry.parent / target).exists(), f'{entry}: {target}')

if __name__ == '__main__':
    unittest.main()
