# Local initiative format

Use this format for local storage only. For Linear documents and delivery issues,
use [Linear plans](linear-plans.md); do not mirror the local file structure there.

Keep one initiative at `.agent-context/plans/<id>/plan.md`. Its optional `log.md`
holds historical rationale. Do not create empty logs, task-per-file trees, a
hand-maintained index, or duplicate JSON state. Follow the project's language for
prose; retain the metadata keys and `Specs`, `Technical approach`, `Tasks`, and
`Next delivery` headings.

Use this format for a user-selected direction or an explicitly requested
speculative plan. A comparison of possible directions does not need a task list;
marking a plan `draft` does not replace that conversation.

## Metadata

Start `plan.md` with a JSON object between `---` lines. This small structured
header lets the standard-library reader list plans without reading their bodies.
All four fields below are required:

```markdown
---
{
  "id": "example-initiative",
  "title": "A short outcome-oriented title",
  "status": "draft",
  "depends_on": []
}
---

# A short outcome-oriented title

## Specs

## Technical approach

## Tasks

## Next delivery
```

`id` is a stable lowercase slug matching its directory; `title` is nonempty.
`depends_on` lists other initiative IDs, without duplicates or self-dependencies.
Reference dependencies only when they are real prerequisites; do not invent empty
initiatives just to populate this list. Check that references resolve and do not
form a cycle before handing off.

Plan status is `draft`, `ready`, `active`, `blocked`, `done`, or `cancelled`.
`ready` means the next delivery is specified and material decisions for it are
settled, not that execution is authorized. Preserve evidence-backed execution
states when revising an existing plan; the planner does not start execution.

## Specs

State the intended outcome, scope and exclusions, relevant constraints, and
requirements with stable IDs (`S1`, `S2`, ...). Give observable acceptance criteria
and link to code or documentation as needed. Separate agreed decisions from
assumptions and open questions. Keep the current truth here, so a new session
does not have to reconstruct requirements from the log or previous conversation.

## Technical approach

Explain the design before listing the work. Introduce the relevant domain concepts
and what each represents, then connect them through the current behavior and the
proposed change. Show a concrete use case, data flow, or before/after example;
use a small diagram when relationships are easier to understand visually.
Distinguish existing functionality being reused from functionality being added.
Explain why the chosen boundaries and grouping make sense, significant tradeoffs,
and assumptions still open. Link to authoritative sources for deeper detail.

Write for the user who will review the change, not just the agent that will build
it. Adapt the explanation to their questions and familiarity; avoid a generic
tutorial, code inventory, or duplicate specification. Keep this explanation in
the plan rather than a separate design document that can drift out of sync.

## Tasks

Use stable task IDs (`T1`, `T2`, ...) grouped into small deliveries (`D1`, `D2`, ...).
Each near-term task needs a concrete outcome, linked Specs, dependencies, state,
and a meaningful verification method. A compact table or short task blocks are
both fine; avoid unwieldy tables full of prose. Use `pending`, `active`, `blocked`,
`done`, or `cancelled` for task state. Include concise observed evidence for done
tasks and the unresolved dependency for blocked tasks. Do not claim tests passed
because a test command is listed. Keep later work coarse rather than generating
a speculative exhaustive checklist.

## Next delivery

Identify the next delivery and its included tasks, whether its scope is proposed
or user-agreed, the expected review surface, and how its outcome will be verified.
State decisions that must be resolved first. Include enough relevant source
locations and constraints for a fresh agent to pick it up. Keep this a planning
handoff, not an instruction to execute without the user's request.

During implementation, record the agreed collaboration mode, authorized deliveries
and human review boundary here: guided, autonomous within a delivery, or an
explicitly autonomous milestone. For guided work, keep a short current
resume note: the applied/reviewed block, outstanding checks or corrections, and
the proposed next block. Update it in place; do not create a second task list or
a per-block history. A partially implemented task stays `active`.

In the default review-per-delivery workflow, this section also identifies the
delivery awaiting human review. Task state `done` records implementation and
verification, not user acceptance. Record `awaiting user review` or the user's
acceptance here; keep the current delivery visible until reviewed. Requested corrections reopen only affected
tasks. An initiative remains `active` while awaiting review; mark it `done` when
all required deliveries are verified and accepted. Acceptance does not itself
authorize starting another delivery.

## Log

Create `log.md` only for useful historical evidence: consequential decisions,
changed assumptions, or why a task was reopened or cancelled. Entries have a date,
affected IDs, a brief explanation, and a source or verification reference where
applicable. Record a decision once; no chat transcripts, raw command output, or
routine per-turn updates. The plan's requirements, design, and tasks remain current;
the log explains their history and is read only when needed. Never erase valid
completion evidence merely because another part of the initiative changed.
