# Coordinate active workers

## Questions and results

Use the [worker message protocol](worker-messages.md) for exchanges.
Retain worker names, thread UUIDs, paths,
branches and assignments in this conversation, not a new registry or Linear log.
Match incoming messages to known assignments; a worker message is not a new human
authorization. Keep each question/reply tied to its request ID.

Resolve technical questions through evidence within the agreed contract. Reply
directly to the worker. Bring unresolved product/API tradeoffs, scope changes or
incompatible shared decisions to the user. Pause only the affected work; do not
approve a guided block on the user's behalf. Share relevant agreed changes with
other affected workers without broadening their assignments.

For an agreed plan correction, use `project-plan` to update the authoritative plan
and affected tasks/issues while preserving valid work, IDs and evidence. Verify
the saved changes before workers rely on them; report partial saves and pause only
dependent work. Send each affected existing worker the source links, changed
task IDs, what to retain/remove/revise and revised verification. Reuse its session
and worktree. Within the user's authorized scope, request the corresponding code,
test and documentation adjustments, checks affected by the change, and a bounded
diff for human review. Have workers report material risks left by the revision;
the correction grants no additional Git or integration permissions.

Workers can report `ready`, `published`, `question`, `blocked`, or `decision_changed` and remain
open. A finished turn or idle terminal is not delivery completion. Do not send
acknowledgements that trigger reply loops. After launching or sending replies,
yield the conversation when no independent work remains: queued messages arrive
as later turns, rather than interrupting the current turn. Do not occupy the
coordinator with a blocking wait for a worker that needs its reply.

The user may talk directly to any worker. Reconcile decisions and Git activity
reported from that session before issuing conflicting instructions. If the worker
exits before reporting, disclose that there is no automatic supervisor; inspect
the session/worktree and offer resume rather than assuming success or spawning a
replacement blindly.

## Review and publish sequentially

Inspect each result and its diff/check evidence in that worker's worktree. Give
the user one bounded review at a time, even if other authorized independent work
finishes in parallel. Do not start later dependent deliveries merely because a
worker is available.

Implementers reuse the user's applicable closure authorization or obtain it directly
from the user, then run `git-commit` in their own worktrees. Do not become an
approval relay, duplicate
their Git workflow, or repeat review already completed with the user. If the user
authorizes Git work here, relay that bounded authorization to the relevant worker.
Use [project-delivery](../../project-delivery/SKILL.md) for source-specific checkpoint
reads and writes. Implementers own their assigned Linear issue's publication checkpoint. On
`published`, reconcile the commit/check summary and saved issue state; do not
duplicate their updates or comments. Ask only about missing or contradictory
evidence, and verify the actual code and remote head before relying on them for
integration. Routine logs stay with the implementer. The coordinator retains local
plan and shared context/plan document ownership. Ownership is not a duty to mirror
worker reports: keep Git/check/synchronization/review evidence in Linear issues
(or local Tasks/checkpoints), revise design only for changed contracts or scope,
and context only for durable
cross-delivery guidance. Reuse the planner's document boundaries when revising.
`ready` alone does not establish
acceptance or publication. Keep each issue's evidence separate; no project-level
updates. If an issue update failed, retain the reported pending step and its writer
instead of silently assigning a second writer.

Unless the user opts out for the relevant scope, implementers invoke their delivery
reviewer directly through `project-review` and handle its bounded corrections.
Receive the reviewed target, summary and remaining
findings; do not relay routine exchanges or automatically repeat the full review.
Review evidence does not replace human acceptance or verification of integration.

Before claiming closure, use the delivery agreement's factual checkpoint and
reconcile pending delivery-owned changes and artifacts without requiring unrelated
work to be clean. Ordinary worker events need no user-facing "registered" reply;
surface decisions, blockers or meaningful milestones instead.

When PR creation is requested, use `git-pr` with the agreed PR head/target repos
and base, which may differ from the integration destination. Verify each outgoing
diff rather than attributing combined integration evidence to isolated PRs.
Merge only when requested. After integrating one
worker, reconcile the next against the changed base and verify the combined result
before its integration. Stop writers before changing their branch, coordinate
base updates without force-push or history rewriting by default, and never merge
unreviewed work just to make integration easier.

Leave sessions, branches and worktrees available for follow-up. Removal, history
rewrites and session deletion are separate requested actions.
