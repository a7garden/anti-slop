#!/usr/bin/env python3
"""Offline structural and regression-fixture checks for this skill package."""

from __future__ import annotations

import json
import re
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from urllib.parse import unquote
from evaluate_behavior import load_suite


ROOT = Path(__file__).resolve().parents[1]  # the skill folder; the validator is portable with it
RULES = ROOT / "references/rules.md"
SKILL = ROOT / "SKILL.md"
CASES = ROOT / "tests/regression_cases.json"
EXECUTION_CASES = ROOT / "tests/execution_cases.json"
EXAMPLES = ROOT / "references/before-after.md"
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def validate_execution_cases() -> int:
    data = json.loads(EXECUTION_CASES.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if data.get("schema_version") != 1 or not cases:
        fail("execution fixtures need schema_version 1 and nonempty cases")
    ids = set()
    routes = set()
    operations = set()
    preflight_policies = set()
    required = {
        "route", "operation", "outcome", "max_skill_questions", "interview",
        "may_edit_existing_target", "output",
    }
    for case in cases:
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id or case_id in ids:
            fail("execution fixture IDs must be nonempty and unique")
        ids.add(case_id)
        if not isinstance(case.get("user_request"), str) or not case["user_request"]:
            fail(f"{case_id} needs a user request")
        if not isinstance(case.get("context"), dict) or not case.get("why"):
            fail(f"{case_id} needs context and a rationale")
        setup = case.get("expected_setup")
        if setup is not None:
            if not isinstance(setup, dict) or set(setup) != {"phase", "actionable_choices", "reuse_known_inputs"}:
                fail(f"{case_id} has incomplete guided setup expectations")
            if setup["phase"] not in {"choose-work", "choose-operation", "choose-target", "choose-target-operation", "ready"}:
                fail(f"{case_id} has unknown setup phase")
            if any(type(setup[key]) is not bool for key in ("actionable_choices", "reuse_known_inputs")):
                fail(f"{case_id} setup expectations need booleans")
            if not setup["reuse_known_inputs"]:
                fail(f"{case_id} cannot discard known setup inputs")
        preflight = case.get("expected_preflight")
        orientation = case.get("expected_orientation")
        if orientation is not None:
            if not isinstance(orientation, dict) or set(orientation) != {"policy", "before_target_question", "grounded_candidates"}:
                fail(f"{case_id} has incomplete project orientation expectations")
            if orientation["policy"] not in {"read-project", "reuse-overview", "target-context-only", "unavailable-fallback"}:
                fail(f"{case_id} has unknown project orientation policy")
            if any(type(orientation[key]) is not bool for key in ("before_target_question", "grounded_candidates")):
                fail(f"{case_id} orientation expectations need booleans")
            if orientation["before_target_question"] != (orientation["policy"] == "read-project"):
                fail(f"{case_id} project discovery order disagrees with its policy")
            if orientation["grounded_candidates"] != (orientation["policy"] in {"read-project", "reuse-overview"}):
                fail(f"{case_id} unsupported context cannot supply grounded candidates")
        if preflight is not None:
            if not isinstance(preflight, dict) or set(preflight) != {
                "domain", "comparison", "before_app_findings", "report_research_gap",
            }:
                fail(f"{case_id} has incomplete domain/UX preparation expectations")
            if preflight["domain"] not in {"establish", "reuse", "bounded", "not-applicable"}:
                fail(f"{case_id} has unknown domain preparation")
            policy = preflight["comparison"]
            if policy not in {"search-and-read", "reuse-inspected", "bounded", "unavailable", "user-skipped", "not-applicable"}:
                fail(f"{case_id} has unknown comparison policy")
            if any(type(preflight[key]) is not bool for key in ("before_app_findings", "report_research_gap")):
                fail(f"{case_id} needs boolean preparation order/gap expectations")
            if policy in {"search-and-read", "reuse-inspected", "unavailable", "user-skipped"} and not preflight["before_app_findings"]:
                fail(f"{case_id} app domain preparation must precede findings")
            if policy in {"unavailable", "user-skipped"} and not preflight["report_research_gap"]:
                fail(f"{case_id} cannot hide unavailable or omitted comparison research")
            if policy == "reuse-inspected" and preflight["domain"] != "reuse":
                fail(f"{case_id} source reuse must retain domain context")
            if preflight["domain"] == "not-applicable" and policy != "not-applicable":
                fail(f"{case_id} non-app work cannot introduce comparator research")
            preflight_policies.add(policy)
        expected = case.get("expected")
        if not isinstance(expected, dict) or set(expected) != required:
            fail(f"{case_id} has incomplete execution expectations")
        route = expected["route"]
        operation = expected["operation"]
        outcome = expected["outcome"]
        questions = expected["max_skill_questions"]
        interview = expected["interview"]
        edits = expected["may_edit_existing_target"]
        output = expected["output"]
        if route not in {"direct", "embedded", "maintenance"}:
            fail(f"{case_id} has unknown invocation route")
        if operation not in {"audit", "browser-audit", "revise", "draft", None}:
            fail(f"{case_id} has unknown operation")
        if outcome not in {"deliver", "clarify", "interview", "await-input", "maintain"}:
            fail(f"{case_id} has unknown outcome")
        if type(questions) is not int or not 0 <= questions <= 3:
            fail(f"{case_id} has invalid question bound")
        if type(interview) is not bool or type(edits) is not bool:
            fail(f"{case_id} needs boolean interview/edit expectations")
        if route == "embedded" and (questions or interview):
            fail(f"{case_id} embedded use cannot introduce skill questions")
        if operation in {"audit", "browser-audit"} and edits:
            fail(f"{case_id} audit cannot edit the existing target")
        if outcome in {"clarify", "interview", "await-input"} and edits:
            fail(f"{case_id} cannot edit while awaiting essential or interview input")
        if interview != (outcome == "interview"):
            fail(f"{case_id} interview expectation disagrees with outcome")
        if outcome == "interview" and (route != "direct" or not questions):
            fail(f"{case_id} interview requires a direct guided or requested question round")
        if outcome == "clarify" and (route != "direct" or not questions):
            fail(f"{case_id} skill clarification requires a direct essential blocker")
        if outcome == "await-input" and (route != "direct" or questions):
            fail(f"{case_id} exhausted setup must wait without more skill questions")
        if outcome == "deliver" and questions:
            fail(f"{case_id} delivery cannot add an unsolicited question round")
        if route == "maintenance":
            if operation is not None or outcome != "maintain" or output != "maintenance_result":
                fail(f"{case_id} maintenance cannot start a runtime operation")
        elif outcome == "maintain":
            fail(f"{case_id} runtime route cannot claim maintenance")
        allowed_output = {
            "deliver": {"audit_report", "browser_audit_report", "revision_result", "artifact_only", "parent_contract", "acknowledgment"},
            "clarify": {"clarification"},
            "interview": {"interview_questions"},
            "await-input": {"input_needed"},
            "maintain": {"maintenance_result"},
        }
        if output not in allowed_output[outcome]:
            fail(f"{case_id} output disagrees with outcome")
        if outcome == "deliver":
            if route == "direct":
                direct_output = {
                    "audit": {"audit_report", "acknowledgment"},
                    "browser-audit": {"browser_audit_report", "acknowledgment"},
                    "revise": {"revision_result", "artifact_only", "acknowledgment"},
                    "draft": {"artifact_only", "acknowledgment"},
                }
                if output not in direct_output.get(operation, set()):
                    fail(f"{case_id} direct output disagrees with operation")
            elif route == "embedded" and output not in {"parent_contract", "artifact_only", "acknowledgment"}:
                fail(f"{case_id} embedded use cannot add a separate skill report")
        if setup is not None:
            if route != "direct":
                fail(f"{case_id} guided setup is direct-only")
            if setup["phase"] == "ready":
                if outcome != "deliver" or questions or setup["actionable_choices"]:
                    fail(f"{case_id} resolved work must proceed without setup questions")
            elif outcome not in {"interview", "clarify"} or not questions or not setup["actionable_choices"]:
                fail(f"{case_id} unresolved setup needs actionable choices")
            if setup["phase"] == "choose-work" and operation is not None:
                fail(f"{case_id} cannot preselect an operation for unknown work")
        routes.add(route)
        if operation is not None:
            operations.add(operation)
    if not {"direct", "embedded", "maintenance"} <= routes or operations != {"audit", "browser-audit", "revise", "draft"}:
        fail("execution fixtures must cover invocation routes and all four operations")
    if preflight_policies != {"search-and-read", "reuse-inspected", "bounded", "unavailable", "user-skipped", "not-applicable"}:
        fail("execution fixtures must cover domain research, reuse, scope, and research gaps")
    return len(cases)


def main() -> None:
    rules_text = RULES.read_text(encoding="utf-8")
    skill_text = SKILL.read_text(encoding="utf-8")
    examples_text = EXAMPLES.read_text(encoding="utf-8")
    data = json.loads(CASES.read_text(encoding="utf-8"))
    if data.get("schema_version") != 2:
        fail("regression fixtures need schema_version 2 (rule applicability and issue decisions)")
    cases = data.get("cases", [])
    execution_count = validate_execution_cases()
    behavior_suite = load_suite()

    relative_links = 0
    missing_links = []
    for markdown in ROOT.rglob("*.md"):
        for raw_target in MARKDOWN_LINK.findall(markdown.read_text(encoding="utf-8")):
            target = raw_target.strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "data:", "#")):
                continue
            target_path = unquote(target.split("#", 1)[0])
            if not target_path:
                continue
            relative_links += 1
            resolved = (markdown.parent / target_path).resolve()
            if not resolved.exists():
                missing_links.append(f"{markdown.relative_to(ROOT)} -> {target}")
    if missing_links:
        fail("broken relative Markdown links: " + "; ".join(missing_links))

    expected_rule_ids = {
        *(f"W{number:02d}" for number in range(1, 30)),
        *(f"D{number:02d}" for number in range(1, 26)),
    }
    headings = set(re.findall(r"^### ([WD]\d{2}) —", rules_text, flags=re.MULTILINE))
    if headings != expected_rule_ids:
        fail(f"canonical rule IDs differ; missing={sorted(expected_rule_ids - headings)}, extra={sorted(headings - expected_rule_ids)}")

    required_rule_fields = (
        "- **Scope:**", "- **Basis:**", "- **Detect:**", "- **Repair:**",
        "- **Exceptions:**", "- **Class/severity:**", "- **Automatic:**",
    )
    rule_blocks = re.split(r"(?=^### [WD]\d{2} —)", rules_text, flags=re.MULTILINE)[1:]
    if len(rule_blocks) != len(headings):
        fail("duplicate canonical rule headings")
    source_ids = set(re.findall(r"^- \*\*(S\d{2}) —", rules_text, flags=re.MULTILINE))
    for block in rule_blocks:
        rule_id = re.match(r"### ([WD]\d{2})", block).group(1)
        body = block
        missing = [field for field in required_rule_fields if field not in body]
        if missing:
            fail(f"{rule_id} lacks rule metadata: {', '.join(missing)}")
        basis = re.search(r"^- \*\*Basis:\*\* (.+)$", body, flags=re.MULTILINE).group(1)
        unknown_sources = set(re.findall(r"\bS\d{2}\b", basis)) - source_ids
        if unknown_sources:
            fail(f"{rule_id} cites unregistered sources: {sorted(unknown_sources)}")

    ids = [case.get("id") for case in cases]
    if not ids or len(ids) != len(set(ids)):
        fail("fixture IDs must be present and unique")

    counts = {"writing": 0, "design": 0}
    clean = {"writing": 0, "design": 0}
    guarded = {"writing": 0, "design": 0}
    covered_rules = set()
    for case in cases:
        profile = case.get("profile")
        if profile not in counts:
            fail(f"{case.get('id')} has unknown profile {profile!r}")
        counts[profile] += 1
        for key in ("input", "why", "applicable_rules", "must_not_flag", "preserve"):
            if key not in case:
                fail(f"{case.get('id')} lacks {key}")
        findings = set(case["applicable_rules"])
        covered_rules.update(findings)
        negatives = set(case["must_not_flag"])
        if findings & negatives:
            fail(f"{case['id']} expects and forbids the same finding")
        if not findings and not case.get("expected_issues"):
            clean[profile] += 1
        if negatives:
            guarded[profile] += 1
        prefix = "W" if profile == "writing" else "D"
        for rule_id in findings | negatives:
            if rule_id not in expected_rule_ids or not rule_id.startswith(prefix):
                fail(f"{case['id']} refers to invalid {profile} rule {rule_id}")
        for literal in case["preserve"]:
            if literal not in case["input"]:
                fail(f"{case['id']} preservation literal is absent from its input: {literal!r}")
        issues = case.get("expected_issues", [])
        if not isinstance(issues, list):
            fail(f"{case['id']} issue decisions must be a list")
        for issue in issues:
            if set(issue) != {"primary", "related", "class", "severity"}:
                fail(f"{case['id']} issue decisions need primary/related rule, class, and severity")
            primary = issue["primary"]
            if primary not in findings and not re.fullmatch(r"(?:CT|UX|VD)-\d{2}", primary):
                fail(f"{case['id']} primary rule lacks applicability or a valid report-local category")
            related = issue["related"]
            if not isinstance(related, list) or len(related) != len(set(related)):
                fail(f"{case['id']} related rules must be unique")
            if primary in related or not set(related) <= findings:
                fail(f"{case['id']} related rules cannot duplicate primary or lack applicability")
            if issue["class"] not in {"error", "warning", "preference"} or issue["severity"] not in {"low", "medium", "high"}:
                fail(f"{case['id']} has invalid issue class/severity")

    for profile in counts:
        if counts[profile] < 20:
            fail(f"need at least 20 {profile} fixtures; found {counts[profile]}")
        if clean[profile] < 8 or guarded[profile] < 8:
            fail(f"{profile} needs at least 8 clean cases and 8 explicit non-finding guards")
    if expected_rule_ids - covered_rules:
        fail(f"rules lack positive fixtures: {sorted(expected_rule_ids - covered_rules)}")

    frontmatter = skill_text.split("---", 2)[1] if skill_text.startswith("---") else ""
    skill_version = re.search(r'^  version:\s*["\']?([^\s"\']+)["\']?\s*$', frontmatter, flags=re.MULTILINE)
    if not skill_version:
        fail("SKILL.md frontmatter lacks metadata.version")
    package_json = ROOT.parent.parent.parent / "package.json"
    if package_json.exists():
        package = json.loads(package_json.read_text(encoding="utf-8"))
        if skill_version.group(1) != package.get("version"):
            fail(f"SKILL.md version {skill_version.group(1)} != package.json version {package.get('version')}")

    print(
        "PASS package integrity: "
        f"{len(headings)} canonical rules; {counts['writing']} writing and {counts['design']} design fixtures; "
        f"clean controls {clean['writing']}/{clean['design']}; guarded cases {guarded['writing']}/{guarded['design']}; "
        f"{relative_links} relative Markdown links resolve; "
        f"{examples_text.count('## ')} examples."
    )
    print(f"PASS execution fixture integrity: {execution_count} invocation/continuation scenarios; routes and operations covered.")
    print(f"PASS behavior fixture integrity: {len(behavior_suite['cases'])} scenarios; {behavior_suite['minimum_repetitions']} repetitions required. No agent executions performed.")
    print("NOTE: these offline checks validate package structure and test coverage, not model judgment or AI authorship.")


if __name__ == "__main__":
    main()
