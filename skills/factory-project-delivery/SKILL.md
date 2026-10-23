---
name: factory-project-delivery
description: Read an existing delivery's context, plan and execution checkpoint, or record its progress in local files or Linear. Use with implementation, coordination or authorized publication; not to create plans or discover tasks for ordinary Git work.
---

# Read and record a delivery

Own access to the selected delivery's authoritative records. The calling workflow
owns implementation, review, scope and authorization. This skill does not launch
agents, implement code, publish Git changes, or authorize another delivery.

## Load the existing delivery

Reuse the established source and delivery selection. If unresolved, use
[factory-project-context](../factory-project-context/SKILL.md); missing local files alone do not
trigger a Linear search. Clarify competing sources instead of migrating or
mirroring them. Read only the applicable storage reference:

- [Local delivery](references/local-delivery.md): versioned or ignored plan files.
- [Linear delivery](references/linear-delivery.md): read the plan and delivery issue.
  Load [Linear publication](references/linear-publication.md) only when an authorized
  update is due, not at implementation startup.

Read the actual applicable project context, plan design, selected tasks and current
checkpoint; reuse relevant contents already read in this session. Assignment
summaries and links alone are insufficient. Consult history only when needed.
Verify repository identity and prerequisites against the checkout. Report missing
sources and consequential contradictions; do not invent decisions or treat task
wording as an override of context.

Make available to the caller: source references, delivery/task IDs, outcome and
acceptance criteria, context constraints, design, prerequisites, current checkpoint,
and established mode, destinations and scoped authorization where recorded.
This is working context, not a new persisted manifest or a substitute for source
reading by another agent. Do not create a second tracker.

## Record observed progress

Use the same source and its reference's write timing. Local plans can record
provisional work; Linear normally records only user-validated, committed, reviewed
and pushed work. Read-only loading never implies permission to update records.

Record facts supplied and verified by the calling workflow: affected tasks, mode,
implementation/check results, review, human acceptance, publication evidence and
next action. Keep verification, acceptance and publication distinct; a completed
task does not authorize the next delivery. Preserve valid evidence and unrelated
work. Change scope/design through [factory-project-plan](../factory-project-plan/SKILL.md), not a
progress update.

Use one designated writer for each record. Native subagents return evidence to
their coordinator; independent workers write only their assigned checkpoints.
Reread before writing and reconcile concurrent edits. Reuse a checkpoint already
saved by `factory-git-commit` or another authorized writer; do not duplicate its update.
Verify saved results and report partial failures separately from successful Git
publication. Return source links, saved/pending checkpoint and next action.
