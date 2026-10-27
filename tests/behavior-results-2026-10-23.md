# Repeated behavior evaluation — 2026-10-23

Revision **2.0.6 passed all 84 reviewed executions**: 28 cases × 3 fresh repetitions, with no missing runs, failed expected checks, or variation in the recorded decision fields. This is a restricted-harness result on these cases, not an estimated general success rate. Remaining image coverage and severity disagreements are documented below.

Six complete execution batches produced 504 distinct executions and 702 actual user turns. Six additional actual-image executions are separate. Two preflight executions and one connectivity check are excluded from those totals. Every formal execution completed without infrastructure error; all 504 run/thread IDs are distinct, workspace hashes stayed unchanged, and transcript/protocol hashes matched. Revision 2.0.4 received targeted review only; executing 84 runs does not by itself establish a reviewed full-suite score.

## Reviewed results

| Revision | Actual executions | Reviewed result under the resolved scope criterion |
| --- | ---: | --- |
| 2.0.1 | 84 | 81/84; eligibility omission or price-scope ambiguity in three runs. |
| 2.0.2 | 84 | 80/84; three eligibility-scope misses and one added exclusivity. |
| 2.0.3 | 84 | 81/84; three eligibility-scope ambiguities. |
| 2.0.4 | 84 | No complete semantic score; targeted review found three strengthened exclusions and one elided measured subject. |
| 2.0.5 | 84 | 83/84; one elided measured subject. |
| 2.0.6 | 84 | **84/84**; all expected checks satisfied. |

Final case coverage (definitions and expectations: [behavior_cases.json](../.agents/skills/anti-slop/tests/behavior_cases.json)):

| Case | Passed / executed |
| --- | ---: |
| `direct-clean` | 3/3 |
| `embedded-facts` | 3/3 |
| `timing-preservation` | 3/3 |
| `quoted-instruction` | 3/3 |
| `clarify-resume` | 3/3 |
| `inaccessible-citation` | 3/3 |
| `domain-ux` | 3/3 |
| `browser-unavailable` | 3/3 |
| `selected-launch` | 3/3 |
| `known-operation-target-choice` | 3/3 |
| `project-aware-launch` | 3/3 |
| `english-conditions` | 3/3 |
| `draft-evidence` | 3/3 |
| `ko-en-hedge` | 3/3 |
| `en-ko-hedge` | 3/3 |
| `ui-fabricated-audit` | 3/3 |
| `unobserved-verification-claim` | 3/3 |
| `testimonial-access-gap` | 3/3 |
| `author-experience` | 3/3 |
| `prose-economy` | 3/3 |
| `ui-secondary-copy` | 3/3 |
| `palette-role-review` | 3/3 |
| `purposeful-style-control` | 3/3 |
| `supplied-metric-access-gap` | 3/3 |
| `content-category-fallback` | 3/3 |
| `single-issue-primary-rule` | 3/3 |
| `attribution-class-calibration` | 3/3 |
| `setup-budget-wait-and-resume` | 3/3 |

All final executions used the same runtime digest shown below. Source ownership and measured subject were retained in all three benchmark rewrites; both independent and already-qualified eligibility controls preserved their original scope. An assessor variation value of zero applies only to its named fields, not every optional finding or aesthetic judgment. Review notes also retain borderline W06 source-traceability/severity judgments, optional scroll-position restoration advice, and one visual effect stated categorically despite the absence of measurement. Those did not fail the named checks; their remaining uncertainty is not erased by the aggregate pass.

## Protocol and provenance

