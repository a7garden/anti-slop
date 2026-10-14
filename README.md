# anti-slop

A review-and-editing skill for AI assistants that audits or revises **writing in any language** and **product UI** for generic, inflated, repetitive, fabricated, inaccessible, or nonfunctional patterns — without flattening the author's voice or turning subjective taste into a defect.

It is guidance for careful editing, **not an AI detector**. It never attributes authorship, never invents replacement facts, and distinguishes proven defects from heuristic warnings and optional taste.

Works with any agent harness that supports the `.agents/skills/` convention (tested with [omp](https://github.com/can1357/oh-my-pi) and codex). The skill folder is self-contained — copy it anywhere.

## Why

AI-assisted text drifts toward a recognizable median: stacked praise, uniform sentence rhythm, sycophantic openers, tacked-on significance, fake metrics, interchangeable card grids. Most advice about this is either a word blacklist (tells drift and get trained away) or a detector (unreliable). This skill takes a third path:

- **Rules describe reader-serving quality**, not model fingerprints. A pattern is a review cue, never evidence of who wrote it.
- **Evidence registry**: every rule cites dated sources with stated limits — including *negative* results (the em dash is a bad tell; "delve" retired; short-sentence cadence was refuted in favor of uniform cadence).
- **Findings come in three classes**: 확실한 오류 (proven error), 휴리스틱 경고 (heuristic warning), 취향 제안 (optional preference). Only the first is a defect. Verification gaps have no defect classification. Supported domain UX and visual design issues outside the 54 rules use report-local UX and VD IDs under the [finding policy](.agents/skills/anti-slop/references/finding-evidence.md).

## Install

One command installs (or updates) into every detected agent harness — omp (`~/.agents/skills`) and codex (`~/.codex/skills`); if neither exists, omp's is created:

```sh
npx github:a7garden/anti-slop
```

Options: `-- --omp`, `-- --codex`, `-- --all`, `-- --dir <path>` (only this target; combine with `--omp`/`--codex` to add them), `-- --list`, `-- --uninstall`. **Update** by re-running the same command; the copy is replaced with the latest `main`. The previous folder, including custom and obsolete files, is retained outside the active skills directory at `../anti-slop-backups/update-*/anti-slop`; the installer prints its path. Customizations must be intentionally reapplied. `--list` has no filesystem side effects.

Manual alternative — the skill folder is self-contained, so plain copying works everywhere:

```sh
# omp
cp -R .agents/skills/anti-slop ~/.agents/skills/

# codex
cp -R .agents/skills/anti-slop ~/.codex/skills/
```

No runtime dependencies. Python 3 is needed for package validation and the behavior evaluator. Manual copying merges into an existing folder; use the installer for replacement updates.

## Use

Send these instructions in the agent chat or use its skill launcher. The terminal executable `anti-slop` is an installer and rejects runtime operations such as `audit`.

- `$anti-slop audit <target>` — ranked punch list, no edits.
- `$anti-slop browser-audit <url or web UI>` (alias: `$anti-slop audit --browser <target>`) — open the UI interactively, visit scoped screens, exercise controls and reachable states, and report evidence and coverage gaps.
- `$anti-slop revise <target>` — bounded edits + change summary.
- `$anti-slop draft <brief>` — the requested deliverable.
- A direct launch with unresolved inputs first orients within an accessible project, then starts a short **choice-based interview** with grounded targets. Without usable project context it offers generic work choices. A clear request to review, write, or edit already determines the operation.

Paste the text or name the screen/component. The user's brief, evidence, and existing product conventions take priority over skill defaults. Requested revisions proceed within their authorized scope; a bare invocation does not authorize a broad rewrite.

**Direct invocation:** the user names or launches the skill. Before asking for an unresolved target, read enough of the accessible project to understand its purpose, users, core flows, and screen/content structure. Briefly explain that basis and offer concrete discovered journeys or artifacts; allow a different target through free-form input. Project orientation is read-only and does not select the whole repository. With no usable project context, offer **글·문장 검토/수정 / 앱·웹 UI 감사/개선 / 새 글 작성** as a fallback. Then collect only the missing target and operation. A known target gets only an operation choice; a complete request proceeds immediately. After selection, the run follows five steps: resolve target and operation → establish the brief from context → inspect or draft → propose or apply repairs → verify and deliver. It announces the resolved operation/target once when progress messages are appropriate. Audit returns scope, findings, and verification limits; revision returns the result and a compact summary; drafting returns the artifact.

**Embedded use:** the agent applies the skill within another task. It keeps that task's scope, progress, and output format. It does not add an interview, mode picker, separate report, or approval step. Loading the skill does not by itself establish a direct invocation.

**Questions:** direct setup uses at most two rounds and three decision questions, with concrete choices rather than an open-ended target question alone. A discovered project-target choice advances only to its missing operation; a fallback category choice advances to its missing target/operation questions; a complete answer starts work without another approval. Deeper tone/brand interviews require a user request; optional preferences otherwise use context. Answers resume the same run. An audit stays an audit until the user asks for revision. Embedded use adds no skill-origin questions; the containing task can still clarify its own essential blockers.

The [execution contract](.agents/skills/anti-slop/references/execution-contract.md) defines routing, continuation, question boundaries, and output precedence.

Drafting starts with the reader, purpose, supported detail, and intended voice. A supplied writing sample takes priority over generic style preferences. Revision checks the whole passage as well as individual words, then checks for meaning drift and over-editing. Clean text can receive no changes.

UI review inspects rendered design as well as interaction. It works from whole-screen hierarchy through grouping/density, typography, component craft, product coherence, and related viewport/state compositions. A grounded visual warning does not need a broken button or a user study: it needs an observed relationship, task/brief basis, likely mechanism, and minimal repair. Working controls alone cannot justify a clean design verdict. Intentional neutral styling, useful repeated records, and generous space can remain sound. Source-only reviews disclose incomplete visual coverage; screenshots cannot establish runtime outcomes or measured accessibility conformance.

App-level design audits retain a screen/viewport/state ledger for **priority, association, redundancy, and fit/craft**. Each check has an observation and a decision: concern, adequate, unknown, or not applicable. All concerns are reconciled with the report before ranking; related examples share a finding rather than inflating the issue count. A coverage summary or artifact link makes omissions visible. Findings are compared across repeated runs by location and mechanism, not by wording or report-local numbering. This reduces silent omissions while preserving legitimate no-finding judgments; it does not promise identical aesthetic opinions.

**Before an app audit:** establish the app's product domain, actual user roles/jobs, domain objects and lifecycle, and core/recovery journeys. Then research comparable apps' relevant UX using inspected sources, and translate that evidence into prioritized audit probes. This preparation applies to app-level browser, native, and source/visual audits. It uses project and existing UX evidence first, without a surprise interview. Comparable features are references, not mandatory parity; defects still require evidence about the target app. Routine component/copy edits stay bounded, continuations reuse applicable verified research, and unavailable or user-prohibited research is reported explicitly. See [domain and UX preparation](.agents/skills/anti-slop/references/domain-research.md).

**Browser audit:** request it explicitly, for example `$anti-slop browser-audit http://localhost:3000`. A natural-language request to open and exercise each screen also selects it. A URL alone supplies a target; the direct setup offers an operation choice. After domain/UX and comparable-app research, the run maps screens and controls, then observes → acts → verifies → records each probe. It covers navigation, dialogs, forms, list controls, reachable error/loading states, keyboard operation, and responsive layouts where tools allow. Repeated rows are sampled explicitly. Missing access, unsafe production actions, and unsupported browser capabilities remain visible as blocked or not-run probes; static screenshots cannot complete this mode. Audit leaves product source unchanged and uses only authorized test interactions. Embedded walkthroughs retain the containing task's operation and output.

See the [browser-audit method](.agents/skills/anti-slop/references/browser-audit.md) for the ledger, completion criteria, and action boundaries.

## What's inside

```
.agents/skills/anti-slop/
├── SKILL.md                     # compact entrypoint, routing links, safeguards
├── references/
│   ├── rules.md                 # 54 rules (W01–W29 writing, D01–D25 design) with sources, exceptions, automation limits
│   ├── writing-profile.md       # Korean profile
│   ├── english-profile.md       # English profile
│   ├── design-profile.md        # rendered visual lenses, interaction, evidence boundaries
│   ├── finding-evidence.md      # canonical/domain UX/visual design categories and evidence limits
│   ├── execution-contract.md    # direct vs embedded runs, stable stages, questions, delivery
│   ├── domain-research.md       # app domain, user journeys, comparable UX research before audit
│   ├── browser-audit.md         # screen/control walkthrough, evidence, coverage, safe test interactions
│   ├── editorial-method.md      # drafting, voice, brief boundaries, long-document checks
│   ├── before-after.md          # grounded rewrite examples
│   └── skill-comparison.md      # writing/design comparisons and browser-audit research
├── tests/
│   ├── regression_cases.json    # 129 fixtures: expected findings + intentional non-findings (Korean & English)
│   ├── execution_cases.json     # 59 invocation, continuation and domain/UX preparation scenarios
│   ├── browser-audit-fixture.html # isolated UI: routes, search, dialog, validation, pending/error, known broken save
│   ├── browser-evaluation.md    # repeatable browser exercises and evidence requirements
│   ├── behavior_cases.json      # 19 realistic scenarios, minimum 3 fresh runs each
│   ├── behavior-evaluation.md   # blind execution and evidence review protocol
│   ├── evaluate_behavior.py     # prepare inputs; assess actual reviewed transcripts
│   └── validate_package.py      # offline structure/fixture validator
└── extensions/                  # optional, inactive hook sample
```

**Languages**: the rule classes are language-agnostic; Korean and English profiles add register-specific cautions. For other languages, apply the rules directly and mark language-specific judgments as lower confidence.

Example rules: significance inflated beyond the facts (W05), vague authority ("연구에 따르면" / "studies show", W06), monotone cadence (W14), assistant scaffolding and leaked editing instructions (W16), invented causes or commitments (W21), interpretation appended without evidence (W27), qualifier density erasing information (W28), calqued phrasing replacing plain wording (W29), fabricated testimonials or metrics (D05/D06), reflow and contrast failures (D12/D15), inconsistent product terms or ambiguous action labels (D25).

## Validation

Run `npm test` from the repository root for package integrity, installer replacement/rollback checks, and behavioral-assessor unit tests. These tests do not invoke models.

```sh
cd .agents/skills/anti-slop && python3 tests/validate_package.py
```

Checks package structure, rule/source metadata, positive fixture coverage for every rule, invocation/domain-research fixture consistency, version consistency, and link integrity. It does not execute the fixture requests or measure model judgment. Repeated observed behavior evaluation follows [behavior-evaluation.md](.agents/skills/anti-slop/tests/behavior-evaluation.md): prepare answer-free requests, run them in an authorized harness, preserve full evidence, and review at least three fresh executions per case. The assessor rejects incomplete suites; its unit tests are synthetic and do not establish skill performance. The skill stores its version stamp in portable `metadata.version`; the installer also reads legacy top-level stamps.

For interactive verification, serve the isolated HTML fixture on loopback and follow [browser-evaluation.md](.agents/skills/anti-slop/tests/browser-evaluation.md). These exercises test actual controls, including a deliberately broken save action. Browser results and capability gaps must be recorded separately from the offline validator.

### 1.8.2 reassessment

- Aligned W19/W20/D05 and their fixtures with the evidence policy: inaccessible verification records or testimonial provenance do not establish fabrication. Actual invented claims remain errors.
- Added cross-language checks for uncertainty, attribution, omitted actors, register, and protected literals; expanded behavior scenarios to cover English revision, drafting, translation, and provenance boundaries.
- Made the UI profile's audit/revise boundary explicit. A fully blocked browser run now delivers a compact limitation report instead of repeated empty sections or an unsolicited test plan.
- Removed exact-prose and example-quota gates from package validation. Structural checks remain separate from observed model behavior; changed wording alone cannot establish a regression.

## Limitations

- Not a detector; tells vary by model version and system prompt and drift over time. Sources are re-checked and the registry carries each one's scope.
- The rules are editing prompts, not a classifier. Heuristics and preferences must never block or silently rewrite a sound choice.

## Sources

The evidence registry in [rules.md](.agents/skills/anti-slop/references/rules.md) cites, among others: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), excess-vocabulary corpus studies ([arXiv:2406.07016](https://arxiv.org/abs/2406.07016)), a slop-measurement taxonomy ([arXiv:2509.19163](https://arxiv.org/abs/2509.19163)), the [sloptells](https://sloptells.com/) measured-tell catalog, W3C WCAG 2.2 guidance, and practitioner design references.

The [2026-10-10 skill comparison](.agents/skills/anti-slop/references/skill-comparison.md) records inspected revisions of Slopbeth, two Humanizer skills, Stop Slop v3, Impeccable, and Gesso, with adopted ideas and rejected defaults. It treats practitioner workflows as examples rather than empirical proof.

The browser follow-up compares Browserbase UI Test, Anthropic Webapp Testing, gstack QA-only, Jezweb UX Audit, and Impeccable Audit. Their pinned sources and design choices are recorded in the same comparison.

## License

[MIT](LICENSE)
