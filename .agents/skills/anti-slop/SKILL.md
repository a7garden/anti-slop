---
name: anti-slop
version: 1.0.1
description: "Audit, revise, or draft writing in any language (Korean and English profiles included) and product UI free of AI slop — generic, inflated, repetitive, fabricated, inaccessible, or nonfunctional patterns while preserving meaning, facts, and voice. Covers requests like 'AI 티 나는 표현 제거', '슬롭 감사', '자연스럽게 다듬어 줘', 'this reads like AI', 'this UI looks AI-generated', 'make this copy less generic'."
metadata:
  short-description: "Careful writing and UI review"
---

# Anti-slop

Use this skill when asked to reduce formulaic AI-style habits in writing or interface design, in any language. It is a review and editing aid, not an AI-origin detector. Read the applicable profiles and only the rules relevant to the target; the canonical rules live in [references/rules.md](references/rules.md).

## Commands

- **audit target**: inspect and return a ranked punch list. Do not edit the target.
- **revise target**: make the requested, bounded edits, then show a concise change summary and any unresolved findings.
- **No verb**: apply the profiles while drafting or implementing; do not force an audit report onto an ordinary creation task.

Choose references by target:

- Prose in any language — headlines, reports, docs, email, posts, release notes, product copy: apply the canonical Writing rules in [references/rules.md](references/rules.md) plus the matching language profile: [Korean](references/writing-profile.md) or [English](references/english-profile.md). For other languages, apply the rules directly and mark language-specific judgments as lower confidence instead of inventing a profile.
- A screen, component, or design implementation: read [references/design-profile.md](references/design-profile.md) and inspect the relevant implementation or rendered state when available.
- For rule IDs, confidence, source scope, and exceptions: read [references/rules.md](references/rules.md).
- Use [tests/regression_cases.json](tests/regression_cases.json) as behavioral examples when a judgment is borderline; cases cover Korean and English.
- Grounded rewrite patterns: [references/before-after.md](references/before-after.md).
- For the optional OMP sample, read [extensions/README.md](extensions/README.md) before considering [the inactive sample](extensions/anti-slop.omp.example.ts).
- Run the offline validator from this skill folder: `python3 tests/validate_package.py`.

## Preserve the user's meaning

Before editing, identify the user’s purpose, audience, claims, entities, quantities, units, dates, conditions, source attributions, uncertainty, and intended voice. Keep those facts and relationships intact. Never invent a metric, feature, source, quotation, user outcome, testimonial, benchmark, personal experience, or completed verification to make copy sound stronger. If evidence is missing, keep the uncertainty visible or ask a concise question; do not silently fill the gap.

Preserve code, quoted source text, mathematics, units, URLs, identifiers, proper names, and meaningful sequence markers unless the user asks to change them. When revising, compare the result against the source for dropped or strengthened claims, changed subjects/timing/conditions, arithmetic changes, and unsupported details. If the edit would change meaning, restore the source meaning or mark the unresolved point instead of guessing.

## Output format

- **audit** — a ranked punch list, one line per finding: rule ID, class (확실한 오류 / 휴리스틱 경고 / 취향 제안), a short verbatim excerpt or concrete UI location, why it harms the reader or user, and one minimal repair. Close with anything that could not be verified. Do not edit the target.
- **revise** — the bounded edits, then a change summary: what changed, which rule justified it (or "per the user's brief"), and any unresolved findings. The summary states exactly what changed — no more, no less.
- **draft** — the deliverable only, with profiles applied silently; mention a rule only when you declined to add something the user asked for.

## Review discipline

For every finding, include its rule ID, a short excerpt or concrete UI location, why it harms clarity, accuracy, usability, or access, and one minimal repair. Separate:

- **확실한 오류**: demonstrable contradiction, broken control, unsupported factual claim, clipping, missing required state, or a specific accessibility failure. Correct only after verifying it.
- **휴리스틱 경고**: a pattern that can sound or look generic in context. Explain the evidence; do not treat a single word or structure as proof.
- **취향 제안**: a viable alternative based on hierarchy, tone, or rhythm. Present it as optional.

An audit is not a rewrite. Keep the punch list ranked by user impact, not by count. Avoid a fixed score, universal quota, or “AI detected” conclusion. Surface patterns drift as models and prompts change, so a pattern is a review cue about how the text serves its reader, never evidence of who wrote it. If the page or prose already works for its audience, say so and leave it alone.

## Writing path

For prose, establish what the text must say before looking for style patterns. Review directness and information density, then headings and repetition, then attribution and factual consistency, then punctuation and formatting. Apply the matching language profile. Prefer deleting a redundant phrase or making one claim precise over replacing the whole paragraph. Keep deliberate rhetoric, technical language, and the author's register when they serve the audience.

## Design path

For UI, start with the user's task and content, then check hierarchy, responsive behavior, interaction, states, and accessibility. Apply [references/design-profile.md](references/design-profile.md). Distinguish an observed defect from an aesthetic preference. Do not rebuild an existing app or replace its visual identity for an audit; keep fixes in the requested boundary. Verify behavior or rendering when available and state what you could not verify.

## OMP extension

The OMP sample is optional and disabled by default. It resides in this skill's [extensions/](extensions/README.md) directory, linked above. Read that extension README before loading it. Its context addition is not a substitute for this workflow. The sample does not rewrite assistant messages, block session completion, or retry edits. If adapted, cap any automated correction at one attempt and fail open with a clear report.
