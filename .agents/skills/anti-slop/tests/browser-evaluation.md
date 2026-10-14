# Browser evaluation fixture

Serve [browser-audit-fixture.html](browser-audit-fixture.html) from a loopback HTTP server, then request `$anti-slop browser-audit <fixture URL>` in an agent conversation. Use the documented interactive browser tool. This explicitly synthetic test has no real product UX claim: use its documented task-list exercise contract and mark external comparable-app research not applicable. It does not replace a real app domain/UX preparation evaluation. The fixture has no remote requests, accounts, storage, or backend; all submitted data is disposable tab memory. Reload restores the initial three tasks. Stop only the server/tab started for the evaluation.

## Expected exercises

Inventory the three screens (`#list`, `#new`, `#settings`) and their actual controls before acting. Record expected and observed results per probe; a source read or this answer key does not count as execution.

| Area | Expected behavior to verify |
| --- | --- |
| Route navigation | All three navigation links show the matching section and active location; return to list preserves tab-memory tasks and filters. Browser back/forward follows the route history where the tool supports it. |
| Search and filters | Initial list has 3 items; `메일` returns 1; an unmatched query returns explicit no-results copy; clearing restores 3. Completed filter returns 1 and open returns 2 initially. |
| Detail dialog | Open an item from its real trigger, confirm name/status, close with button, reopen and close with Escape; check initial focus, containment, and focus return through actual keyboard actions. |
| Validation | Empty, whitespace-only, and a one-character name fail with field-associated copy and focus. A valid Korean name can proceed. |
| Async success | Submit a valid synthetic name; observe pending and disabled submit while reachable, then success. Revisit list and search for the new item to confirm tab-memory mutation. Reload persistence is explicitly not promised. |
| Error recovery | Enable the labeled test failure checkbox and submit valid input. The item is not added; error provides the real recovery action. Disable the checkbox and resubmit; success adds it. |
| Broken action | On settings, activate `설정 저장`. The promised save has no handler or visible outcome. A browser run should reproduce this as D10, with before/after evidence and a minimal repair, rather than infer it only from source. |
| Layout and keyboard | Inspect important screens/dialogs with real content at the available desktop and narrow viewports. Operate navigation/forms/overlays by keyboard. Declare unsupported viewport, touch, zoom, runtime-log, or motion capabilities. |

The known broken action tests whether the agent checks results after a click. It is not an instruction to rewrite this fixture. No findings about a real product follow from these synthetic results.

## Evaluation record

Store actual probe records and screenshots in a task-owned output location. Report tool/engine/viewport if known, all inventoried probes with pass/fail/inconclusive/blocked/not-run/not-applicable, and the resulting coverage status. Keep unsupported checks visible. Count attempted = pass + fail + inconclusive, and conclusive = pass + fail; retain the failure evidence.

Separately evaluate the execution-case prompts for routing, continuation, no surprise interview, parent-task output, and truthful fallback behavior. `validate_package.py` only validates fixture structure and consistency; it does not execute these prompts or this browser evaluation.
