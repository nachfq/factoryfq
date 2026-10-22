---
name: project-plan
description: Help choose what to work on next and collaboratively build or revise a plan in local files or Linear documents and delivery issues. Use for planning small, reviewable deliveries or suggesting next steps from project context, not for implementation.
---

# Plan project work

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Act as the planner in this conversation. A starting point can be an idea, a problem,
or simply "what should we do next?" Planning authorizes plan artifacts, not code
changes, commits, or implementation. Keep implementation for a separate session;
this skill does not create or coordinate an implementer agent.

## Recover relevant context

Read applicable instructions and reuse relevant context and its established source.
Use [project-context](../project-context/SKILL.md) only to resolve a missing source
or association, or perform requested setup. Honor the user's selected plan
destination; otherwise reuse the established context source for a new plan and
the existing plan's destination for revisions. If sources compete or the choice
is missing, resolve it before writing. Do not migrate, mirror, or silently fall
back to local files when Linear is unavailable.

For local plans, use the reader below and [local plan format](references/plan-format.md).
For Linear, follow [Linear plans](references/linear-plans.md) to verify the project,
read its context, and locate documents and delivery issues selectively. Do not
run the local reader or initialize `.agent-context` for the Linear route. Do not
choose an active initiative merely because it is newest. Read relevant history
only when needed to understand a decision.

For local plans, set up missing storage through `project-context` before writing.
Read-only exploration can continue while the destination choice is pending.
Missing discovery is not a gate: gather what this decision needs. Use
[project-discover](../project-discover/SKILL.md) when the user needs broader project
onboarding rather than a focused next-step discussion.

## Choose a direction together

Ground suggestions in the user's goals, current code, existing plans, and blockers.
Filter candidate work by this repository's responsibilities, agreed scope, and
work or validation already covered. Related repos provide context; their pending
work does not automatically belong here. Reopen a settled decision or propose
another review only when new evidence or an explicit request warrants it.

For an open-ended request, offer useful options when they exist, explain tradeoffs,
and recommend a next step. Waiting for feedback or choosing no new work is a valid
recommendation: explain what decision or evidence would unblock progress, without
inventing a task or plan to fill the gap. Investigate repo facts yourself; ask
focused questions about intent and consequential choices, letting each answer
shape the next question. Do not repeat settled decisions, impose a fixed interview,
or treat a recommendation as the user's choice.

A request to analyze what to do next starts a comparison and conversation. Present
the evidence and recommendation, then resolve the user's direction before breaking
it into implementation tasks. A saved draft is not evidence of that choice. Any
persisted comparison remains analysis; it need not use the plan's Specs/Tasks
format and must not create delivery issues for an unchosen direction.

Research a named uncertainty when needed. Delegate bounded read-only investigations
when they save context or allow useful parallel work; keep user dialogue here.
If evidence is insufficient to plan implementation, a scoped investigation with a
clear question and expected evidence can itself be the next delivery. Do not
invent implementation tasks before that uncertainty is resolved.

## Build a reviewable plan

Apply the relevant project-context criteria to the proposed design, scope and
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

Before implementation, agree the delivery's [destinations and closure scope](../project-implement/references/delivery-contract.md).
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

## Revise and hand off

When new evidence challenges a plan, identify the affected assumption and impact.
Discuss meaningful changes to goals or scope; findings do not authorize expansion.
For a consequential correction, explain what stays, what is removed or simplified,
why, and any remaining risk before applying the revised agreement. Respect a
requested proposal-first checkpoint; otherwise reuse already explicit authorization.
Update affected Specs, Technical approach, and Tasks together, preserve valid work
and stable IDs, and record only consequential decision changes in the destination's
history location. Keep design and open contracts in the plan; execution evidence
belongs in Linear issues or local Tasks/Next delivery, not Specs/Technical approach.
Do not rewrite project context to justify an implementation or an unsupported plan
decision. Update durable criteria only when the user actually changes them.
Do not update project context for each feature clarification. Consolidate repeated
explanations instead of appending a clarification for every exchange. Mark completion only
from supplied or observed evidence; a suggested solution is not completed work.

Before handing off, read back the saved plan, check requirement/task references,
dependencies, and verification. For local plans, run the reader to confirm it is
discoverable; for Linear, verify document/issue links and saved issue fields.
Walk the user through the proposed behavior, design rationale, and how the next
delivery contributes to it; a task list or file link alone is not a handoff.
Include the plan path or document and issue URLs, proposed or agreed scope, and
unresolved decisions. For work already assigned, include the affected delivery/task
IDs and the agreed change in outcome, constraints and verification, so the
coordinator can update existing workers without restarting unaffected work. The plan
must be understandable to the user and usable by a fresh implementation session.
A ready plan or agreed scope is not permission to execute every delivery. Stop at the planning
handoff; do not begin implementing. `project-implement` can consume local plans
or Linear delivery issues when the user requests execution in a fresh session.

## Read local plans selectively

Resolve `SKILL_DIR` to this skill's directory; the reader requires Python 3 and Git.

```sh
python3 "$SKILL_DIR/scripts/read_plan.py" --repo "$REPO" list
python3 "$SKILL_DIR/scripts/read_plan.py" --repo "$REPO" show initiative-id
```

`list` reads metadata only and generates an index without maintaining a second
state file. `show` reads only the selected `plan.md`, never `log.md`. Both are
read-only and work from a repo root or subdirectory. Search a relevant log by
requirement/task ID when needed instead of loading all initiative histories.
