# Interface design profile

Review the interface against its user task, content, context, and current implementation. Aesthetic defaults can be useful when they fit. Do not prescribe one font, palette, card count, density, navigation shape, or visual style for every product.

## Review order

1. **Content and hierarchy:** does the most useful information lead? Do labels and headings describe real content? Does decoration compete with the task?
2. **Structure:** are repeated cards, badges, gradients, icons, sections, or patterns serving distinct information? Does the page feel like its product rather than an interchangeable template?
3. **Truth and relevance:** are numbers, charts, logos, testimonials, product screenshots, and images real, supplied, and relevant? Remove a fabricated proof element; never invent a replacement.
4. **Interaction:** verify that controls work, links have meaningful destinations, and hover/focus/pressed/disabled behavior agrees with the control's actual state.
5. **States and access:** inspect loading, empty, error, success, keyboard focus, names, contrast, zoom/reflow, and reduced motion where applicable.

## Distinguish defects from taste

- **Defect:** a control does nothing or misleads; text clips at a tested viewport; focus is unavailable; an error/empty state blocks the task; an image misstates the product; a measured contrast or reflow requirement fails.
- **Heuristic:** repeated same-size cards, gradient backgrounds, pill badges, decorative icons, an eyebrow plus multiple headings, or a hero/three-features/CTA/footer rhythm appears without information or product rationale. Explain the resulting hierarchy or sameness.
- **Taste:** a centered layout, serif type, generous space, dark mode, a card, gradient, badge, or illustration can fit. Offer another treatment only as an option unless it harms the user's task.

## Implementation checks

- Resize and test actual layouts. WCAG 2.2 reflow guidance calls for content to remain available without two-dimensional scrolling at the specified equivalent width; inspect wrapping and zoom instead of hiding evidence. Do not use overflow-x: clip to conceal content that does not fit.
- Evaluate WCAG contrast using the applicable WCAG method and criteria. APCA can inform design exploration, but it is not interchangeable with a WCAG conformance ratio or an equal pass condition.
- Let controls wrap when language, width, and usability require it. Do not force every button onto one line.
- Give interactive elements accessible names and visible keyboard focus; preserve semantic HTML and a usable tab order. Check touch target, motion, and error behavior in context rather than turning a one-size threshold into an unrequested redesign.
- Use real data. A blank chart may be an empty state; label it honestly. Do not create decorative metrics, fake customer marks, or fabricated testimonials to fill a layout.

