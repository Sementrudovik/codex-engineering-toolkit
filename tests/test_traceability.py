from pathlib import Path
import importlib.util,json,tempfile,unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('trace_check',ROOT/'.agents/skills/requirements-traceability/scripts/check_traceability.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class TraceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.file=self.root/'graph.json'
        self.graph={'artifacts':[{'id':'R','type':'requirement','requirement_kind':'FR'},{'id':'A','type':'acceptance'},{'id':'V','type':'verification'}],'links':[{'from':'A','to':'R','relation':'verifies'},{'from':'V','to':'A','relation':'verifies'}],'evidence':[{'verification_id':'V','result':'PASS','artifact':'results.json'}]}
        (self.root/'results.json').write_text(json.dumps({'checks':{'V':'PASS'}}))
    def run_graph(self):
        self.file.write_text(json.dumps(self.graph));return m.check(self.file)
    def test_valid_graph(self):
        r=self.run_graph();self.assertEqual(r['fr_with_planned_acceptance'],1);self.assertEqual(r['recorded_pass'],['V'])
    def test_broken_link(self):
        self.graph['links'][0]['to']='MISSING'
        with self.assertRaises(ValueError):self.run_graph()
    def test_duplicate_id(self):
        self.graph['artifacts'].append({'id':'R','type':'source'})
        with self.assertRaises(ValueError):self.run_graph()
    def test_false_pass(self):
        (self.root/'results.json').write_text(json.dumps({'checks':{'V':'NOT_RUN'}}))
        with self.assertRaises(ValueError):self.run_graph()
    def test_out_of_root_evidence(self):
        self.graph['evidence'][0]['artifact']='../outside.json'
        with self.assertRaises(ValueError):self.run_graph()
    def test_missing_acceptance_reported(self):
        self.graph['links']=[]
        r=self.run_graph();self.assertEqual(r['uncovered_fr'],['R'])
    def test_type_mismatch(self):
        self.graph['links'][0]['relation']='implements'
        with self.assertRaises(ValueError):self.run_graph()

if __name__=='__main__':unittest.main()
