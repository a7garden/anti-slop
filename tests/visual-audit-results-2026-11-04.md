# Focused visual audit — 2026-11-04

Anti-slop 2.2.0 adds `visual-audit` and `audit --visual` as entrypoints to audit with the visual method. Existing design/style criteria and the relationship ledger remain authoritative. A requested fix uses revision with matched post-change checks. No canonical rule or mandatory scanner was added.

The candidate completed **24 actual model executions**: four supplied-image scenarios and four restricted-evidence scenarios, three fresh runs each. These are regression exercises, not a full-suite pass or measured improvement over 2.1.2. The image results include a deduplication concern and variation in a table-layout judgment; an aggregate quality pass is not claimed.

## Actual rendering and interaction

Playwright Test 1.64.1 used an isolated headless Chrome 156.0.8078.80 on macOS. The four local fixture views were rendered, captured and visually inspected by the maintainer. Device scale and visual viewport scale were 1; theme was light. No production data or personal browser profile was used.

| View | Observed conditions and evidence |
| --- | --- |
| Approval A and B | Both captured at 1100 × 740 CSS/image pixels, same content and initial closed disclosure. The identity region changed from 500 to 275 CSS px; brand type from 66 to 24 px. The task region moved to the leading side and the preview gained the purple accent. Source text matched. These measurements support a changed visual relationship; they do not measure user performance. |
| Approval preview | In both variants, focusing the native disclosure and pressing Enter opened the $124.00 preview; Enter closed it. The amount, person and payment-consequence statement remained. No payment executes in the fixture. |
| Narrow rates | Viewport 320 × 720 CSS px; capture 320 × 468 image px. Page client/scroll widths both 320. Table region client/scroll widths 286/592. Focus plus repeated ArrowRight moved scrollLeft to 238. Rate definitions opened and closed with Enter. Surrounding content remained within the viewport. |
| Festival | 1100 × 740 CSS/image pixels. The supplied violet gradient and serif direction remained, with visible date, venue, price and schedule. The synthetic ticket control was not exercised as checkout. |

The first table test incorrectly expected End to move the horizontal region; it failed with scrollLeft 0. Replacing that test input with ArrowRight passed the targeted rerun. Fixture code was unchanged. This is a corrected test assumption, not a product fix. Final coverage is three passing original view tests plus the corrected rates rerun.

The approval pair is a prepared CSS comparison, not a model-authored repair. The maintainer verified matching capture conditions and the affected local disclosures. There was no autonomous model edit-and-render loop, native-app session, contrast calculation, accessibility-conformance assessment, or user study.

## Observed model decisions

Each image run received one actual PNG through app-server `localImage`, its capture metadata, the scenario prompt and runtime references. Paired images, prior outputs and reviewer anchors were withheld. Rates runs additionally received the harness's actual page-fit/keyboard-scroll observations, clearly attributed to the separate harness. The models themselves had no browser or mutation tools.

| Image scenario | Runs | Maintainer reading |
| --- | --- | --- |
| Approval A | 3 | All found the identity-versus-approval hierarchy concern and preserved useful information/identity. Two reported one D08 issue. One split identity dominance and the subdued preview into D08 and VD-01; main and the independent reviewer consider that an over-split warning with inflated severity within the same relationship. |
| Approval B | 3 | No forced layout/color finding. All recognized task/action emphasis and left the pale identity rail intact. Open-preview and interaction limits remained explicit. |
| Narrow rates | 3 | All retained the table, units and horizontal scrolling. Two proposed narrowing the Region column because the first rate's heading and units are cut at the initial edge; one found no required change. The visible basis is real, but severity/necessity varies. The independent reviewer confirmed these should not be counted as unsupported findings; the original reviewer anchor was corrected to permit them and to acknowledge that scrolled region labels leave view. None called the scrollbar alone a reflow failure or asserted conformance. This control tests preservation, not an obligatory zero-findings answer. |
| Festival | 3 | No forced finding; gradient, serif, spacing and information preserved. No claimed checkout or measured contrast success. |

The four restricted-evidence cases also completed three runs each. The worker and main read all 12 outputs against their named checks: source-only CSS remained provisional; supplied observations were not claimed as firsthand; native-image metadata without image bytes produced no invented visual verdict; and differing viewport/theme/panel states did not certify a repair. These named checks passed in the observed responses.

## Provenance and limits

- Runtime digest: `16a09cc0e70b15f00ff4bb2ab037b46a67df790f4ec5e5a70e67130325d52764`. The frozen runtime snapshot matched the candidate runtime files when these checks ran.
- Observed model/configuration: `gpt-6.1-sol`, reasoning `high`, service tier `default`, Codex Desktop 0.164.0 app-server. Each run used a fresh ephemeral thread. Global `/Users/garden/.codex/AGENTS.md` remained an instruction source.
- Runtime sources were preloaded. These executions do not establish skill discovery, selective module loading, live tool selection or autonomous UI inspection. Expected fields and reviewer-only anchors were excluded from executor inputs.
- Main recomputed transcript/protocol and attached-image hashes, checked 24 distinct run/thread IDs, completed turns, unchanged workspace hashes, and absence of tool/hook items. Integrity does not establish semantic quality. Image assessments are manually reviewed, not automatically graded.
- Local evidence is retained under `.orch/evaluation/visual-v220/`: frozen snapshot, capture script/PNGs/measurements, blind inputs, image and restricted protocol/trace records, manual judgments and integrity checks. These ignored local artifacts are not included in the npm package.
- Only four of the 43 behavior scenarios were executed here. The complete behavior suite requires 129 runs. The separate four-scenario image exercise ran 12 times. No prior-version baseline or held-out product was tested.

## Independent review and corrections

A fresh Claude Opus 5.5 review at high effort (`20261104-211430-claude-review`) recommended go with no blocking/high-severity defect. It directly viewed the approval pair, initial/scrolled table and festival captures, and read all 12 image-run final answers. It read the restricted manual annotations and one of the 12 restricted traces, not the other 11. It inspected the package-check log without rerunning those commands.

The review identified a misleading rates answer-key assumption, the duplicate approval warning, and the absence of an actual revise-and-render execution. The rates anchors now allow a supported column-width or row-identification concern while preserving density/units; the report records the duplicate and unexercised revision path. Viewport-versus-image dimensions are explicit in the protocol. Unknown fixture query values now display an error rather than silently selecting another scenario. Valid scenario markup/styles and all runtime instructions are unchanged by these test/report corrections. A final browser check reproduced all four capture PNG hashes from the current source and verified both the explicit unknown-case error and the default case. Both checks passed; the original image inputs still match the current valid views.

`expected_method` is structural fixture metadata, not a machine-observed behavior field. Method following was assessed by reading the actual responses. The approval pair changes order, width, type scale and fills together; it demonstrates the combined relationship, not the contribution of any one change. The existing visual module already requires repair outcomes; the suggested repetition in the general Revise delivery row was left out to avoid duplicating that authority. The successful restricted checks and the image findings/limitations remain separate conclusions.

## Package validation

`npm test` passed: 54 rules, 161 applicability fixtures, 66 execution scenarios, 43 behavior scenarios, four visual scenario definitions, eight installer tests and ten Python unit tests. Skill Creator validation and `git diff --check` passed. Package dry-run inspection confirmed the module, fixtures and report are included while local `.orch` evidence is excluded; it is separate from model/rendered validation.
