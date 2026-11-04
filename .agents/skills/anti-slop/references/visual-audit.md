# Focused visual audit

Use for `visual-audit <target>`, `audit --visual <target>`, or a scoped request to verify rendered layout, color, typography, and composition. Both aliases resolve to **audit with the visual method**. A request to apply fixes resolves to **revise with this method**; preserve existing authorization and continue through affected checks.

The [execution contract](execution-contract.md) owns routing and edit authority. [Interface composition](design-profile.md) and [visual style](visual-style.md) own the design criteria; [finding policy](finding-evidence.md) owns classification and severity. Use their existing relationship ledger, not another score or parallel checklist. Read only relevant canonical rules when reporting findings.

## Establish the comparison

Identify the selected screen/component, the decision or experience it supports, protected identity/information, and the available evidence. Use the brief and inspected target; do not invent a user study or require a new interview. A bounded visual request stays bounded. Whole-app audits retain the existing [domain preparation](domain-research.md) requirement, including its gap and scope handling.

Choose representative views and material states from the target: the requested capture, affected width, relevant panel or state, and important content extremes when they change the judgment. There is no fixed viewport quota or all-state sweep. Supplied captures can complete a capture-based review within their limits. Web and native targets use the host's applicable UI tools; native apps do not require a web preview. To reveal web states or operate controls, use the [browser method](browser-audit.md) and its authority, observation, and cleanup rules. Capturing a screen does not verify its controls.

Keep a compact evidence entry for each reviewed view:

- Capture/source location and screen or region; identify supplied versus newly observed evidence.
- Actual image dimensions and, when known, viewport, scale/zoom, theme, content, and UI state. Image pixels are not automatically CSS pixels or native logical points.
- The applicable rows of the design ledger, any measurement and its method, and remaining gaps.

A source file or palette token is evidence of configuration. If no render/capture can be inspected, report useful source observations and the missing rendered evidence without judging visual quality or claiming a completed visual audit. Never generate a stand-in screen and present it as the target. Unknown capture metadata stays unknown; it does not invalidate relationships that are visibly supported.

## Observe, then measure what can resolve a question

Inspect the whole composition at readable size before details. Follow priority, association, redundancy, style/color, and fit/craft in the existing ledger. Consider a concrete reason to retain a candidate choice before calling it a problem. A deliberate gradient, serif, repeated record grid, dense comparison view, or sparse settings page can be appropriate.

Use available read-only measurements to test a specific observation:

| Question | Useful evidence and boundary |
| --- | --- |
| Do related elements actually align or separate? | Rendered bounds, gaps, baselines, and the visible grouping boundary. Record units and scale; do not infer geometry from DOM order alone. An unequal gap is not by itself a defect. |
| Is needed content clipped or unreachable? | Actual viewport and scroll-container bounds, wrapping, and the visible content/control. Preserve the scoped table/map exceptions and inspect surrounding controls separately. A scrollbar alone is not failure. |
| Are color roles or text visibility conflicting? | Actual adjacent foreground/background, area, saturation, type emphasis, and state meaning. Tokens help locate causes but may differ from the composite render. Record any opacity, image/gradient background, or unknown state that limits measurement. |
| Does a contrast claim hold? | Identify the applicable criterion, actual composited colors/background, and a supported calculation. Screenshot impressions or sampled antialiased text pixels cannot establish a WCAG conformance result. Use current applicable guidance; keep visual legibility judgment separate. |
| Is a state distinguishable? | Inspect that state and the relevant comparison state, including text/icon cues. Do not infer hover, focus, selection, or error behavior from one static capture. |

Use existing project/host inspection tools; do not install a scanner merely for this method. When measurements are unavailable, keep supported visual judgments and disclose the specific limit. Avoid invented pixel values, inferred color ratios, and quality scores based on card count, palette count, or whitespace proportion.

## Make a supported finding

Tie each finding to **capture/region → observed relationship → task or visual brief → consequence → bounded repair**. Keep source-derived causes separate from observed effects. For example, a dominant secondary profile panel beside a faint approval action can support a hierarchy warning; measured user confusion or delay needs separate evidence. A clipped required control can support an access finding when actually observed under the applicable conditions.

Apply the shared rule mapping and deduplication once. For a visual judgment, name the mechanism and preserve it as judgment; for a measured failure, include the actual result and method. An unobserved binding/state remains a gap. A viable alternative palette is an optional direction unless the brief or observed relationship supports a defect. No issue quota or automatic redesign follows from the audit.

## Recheck an authorized repair

During revision, retain the original observations and capture the changed target after applying the scoped repair. Recheck under matching viewport/scale, theme, representative content, and UI state wherever those conditions matter. A larger viewport or different record set cannot establish that the original clipping or hierarchy problem was fixed. Record material differences; re-create the original condition when possible, otherwise leave that comparison inconclusive.

Compare the issue's location and mechanism, not just screenshot pixel differences. Check relevant neighboring roles and affected states for regression: a stronger accent must not erase selected/error distinctions, and tighter spacing must not hide a condition. Preserve names, facts, features, identity, and necessary labels under the shared contract. If only a screenshot was reviewed and no editable target is available, a proposed repair is not an applied or verified fix.

Record each affected issue as resolved with observed evidence, still present, or unverified/inconclusive. If the host cannot render the change, finish authorized source work when possible and report the pending visual check. Do not claim the changed source proves the visible result or restart approval for work already authorized.

## Deliver within the requested format

Give the scoped view/state coverage, ranked evidence-linked findings, and material measurement or interaction gaps. Revision adds the observed recheck results. Reuse the design ledger and parent task's output; create an audit file only when useful or requested. A clean visual review may simply state which relationships fit and what was inspected. Stop after delivery without turning the result into an unsolicited redesign.

For maintainer checks and purposeful colorful/dense controls, use [visual audit evaluation](../tests/visual-audit-evaluation.md). Its reviewer anchors are not runtime findings or facts about another product.
