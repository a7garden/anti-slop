#!/usr/bin/env python3
"""Prepare blind requests or assess reviewer-annotated, actual execution transcripts.

This script never invokes an agent and never infers model quality from fixture shape.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUITE = Path(__file__).with_name("behavior_cases.json")


def skill_digest(root: Path = ROOT) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if path.is_file() and (path.name == "SKILL.md" or path.relative_to(root).parts[0] in {"references", "agents"}):
            digest.update(path.relative_to(root).as_posix().encode() + b"\0" + path.read_bytes() + b"\0")
    return digest.hexdigest()


def load_suite(path: Path = SUITE) -> dict:
    suite = json.loads(path.read_text())
    if suite.get("schema_version") != 1 or suite.get("minimum_repetitions", 0) < 3:
        raise ValueError("Need schema_version 1 and at least three repetitions")
    ids = set()
    for case in suite["cases"]:
        if not case.get("id") or case["id"] in ids:
            raise ValueError("Case IDs must be unique")
        ids.add(case["id"])
        if not case.get("context") or not case.get("turns") or not all(isinstance(t, str) and t for t in case["turns"]):
            raise ValueError("Each case needs context and nonempty user turns")
        exp = case["expected"]
        if exp["route"] not in {"direct", "embedded"} or exp["operation"] not in {"audit", "browser-audit", "revise", "draft"}:
            raise ValueError("Unknown route/operation")
        if type(exp["max_skill_questions"]) is not int or exp["max_skill_questions"] < 0:
            raise ValueError("Invalid question bound")
        if not exp["checks"] or len(exp["checks"]) != len(set(exp["checks"])):
            raise ValueError("Need unique semantic checks")
    return suite


def prepare(output: Path) -> None:
    suite = load_suite()
    output.mkdir(parents=True, exist_ok=False)
    # Deliberately omit expectations and rationale from evaluated-agent inputs.
    for case in suite["cases"]:
        request = {key: case[key] for key in ("id", "context", "turns")}
        (output / f"{case['id']}.json").write_text(json.dumps(request, ensure_ascii=False, indent=2) + "\n")
    (output / "run-manifest.json").write_text(json.dumps({
        "skill_digest": skill_digest(), "minimum_repetitions": suite["minimum_repetitions"],
        "case_ids": [c["id"] for c in suite["cases"]],
    }, indent=2) + "\n")


def assess(records_path: Path, suite: dict | None = None, expected_digest: str | None = None) -> dict:
    suite = suite or load_suite()
    expected_digest = expected_digest or skill_digest()
    cases = {c["id"]: c for c in suite["cases"]}
    counts = {key: 0 for key in cases}
    decisions = {key: set() for key in cases}
    seen = set()
    failures = []
    provenance = set()
    for line in records_path.read_text().splitlines():
        if not line.strip():
            continue
        run = json.loads(line)
        case_id = run["case_id"]
        if case_id not in cases:
            raise ValueError(f"Unknown case: {case_id}")
        repetition = run["repetition"]
        if type(repetition) is not int or repetition < 1 or (case_id, repetition) in seen:
            raise ValueError("Repetition must be unique and positive per case")
        seen.add((case_id, repetition))
        if run["skill_digest"] != expected_digest:
            raise ValueError("Execution used a different skill revision")
        for key in ("model", "harness", "run_id", "reviewer", "executed_at"):
            if not isinstance(run.get(key), str) or not run[key].strip():
                raise ValueError(f"Need actual run provenance: {key}")
        if run["run_id"] in provenance:
            raise ValueError("Each repetition needs a distinct actual run")
        provenance.add(run["run_id"])
        trace_path = records_path.parent / run["trace_path"]
        raw = trace_path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != run["trace_sha256"]:
            raise ValueError("Trace content does not match its recorded digest")
        trace = raw.decode("utf-8")
        for turn in cases[case_id]["turns"]:
            if turn not in trace:
                raise ValueError(f"Trace lacks a supplied user turn: {case_id}")
        observed = run["observed"]
        exp = cases[case_id]["expected"]
        fields = ["route", "operation", "skill_questions", *exp["checks"]]
        if set(observed) != set(fields):
            raise ValueError("Review annotations must cover exactly the requested fields")
        values = {}
        for field in fields:
            annotation = observed[field]
            evidence = annotation.get("evidence", [])
            if not evidence or not annotation.get("reason"):
                raise ValueError("Every judgment needs trace evidence and a review reason")
            for item in evidence:
                excerpt, start = item.get("excerpt"), item.get("start")
                if not isinstance(excerpt, str) or not excerpt or type(start) is not int or start < 0 or trace[start:start + len(excerpt)] != excerpt:
                    raise ValueError("Evidence must reference exact text at a valid trace offset")
            values[field] = annotation["value"]
        if values["route"] not in {"direct", "embedded"} or values["operation"] not in {"audit", "browser-audit", "revise", "draft"}:
            raise ValueError("Invalid observed route/operation")
        if type(values["skill_questions"]) is not int or values["skill_questions"] < 0:
            raise ValueError("Question count must be a nonnegative integer")
        if any(type(values[key]) is not bool for key in exp["checks"]):
            raise ValueError("Semantic check observations must be booleans")
        broken = [key for key in ("route", "operation") if values[key] != exp[key]]
        if values["skill_questions"] > exp["max_skill_questions"]:
            broken.append("skill_questions")
        broken += [key for key in exp["checks"] if not values[key]]
        if broken:
            failures.append({"case_id": case_id, "repetition": repetition, "checks": broken})
        counts[case_id] += 1
        # Wording may vary. Compare decisions and semantic checks, not literal outputs.
        decisions[case_id].add(tuple(values[key] for key in fields))
    missing = {key: suite["minimum_repetitions"] - count for key, count in counts.items() if count < suite["minimum_repetitions"]}
    return {
        "status": "incomplete" if missing else ("failed" if failures else "passed"),
        "actual_runs": sum(counts.values()), "per_case_runs": counts, "missing_repetitions": missing,
        "failures": failures, "decision_variation": [key for key, variants in decisions.items() if len(variants) > 1],
        "skill_digest": expected_digest,
        "limit": "Reviewer-annotated observed runs; no automatic proof of semantic correctness or authorship. Trace hashes establish integrity, not origin.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prepare", type=Path, metavar="NEW_OUTPUT_DIR")
    group.add_argument("--assess", type=Path, metavar="RUNS_JSONL")
    parser.add_argument("--skill-snapshot", type=Path,
                        help="Assess an archived run against its preserved runtime snapshot instead of the current skill")
    args = parser.parse_args()
    if args.skill_snapshot and args.prepare:
        parser.error("--skill-snapshot applies to --assess, not --prepare")
    if args.prepare:
        prepare(args.prepare)
        print("Prepared blind requests. No model executions performed.")
    else:
        report = assess(args.assess, expected_digest=skill_digest(args.skill_snapshot) if args.skill_snapshot else None)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["status"] != "passed":
            raise SystemExit(1)


if __name__ == "__main__":
    main()
