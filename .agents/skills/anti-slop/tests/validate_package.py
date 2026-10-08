#!/usr/bin/env python3
"""Offline structural and regression-fixture checks for this skill package."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]  # the skill folder; the validator is portable with it
RULES = ROOT / "references/rules.md"
SKILL = ROOT / "SKILL.md"
CASES = ROOT / "tests/regression_cases.json"
EXAMPLES = ROOT / "references/before-after.md"
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    rules_text = RULES.read_text(encoding="utf-8")
    skill_text = SKILL.read_text(encoding="utf-8")
    examples_text = EXAMPLES.read_text(encoding="utf-8")
    data = json.loads(CASES.read_text(encoding="utf-8"))
    cases = data.get("cases", [])

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
        *(f"D{number:02d}" for number in range(1, 25)),
    }
    headings = set(re.findall(r"^### ([WD]\d{2}) —", rules_text, flags=re.MULTILINE))
    if headings != expected_rule_ids:
        fail(f"canonical rule IDs differ; missing={sorted(expected_rule_ids - headings)}, extra={sorted(headings - expected_rule_ids)}")

    required_rule_fields = (
        "- **Scope:**", "- **Basis:**", "- **Detect:**", "- **Repair:**",
        "- **Exceptions:**", "- **Class/severity:**", "- **Automatic:**",
    )
    rule_blocks = re.split(r"(?=^### [WD]\d{2} —)", rules_text, flags=re.MULTILINE)[1:]
    for block in rule_blocks:
        rule_id = re.match(r"### ([WD]\d{2})", block).group(1)
        body = block
        missing = [field for field in required_rule_fields if field not in body]
        if missing:
            fail(f"{rule_id} lacks rule metadata: {', '.join(missing)}")

    ids = [case.get("id") for case in cases]
    if not ids or len(ids) != len(set(ids)):
        fail("fixture IDs must be present and unique")

    counts = {"writing": 0, "design": 0}
    clean = {"writing": 0, "design": 0}
    guarded = {"writing": 0, "design": 0}
    for case in cases:
        profile = case.get("profile")
        if profile not in counts:
            fail(f"{case.get('id')} has unknown profile {profile!r}")
        counts[profile] += 1
        for key in ("input", "why", "expect_findings", "must_not_flag", "preserve"):
            if key not in case:
                fail(f"{case.get('id')} lacks {key}")
        findings = set(case["expect_findings"])
        negatives = set(case["must_not_flag"])
        if findings & negatives:
            fail(f"{case['id']} expects and forbids the same finding")
        if not findings:
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

    for profile in counts:
        if counts[profile] < 20:
            fail(f"need at least 20 {profile} fixtures; found {counts[profile]}")
        if clean[profile] < 8 or guarded[profile] < 8:
            fail(f"{profile} needs at least 8 clean cases and 8 explicit non-finding guards")

    safeguards = (
        "not an AI-origin detector", "Never invent a metric", "uncertainty",
        "meaningful sequence markers", "audit target", "revise target",
    )
    for safeguard in safeguards:
        if safeguard.lower() not in skill_text.lower():
            fail(f"SKILL.md is missing safeguard or command: {safeguard}")

    if examples_text.count("## ") < 8:
        fail("expected at least 8 before/after or no-change examples")
    for phrase in ("32%", "no latency measurement", "overflow-x: clip", "No finding."):
        if phrase not in examples_text:
            fail(f"examples are missing an over-editing/fact-safety demonstration: {phrase}")

    print(
        "PASS package integrity: "
        f"{len(headings)} canonical rules; {counts['writing']} writing and {counts['design']} design fixtures; "
        f"clean controls {clean['writing']}/{clean['design']}; guarded cases {guarded['writing']}/{guarded['design']}; "
        f"{relative_links} relative Markdown links resolve; "
        "8 examples and required safeguards present."
    )
    print("NOTE: these offline checks validate package structure and test coverage, not model judgment or AI authorship.")


if __name__ == "__main__":
    main()
