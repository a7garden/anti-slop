# Visual style and color

Use for UI design, styling, palette, type, surfaces, icons, and decoration. Style is in scope even if the UI has no photographs or generated assets. For screen composition use [design-profile.md](design-profile.md); for classification use [finding-evidence.md](finding-evidence.md).

## Establish a visual basis

Read the actual brief, existing tokens, identity assets, and related screens within scope. Inspect rendered examples at relevant sizes when available. Distinguish a declared product convention from an agent's assumption or an unchosen default; only the first constrains a redesign. Source tokens can establish configured values, not their full rendered effect. Record unavailable theme, state, background, or viewport evidence as a gap.

## Review the visual language

| Lens | Concrete checks |
| --- | --- |
| Style fit | Does the visual treatment support this content, audience, platform, and requested tone? Inspect specific competing elements rather than calling the result “generic” or “AI-looking.” Familiar forms can fit; difference alone is not quality. |
| Palette roles | Compare primary action, secondary action, selection, status, data, and decorative color. Flag a repeated use that gives unlike roles misleadingly equal emphasis or makes one color mean incompatible states in the same context. Do not require an arbitrary color count. |
| Emphasis and legibility | Inspect foreground/background relationships, saturation, area, type weight, hierarchy, and state visibility. A large decorative accent can compete with the current decision even when its text contrast passes. A muted palette can also hide needed emphasis. |
| Type and surfaces | Compare type roles, language coverage, line length, borders, shadows, radii, texture, and translucency across related components. Name the inconsistent relationship or brief mismatch; do not mandate one font, corner radius, or surface treatment. |
| Decoration and identity | Assess gradients, glow, illustrations, icons, motion, and brand elements for their role and visual cost. Keep purposeful atmosphere. Remove decoration or extra copy that merely fills space, repeats a label, or obscures the task. |
| States and themes | Check relevant hover, focus, selected, disabled, pending, error, and existing light/dark states. Do not assume a palette works in another theme or use color as the only way to convey necessary status. Check actual adjacent colors and backgrounds. |

Color and styling concerns can be grounded heuristic warnings without a broken button or user study. For example, an observed secondary panel using the sole high-saturation accent while a required approval action visually recedes can justify a hierarchy warning. Name the task and visible competition; do not claim measured confusion or delay.

A purple gradient, monochrome shell, serif heading, or bright palette is not a finding by itself. An explicit visual brief can support a style-fit finding even if interactions work. In a review, an alternative palette without a brief or task-based reason remains optional taste. In an authorized redesign, choosing one needs a product or brief rationale, not a finding against the old palette.

## Verify and repair

For a contrast or other accessibility claim, identify the applicable criterion and level, actual rendered colors/backgrounds, measurement, and exceptions. APCA is not interchangeable with a WCAG ratio. A screenshot-based impression can identify a legibility concern, not establish a measured standards failure. Use verified current guidance before making a new conformance claim.

Match the change to the [edit extent](execution-contract.md#2-establish-the-brief). A bounded fix chooses the smallest repair that restores the intended role: adjust an accent's area or saturation, restore semantic tokens, alter text weight, align surface treatments, or remove an unnecessary embellishment; it never replaces a palette or identity to fix one relationship. Polish may realign related tokens across the selected screen. A redesign may replace unprotected palette, type, and surfaces as one system, using the [authoring recipes](design-profile.md#authoring-and-redesign) where no authoritative system exists. Inspect affected neighboring roles, relevant themes, and state distinctions after a token change; do not treat a global search-and-replace as verified styling.

For a review finding, report the actual screen/component, observed style or color relationship, brief/task basis, likely mechanism, and minimal repair. Map to a fitting D rule or a report-local VD finding. Keep visual judgment separate from measured accessibility and runtime verification.
