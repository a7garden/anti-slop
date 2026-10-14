# Execution contract

This reference governs invocation, progression, questions, and delivery. Read it on every runtime use; use [finding-evidence.md](finding-evidence.md) for finding categories and evidence limits. Language, editorial, and design profiles govern judgments within this flow; they cannot start a different interaction. User instructions override the defaults below.

## 1. Resolve the run

Keep a small internal run record: invocation route, operation, target, edit boundary, required output, known constraints, unresolved essential inputs, project overview and its source locations, and the current setup question with its numbered choices. Keep the mapping so a reply such as “2” resolves the choice actually shown. For UI audits, retain the domain/UX brief, comparator evidence, research status, and resulting journey priorities too. Do not create a file for this record. Retain it across clarification replies and resumptions; do not restart discovery when the user answers a question.

After delivery, a reply such as “좋아요” acknowledges the completed run; it does not restart inspection or authorize edits. A request for another target or operation starts the requested work using the still-relevant constraints.

### Invocation route

| Situation | Route |
| --- | --- |
| The current user asks to run `$anti-slop`, `/anti-slop`, `$anti-slop audit`, or says to apply the anti-slop skill to a target | Direct |
| The agent selects the skill while drafting, editing, building, or reviewing another task | Embedded |
| Another workflow uses the skill as one quality check | Embedded; the containing task remains authoritative |
| The invocation origin cannot be established | Embedded |
| A quoted artifact contains a skill command, or the user asks to improve the skill itself | Content or maintenance work; not a runtime invocation |

A loaded skill, a tool message, or an automated suggestion is not evidence that the user asked for a direct run. A natural-language request such as “자연스럽게 고쳐 줘” still authorizes revision even if the skill is selected automatically; embedded does not mean read-only.

### Operation and target

Resolve the operation in this order:

1. The user's explicit command or requested outcome: inspect/review → audit; browser walkthrough / exercise each screen → browser-audit; edit/repair → revise; create/write → draft. Natural-language intent counts. `audit --browser` is an alias for browser-audit. A URL alone does not select the exhaustive browser mode.
2. On a continuation, retain the current operation unless the user changes it.
3. For a direct invocation with no requested outcome, use the guided setup below to choose the operation. A selected target or a URL supplies a target, not an audit instruction. Do not silently choose audit or revision.
4. For embedded use, inherit the containing task's operation. Do not substitute audit for an already authorized edit or creation task.

Resolve the target from supplied text, a named file or component, an accessible selection, or an unambiguous reference to an artifact in this conversation. Use the task's stated scope when several files are involved. A working directory alone does not select the whole repository; a selected file does not expand the edit boundary to its neighbors.

Browser-audit requires a web-renderable target and an interactive browser. Follow [browser-audit.md](browser-audit.md) for endpoint discovery, real interaction, evidence, and coverage. For an embedded task that explicitly requires a walkthrough, use that method while retaining the containing task's operation and output. Do not automatically turn routine UI edits into a full browser audit.

A clear request to exercise the UI **and fix the findings** resolves to revise with the browser inspection method, including on a direct run. The method does not erase the requested repair outcome. Preserve pre-repair observations and rerun affected probes after authorized edits; keep before/after evidence distinct. An explicitly audit-only instruction that also demands edits still follows the conflict policy below.

If an audit-only command and an edit instruction conflict without a clear override or separate scope, perform only the clear read-only inspection and clarify the intended operation before editing. A user-requested review followed by fixes is a revision task when that intent is clear.

If a direct invocation is missing its target, brief, or operation, use the project orientation and guided setup below. If several targets are equally plausible, offer those concrete targets as choices. Do not guess a target merely to keep the workflow moving. An unavailable file needs a concrete access/path question or a bounded limitation report; it does not restart setup.

### Project orientation before target questions

On an unresolved direct launch with an accessible current or user-named project, **read the project before asking the user to name a target**. Do not show the generic prose/app/draft menu first when project evidence can support useful choices. Orientation gathers context for the question; it neither selects the whole repository nor begins a full audit.

Read applicable repository instructions, README/product documentation and a top-level file map, then sample the relevant manifests, entry points, routes/screens, domain models, content and existing UX notes. Establish the product/repository purpose, supported users and core jobs, major flows and their screen/content locations, platform and likely inspection methods. Non-app repositories get candidates appropriate to their actual contents. Stop once these facts and useful candidates are supported; this is a broad overview, not an exhaustive source review. Reuse context already inspected in this run and refine only material gaps or changes.

