"""Unit tests use synthetic traces; they are NOT actual skill executions."""
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from evaluate_behavior import assess, load_suite, prepare


class EvaluatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.suite = {"minimum_repetitions": 3, "cases": [{
            "id": "sample", "turns": ["test request"],
            "expected": {"route": "direct", "operation": "audit", "max_skill_questions": 0,
                         "checks": ["meaning_preserved"]},
        }]}
        self.trace = "test request\nassistant: inspected; original unchanged.\n"
        (self.root / "trace.txt").write_text(self.trace)
        def annotation(value):
            return {"value": value, "reason": "Synthetic unit-test observation only",
                    "evidence": [{"start": 0, "excerpt": "test request"}]}
        self.record = {
            "case_id": "sample", "repetition": 1, "skill_digest": "test-digest",
            "model": "unit-test", "harness": "unit-test", "run_id": "synthetic-1",
            "reviewer": "unit-test", "executed_at": "synthetic timestamp",
            "trace_path": "trace.txt", "trace_sha256": hashlib.sha256(self.trace.encode()).hexdigest(),
            "observed": {"route": annotation("direct"), "operation": annotation("audit"),
                         "skill_questions": annotation(0), "meaning_preserved": annotation(True)},
        }

    def assess(self, records):
        path = self.root / "runs.jsonl"
        path.write_text("\n".join(json.dumps(r) for r in records))
        return assess(path, self.suite, "test-digest")

    def repeated(self):
        records = []
        for index in range(1, 4):
            record = copy.deepcopy(self.record)
            record.update(repetition=index, run_id=f"synthetic-{index}")
            records.append(record)
        return records

    def test_incomplete_and_empty_cannot_pass(self):
        self.assertEqual(self.assess([])["status"], "incomplete")
        self.assertEqual(self.assess([self.record])["missing_repetitions"], {"sample": 2})

    def test_repeated_matching_annotations_pass_only_assessor(self):
        self.assertEqual(self.assess(self.repeated())["status"], "passed")

    def test_question_or_meaning_failure_and_decision_variation(self):
        records = self.repeated()
        records[1]["observed"]["skill_questions"]["value"] = 1
        records[2]["observed"]["meaning_preserved"]["value"] = False
        report = self.assess(records)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(len(report["failures"]), 2)
        self.assertEqual(report["decision_variation"], ["sample"])

    def test_bad_digest_evidence_and_duplicate_run_rejected(self):
        corruptions = [
            lambda r: r.update(skill_digest="old-revision"),
            lambda r: r.update(trace_sha256="invalid"),
            lambda r: r["observed"]["route"]["evidence"][0].update(start=4),
            lambda r: r["observed"]["route"].update(evidence=[]),
            lambda r: r["observed"]["meaning_preserved"].update(value="true"),
        ]
        for corrupt in corruptions:
            with self.subTest(corruption=corrupt):
                record = copy.deepcopy(self.record)
                corrupt(record)
                with self.assertRaises(ValueError):
                    self.assess([record])
        with self.assertRaises(ValueError):
            self.assess([self.record, self.record])
        records = self.repeated()
        records[1]["run_id"] = records[0]["run_id"]
        with self.assertRaises(ValueError):
            self.assess(records)

    def test_blind_preparation_omits_answers(self):
        output = self.root / "inputs"
        prepare(output)
        for path in output.glob("*.json"):
            self.assertNotIn("expected", json.loads(path.read_text()))
        suite = load_suite()
        self.assertEqual(len(list(output.glob("*.json"))), len(suite["cases"]) + 1)
        with self.assertRaises(FileExistsError):
            prepare(output)


if __name__ == "__main__":
    unittest.main()
