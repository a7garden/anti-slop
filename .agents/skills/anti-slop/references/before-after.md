# Before and after

These paired examples show a change fitted to the authorized extent, usually the smallest useful one. Values in them are illustrative, not universal. Each before block is followed by the evidence needed to revise it; examples do not authorize inventing replacement facts.

For UI authoring, also inspect the [renderable design examples](design-examples.html): an authorized redesign, navigation alignment, and a purposeful style kept intact. They are illustrative alternatives, not measured usability results or layouts to copy into unrelated products.

## 1. Abstract praise to supplied behavior

**Given:** the form stores a name and address, then fills them into the next application.

**Before**

> 새로운 차원의 혁신으로 신청 경험의 본질을 바꿉니다.

**After**

> 신청자 이름과 주소를 저장하면 다음 신청서에 자동 입력됩니다.

**Why:** the edit names the supplied behavior and drops unsupported scale claims.

## 2. Missing metric stays missing

**Given:** comparison with the author's source confirms that an editor invented the 32% metric. The source says only that the response path changed. This is not merely an inaccessible measurement record.

**Before**

> 응답 시간이 32% 빨라졌습니다.

**After**

> 응답 처리 경로가 바뀌었습니다.

**Why:** remove the confirmed invented claim and retain the supplied fact. If the author had supplied the 32% claim but its records were inaccessible, preserve attribution and report the verification gap outside the artifact instead.

## 3. Keep a useful colon and comparison scope

**Given:** a medical-title comparison reports the values below; it does not study Korean prose.

**Before**

> 2025년 신청 안내: 제출 서류와 접수 일정

**After**

> 2025년 신청 안내: 제출 서류와 접수 일정

**Why:** leave a clear title untouched. A separate research summary must keep its medical-title population and cannot generalize to all Korean writing.

## 4. Remove repeated labels, keep the actual fields

**Given:** these values are the supplied dates and destination.

**Before**

> **접수 기간:** 접수 기간은 2025년 4월 1일부터 5월 2일까지입니다.  
> **제출처:** 제출은 신청 포털에서 하면 됩니다.

**After**

> - 접수 기간: 2025년 4월 1일~5월 2일  
> - 제출처: 신청 포털

**Why:** the labels now help scanning instead of repeating their values. The dates and destination are unchanged.

## 5. Remove a fabricated proof block, not replace it with new proof

**Given:** the developer confirms that the displayed customer and quote were invented to fill the layout. This establishes fabrication; unavailable provenance by itself would not.

**Before**

> “이 제품 덕분에 업무가 10배 빨라졌습니다.” — 김서연, 고객

**After**

> Remove the testimonial block until an authorized, verifiable customer quote is supplied.

**Why:** changing the quote or swapping in an invented metric would preserve the same factual problem.

## 6. Fix the actual responsive failure

**Given:** at 320 CSS px the content is cut off; inspection shows a fixed-width shell and clipping rule.

**Before**

    .page { width: 1200px; overflow-x: clip; }

**After**

    .page { width: min(100%, 72rem); margin-inline: auto; }

**Why:** remove the fixed width and test wrapping/reflow at the failing viewport. Clipping is not a repair. This illustrative CSS still needs verification against the actual layout and content.

## 7. Make the control's behavior real

**Given:** inspection confirms the button's intended action is to save a draft.

**Before**

    <button>저장</button>

**After**

    <button type="button" onclick="saveDraft()">저장</button>

**Why:** this only works if saveDraft is the real project action and the result/error states are implemented. Do not copy this snippet over an existing app without checking its framework and behavior.

## 8. Leave style as style unless a user cost is shown

**Given:** a centered serif headline remains readable at tested widths and matches the brief.

**Before**

> A reviewer marks the centered serif headline as a failure because AI tools often center headings.

**After**

> No finding. Keep the current heading. Offer another alignment only if it would improve a stated task, hierarchy, brand fit, or measured access issue.

**Why:** a pattern association is not evidence that this composition is defective.

## 9. Drop the tacked-on interpretation, keep the fact

**Given:** the source states only the opening date; no analysis accompanies it.

**Before**

> 접수 기간은 4월 1일부터 시작됩니다. 이는 행정 혁신의 방향을 보여 줍니다.

**After**

> 접수 기간은 4월 1일부터 시작됩니다.

**Why:** the tail claimed significance no supplied evidence supports; deleting it keeps the verifiable fact intact.

## 10. Keep the required disclosure once, cut the pile

**Given:** one medical disclaimer is required; the draft repeats hedges and the notice in three paragraphs.

**Before**

> 복용 효과는 개인에 따라 다를 수 있습니다. 전문가와 상담하시기 바랍니다. (같은 문단 구성이 세 번 반복)

**After**

> 복용 효과는 개인에 따라 다를 수 있습니다. 전문가와 상담하세요.

**Why:** keep the outcome uncertainty and required notice once. The source supplied no dose, frequency, or consultation timing, so the rewrite cannot add one.

## 11. Apply the brief without printing it