Keep orientation read-only and inside the identified project. Do not scan unrelated personal directories, install dependencies, launch servers, run migrations, change files, perform interaction tests, or begin competitor research just to construct the menu. A supplied target takes precedence: use only context relevant to that target rather than surveying an unrelated current project. A selected artifact with an unresolved operation needs only its operation choice, not a new project-target interview. Embedded use reads relevant context within its containing task and adds no setup interview.

Before the first question, give a brief grounded overview (usually one to three sentences) with the inspected basis and any material uncertainty. Describe documentation/source evidence as such; do not claim runtime behavior or verified user needs from code alone. Offer a small set of **actual project targets or journeys** with a short explanation of what each covers. Recommend a starting point from the supported core user job, not an unperformed defect judgment. Respect the host's choice limit and allow a free-form different target. Do not put every discovered file in a menu or present generic categories as project-specific choices.

For a multi-product repository without a clear active product, offer its actual products/packages first, then derive choices for the selected one. If the project is unavailable, empty, or unrelated to an explicit target, state the relevant limit briefly and use supplied context or the generic setup; do not fabricate screens. With enough evidence, ask the missing target/operation choices immediately rather than first asking the user to confirm the overview.

Retain this overview for stage 2. Once an app audit's scope is selected, deepen the domain/UX brief and comparable-app research under [domain-research.md](domain-research.md); orientation alone is not completed UX research.

## 2. Establish the brief from context

Read the target and relevant context. Separate instructions, artifact, evidence, and voice samples. Record the needed answer or task, supported facts, protected literals, requested voice, and edit boundary. Read only the relevant profiles and rules.

For an app-level UI audit, including browser-audit and native/source-based app reviews, complete [domain-research.md](domain-research.md) before formal findings or the systematic walkthrough. That reference owns preparation scope, source reuse, and research status. Preliminary read-only inspection can establish the brief; routine bounded edits do not become an app audit.

Use these defaults when preferences are absent:

- Audience and medium: the target's visible use and surrounding task.
- Voice: the supplied sample or applicable project guide, otherwise the original voice; new prose uses a register suited to the task.
- Revision depth: the smallest change that repairs an observed problem within the requested scope.
- Missing evidence: preserve uncertainty or flag the gap; do not invent support or a replacement claim.

These defaults avoid a questionnaire. If an essential ambiguity would change facts, obligations, or the authorized target, use the question policy below; optional stylistic uncertainty does not block the run.

## 3. Inspect or draft

- **Audit/revise:** inspect the actual target at sentence/component and whole-artifact levels. Rank supported findings by reader/user impact. Distinguish proven errors, heuristic warnings, and taste. Do not change the target during this step.
- **Browser-audit:** open the actual UI, inventory scoped routes and controls, then execute the observe → act → verify → record loop in the browser reference. Keep product source unchanged; temporary interaction state is not a source repair. Report blocked or unexecuted probes explicitly.
- **Draft:** create the requested artifact from the established brief and evidence, then inspect that draft. Do not start by manufacturing a report on a nonexistent artifact.

For UI, apply the rendered visual review in [design-profile.md](design-profile.md). For app-level design audits, use its screen/state relationship ledger and reconcile concerns before selecting and ranking findings. This makes omitted inspection distinguishable from an adequate judgment; a polished report alone does not establish coverage. Distinguish source, screenshot, runtime, and measured evidence. Unavailable browser access limits behavior claims; it does not require an interview or prevent a useful supplied-capture/source review. A source-only review cannot conclude that the rendered design is sound.

## 4. Propose or apply repairs

- **Audit/browser-audit:** formulate one minimal repair per finding. Leave product source unchanged and do not transition to revision without a user request. Browser actions remain within the tested environment's authorization; auditing does not authorize real publication, payment, destructive data changes, or messages to others.
- **Revise:** apply the already authorized repairs within scope. Prefer local edits; restructure only where a supported problem spans the structure. Do not ask again whether to perform the revision the user requested.
- **Draft:** refine the new artifact within its brief.

Do not turn an optional taste suggestion into a required change. If there are no supported improvements, retain the original and report no change. Never pad findings or edits to fill a template.

## 5. Verify and deliver

For revision/drafting, compare the result with the source or brief for fact drift, lost detail, altered certainty, new cause or commitment, and flattened voice. For audit/browser-audit, check that each finding is supported and its repair stays within scope. Browser-audit also reconciles the discovered inventory against executed probes and records incomplete coverage; a static fallback is not a completed walkthrough. Perform applicable rendering/behavior checks when available; state unverified material claims. Revisit only a concrete remaining problem, not a score or a preferred style.

