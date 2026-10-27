import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";

const reviewContext = [
  "When reviewing writing or UI for generic patterns, preserve the user's facts, units, sources, uncertainty, and intent.",
  "Treat style signals as contextual warnings, not proof of AI authorship. Separate verified defects from heuristics and taste.",
  "Do not invent metrics, testimonials, citations, features, or verification. For an audit, report findings without editing.",
  "When automatically applying anti-slop, keep the current task's scope and output format; do not start an interview or a separate skill workflow. A user-named run follows the skill's execution contract.",
].join("\n");

export default function antiSlopExample(pi: ExtensionAPI): void {
  pi.on("before_agent_start", (event) => ({
    systemPrompt: [...event.systemPrompt, reviewContext],
  }));

  pi.on("session_stop", (_event, ctx) => {
    ctx.ui.notify(
      "If this turn changed copy or UI, consider using $anti-slop audit in chat before shipping.",
      "info",
    );
    // Intentionally return void: do not block or continue the main session.
  });

  // agent_end is notification-only and is not a completion gate.
  // assistant_message is not changed: streaming text cannot be recalled.
}