**Given:** artifact: “접수는 5월 2일에 끝납니다.” Editing instruction: “짧게 쓰고, 마감일은 그대로 두세요.”

**Before**

> 접수는 5월 2일에 끝납니다. 짧게 쓰고, 마감일은 그대로 두세요.

**After**

> 접수는 5월 2일에 끝납니다.

**Why:** the second sentence addresses the editor, not the reader. A quoted instruction in an actual script would remain part of the artifact.

## 12. Preserve a supplied voice

**Given:** the author's sample uses informal endings and fragments. The source is an attributed personal note; the user asks only for redundant wording to be removed.

**Before**

> 좋았어. 좀 무서웠고. 아직은, 잘 모르겠어. 아직은 잘 모르겠다는 생각이야.

**After**

> 좋았어. 좀 무서웠고. 아직은, 잘 모르겠어.

**Why:** delete duplicated meaning without imposing formal endings, resolving mixed feelings, or inventing an explanation for them.

## 13. Reject a plausible cause added by the editor

**Given:** costs rose 18% during the migration. The source does not explain why.

**Before**

> Costs rose 18% during the migration because both systems ran in parallel.

**After**

> Costs rose 18% during the migration.

**Why:** temporal overlap does not establish causality. A plausible mechanism is still an unsupported addition (W21).

## 14. Keep interface terms stable

**Given:** the product calls the object “초안”. The button saves that object without publishing it.

**Before**

> 제목: 초안 편집. 버튼: 콘텐츠 확정. 성공 메시지: 문서를 발행했습니다.

**After**

> 제목: 초안 편집. 버튼: 초안 저장. 성공 메시지: 초안을 저장했습니다.

**Why:** stable terminology makes the flow understandable (D25), and the labels now describe the verified save action (D10). Do not infer publication from a generic button label.


## 15. Let layout carry an obvious relationship

**Given:** a rendered Downloads page has a heading “Downloads” and a button “Download CSV”. A subtitle says “Download your files here”, and a second line says “Click Download CSV to download a CSV”. Neither line contains a condition, consequence, or instruction beyond the visible control.

**After:** keep the heading and button; remove the two redundant lines. Retain a separate “Paid accounts only” condition if that condition applies.

**Why:** layout and the action label already provide orientation. Economy does not authorize dropping eligibility or accessible names (D04).

## 16. Repair emphasis without replacing the palette

**Given:** an approval screen's brief prioritizes the pending approval. The rendered secondary profile panel takes the sole saturated accent across half the viewport; the approval action uses the same faint treatment as inactive metadata.

**After:** reduce the secondary panel's accent area and restore the primary-action emphasis using the existing palette. Inspect focus, disabled, and relevant theme states afterward.

**Why:** the observed competition supports a visual hierarchy warning, not a ban on bright color. No measured user delay or standards failure has been established.

## 17. Redesign on request, without a defect claim

**Given:** the owner asks for a redesign of a field-survey dashboard so it suits researchers logging site visits. The current screen uses the framework's default font and starter blue; only the product name and logo file are declared identity.

**After:** form a working brief (survey teams recording visits; exact, outdoorsy, unhurried; keep logo, name, metrics, filters, and every state; emphasize the visit log), then apply a new palette, type pairing, and layout across the dashboard. The logo, data, and features are unchanged.

**Why:** the request authorizes system-level choices. The old blue needs no finding against it, and the delivery reports the changes rather than a defect list. An audit of the same screen would still classify only evidenced issues.

## 18. Align icon boxes and comparison figures

**Given:** in a rendered sidebar, icons of different widths push labels to different start positions. A comparison table shows `12.5%`, `8%`, and `−3.25%` in one column; its supplied data contract specifies exact values displayed to two decimal places.

**After:** give every icon the same box, for example 20 px, and the same gap, so labels share one edge; center each icon on its label's first line. Show the figures as `12.50%`, `8.00%`, and `−3.25%` with tabular numerals and right alignment.

**Why:** shared edges and one number format make rows comparable. The data contract supports the decimal padding here; without it, preserve the supplied precision and align the figures rather than implying more precision for appearance. The 20 px box is an example; the project's icon set and density decide the value.

## 19. Let the content carry the color

**Given:** a photo-archive home screen applies a saturated gradient and glow to navigation, buttons, and card borders. The user's own photos appear as small grey thumbnails.

**After:** move navigation and controls to neutral roles with one accent for the primary action, and give the photographs the size and space to lead. No stock art or generated image is added.

**Counterexample:** a children's reading app whose illustrated characters and colored frames are its declared identity keeps them. Repair only an observed competition with the reading action (D08).

**Why:** richness belongs where it serves the content. Removing an identity that does its job would be a loss, not restraint.

## 20. Sound settings screen, no change

**Given:** a polish request for a settings screen. Sections are grouped, labels persist, switches align with their rows, conditions sit beside the setting they qualify, and the platform's standard styling renders cleanly at tested widths.

**After:** no change; say briefly that the screen already fits its task.

**Why:** a familiar pattern is the right answer here. Lacking a distinctive detail is not a defect, and polish does not license change for its own sake.
