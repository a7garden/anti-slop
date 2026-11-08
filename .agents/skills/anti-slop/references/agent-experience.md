# Agent experience

Use when an interface lets people delegate work to an AI agent, supervise it, or review what it did: agent chats, coding and research agents, background tasks, tool runs, approvals, and recaps. It extends [design-profile.md](design-profile.md) and its [authoring stance](design-profile.md#authoring-stance); it does not apply to an ordinary screen that merely contains generated text.

## Design for delegation, not dialogue

A chat transcript records what was said; delegation needs to show what the agent was allowed to do, what it is doing, what it changed, and how to take it back. The user is often away while the agent works and returns to judge a result they did not watch. Make the run, its footprint, and the pending decision the primary objects; conversation is one input among them, not the container for everything.

Size the supervision to the work. Judge **stakes** (what a wrong action costs), **reversibility**, **duration**, and **ambiguity**. A short, reversible edit can run at once and show its result; a long run or an irreversible send, spend, or delete needs scope and plan before action and an explicit point of no return. Do not install every surface below on a one-step suggestion.

## Surfaces by phase

Each row names a job, not a mandated widget. Design the component the content needs (see [authoring stance](design-profile.md#authoring-stance)); a list, timeline, strip, or inline mark may serve a job better than a stock card or modal.

| Phase | Job the interface must do | Common failure |
| --- | --- | --- |
| Intent | Capture the goal with its constraints; ask only the questions that change the plan, with defaults. | A blank prompt that lets the agent guess unstated constraints; a questionnaire before trivial work. |
| Scope | Show what the agent can read, write, spend, or send, and what it cannot, before and during the run. | Authority defined only in settings, invisible at the moment it matters. |
| Plan | For multi-step or high-stakes work, show steps the user can edit or reject before they run; keep the plan visible as the run proceeds. | A read-only plan that forces accept-all or restart. |
| Run | Present-tense status of each step (pending, active, done, failed), elapsed time, and the artifacts it touched. Distinguish *working*, *waiting on you*, and *stopped*. | One spinner and "Working…"; a percentage with no known denominator; *waiting on you* rendered like *working*. |
| Actions and reasoning | Show world-changing actions (commands, edits, sends) as first-class records with input, result, and duration; keep reasoning summarized and collapsed. | Actions buried in narration; a decision the user must make hidden inside collapsed reasoning. |
| Checkpoint | Ask in proportion to risk: no prompt for reads, batched approval for same-tier writes, a separate deliberate form for destructive or external actions, each naming its consequence and target. | A modal per action, training reflexive approval; destructive and routine prompts that look identical. |
| Interrupt | Pause at a safe boundary, keep completed work, accept a correction, and show the revised plan before resuming. Label the control by what it actually does. | A Stop that silently discards finished steps. |
| Result | Lead with the footprint: changed files, records, messages, sources. Then state what was verified, what was assumed, and what was not done. | Paragraphs of narration before the two files that changed; uniform confidence for tested and untested claims. |
| Recovery | Undo, checkpoints, or restore where the product supports them; mark irreversible actions before they happen and keep that mark in the history. | A chat log as the only audit trail. |
| Return | On re-entry, show what changed, what needs a decision, and what failed, linked to the evidence rather than retold. | A wall of transcript to scroll after a long absence. |

## Streaming and attention

- Keep layout stable while output streams: reserve space for arriving content, do not jump the reader's scroll position, and let finished parts become readable and selectable before the run ends.
- Make provenance visible: user input, agent output, tool output, and quoted sources should be distinguishable without heavy chrome; a citation links to its source.
- Interrupt the user only for a decision, a blocked state, or completion they asked to hear about. Everything else is ambient status the user can look at.
- Several concurrent runs need a compact roster with each run's state; *waiting on you* outranks *working* in emphasis.
- Motion signals a real state change (step started, step done, needs you). Continuous decorative animation hides the difference between busy and hung.

## Truth boundary

Every surface shows only what the agent and product actually do. Do not draw a per-action undo, a pause that keeps state, a cost or time estimate, a confidence score, a sandbox preview, run history, or a checkpoint shortcut such as "always allow" or "add to allowlist" unless the capability exists or the brief explicitly includes building it; follow [separate presentation from capability](design-profile.md#authoring-and-redesign). When a capability is absent, say so where it matters ("This send cannot be undone") instead of implying safety. Never mark a step verified because the agent claimed it; verified means the check ran and its result is shown.

## In reviews

This module guides authoring. In an audit, the absence of a surface listed above is not a defect by itself. A finding needs an observed relationship and a task consequence, such as a destructive approval styled identically to a read, a waiting state indistinguishable from progress, or a result that reports success for checks never run. Map it to a fitting D rule or report-local UX/VD category under [finding-evidence.md](finding-evidence.md).
