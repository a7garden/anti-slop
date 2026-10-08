# Optional OMP extension sample (inactive)

The project was checked with the locally installed **omp 18.8.0**. The OMP extension guide lists before_agent_start, session_stop, agent_end, and assistant_message. The sample uses only the first two: it appends a short policy context when preparing a user prompt and shows a single, non-blocking reminder at main-session stop. It deliberately returns no stop decision, does not rewrite assistant messages, and never triggers an edit retry.

To try it, consult the installed OMP version's official extension-loading guide and load [anti-slop.omp.example.ts](anti-slop.omp.example.ts) explicitly for one project. Do not move it to a global extension directory as part of installing this skill. The sample's import is typed against @oh-my-pi/pi-coding-agent; compile and smoke-test it in the target OMP project before enabling. The core skill works without OMP.

The official guide says agent_end is notification-only and cannot be used as a blocking gate. session_stop can technically request continuation or block in current OMP, but this sample does neither. Do not add automatic rewriting there. If a future experiment adds a corrective pass, permit at most one and fail open with a report. Never claim assistant_message can retract text already sent in streaming updates.

Reference, checked 2026-10-07: https://github.com/can1357/oh-my-pi/blob/main/docs/extensions.md