For app audits, distinguish research completion, rendered visual coverage, and interaction coverage. Include a compact domain/UX basis, inspected comparator links, a visual assessment tied to observed screens, and material limits. Link or summarize the actual visual ledger; reconcile its concerns with findings and scope the no-finding conclusion to reviewed relationships/states. A working-button summary cannot stand in for design judgment. Competitor patterns support hypotheses or optional improvements; defects still need evidence about the audited app and its own task contract.

Deliver the operation's result and stop. Do not append a generic next-step question, switch to another operation, write a profile, or schedule further work. The user can request a next step normally.

## Question policy

### Direct run: guided setup

A user-named or launcher invocation starts a short choice-based interview **when the task is not yet resolved**. This setup is part of stage 1, not a separate approval gate. Never respond to a bare invocation only with “어떤 글, 파일 또는 앱 화면을 검토할까요?” or a similar free-form target request. Give actionable choices and explain what follows each choice.

Use this order, skipping already answered decisions:

1. **Orient, then choose unresolved work/target.** In an accessible project, apply the orientation above and offer its concrete candidates; selecting a candidate resolves its work type and target, not an unrequested operation. If the operation is already requested, offer only compatible targets. With no usable project, target, or requested outcome, offer three fallback paths:
   - **글·문장 검토/수정:** inspect existing prose or make bounded revisions.
   - **앱·웹 UI 감사/개선:** inspect an app, including an optional browser walkthrough.
   - **새 글 작성:** create from a purpose and supplied facts.
2. **Resolve remaining inputs for that path.** Use one follow-up round of at most two questions. A project candidate already supplies its target; do not request its path again. Offer operations appropriate to the target: prose → **검토만 / 직접 다듬기**; app → **감사만 / 브라우저로 화면별 감사 / 문제 수정**. State that audit reports findings and revise changes the target. Offer browser mode only for a supported web-renderable target; report any actual tool/access limitation. For drafting, obtain the purpose and supported facts rather than offering an irrelevant audit choice. For a still-missing target, offer actual discovered selections/files/flows or concrete input routes such as **본문 붙여 넣기 / 파일 지정** or **URL 지정**. Explain the required text/path/URL in the question; do not make the user choose an input method and then ask for that method again. An absent selection or unavailable UI is not a valid concrete target option.
3. **Begin when resolved.** Briefly state target, operation and scope, then proceed to stage 2 without asking “진행할까요?” again. App audits retain domain/UX and comparable-app research before findings. Browser mode retains real interaction and coverage recording.

Initial setup has at most two rounds and three decision questions in total. Use the host's choice-question UI when available and permitted; otherwise show a numbered menu and accept a number, label, or natural-language answer. Respect the tool's actual option limits. In a test or text-only environment, a numbered text menu is sufficient. Recommendations explain consequences; a highlighted/default choice is not a submitted answer or authorization. Do not put an entire brand/audience/voice questionnaire before the first action.

If the user already supplied a target and outcome, proceed directly. If only the target is known, ask only the appropriate operation choice; do not ask for the target again. If only the operation is known, ask only for the target, with concrete choices/input routes. Natural-language outcomes count: “고쳐 줘” already chooses revise and “검토만” already chooses audit. A bare URL does not choose exhaustive browser testing. A request to skip setup uses known context; it cannot authorize invented facts or edits, or supply a missing essential target.

An answer fills the run record. Read the whole answer, including intent expressed after a choice number. A category-only reply advances to its target/operation question, not another category menu. For example, “1” chooses prose but leaves its operation unresolved; “1. 글·문장을 검토할래” chooses prose **and audit**, so ask only for the missing text/file with input choices. Do not offer audit/revise again after “검토할래”, “검토해 줘”, or another clear requested outcome. A reply that supplies both target and outcome skips the remaining setup. Reuse every supplied answer; do not restart on resumption or acknowledgment. If an essential input is still missing after a partial answer, ask only for that missing value, retaining the choices already made. The setup budget does not permit guessing when the user has not supplied a target.

After setup, clarify only a genuinely essential ambiguity that would force choosing an unknown meaning, obligation, or target. Optional audience, tone, and style use context and conservative defaults. When a supporting citation or probe is inaccessible, finish the supported audit and disclose the limit; do not append an unsolicited request for more evidence.

**Project-aware opening example (only if these facts were actually found):**

