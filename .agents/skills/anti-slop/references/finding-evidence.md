# Finding categories and evidence

This reference governs classification for all findings. The execution contract governs delivery. User requests can narrow the audit; a broader category does not expand authorization.

## Choose the right category

Use W01–W29 or D01–D25 when the observation fits the canonical rule's detection conditions and exceptions. Do not stretch a rule or invent a canonical ID to fill a template. A severity field does not broaden the detection conditions: W21 concerns drift/differences between statements, not every absent contextual detail. A hypothetical need for an unstated year is not a W21 finding; mention it only as an optional context note when useful.

An in-scope domain/user-journey problem outside those rules can use a report-local **UX-01**, **UX-02**, etc., labeled **domain UX**. State the supported job, target requirement or visible promise, affected journey, actual evidence, user impact, and minimal repair. These IDs identify this report's observations; they are not additions to the canonical catalog. Do not count the same problem twice under both categories.

For example, a supplied workflow requires checking overlapping bookings, but the observed journey makes users reopen each booking individually to discover overlaps. If no canonical rule fits, a domain UX finding can explain that observed friction and a bounded improvement. Without the requirement or observation, it remains a hypothesis to investigate. A competing app's conflict calendar does not prove a defect here.

An observed composition or component-craft concern outside the canonical rules can use report-local **VD-01**, **VD-02**, etc., labeled **visual design**. Include the actual screen/region/capture, competing visual relationships, supported task or design-brief basis, likely effect, and one minimal repair. These are report-local IDs, not additional canonical rules. Use one best-fitting category per issue; do not duplicate it under D, UX, and VD.

## Classify the evidence, then the finding

- **Proven error / 확실한 오류:** direct evidence shows a contradiction, broken behavior, violated target requirement, or applicable measured standard failure. Give the evidence and scope.
- **Heuristic warning / 휴리스틱 경고:** contextual evidence suggests avoidable generic writing or UX friction. Explain the mechanism; do not claim measured user preference, speed, or failure without evidence.
- **Optional taste / 취향 제안:** a viable alternative in tone, rhythm, hierarchy, or presentation. It is not a required repair.

A grounded visual warning is not optional taste merely because the app still functions or its overall style is intentional. Visible control/label separation or misallocated emphasis can support a heuristic interpretation without a user study. The observed relationship must be real and its task relevance explained; an imagined runtime failure, aesthetic dislike, or a competitor's different layout cannot supply that basis.

Access or evidence gaps have **no defect classification**. Report an inaccessible citation, unobserved control outcome, or missing measurement in verification limits. Lack of access does not prove fabrication or failure. Independent evidence may establish a defect despite that gap; cite that evidence specifically.

A concern that exists only if an **unobserved binding or behavior** is true remains a hypothesis or verification probe, not a canonical heuristic warning. For example, a source snapshot contains change-confirmation copy but does not show which screen uses it; that missing connection does not establish that registration uses misleading copy. Keep the proposed check in verification limits until the relevant binding or observed context supports the rule's detection conditions.

Name evidence kinds accurately: supplied requirement, inspected source, documented behavior, visual observation, operated interaction, or measured value. A screenshot cannot prove persistence; a help page cannot prove an action was executed. For accessibility, identify the criterion, level, applicability conditions, and actual observation/measurement; do not claim whole-product conformance from a few probes. Research about surface habits supplies review cues, not authorship evidence.

Rank by supported reader/user impact. Include location or excerpt, impact, and one minimal repair; browser findings also need replay actions, expected/observed result, and actual evidence references. Preserve material limits even in a compact report. Do not manufacture findings for an otherwise sound artifact.
