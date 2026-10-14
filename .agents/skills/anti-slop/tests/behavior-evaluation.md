# Repeated behavior evaluation

Package validation checks data integrity. This evaluation checks **observed agent decisions** on realistic requests: routing, question boundaries, continuation, meaning preservation, edit scope, and truthful evidence. It is separate from the browser fixture's control tests.

## Run protocol

Use [behavior_cases.json](behavior_cases.json): nineteen scenarios, at least three fresh executions each (57 runs). Keep model, harness, skill revision, and available tools constant within a comparison. Record actual settings rather than assuming defaults. These cases cover all four operations and supplement the 59 broader [execution scenarios](execution_cases.json); they do not prove all scenarios pass.

Prepare evaluator inputs without answers:

```sh
python3 tests/evaluate_behavior.py --prepare /absolute/path/to/new-evaluation-inputs
```

The output contains only context and user turns, plus a revision manifest. Give the evaluated agent the skill and one prepared request at a time. Do not give it expected checks, the browser answer key, prior failures, or the reviewer's conclusions. Supply a case's stated tool restriction as an environment constraint; never forge a tool result. Send continuation turns in order after the preceding response. Start each repetition with fresh state; preserve context only within its continuation scenario. Keep raw transcript/tool events and relevant file before/after snapshots. For inline-text cases in a restricted response-only harness, preserve every delivered response and restriction; state if private tool/progress events are unavailable. Such records support response/meaning judgments, not independent certification of unseen actions. A filesystem or browser-action evaluation requires the actual tool/artifact evidence. Do not allow evaluation to modify the real project or contact real users/accounts.

Use an authorized independent evaluator when available. This helper **does not start agents or call models**. Follow the host's delegation policy before starting one. Self-evaluation or a run shown the answers can be recorded as exploratory evidence but must not be presented as independent validation. A prepared input, invented transcript, unit-test sample, or annotation alone is not an agent execution.

## Review actual evidence

A reviewer reads the full transcript and artifacts without supplying answers during execution. Count skill-origin clarification/interview questions; do not count a quoted question or a question in the requested artifact. A multi-turn case's count spans the entire run. Review route/operation against the current user intent and continuation, not an agent's self-label.

For each case's semantic checks, record a boolean, reason, and exact evidence references:

- `scope_preserved`: edits/actions stay within the authorized target; audit leaves source unchanged. Inspect tool events and relevant file snapshots, not just the final answer.
- `meaning_preserved`: retain facts, timing, uncertainty, conditions, quantities, and voice; compare the full source/result. Concision does not permit a new obligation or deadline.
- `verification_honest`: claimed inspections/tests have observed evidence; blocked, inaccessible, and unperformed work remain visible.
- `finding_mapping_supported`: each reported canonical finding satisfies that rule’s detection conditions; an access gap has no defect class and a domain UX item need not be forced into a canonical rule.
- `structured_entry_choices`: unresolved direct setup gives actionable choices rather than only an open-ended target request. `contextual_setup_choices`: a category selection advances to relevant target/operation choices. `known_target_reused` and `known_operation_reused`: do not re-ask supplied inputs. `project_read_before_question` requires actual read evidence before the first question; `project_choices_grounded` compares the offered candidates with the raw project snapshot, not with an expected menu string. The source snapshot is at `tests/fixtures/project-context` in the skill folder; it supports context and source-review judgments, not runtime claims.
- Other checks are named for the case's observable contract: artifact-only output, no forced findings, no false-citation judgment from access alone, retained continuation and acknowledgment, domain-grounded UX without forced canonical mapping, research gaps, and no false browser completion.
- `source_claim_not_self_verification` and `access_gap_not_fabrication`: unavailable records do not turn an existing author/testimonial claim into a falsehood, and the reviewer does not adopt it as independently verified. `fabrication_reported_without_repair`: known invented proof is reported as a finding, without claiming an applied edit in audit mode.
- `blocked_report_proportionate`: with no inspected target material, report the actual access and evidence limits without repeating them under a full audit template or adding an unrequested generic plan. Partial runs must still preserve their observed findings.

Semantic review requires judgment; an exact word match cannot establish it. Require trace evidence and a reason even for passes. Negative conclusions about actions not performed need the complete tool transcript/artifact comparison, with a cited relevant span and the completeness basis in the reason.

