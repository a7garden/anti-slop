# State truth and scoped reflow — 2026-11-02

Anti-slop **2.1.2 completed 21 final focused response-only executions**: seven cases, three fresh repetitions each. The maintainer's semantic review passed all 21. A fresh Claude Opus 5.5 follow-up reader also passed every listed check in all 21 final runs and gave the corrected candidate a go decision. This is not a full-suite pass, a rendered UI assessment, or an estimate of improvement over 2.1.1.

## Research and change

The [source comparison](../.agents/skills/anti-slop/references/skill-comparison.md#content-and-state-resilience-2026-11-02) records inspected primary sources, pinned skill revisions, adopted ideas, and rejected defaults. Carbon and GOV.UK informed state-specific messages and purposeful validation repetition; W3C clarified the scope of reflow exceptions and the difference between a narrow viewport and text enlargement. Impeccable contributed representative content probes, with its universal stress sweeps and feature requirements excluded. Current Anthropic and writing-skill guidance mostly overlapped with existing protections and did not justify additional rules.

The existing design profile, browser checks, and D11/D12 were refined. No canonical rule was added. Failure must not become a confirmed zero count or a field correction without evidence. Supported recovery stays bounded by actual capabilities. Useful field/summary repetition remains. Necessary table relationships may remain two-dimensional while ordinary cells and surrounding controls are inspected separately. Layout checks use relevant content rather than a universal language or data-size sweep.

## Preliminary batch and corrections

A preceding candidate completed 18 runs at runtime digest `cbabad5d21c85907528b58b8708eeddbb40959c4e1df10dd860eb44dc9c1808e`. A fresh Claude Opus 5.5 reader passed their entire check sets, then identified a missing D10 fixture classification, scope ambiguity in the scrollbar wording, and severity/recovery rationale needing clarification. The corrections preserve the official distinction between a scrollbar and non-excepted content that actually needs two-dimensional scrolling. An ordinary-prose counterexample was added before the final fresh batch. Preliminary and final executions are separate, not pooled as final-version passes.

## Observed decisions

| Case | Runs | Maintainer result |
| --- | --- | --- |
| `list-timeout-shown-as-empty` | 3 | D11 for the unsupported zero/first-use state and D10 for the excluded creation CTA; remove misleading claims without inventing retry/offline support |
| `confirmed-empty-filtered-search` | 3 | No forced finding for successful zero matches with a working clear-filter action |
| `service-unavailable-field-blame` | 3 | D11 for the false email correction; describe the service failure, retain values, add no unsupported recovery |
| `field-error-summary-repeat` | 3 | Preserve useful linked-summary and inline-field repetition without a redundancy finding |
| `table-reflow-local-scroll` | 3 | Preserve necessary table relationships; no forced overflow finding or unearned conformance claim |
| `table-controls-clipped-320` | 3 | D12 for the unreachable pagination action; repair the surrounding row while retaining the table |
| `ordinary-content-page-overflow` | 3 | D12 for ordinary prose requiring two-dimensional scrolling; use a fluid text container without hiding overflow |

All recorded responses stayed within the component audit, asked no setup questions, and distinguished supplied observations from independently performed tests. The misleading-state findings used medium severity; the clipped pagination action and non-reflowing article used high severity. The timeout's two findings concern different mechanisms and repairs, not duplicate classifications of one issue.

## Evidence and limits

- Recorded configuration: `gpt-6.1-sol`, effort `high`, service tier `default`, Codex Desktop `0.164.0` app-server harness.
- Runtime digest: `fa9711fb3e912aad32a9b433d3b82685b049a7a267262367c9972fd128bed531`. Frozen snapshot and prepared manifest match. Evaluation sources were preloaded; inputs excluded expected checks, verdict hints, and prior outputs.
- All 21 executions completed with distinct run/thread IDs. Workspace before/after hashes match, trace/protocol hashes were recomputed, and no tool calls or lifecycle-hook prompts appeared.
- Evidence is retained locally under `.orch/evaluation/research-v212-final/`: frozen sources, blind inputs, protocol and trace records, integrity checks, and 162 maintainer annotations. The mechanical focused assessor reports `passed`; its full-suite counterpart reports `incomplete` with 32 unrun cases. The complete suite requires 117 executions.
- Global `/Users/garden/.codex/AGENTS.md` remained an instruction source. The owner replaced its routing section between the preliminary and final batches; the final file hash is retained locally, and no controlled comparison between batches is claimed. There was no old-versus-new baseline, held-out product, actual browser interaction, text-zoom execution, or assistive-technology test. These selected tuning/regression cases establish only the observed response decisions. Hash validation does not establish semantic correctness.

## Independent follow-up

Two independent-vendor review rounds completed at high effort: the initial source/execution review (`20261102-003133-claude-review`), then the capped fix-only/final-evidence follow-up (`20261102-004117-claude-review`). Both recorded actual model `claude-opus-5-5`. The follow-up confirmed the fixes and independently passed all 21 final outputs against their listed checks. It inspected the actual traces, execution metadata, protocol item types, and source comparisons; no expected-check leakage was found.

The reviewers’ permission layers denied npm/Python/hash commands; the final reviewer also could not run `git diff --check`. They inspected recorded npm output rather than reproducing it and did not fetch the external sources. The main agent actually ran the package, hash, and diff checks. Maintainer annotations and independent semantic judgments remain separate provenance; hash/command reproduction is not claimed independent. The two rounds are complete; minor optional wording and source-registry notes were retained without adding requirements or another review cycle.

## Package checks

`npm test` passed: 54 canonical rules, 161 applicability fixtures, 60 execution scenarios, 39 behavior scenarios, seven installer tests, and ten Python unit tests. Skill Creator validation and `git diff --check` passed. A package dry run excluded local `.orch` evidence. Fixture validation checks structure; actual model executions and semantic review are reported separately above.
