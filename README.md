# anti-slop

A review-and-editing skill for AI assistants that audits or revises **writing in any language** and **product UI** for generic, inflated, repetitive, fabricated, inaccessible, or nonfunctional patterns — without flattening the author's voice or turning subjective taste into a defect.

It is guidance for careful editing, **not an AI detector**. It never attributes authorship, never invents replacement facts, and distinguishes proven defects from heuristic warnings and optional taste.

Works with any agent harness that supports the `.agents/skills/` convention (tested with [omp](https://github.com/can1357/oh-my-pi) and codex). The skill folder is self-contained — copy it anywhere.

## Why

AI-assisted text drifts toward a recognizable median: stacked praise, uniform sentence rhythm, sycophantic openers, tacked-on significance, fake metrics, interchangeable card grids. Most advice about this is either a word blacklist (tells drift and get trained away) or a detector (unreliable). This skill takes a third path:

- **Rules describe reader-serving quality**, not model fingerprints. A pattern is a review cue, never evidence of who wrote it.
- **Evidence registry**: every rule cites dated sources with stated limits — including *negative* results (the em dash is a bad tell; "delve" retired; short-sentence cadence was refuted in favor of uniform cadence).
- **Findings come in three classes**: 확실한 오류 (proven error), 휴리스틱 경고 (heuristic warning), 취향 제안 (optional preference). Only the first is a defect.

## Install

One command installs (or updates) into every detected agent harness — omp (`~/.agents/skills`) and codex (`~/.codex/skills`); if neither exists, omp's is created:

```sh
npx @a7garden/anti-slop
```

Also works straight from GitHub without the npm registry: `npx github:a7garden/anti-slop`.

Options: `-- --omp`, `-- --codex`, `-- --all`, `-- --dir <path>` (extra target), `-- --list`, `-- --uninstall`. **Update** by re-running the same command; the copy is replaced with the latest version.

Manual alternative — the skill folder is self-contained, so plain copying works everywhere:

```sh
# omp
cp -R .agents/skills/anti-slop ~/.agents/skills/

# codex
cp -R .agents/skills/anti-slop ~/.codex/skills/
```

No runtime dependencies. Python 3 is only needed for the offline validator.

## Use

- `anti-slop audit <target>` — ranked punch list, no edits.
- `anti-slop revise <target>` — bounded edits + change summary.
- no verb — the profiles apply while drafting.

Paste the text or name the screen/component. Ask before broad rewrites. The user's brief, evidence, and existing product conventions take priority over skill defaults.

## What's inside

```
.agents/skills/anti-slop/
├── SKILL.md                     # invocation, workflow, safeguards
├── references/
│   ├── rules.md                 # 53 rules (W01–W29 writing, D01–D24 design) with sources, exceptions, automation limits
│   ├── writing-profile.md       # Korean profile
│   ├── english-profile.md       # English profile
│   ├── design-profile.md        # UI review profile
│   └── before-after.md          # grounded rewrite examples
├── tests/
│   ├── regression_cases.json    # 95 fixtures: expected findings + intentional non-findings (Korean & English)
│   └── validate_package.py      # offline structure/fixture validator
└── extensions/                  # optional, inactive hook sample
```

**Languages**: the rule classes are language-agnostic; Korean and English profiles add register-specific cautions. For other languages, apply the rules directly and mark language-specific judgments as lower confidence.

Example rules: significance inflated beyond the facts (W05), vague authority ("연구에 따르면" / "studies show", W06), monotone cadence (W14), assistant scaffolding in deliverables ("좋은 질문이네요!", "Hope this helps!", W16), interpretation appended without evidence (W27), qualifier density erasing information (W28), calqued phrasing replacing plain wording (W29), fabricated testimonials or metrics (D05/D06), reflow and contrast failures (D12/D15).

## Validation

```sh
cd .agents/skills/anti-slop && python3 tests/validate_package.py
```

Checks package structure, rule metadata, fixture coverage, and link integrity. It does not measure model judgment.

## Limitations

- Not a detector; tells vary by model version and system prompt and drift over time. Sources are re-checked and the registry carries each one's scope.
- The rules are editing prompts, not a classifier. Heuristics and preferences must never block or silently rewrite a sound choice.

## Sources

The evidence registry in [rules.md](.agents/skills/anti-slop/references/rules.md) cites, among others: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), excess-vocabulary corpus studies ([arXiv:2406.07016](https://arxiv.org/abs/2406.07016)), a slop-measurement taxonomy ([arXiv:2509.19163](https://arxiv.org/abs/2509.19163)), the [sloptells](https://sloptells.com/) measured-tell catalog, W3C WCAG 2.2 guidance, and practitioner design references.

## License

[MIT](LICENSE)