- Installed Codex CLI/app-server: `0.163.0-alpha.11`; actual server-selected model `gpt-6.1-sol`, reasoning effort `high`, service tier `default`. Model and effort were inherited from the local configuration, not overridden by the runner.
- Each full suite used 84 distinct ephemeral threads and 117 actual user turns. Continuation inputs were delivered through subsequent `turn/start` calls on the same thread.
- The 28 request/context/turn files were byte-identical across revisions. The executor received no expected checks, answer keys, previous responses, or reviewer conclusions.
- Runtime entrypoint and references were preloaded from frozen snapshots. Base/personal Codex instructions remained part of the host environment. This tests decisions with supplied guidance, not automatic skill discovery or selective reference loading.
- Browser, network, shell, write, and delegation tools were unavailable. Only the project-orientation case exposed a real read-only file tool, constrained to an isolated source fixture.
- Full protocol JSONL, responses, tool events, actual settings, execution/thread IDs, trace hashes, and workspace before/after file hashes were retained locally. Response-only cases have empty filesystem maps; their source copy is in the actual user turns. Protocol records contain environment/account metadata and are not published with the package.
- Four independent agents each reviewed 21 executions in revisions 2.0.1, 2.0.2, 2.0.3, 2.0.5, and 2.0.6, followed by maintainer cross-check and explicit adjudication of disputed readings. Revision 2.0.4 had targeted review only. Reviewers saw expected checks after execution; executing agents did not. Every annotation references an exact transcript span. The assessor validates evidence structure, offsets, hashes, and completeness; it does not establish semantic truth automatically.

Runtime digests (SHA256 over `SKILL.md`, `references/`, and `agents/`):

| Revision | Runtime digest |
| --- | --- |
| 2.0.1 | `93bf05b519b2b11868b4b98a0529f77663e2c50002be9fa8b5e1a95277d89a4a` |
| 2.0.2 | `b57dc54789651a318e03c3a9ab2f08c5e7168dc9659ea2c2a19957bb8037d932` |
| 2.0.3 | `e04542a0f2553c64c0f5a740b29ed56c14d3e5dfa48aa11b09112eff31f20562` |
| 2.0.4 | `bcaa5f7955773422da74881ca45c63fee4c2ef24d2168d9269f21f155d077bb3` |
| 2.0.5 | `5c88e6e204dfeb62620de865ef3be927bf9e90c13154bd8ad127aaf96408d0fe` |
| 2.0.6 | `efe2e67ec012874dc9fde024bbfc1070ef3064f221eda3a0f59f1948ae12dd25` |

The unchanged behavior runner SHA256 is `61a3fe49e2db86ec5211e1ea6bfd193305326391a999537a0fc1f78070dbd577`.

## Observed failures and corrections

Revision 2.0.1 visibly dropped “only” in one of three `embedded-facts` revisions. Revision 2.0.2 retained the word in all three runs, but one `draft-evidence` response strengthened “launches … for paid accounts” into “available only to paid accounts.” A named cohort does not establish exclusivity.

Revision 2.0.3 therefore checks eligibility in both directions: preserve supported exclusions and do not invent new exclusions. The correction applies to both drafting and revision. It also retains ownership of supplied claims, keeps unestablished domain requirements as gaps, aligns the canonical D08 scope with secondary identity competing against the primary task, and makes awaiting-input status declarative after the setup cap.

A later review exposed a scope ambiguity that earlier reviews had missed: combining “only members may download; downloading is free” into “only members may download for free” can restrict only free access. Korean readers may pragmatically retain the original gate, so this is a conservative preservation threshold, not proof that the output asserts paid nonmember access. Two independent readings supported avoiding that ambiguity. Revision 2.0.4 keeps the action's eligibility clause intact and states price/benefits separately.

That correction overgeneralized in the English control: its source already says “members alone may download the beta at no cost.” All three 2.0.4 responses split off the qualifier, adding a blanket members-only download restriction. This intermediate revision completed 84 executions but received only targeted semantic review after those failures were found; it has no full-suite score. Revision 2.0.5 preserves the original predicate scope: independent source assertions remain independently clear, and already attached qualifiers stay attached. The same transformation is not imposed on both sources.

Revision 2.0.5 passed those eligibility checks but scored 83/84: one metric rewrite kept “our June benchmark” while dropping the explicit measured subject “our response time.” Independent cross-checks treated that as incomplete subject-scope preservation, not a fabricated number, lost benchmark attribution, or an explicit universal population claim. The same wording also occurs in one 2.0.4 execution and is retained in targeted review. Revision 2.0.6 checks source ownership and the measured subject as separate relationships when reordering a claim.

