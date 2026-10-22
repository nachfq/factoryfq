---
name: project-implement
description: Implement or revise one planned delivery in guided or autonomous mode, returning the result for human review.
---

# Implement one reviewable delivery

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Act as the implementation coordinator in this conversation. Read the saved plan
instead of relying on the planner's conversation. By default, execute one delivery
and stop for user review. Remaining tasks, worker completion, passing checks, or
an open PR do not authorize the next delivery. Honor an explicit request for wider
autonomous execution; do not infer it from a roadmap or a plan marked ready.

When launched as an independent worker, first read the assigned
[implementer role](../project-coordinate/references/implementer.md). Its ownership
and delegation limits override coordinator defaults; it permits only the bounded
independent reviewer, not more implementation workers.

Read references only at their stated trigger, not recursively at startup. Reuse
instructions already loaded when still applicable.

## Select the authorized delivery

Use [project-delivery](../project-delivery/SKILL.md) to load the selected delivery
from its established source, including the actual applicable project context.
Reuse relevant contents already read; an assignment summary or link alone is not
sufficient. Apply context criteria to implementation choices and reconcile
consequential conflicts with the plan. Respect explicit user exceptions.

Read Specs, Technical approach, and the selected delivery's tasks and checkpoint
from their authoritative locations; consult history only for relevant decisions.
Match the user's request to a concrete delivery or explicitly bounded subset.
If the intended plan or scope
is unclear, resolve that before editing. Reuse an already clear request without
asking for approval again. If the plan is missing essential scope or decisions,
return those gaps for planning rather than inventing the implementation contract.

Check any pending human review first. An implementation marked done is not an
accepted delivery. Apply requested corrections to that delivery before starting
dependent work. A positive review alone does not authorize another delivery.
Briefly state the selected outcome, task IDs, scope boundaries, and verification.
Use the [delivery agreement](references/delivery-contract.md) to resolve artifact
and publication destinations and reuse scoped user authorization. An independent
worker receives this agreement in its assignment; clarify missing consequential
choices without rediscovering settled ones.

## Choose the collaboration mode

Use the user's requested mode or an applicable agreed preference. If neither is
known, ask once before editing: guided blocks or autonomous execution of the
selected delivery? Keep the choice in the current checkpoint through
`project-delivery`, using its source-specific write timing.
The user can change modes mid-delivery;
preserve completed work and adjust the next checkpoint. Autonomous
mode alone never authorizes additional deliveries or Git publication.

Before editing, read only the chosen mode's reference:

- [Guided](references/guided.md): one meaningful block, explain it and wait for
  the user's go-ahead before the next; no background work on future blocks.
- [Autonomous](references/autonomous.md): finish the selected delivery, then return
  for human review; routine implementation details do not require approval.

If the user changes modes, load the newly applicable reference at that point.

## Inspect and implement

Inspect the branch, working tree, relevant code, and prerequisite evidence. Preserve
existing edits and distinguish them from this delivery's changes. Resolve actual
overlaps before writing; do not reset, stash, or switch away someone else's work.
Check plan assumptions against the current code. Handle small work directly.
When delegating substantial bounded work as a coordinator, first read
[delegation](references/delegation.md). Delegation must stay within the current
mode, authorized delivery and file ownership; it never bypasses human checkpoints.

## Handle discoveries without expanding scope

Distinguish a technical unknown that inspection can resolve from an unresolved
product or design choice: requirements, public API behavior, dependencies, or a
tradeoff that changes the agreed outcome. Resolve routine implementation details
within the agreed outcome and keep the technical explanation current. If a
consequential choice remains open, or evidence invalidates the design or materially
changes scope, behavior, or review size, pause the affected work and report the
assumption, evidence, impacted IDs, and bounded alternatives to the user/planner.
Continue only independent work allowed by the current mode and checkpoint. In
guided mode, this never permits starting another block while awaiting review.
Do not silently rewrite requirements, add future features, or force the code to
match a false plan.
Resume affected work after the consequential revision is agreed; preserve valid
work and reopen only tasks whose prior result was invalidated.

## Integrate, verify, and maintain state

Review the combined diff against the delivery's acceptance criteria and exclusions.
Also contrast the solution with the applicable project-context criteria: is each
added behavior, abstraction, dependency, test or document warranted by this
delivery? Correct unjustified additions within scope before handoff; explain any
remaining conflict. Passing checks alone does not establish that fit.
Run relevant checks on the integrated result, reusing still-valid evidence where
appropriate. Worker success alone does not prove the pieces work together. Complete
in-scope fixes; report failed, skipped, or unavailable checks honestly.
Use `project-delivery` to maintain the current checkpoint under its source's write
rules, including provisional notes when persistence must wait.

In either mode, once implementation and checks are complete, present the delivery
as awaiting user review. Do not advance to later work or claim acceptance before
user review. Report actual blockers and unfinished checks instead of claiming a
review-ready result.

## Continue at the appropriate boundary

After a guided block, follow its checkpoint and wait before the next block. Once the
whole selected delivery and its checks are complete, read
[handoff](references/handoff.md) for independent review and the final user handoff.
Also read it when explicitly asked for a delivery review. Independent review is
required at that boundary unless opted out or valid evidence covers the identical
target; it does not replace human acceptance or authorize Git operations.

Read [publication](references/publication.md) only when commit/push is requested
or an applicable scoped closure agreement authorizes it. Code approval alone is
insufficient. PRs, releases and merges require separate authorization.
