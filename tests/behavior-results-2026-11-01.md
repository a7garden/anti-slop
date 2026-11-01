# Focused design-authoring evaluation — 2026-11-01

Anti-slop **2.1.0 completed 15 reviewed executions**: five cases, three fresh repetitions each. A subsequent review withdrew the preservation pass for two redesign responses that assume unsupported existing behavior; the original blanket pass claim was too broad. The other 13 retain their original reader verdicts, not a new comprehensive reassessment. This is a focused response-only result on implementation specifications and bounded audits. It does not establish a full-suite pass, rendered design quality, live interaction correctness, accessibility conformance, or improvement over 2.0.6.

## What changed

The previous smallest-repair and identity-preservation wording did not distinguish a bounded repair from an authorized redesign. Version 2.1.0 permits coherent changes to unprotected layout, type, and palette when requested, without first inventing a defect or adding an approval gate. It adds a product-derived working brief, adjustable craft recipes, content-led emphasis, and original illustrative design examples. Audits remain read-only and evidence-based; protected facts, identity, features, states, and accessibility remain constraints.

The [comparison notes](../.agents/skills/anti-slop/references/skill-comparison.md#design-authoring-unslop) record what was conceded, adopted from the unslop comparison, and rejected. The comparison identifies instruction-level gaps; it is not an empirical before/after result.

## Reviewed outcomes

A fresh Codex reader originally inspected every named semantic check against the actual outputs and relevant protocol evidence, after the writing was finished. It reported 105 check decisions across the 15 executions. A summary of that review is retained; no per-check annotated assessor file was produced. The subsequent independent review identified the two unsupported assumptions below and the missing explicit capability check in the redesign case. All runs had zero skill-origin questions. All nine responses requiring artifact-only delivery satisfied it; the six audit responses could include brief progress commentary.

| Case | Repetition 1 | Repetition 2 | Repetition 3 | Observed boundary |
| --- | --- | --- | --- | --- |
| `authorized-visual-redesign` | Original pass retained | Preservation pass withdrawn | Preservation pass withdrawn | Concrete replacement language, but repetitions 2 and 3 assume unsupported existing behavior |
| `design-draft-concrete-defaults` | Pass | Pass | Pass | Concrete spacing, type and palette roles; supplied invoice fields and viewing action; no payments, automation or compulsory art |
| `sound-settings-control` | Pass | Pass | Pass | Existing arrangement retained; no forced redesign, novelty or style mandate; supplied-observation limits stated |
| `purposeful-style-control` | Pass | Pass | Pass | Approved violet gradient and serif identity retained without fabricated findings |
| `supplied-metric-access-gap` | Pass | Pass | Pass | 32%, June benchmark ownership and measured subject retained; no independent-verification claim |

Redesign repetition 2 says “Retain the current due-date editing control”; repetition 3 says “Use the application’s existing overdue calculation.” Neither dependency is supplied by this synthetic case, whose context explicitly supplies all product facts. Calling them preservation dependencies does not establish their existence. These responses fail the capability-preservation boundary; the original case lacked an explicit `no_fabricated_capability` check. The retained traces are `.orch/evaluation/unslop-v21-isolated/records/runs/authorized-visual-redesign-2/trace.txt:65` and `authorized-visual-redesign-3/trace.txt:59`. This identifies unsupported assumptions, not proven failures in a real application. The 2.1.1 correction adds the missing check, a read-only-date control case, and runtime guidance distinguishing presentation choices from capability claims.

One specification also contains a self-corrected hexadecimal-token typo. The named checks do not establish implementation polish or substitute for building a design.

## Protocol and integrity

- Actual server-selected configuration: `gpt-6.1-sol`, reasoning effort `high`, service tier `default`.
- Runtime snapshot digest: `cf88fe767746bd7f35bfc9d596380cd5e33717b0e0abb930ba343b3ded192ec9`.
- At the time of the 2.1.0 evaluation, source, frozen snapshot and prepared-input manifest digests matched. The recorder preloaded its listed runtime references; it did not expose expected checks or reviewer conclusions to execution agents.
- All 15 run IDs and thread IDs were distinct. All executions completed; workspace hashes remained unchanged. Recorded trace/protocol SHA256 values were independently recomputed and matched.
- Tools were unavailable in these selected response-only cases. No hook prompts or tool calls appeared in the clean batch.
- Global user `AGENTS.md` remained an actual server-reported instruction source in every run. It contains UI guidance that overlaps the skill, so this experiment does not isolate the skill's contribution from user defaults. This is declared inherited context, not an instruction-free experiment.
- The existing recorder, blind-input preparation and cases are in [run_behavior.py](../.agents/skills/anti-slop/tests/run_behavior.py), [evaluate_behavior.py](../.agents/skills/anti-slop/tests/evaluate_behavior.py) and [behavior_cases.json](../.agents/skills/anti-slop/tests/behavior_cases.json). Model effort was overridden only for the task process; global settings were not edited.

The machine-local evidence is retained under `.orch/evaluation/unslop-v21-isolated/`: `records/runs/<case>-<repetition>/` contains actual protocol, trace, metadata, and before/after hashes; `review-extraction.txt` retains assistant responses; `semantic-review-summary.json` retains the independent reader's summary and limits. These raw records are not distributed in the package. This report summarizes their review.

## Failure capture and recovery

An earlier 15-run batch completed but inherited lifecycle memory hooks. Those hooks appended memory-recording messages to otherwise requested artifacts. It is retained under `.orch/evaluation/unslop-v21/` and **excluded from semantic success counts**. Completion alone did not establish a pass.

The contained fix disables lifecycle hooks and sets the project-instruction byte limit to zero only in the evaluation process/thread configuration. The recorder now rejects an unexpected `hookPrompt` as an execution error while preserving raw evidence. A synthetic regression reproduces that event and verifies rejection. These settings are documented in the [official OpenAI configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).

One separate real preflight confirmed zero hook prompts and a single requested artifact response. It also showed that the global user instruction source remained present despite the project byte limit. We retained and disclosed that context, then ran the 15 fresh executions above. The preflight is excluded from their totals. Overall, 31 real executions were recorded: 15 contaminated, one preflight, and 15 clean reviewed executions.

## Other checks and limits

- `npm test` passed: package structure and links, 154 rule-applicability fixtures, 60 execution scenarios, 31 behavior scenarios, seven installer tests and ten Python unit tests. Fixture validation does not execute those scenarios.
- Skill Creator `quick_validate.py` reported `Skill is valid!`; `git diff --check` was clean.
- A package dry-run included the new HTML and attribution/comparison references and excluded private `.orch` artifacts.
- The original [design examples](../.agents/skills/anti-slop/references/design-examples.html) received source review. A source-level record/state comparison confirmed that both planner arrangements expose the same four tasks, due dates and completion states. An accessibility-label omission found in review was corrected.
- Local browser use was disabled in Work settings. No browser rendering or assistive-technology execution of that sheet was completed; its visual presentation remains unverified. The temporary local server was stopped, and no browser tab was created.

The 2.1.0 behavior suite required **93** executions and was not rerun in full here. The 2.1.1 correction expands it to **96** required executions; this historical report does not cover that revision. Historical [2.0.6 results](behavior-results-2026-10-23.md) remain separate; these selected cases do not estimate a general success rate or prove an improvement over that revision.