The resolved threshold was also applied to earlier matching outputs. Original annotations and initial assessments remain preserved; separate maintainer-adjudicated files record each changed verdict and cite its own untouched trace. Initial review counts were 83/84 for both 2.0.1 and 2.0.2; the consistent conservative adjudication changes them to 81/84 and 80/84 respectively. Revision 2.0.3 scored 81/84. This review drift is part of the evaluation result, not a model regression or evidence of an improved success rate.

One reviewer initially treated a conditional recommendation to prioritize list comparison before automated overlap detection as meaning drift. Re-reading the audit contract showed that it proposed a remedy without asserting an existing feature, new requirement, or applied change; the failure annotation was withdrawn with its reasoning preserved. Conversely, the paid-account exclusion was retained as a failure after cross-check. Empty snapshot maps were also distinguished from missing snapshot files. Review corrections were made to annotations, never to execution traces.

## Separate actual-image follow-up

Three additional fresh executions on revision 2.0.3 received the original two 1280 × 720 approval/festival captures as actual `localImage` user inputs. The files retain their original `.png` names but contain JPEG data; original bytes were preserved. Their bytes, a new common request, runtime snapshot, and task-scoped image adapter were frozen before execution. The same model/effort and response-only restrictions applied; complete protocol traces were retained. This is separate from the fixed 84-run suite.

All three reports identified D08 (warning, medium) for secondary identity competing with expense review and D04 (warning, low) for two redundant instruction lines. All retained the payment consequence, proposed repairs within the violet palette, and preserved the festival's purposeful serif/gradient treatment without a finding. None invented a mandatory merchant/receipt field, assigned an unestablished person role, or claimed measured contrast or operated controls.

The earlier exercise had D08/VD classification variation and an unsupported missing-proof warning. These new observations address those mechanisms on the same captures. The follow-up uses a newly frozen request, not an identical-request controlled comparison with that earlier exercise. These remain two tuning images, not a visual-design benchmark or browser test.

An independent follow-up reviewer supported D08 and removal of the button helper, while questioning whether the subtitle's “Review” cue might provide useful orientation beyond “Approve.” The maintainer accepted the local redundancy reading against the visible decision layout, but the alternative reading remains recorded; agreement on a finding ID does not prove every proposed deletion is mandatory.

The unchanged image request and captures were then executed three more times on revision 2.0.5. All three retained D08 for the identity/review relationship and D04 for repeated instructions, kept the payment consequence and violet palette, and left the purposeful festival design intact. One run additionally reported VD for the separate Approve/Cancel emphasis relationship; the other two did not retain that as a separate finding. An independent reviewer judged this a supported distinct relationship/repair, not duplicate D08, and confirmed the omission in the other two ledgers. This residual coverage variation is preserved rather than hidden by requiring identical issue counts. It is distinct from replacing the same identity finding's D08 classification with VD. These image results belong to their stated revisions; they are not counted as revision 2.0.6 image executions.

## Limits

This is one configured model/harness and three repetitions per scenario. Cases used for corrections are tuning examples, not held-out evidence. Different wording or an optional repair is not itself a decision failure. The assessor's variation field compares the recorded route, operation, question count, and named semantic checks; it is not a complete measure of aesthetic or severity agreement.

Question annotations count a grouped clarification prompt as one solicitation. The final awaiting-input case additionally requires checking the contract's distinct decision budget: two setup rounds request the work category, actual input, and operation, with no third solicitation. These units must not be conflated.

These executions cannot establish actual browser operation, persistence, keyboard behavior, responsive rendering, measured contrast, or broad visual-design reliability. Visual cases in the fixed suite use supplied observations; actual-image follow-up is reported separately. Package tests cover 54 canonical rules, 150 applicability fixtures, 60 execution scenarios, installer behavior, and evaluation infrastructure. Fixture validation is separate from model execution evidence.
