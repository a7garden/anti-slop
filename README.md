# anti-slop

A modular quality framework for prose and product interfaces. It drafts, audits, and revises sentences, UI copy, layout, typography, visual style, color, imagery, and interaction while preserving meaning, voice, and product identity.

It is not an AI detector. A word, punctuation mark, palette, card, or gradient is a review cue, never proof of authorship or poor quality.

## Quality principles

- Give the reader the needed answer and the user a clear task path.
- Avoid unnecessary secondary labels and explanatory text. Let layout carry grouping and hierarchy; preserve meaningful labels, conditions, accessible names, units, and recovery.
- Check style and color against the actual brief, content, emphasis, and state. Do not replace every identity with a neutral theme or ban a color/font by default.
- Preserve facts, uncertainty, attribution, conditions, voice, and protected literals. Never invent proof, features, experiences, causes, or commitments.
- Separate demonstrated errors, contextual warnings, optional taste, and unverified gaps. Class and severity are independent.
- Report one underlying issue once, with one primary rule, evidence, consequence, and a bounded repair. Preserve clean material.

## Install

Works with harnesses supporting `.agents/skills/`, including omp and Codex. The folder is portable and has no runtime dependencies.

```sh
npx github:a7garden/anti-slop
```

The installer updates every detected harness (`~/.agents/skills`, `~/.codex/skills`); if neither exists, it creates the former. Options:

- `-- --omp`, `-- --codex`, or `-- --all` select known harnesses.
- `-- --dir <path>` selects only that destination unless combined with a harness flag.
- `-- --list` previews destinations without filesystem changes.
- `-- --uninstall` removes selected installations.

Re-running the installer replaces the active folder and retains the previous copy, including custom and obsolete files, at `../anti-slop-backups/update-*/anti-slop`. It prints the backup path; intentionally reapply any customizations. Manual copying also works but merges into an existing folder.

## Use

Send instructions in agent chat; the packaged executable only installs the skill.

- `$anti-slop audit <target>` — inspect and propose repairs; leave source unchanged.
- `$anti-slop browser-audit <web target>` — operate the scoped UI and record actual results and coverage. `audit --browser` is an alias.
- `$anti-slop revise <target>` — apply authorized bounded edits and verify them.
- `$anti-slop draft <brief>` — create the requested deliverable.

A request to exercise and fix a UI uses revision with the browser method. A URL alone provides a target, not an operation. Ordinary component or copy work does not become a whole-app audit.

For an unresolved direct launch, the agent reads enough of an accessible project to offer grounded target choices. It asks only missing target/operation questions, with at most two setup rounds and three decision questions. At the limit, it retains known choices and waits for missing input. Complete requests proceed immediately.

Embedded use follows the containing task without another interview, report, or approval gate. The user's explicit scope and output format take precedence. Internal instructions are English; deliverables follow the requested language, with Korean and English examples retained where they test language-specific decisions.

## Framework modules

One entrypoint routes to relevant references instead of loading every checklist or duplicating workflows across separate skills.

| Module | Authority |
| --- | --- |
| [Shared quality framework](.agents/skills/anti-slop/references/quality-framework.md) | Scope, precedence, economy, truth, voice, and stopping discipline across media. |
| [Execution contract](.agents/skills/anti-slop/references/execution-contract.md) | Routing, short setup, continuation, five-stage progression, edit boundaries, and delivery. |
| [Editorial method](.agents/skills/anti-slop/references/editorial-method.md) | Drafting, source/brief separation, sentence/document review, translation, and final meaning check; [Korean](.agents/skills/anti-slop/references/writing-profile.md) and [English](.agents/skills/anti-slop/references/english-profile.md) profiles supply language cautions. |
| [Interface composition](.agents/skills/anti-slop/references/design-profile.md) | Screen/region/component relationships and a ledger for priority, association, redundancy, style/color, and fit/craft. |
| [Visual style and color](.agents/skills/anti-slop/references/visual-style.md) | Palette roles, accents, typography, surfaces, identity, state/theme behavior, and bounded styling repairs. |
| [Domain and UX preparation](.agents/skills/anti-slop/references/domain-research.md) | Grounded jobs/journeys and inspected comparable-app evidence before app-level audits; bounded work stays bounded. |
| [Browser audit](.agents/skills/anti-slop/references/browser-audit.md) | Observe, act, verify, record; scoped inventory, coverage, safe test authority, and cleanup. |
| [Finding policy](.agents/skills/anti-slop/references/finding-evidence.md) | Primary/related rules, report-local content/UX/visual categories, evidence class, severity, and gaps. |
| [Canonical rules](.agents/skills/anti-slop/references/rules.md) | 54 rules: W01–W29 and D01–D25, with sources, detection conditions, exceptions, and automation limits. |

Existing rule IDs remain stable. Report-local `CT`, `UX`, and `VD` categories cover supported issues outside the catalog without forcing a fit. Review guardrails such as arbitrary-style mandates are not themselves product defects.

A rendered visual warning needs an observed relationship and task/brief basis; it does not require a broken button or user study. A screenshot cannot establish persistence, keyboard behavior, an absent accessible name, or measured accessibility conformance. Working controls alone cannot establish good visual design. Research and verification gaps remain explicit.

## Validation

```sh
npm test
```

This checks package structure and links, rule/source metadata, regression and execution fixture integrity, installer replacement/rollback, and the evidence assessor's unit tests. It does not run models or certify semantic judgment.

The current package includes 143 rule-applicability fixtures, 60 execution scenarios, and 28 behavior scenarios. Regression schema 2 distinguishes applicable rule conditions from deduplicated issue decisions; focused cases specify primary/related rules, class, and severity. Fixture data is not execution evidence.

For a portable copy:

```sh
cd .agents/skills/anti-slop
python3 tests/validate_package.py
```

Use [behavior evaluation](.agents/skills/anti-slop/tests/behavior-evaluation.md) for repeated observed executions: at least three fresh runs per scenario, frozen inputs/revision/settings, preserved evidence, and review for unsupported findings as well as omissions. The complete behavior suite requires 84 runs. Focused exercises are reported separately and cannot establish a full-suite pass.

The [browser fixture](.agents/skills/anti-slop/tests/browser-audit-fixture.html) tests actual interactions under the [browser evaluation protocol](.agents/skills/anti-slop/tests/browser-evaluation.md). The [visual fixture](.agents/skills/anti-slop/tests/visual-quality-fixture.html) supports capture-based composition/style/copy exercises; the [style control](.agents/skills/anti-slop/tests/visual-style-control.html) supplies a purposeful serif/gradient contrast case. These fixtures’ static controls do not implement a transaction or persistence.

The [source registry](.agents/skills/anti-slop/references/rules.md) and [comparison notes](.agents/skills/anti-slop/references/skill-comparison.md) record evidence dates, limits, adopted methods, and rejected defaults. Surface habits drift; editorial and practitioner references are not validated authorship classifiers. The [OMP extension sample](.agents/skills/anti-slop/extensions/README.md) remains optional and inactive.