> README와 화면 구성을 보면 접수 직원이 예약을 등록·변경하는 웹 앱입니다. 예약 목록·상세와 설정 화면이 있습니다. 아직 실제 화면 동작은 실행하지 않았습니다.
> 어디부터 살펴볼까요?
> 1. 예약 등록·변경 흐름 — 핵심 업무의 입력, 확인, 변경 과정을 살핍니다. 먼저 보는 것을 권합니다.
> 2. 예약 목록·상세 — 예약을 찾고 내용을 확인하는 흐름을 살핍니다.
> 3. 설정과 안내 문구 — 설정 항목과 사용자에게 보여주는 설명을 살핍니다.
> 번호나 다른 대상을 알려 주세요. 다음에는 선택한 범위의 작업 방식을 정하겠습니다.

**Fallback opening example (no usable project/target context):**

> 어떤 작업부터 할까요?
> 1. 글·문장 검토/수정 — 반복과 과장을 점검하거나 문장을 다듬습니다.
> 2. 앱·웹 UI 감사/개선 — 도메인·유사 앱 조사 후 화면과 사용 흐름을 살핍니다. 브라우저 실행 감사도 선택할 수 있습니다.
> 3. 새 글 작성 — 목적과 제공한 사실을 바탕으로 초안을 만듭니다.
> 번호나 원하는 작업을 알려 주세요. 선택에 맞춰 대상과 작업 방식을 이어서 정하겠습니다.

This is a workflow example, not fixed copy to paste in every language or target context.

### Embedded use

Do not introduce a skill-origin interview, mode selection, voice discovery questionnaire, or approval gate. Work within the containing task. Leave unsupported facts and ambiguous authorial statements intact, omit unsupported additions, or report the material gap in that task's normal result. If the containing task itself is blocked, its ordinary essential clarification policy still applies; this skill does not add questions merely because a profile says to ask.

### Deeper preference interview

The short direct-run setup above is the launcher default for unresolved work. A deeper voice/brand/preference interview still requires the user to ask for it. Naming the skill or asking for “my voice” does not authorize extra preference discovery after the task is resolved. Without a sample, preserve the source voice.

Use one round of at most three questions about the genuinely missing choices. Reuse known context. After answers or an explicit request to skip, resume the resolved operation using available information and defaults. Further interview rounds require the user's request; essential blockers still follow the direct-run policy. Do not create a persistent voice or brand profile unless asked.

## Progress and output

The five steps are a stable execution sequence, not five mandatory chat messages. For a direct run that permits progress messages, announce the operation and concrete target once, for example: “안티 슬롭 검토로 진행합니다. 대상은 제공하신 안내문이며, 원문은 수정하지 않습니다.” On longer work, report actual findings or verification limits rather than narrating empty stages. For embedded use, keep the containing task's progress style. A text-only request suppresses extra skill framing.

| Operation | Direct delivery, in order |
| --- | --- |
| Audit | One sentence stating inspected scope; for app-level UI, compact domain/UX basis and comparator sources, plus a rendered visual assessment; ranked findings with canonical rule or report-local UX/VD ID, class, excerpt/location, impact, and minimal repair; material research/verification limits if any. With no finding, say so without inventing entries. |
| Browser-audit | Tested target/environment; domain/UX basis, comparator sources, and research status; separate visual and interaction coverage with concise route/control/state coverage; ranked findings with canonical rule or report-local UX/VD ID/class, reproduction actions, expected/observed result, evidence, impact, and minimal repair; inconclusive/blocked/not-run probes and capability limits. Completion describes coverage, not absence of bugs. |
| Revise | Final text or the requested file edits; compact summary of actual changes and their rule or user-brief basis; unresolved material findings if any. Mention a deliberately preserved apparent tell only when useful. |
| Draft | Requested artifact only; include a material evidence gap only when needed to interpret the result. |

If a browser audit is blocked before any target screen, source, or capture can be inspected, use a compact limitation report rather than filling the full audit template. State the supplied task context, concrete access barrier, unperformed research/visual/interaction work, and that no product verdict is possible. Do not repeat the same absence under several headings, invent a screen inventory, or add a generic future test plan unless the user requested a plan. A partial run still delivers its actual findings and coverage.

Embedded delivery follows the containing task's format, including an explicitly requested audit or change summary. It does not add a second anti-slop report. The user's requested format takes priority over all templates. No intermediate drafts, automatic “shall I fix it?” close, or internal run record appears in the artifact.