## Record and assess

Each `runs.jsonl` line has this shape (illustrative schema, **not executed evidence**):

```json
{
  "case_id": "direct-clean",
  "repetition": 1,
  "skill_digest": "digest from run-manifest.json",
  "model": "actual model/version",
  "harness": "actual harness/version and settings",
  "run_id": "distinct actual execution identifier",
  "executed_at": "actual execution date/time",
  "reviewer": "actual reviewer and independent/self-evaluation status",
  "trace_path": "traces/direct-clean-1.txt",
  "trace_sha256": "sha256 of the preserved UTF-8 transcript",
  "observed": {
    "route": {"value": "direct", "reason": "review basis", "evidence": [{"start": 0, "excerpt": "exact trace span"}]},
    "operation": {"value": "audit", "reason": "review basis", "evidence": [{"start": 0, "excerpt": "exact trace span"}]},
    "skill_questions": {"value": 0, "reason": "review basis", "evidence": [{"start": 0, "excerpt": "exact trace span"}]},
    "scope_preserved": {"value": true, "reason": "review basis", "evidence": [{"start": 0, "excerpt": "exact trace span"}]}
  }
}
```

Include **all** checks requested by that case, not just `scope_preserved`. Offsets are Python Unicode character offsets into the decoded transcript; SHA256 uses raw bytes. Paths are relative to the records file or absolute. Preserve full traces with tool observations and relevant before/after artifacts; redact secrets before hashing and note redactions. Run IDs must identify distinct executions, not renamed copies.

```sh
python3 tests/evaluate_behavior.py --assess /absolute/path/to/runs.jsonl
```

The assessor rejects missing/mismatched evidence, different skill revisions, duplicate runs, and malformed annotations. It compares reviewed outcomes against hidden expectations and reports missing repetitions, failures, and variation in decisions. Wording variation is allowed. An incomplete suite cannot pass. Trace hashes check integrity, not authenticity; review provenance and source artifacts separately. Do not present reviewer annotation as automatic proof of semantic quality.

Report actual run count, settings/revision, per-case results, failures and material limits. Make changes supported by failures and rerun affected cases on the new revision; do not merge old-revision passes into the new report. Report browser coverage separately. No repeated-model validation is implied by `npm test` or by preparing this suite.

## Focused rendered-design evaluations

For a reported design miss, add a scoped evaluation outside the fixed behavior suite. Capture the actual target under an identified authorized environment, preserving route, viewport, action and image evidence. Freeze the request, captures, source snapshot/relevant revision, tools, and comparator material across before/after runs. Run at least three fresh agents per case without expected issues, prior reports, or reviewer conclusions. Distinguish an agent's supplied-capture review from an independently operated browser walkthrough. If source changes during evaluation, record the change and avoid a controlled-comparison claim for affected judgments.

The maintainer reviews whether each visual warning names an observed relationship, a supported task/brief, a plausible mechanism explicitly presented as judgment, and a bounded repair. Track unsupported warnings and forced style changes as well as omissions. Include a viable simple screen or relevant negative control so increased criticism is not mistaken for improved judgment. Do not use issue counts, matching expected words, or a single reviewer's aesthetic verdict as an objective quality score. Preserve actual responses, revision digests, evidence references, and unavailable private-tool-transcript limits. Report this as focused evaluation rather than a full-suite pass.

For consistency comparisons, freeze the input **before both revisions run**, including exact screen/viewport/state captures and any source extracts. Keep the request and output allowance identical apart from the skill path and run ID. Declare the supported anchor issues before the retest, with screenshot/region/mechanism and an independently reviewed task basis when available. Do not give those anchors or prior outputs to the execution agents. A disputed aesthetic direction is not a mandatory anchor; retain disagreements rather than tuning the skill to one reviewer's preferred layout.

Review omissions in two parts: was the relevant state/check inspected, and was its concern retained or specifically dismissed? Compare semantic issue identities and their evidence, not headings or detector terms. Check that ledger concerns reconcile with findings, merged entries, or specific dismissals, and that unknown states do not receive clean judgments. Record per-anchor detection across repetitions, unsupported warnings, material severity variation, coverage gaps, and clean-control results. An issue appearing in all three runs of one product is a bounded observation, not a general reliability estimate. Keep held-out views or products separate from the tuning examples when extending the evaluation.
