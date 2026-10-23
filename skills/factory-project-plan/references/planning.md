# Build a reviewable plan

Apply the relevant project context criteria to the proposed design, scope and
verification, not just to the introduction. Before calling a plan ready, remove
unsupported obligations and identify consequential departures from those criteria.
Explain the need, a simpler compatible alternative and the tradeoff; obtain the
user's agreement before treating a departure as settled. Reuse explicit exceptions
already agreed for this scope. Approval of a milestone or autonomous execution
does not authorize undisclosed exceptions. Routine compatible choices need no new
approval. Keep the source linked rather than copying context into every task.

Choose verification from the delivery's risks and responsibilities: distinguish
checks of owned behavior, existing coverage being reused, and usage examples.
Specify the smallest sufficient validation and any material gap it leaves. A
runtime requirement does not by itself prescribe a test language, new framework
or separate suite; justify added infrastructure or overlapping coverage by the
otherwise uncovered risk. Keep this rationale with the affected acceptance criteria,
not in a new checklist or document.

Once the user has chosen a direction, create or update one initiative in the
selected destination, following its format above. Reuse a direction already explicit
in the request or prior decisions without asking again. An explicit request for a
full speculative draft is also sufficient: label its assumptions and unselected
direction clearly. Otherwise, keep the discussion open or close with the agreed
wait condition rather than presenting implementation tasks for an unchosen option.
Keep unresolved scope choices visible in a draft. Reuse an existing matching
initiative rather than creating new artifacts for each session or revision. In
Linear, an explicitly speculative draft stays a document until the user chooses
the direction or specifically asks for draft issues.

Before the task breakdown, explain the technical approach for the human reviewer:
the relevant concepts and their relationships, how things work today, what will
change, and why. Use a concrete flow or example so the user can assess the design
without reconstructing it from code or task names. Scale detail to their familiarity
and the change; this does not require approval of every implementation detail.

Connect requirements to stable task IDs, dependencies, acceptance criteria, and
verification. Group tasks by coherent delivery outcomes, not by file type. Detail
the next delivery enough for a fresh agent to understand it; keep later deliveries
coarse until their assumptions are supported. An initiative may contain several
deliveries; it is not automatically one module, one commit, or one PR.

Before implementation, agree the delivery's [destinations and closure scope](../../factory-project-implement/references/delivery-contract.md).
Keep this operational agreement in its issue or local Next delivery, not project
context or a second execution ledger. A design-level publication split may be
summarized in the plan; runtime branches and checkpoints belong with the delivery.

Human review capacity limits delivery size. Prefer one concrete outcome with its
necessary tests and docs. Explain what the user will review and how it will be
verified. Resolve choices that materially affect its size before calling a delivery
small or ready. Split a cognitively large delivery into useful smaller outcomes rather
than using an arbitrary line limit. Parallelizable tasks still belong to one
integrated delivery for review; do not schedule a pile of concurrent deliveries
unless requested. Agree the next delivery's scope with the user.
