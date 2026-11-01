# Capability-preservation correction — 2026-11-01

Anti-slop **2.1.1 completed a final 12-run response-only retest**: four cases, three repetitions each. The maintainer's review found the requested capabilities preserved in all 12 under the clarified rubric. A preceding candidate also completed 12 runs; independent review retained a capability failure in one response, prompting the final correction. These are two separate batches, not 24 final-version passes. This is a focused implementation-specification and supplied-observation evaluation, not a full-suite pass, a rendered-design assessment, or a general reliability estimate.

## Correction

The [corrected 2.1.0 report](behavior-results-2026-11-01.md) withdraws two preservation passes: those outputs assumed existing functionality absent from the supplied facts. Describing an assumption as something to preserve did not justify it.

The runtime now distinguishes visual choices from claims about existing actions, calculations, and functional states. Conditional preservation is allowed where support is unknown, without introducing an excluded capability. Presentation derived from supplied fields remains allowed. The original redesign request is unchanged; its checks now explicitly include `no_fabricated_capability`. A new Dayfile control supplies read-only due dates and completion toggles while excluding editing, creation, deletion, reminders, sync, and server-provided overdue state.

## Independent review and further correction

The first candidate used runtime digest `2dac1be3c72efb2da03f77b90495721a71eaf24cd37c0f4ace35d151c0401bdb`. A fresh Claude Opus 5.5 reader inspected all 12 outputs, their inputs, checks, and protocol evidence. It conservatively failed `authorized-visual-redesign` repetition 3 for “Keep records outside the displayed week accessible through existing product behavior”: the input does not establish that access path. The maintainer accepted this verdict, correcting the initial 12/12 reading to 11/12.

The reader also identified ambiguity between a generic safeguard to retain supported behavior and a composition that depends on a specific unknown capability. The final runtime and rubric now distinguish these explicitly. The runtime's exact examples of the earlier failures were removed in favor of that general distinction. These are tuning and regression cases, including an explicit-exclusion control; no held-out generalization test was performed.

The reader's permission layer blocked file writes and Python execution. The maintainer serialized its explicit per-check judgments into the existing assessor schema, retaining that provenance, and ran the mechanical assessor: the first four-case batch reports `failed` for the single capability check. After the capped follow-up review, the maintainer owned the correction and reviewed the final fresh retest; **the final retest is self-reviewed, not independent validation**.

## Observed outcomes

| Case | Repetitions reviewed | Maintainer verdict | Observed boundary |
| --- | --- | --- | --- |
| `authorized-visual-redesign` | 3 | Pass in each | Concrete replacement layout, type, and palette; Weekdesk, task data, due dates, and completion retained; no specific unsupported editing action or overdue calculation asserted |
| `redesign-readonly-dates-control` | 3 | Pass in each | Dates remain read-only; completion remains the supported action; grouping by date is allowed without adding task-management or import controls |
| `design-draft-concrete-defaults` | 3 | Pass in each | Concrete visual defaults with supplied invoice fields and one viewing action per row; no payment or automation capability added |
| `purposeful-style-control` | 3 | Pass in each | Approved violet gradient and serif treatment retained; no forced finding from the supplied observation |

All nine final implementation specifications used artifact-only delivery. The three audit runs included a brief progress message and a final assessment, which their case permits. No skill-origin questions or new approval gates appeared. Generic instructions to preserve supported behavior were not treated as claims that a particular additional function exists; a concrete dependency on unknown behavior needs an explicit support condition. For example, final Weekdesk specifications mention existing action/edit-trigger categories as safeguards without adding a named control; outside-week records are conditional on applicability or current scope. Those sentences do not certify the underlying implementation.

## Execution evidence and limits

- Actual recorded configuration: `gpt-6.1-sol`, reasoning effort `high`, service tier `default`.
- Final runtime digest: `0d7cce69c9cc2011bd11b65d5795ca6901ac4513a8ee248c91f0dc1ad1807a4f`. Source, frozen snapshot, and prepared-input manifest match.
- All 12 executions completed with distinct run and thread IDs. Workspaces were unchanged; trace and protocol hashes were recomputed and matched. No hook prompts or tool calls appeared.
- The existing harness supplied the frozen runtime and blind case inputs, excluding expected checks and prior verdicts. Tools were unavailable. Global settings were unchanged.
- Global user `AGENTS.md` remained an actual instruction source. Its overlapping UI guidance prevents isolating the skill's contribution from user defaults.
- Machine-local final evidence is retained under `.orch/evaluation/unslop-v211-final/`; the first candidate remains under `.orch/evaluation/unslop-v211-preservation/`. Both retain actual executions in `records/runs/`, 132 annotated fields in `assessor.jsonl`, and focused/full-suite assessment results. The final focused assessment reports `passed` from the maintainer's judgments; the full-suite assessment remains `incomplete` with 28 unrun cases. Hash/annotation validation does not automatically establish semantic correctness. Raw records are not distributed in the package.

These executions are new 2.1.1 candidate evidence; batches and old-revision passes are not pooled into final totals. Both batches used the same four case requests and recorded model configuration. No rendering, browser interaction, or assistive-technology validation was performed. The complete suite now requires **96** executions and was not run in full. The small selected sample does not establish a general improvement rate over 2.1.0.

## Package checks

`npm test` passed: 54 canonical rules, 154 applicability fixtures, 60 execution scenarios, 32 behavior scenarios, seven installer tests, and ten Python unit tests. Scenario/fixture validation is structural and does not execute the full behavior suite. Skill Creator validation passed, and `git diff --check` was clean.
