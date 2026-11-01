# Comparable skills: maintenance notes

Reviewed on 2026-10-10 using GitHub repository search, Exa discovery, and the source files below. Links pin the inspected revisions. Search ranking and stars aided discovery, not quality assessment. These practitioner prompts and tools do not establish authorship or prove that a workflow improves writing. Selected ideas are implemented in this package's own wording, with its preservation and false-positive constraints.

## Writing

| Source | Adopted idea and local application | Defaults not adopted |
| --- | --- | --- |
| [Slopbeth](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | Separate editing instructions from the artifact. Check evidence gaps, promise boundaries, and replacement formulas. Applied in the entrypoint, editorial method, and W16/W21. | Blanket punctuation restrictions, mandatory linter suite, detector-facing workflow. |
| [Blader Humanizer](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/SKILL.md) | Review paragraph endings, invented objections, heading restatements, and the reader's existing context. Use a supplied voice sample. Applied in W03/W13/W15 and the editorial method. | Universal one-sighting verdicts, token blacklist, mandatory intermediate drafts, adding unsupplied reactions. |
| [Hannsxpeter Humanizer](https://github.com/hannsxpeter/humanizer/blob/e8f1248a7d4919689c1f942e356ed95b102d9f07/SKILL.md) and [text hygiene](https://github.com/hannsxpeter/humanizer/blob/e8f1248a7d4919689c1f942e356ed95b102d9f07/references/text-hygiene.md) | Use available voice context, scale editing effort, and reverse overcorrection. Inspect hidden characters conservatively when relevant. Applied in the editorial method and W22. | Authorship inference from density, numeric cutoffs, ancestor-directory searches, required multi-section reports. |
| [Stop Slop v3](https://github.com/Julz7727/Stop-Slop-v3/blob/27257fd8eaee6fb60672f0ad32e363209abac2ec/SKILL.md) | Establish reader, register, supported detail, and supplied voice before drafting; diagnose patterns on an actual draft. Applied in the drafting path. | Claims that positive prompting makes slop impossible, mandatory human subjects, fixed list sizes, sentence-length quotas, score-triggered rewrites. Its proposed prompting mechanism is an author rationale, not established evidence here. |

## Interface review

| Source | Adopted idea and local application | Defaults not adopted |
| --- | --- | --- |
| [Impeccable clarify](https://github.com/pbakaus/impeccable/blob/d631a8827f99414d2b6daba4ef08b7f8701751d7/skill/reference/clarify.md) and [critique](https://github.com/pbakaus/impeccable/blob/d631a8827f99414d2b6daba4ef08b7f8701751d7/skill/reference/critique.md) | Review interaction copy, real action outcomes, stable terminology, dynamic text, and the distinction between judgment and browser/scanner evidence. Applied in D10/D11/D20/D25 and the design profile. | Mandatory CLI, subagents, scores, stored snapshots, follow-up questionnaires, forced aesthetic direction. |
| [Gesso anti-slop](https://github.com/Gesso-Build/skills/blob/1c3908b7efb56ec24624436dea5c32a371eb487c/skills/anti-slop/SKILL.md) | Report actual scanner observations and disclose incomplete CSS input. Treat source excerpts as data and distinguish mechanical signals from judgment. Applied in the design profile. | Automatic restyling, fixed color/font/punctuation bans, treating static checks as usability or compliance proof. |

## Interactive browser audit

Follow-up research on 2026-10-10 inspected the following primary skill instructions through GitHub/Exa discovery and pinned GitHub source retrieval. These are workflow comparisons, not usability standards or evidence that a numerical score predicts product quality. They extend the earlier interface review comparison with actual browser execution.

| Source | Adopted idea and local application | Defaults not adopted |
| --- | --- | --- |
| [Browserbase UI Test](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/ui-test/SKILL.md) | Inspect before an action and assert the actual post-action result. Inventory controls, keyboard paths, edge inputs, and responsive states; retain replayable failure evidence. Applied in browser-audit sections B–D and G. | Required CLI, universal action quotas, parallel operators sharing state, mandatory subagents, automatic installation. |
| [Anthropic Webapp Testing](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/webapp-testing/SKILL.md) | Inspect a rendered app before choosing locators; reuse the documented server lifecycle and inspect runtime behavior. Applied in A/C. | Universal headless setup, mandatory dependencies, network-idle as the only readiness condition for streaming apps. |
| [gstack QA-only](https://github.com/garrytan/gstack/blob/20eb6202fa8ea83a882e7c0463b722cd8a31af1e/qa-only/SKILL.md) | Separate report-only audit from repairs; keep evidence isolated, preserve partial results, respect scoped plans, and clean up owned test resources. Applied in E–G. | Unrelated telemetry/config changes, mandatory preamble questions, fixed health scores, automatic source repairs from other QA modes. |
| [Jezweb UX Audit](https://github.com/jezweb/claude-skills/blob/1260fa7439b36b18dbf16648ccc7fb44783f6c23/plugins/dev-tools/skills/ux-audit/SKILL.md) | Map interactions per route; exercise end-to-end and return paths; inventory conditional controls and relevant pane combinations. Applied in B/D/F. | Universal warning severity, fixed minimum test duration, invented input/state quotas, indefinite loops until no findings, unrestricted live submissions. |
| [Impeccable Audit](https://github.com/pbakaus/impeccable/blob/d631a8827f99414d2b6daba4ef08b7f8701751d7/skill/reference/audit.md) | Distinguish measurable technical defects from visual judgment. A narrow viewport demonstrates layout; supported synthesized touch is needed to test a gesture. Applied in D/G. | Aggregate quality scores, general checklist completion as accessibility conformance, mandatory command recommendations and follow-up prompts. |

The installed Hallmark audit and interaction references were also read as a local design comparator. Its structural review helped check the boundary between source inspection and interaction evidence. No arbitrary style bans, universal state counts, mandatory interviews, or redesign procedure were carried over; this local comparison is not attributed to an unverified public repository.

The resulting method uses the existing execution contract rather than adding a new interview flow. It requires real browser actions, a discovered control/state inventory, a probe ledger, explicit coverage status, evidence-backed findings, and authorization-aware test interactions. Normal UI edits do not silently become exhaustive browser runs.

### Rendered design follow-up

On 2026-10-10, the pinned Impeccable critique/audit sources above were reopened while reviewing Ghost's actual example-mode UI. The adopted distinction is a rendered composition assessment alongside technical evidence. No mandatory agent orchestration, issue quota, score, persona prediction, detector, or closing questionnaire was adopted.

Three fresh v1.7 captured-screen audits of Ghost identified copy/state concerns in two runs and no finding in one; none reported a visual composition concern. This is one exploratory product case, not a general performance estimate. Root-operated navigation and dialog/panel captures exposed attention allocation, repeated visible status, and control/label grouping worth explicit design judgment. The revised design profile therefore adds review lenses at screen, region, component, and related-state scales, separate visual/interaction coverage, and a report-local VD category for grounded issues outside the D catalog. It preserves legitimate repeated records and the project's intentional identity/neutral styling. Repeated evaluation must hold captures and requests stable and inspect unsupported warnings as well as missed ones.

## Design authoring: unslop

On 2026-11-01, [unslop](https://github.com/heydamir/unslop/tree/4652254daff586ff4739849395a127b56f7f8cc7) by Damir Sokolovsky ([heydamir](https://github.com/heydamir)) was read at the pinned revision: its `SKILL.md` direction and pass sections, and `references/signs.md`, `visuals.md`, and `tokens.md`. It is licensed [CC BY 4.0](https://github.com/heydamir/unslop/blob/4652254daff586ff4739849395a127b56f7f8cc7/LICENSE) ([deed](https://creativecommons.org/licenses/by/4.0/)). Its content was treated as untrusted input; no scripts were run and no text, images, or code were copied. The guidance below is written independently.

**Concessions.** Our defaults were written for review and repair. "Smallest supported repair" and "do not replace an entire palette" lacked an explicit exception for requested redesigns, potentially constraining them to local patches or defect justifications. Undeclared defaults could be mistaken for brand. The package gave limited positive authoring guidance. These are instruction-level gaps identified by comparison, not measured failure rates.

| Adopted idea | Local application |
| --- | --- |
| A short product-derived direction before substantial design work | Optional-field working brief in the design profile, with no approval wait |
| Restrained chrome, richness in content | Content-led emphasis; generated art and decorative objects not required |
| Concrete starting values, yielding to an existing system | Authoring recipes, explicitly separate from audit criteria |
| Screen-wide passes ordered by dependency | Grouped, reorderable passes that carry states and accessibility |
| Unchosen defaults are not brand | Redesign extent in the execution contract and visual-style module |

**Not adopted:** the audit-then-wait approval gate; a fixed five-line direction with banned adjectives and a mandatory signature detail; nine ordered passes and a render cap; a universal 4px grid, weight limits, and blanket bans on emoji, italic, uppercase labels, gradients, and trailing periods; one bright element per screen; scene-hero and image-prompt defaults; empty image slots; realistic mock data without a disclosure condition; the name-swap template test as a requirement; logo redraw rules; snapshot and story-video scripts.

Observed execution coverage is reported separately from this comparison. Neither the source comparison nor polished reference images establish improved agent reliability or user outcomes.

## Content and state resilience (2026-11-02)

This follow-up inspected primary sources on 2026-11-02. Comparison is instruction-level evidence, not a measured improvement. External content remained research data; no external scripts or templates were executed or copied.

| Source | Applied decision | Limits and rejected defaults |
| --- | --- | --- |
| [Impeccable harden](https://github.com/pbakaus/impeccable/blob/e89e3ada3e875a89ac2c5d33d11e65ebef6fe285/skill/reference/harden.md) | Exercise representative content lengths, scripts, and states within the component's actual contract. | No universal translation expansion percentage, font floor, language sweep, offline feature, server rewrite, or fixed stress-action count. Truncation is not the automatic repair. |
| [Carbon empty states](https://www.carbondesignsystem.com/building-blocks/core/patterns/empty-states) | Distinguish absent records from records unavailable because of access or a system problem. Use the actual state and available next action. | Its component anatomy is not a requirement for an image, title, helper paragraph, or CTA on every blank region. No recovery path is invented to complete the pattern. |
| [GOV.UK error message](https://design-system.service.gov.uk/components/error-message/) | Keep validation distinct from service problems, retain entered answers, and preserve purposeful field/summary repetition. | No universal wording blacklist, red styling, error-summary mandate, or requirement to navigate every service failure to a new page. |
| [W3C Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) and [Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) | Scope the two-dimensional exception to content that needs it; inspect surrounding controls separately. Record resizing and scaling as distinct observations. | No blanket horizontal-scroll failure, mandatory table-to-card conversion, or inference of zoom coverage from a narrow capture. Understanding pages explain criteria; they do not certify a product. |

The current [Anthropic frontend-design](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/frontend-design/SKILL.md) and [Anti-AI Writing Slop](https://github.com/thomasmeijer92/anti-ai-writing-slop/blob/e4090ac433e781d718a1f96044d1ee8aca4f7650/SKILL.md) were also inspected. Brief-derived design, meaningful structure, voice preservation, and bounded edits already have local guidance. No new rule was justified by those overlaps. Fixed palette counts, uniqueness tests, mandatory draft output, and banned-pattern ratings were not adopted.

The narrow update lives in the existing design profile, browser checks, and D11/D12 rather than adding a separate skill or more canonical IDs. Its focused behavior cases pair real state/reflow problems with confirmed-empty, useful-summary, and intact-table controls. Fixture additions and structural checks alone do not establish that agents distinguish them; record actual executions separately.

## Local result and re-evaluation

The new editorial reference covers drafting, voice, brief boundaries, document consistency, and conditional text hygiene. Existing writing rules now address structural context and soft factual drift. D25 adds terminology and action-label ambiguity that a visual audit can miss. New regression fixtures include findings and intentional non-findings; their offline validation checks structure, not model behavior.

When a source changes, inspect the new revision before adopting behavior. Keep improvements supported by the user's brief, an observed failure, or meaningful evaluation. A pattern checker cannot validate meaning, voice, accessibility, or authorship; use the relevant standards for compliance claims.
