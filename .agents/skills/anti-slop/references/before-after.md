# Before and after

These paired examples show the smallest useful change. Each before block is followed by the evidence needed to revise it; examples do not authorize inventing replacement facts.

## 1. Abstract praise to supplied behavior

**Given:** the form stores a name and address, then fills them into the next application.

**Before**

> 새로운 차원의 혁신으로 신청 경험의 본질을 바꿉니다.

**After**

> 신청자 이름과 주소를 저장하면 다음 신청서에 자동 입력됩니다.

**Why:** the edit names the supplied behavior and drops unsupported scale claims.

## 2. Missing metric stays missing

**Given:** the brief contains no latency measurement.

**Before**

> 응답 시간이 32% 빨라졌습니다.

**After**

> 제공된 자료에는 응답 시간 측정값이 없습니다.

**Why:** the rewrite does not invent a more plausible number or imply that a test was run.

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

**Given:** no customer quote, customer name, or adoption metric was provided.

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

> 복용 전 의사와 상담이 필요합니다. 하루 한 번 복용하세요.

**Why:** the required notice appears once where it applies; repeated hedges erased the instruction without adding safety.

