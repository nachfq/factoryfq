---
name: project-coordinate
description: Coordinate independent interactive Codex workers with separate branches and worktrees, including parallel implementation, questions, and sequential human review. Use when asked to launch or coordinate workers, not for ordinary single-session implementation.
---

# Coordinate independent workers

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Act as coordinator in the user's current session, keeping its selected model.
Workers are independent interactive Codex sessions, not native subagents. They
remain accessible to the user. Start only the work the user authorized; a request
to assess parallelism authorizes inspection, not worker execution.

## Select and bound the work

Read applicable instructions and reuse relevant context and its established source.
Use `project-context` only to resolve a missing source or association, or requested setup.
Read the selected plan, issues, current code, Git state, and prerequisite evidence.
Read the applicable project context if not already available in this session;
knowing its location is not knowing its criteria. Check the proposed assignments
against those criteria, and resolve consequential conflicts before dispatch.
Use [project-plan](../project-plan/SKILL.md) for consequential revisions, including
its context-exception and verification decisions; do not defer unresolved planning
conflicts to implementers or reviewers. This is not a mandatory new planning phase.
Explicit requests to implement named deliveries are sufficient scope.

Check whether the work is actually independent: agreed interfaces, prerequisite
code, testability, and file ownership. Do not manufacture parallelism or treat
worktrees as protection against incompatible API changes. Resolve shared interfaces
before launch; assign shared files by section or serialize their changes. A task
explicitly deferred in the plan needs an agreed scheduling revision before launch.

For each worker, state its outcome, task IDs, owned files/sections, exclusions,
checks, and collaboration mode. Reuse the user's preference; if unspecified, ask
once for guided or autonomous implementation of the selected scope. Guided workers
stop after each block for the user; autonomous workers complete only their assigned
delivery. Read-only review by the coordinator is not the user's acceptance.

Resolve the [delivery destinations and closure agreement](../project-implement/references/delivery-contract.md)
before launch. Choose a verified starting commit containing accepted prerequisites
for each worker, using a shared base where needed. Distinguish work branches,
combined integration and intended PR targets, including upstream versus fork.
Give shared docs/examples an explicit destination. Do not include uncommitted edits
implicitly or reset the main checkout. Check CI triggers against the actual PR bases.

## Configure and launch

Read `${XDG_CONFIG_HOME:-$HOME/.config}/factoryfq/config.json`. The optional `workers`
object has `worktrees_root`, boolean `yolo`, and `types.<role>.{model,reasoning_effort}`. Defaults are
`~/.local/share/factoryfq/worktrees`, role `implementer`, model `gpt-6.1-sol`, and
reasoning `high`. Explicit per-task choices override configuration, then defaults.
Do not change the coordinator's model or silently substitute an unavailable model.
This launcher creates independent `implementer` sessions. The separate
[project-review](../project-review/SKILL.md) workflow defines a native read-only
`reviewer`, configured under `workers.types.reviewer`. A config entry alone does
not create a new worker capability.

`workers.yolo` defaults to `false`: preserve Codex's configured permissions.
When `true`, launch workers with `--dangerously-bypass-approvals-and-sandbox`.
This controls execution permissions only; guided checkpoints, scope and publication
rules still apply. Reject non-boolean values rather than interpreting string truthiness.
Changes apply on launch or explicit resume, not to already running sessions.

`workers.herdr.layout` selects `agent` (default, one pane) or
`agent-nvim-lazygit` (implementer left, Neovim with LazyGit right, same worktree).
Apply only through the Herdr adapter; explicit task preferences override config.
The editor layout does not change worker permissions or collaboration mode.

The worktrees root must already exist and be writable. It may be a symlink to a
larger disk; a missing/broken link or unmounted destination is a setup problem,
not permission to create storage elsewhere. Use `ROOT/OWNER/REPO/WORKER`, deriving
repository identity from the intended Git remote. Resolve ambiguous identity.
Validate name components and path containment, including symlinks; never accept
path traversal. Use a short stable name such as `issue-123-pools` for the worktree,
terminal and Codex chat, with branch `work/issue-123-pools`.

Read [Codex and Herdr sessions](references/codex-herdr.md) when launching or
resuming sessions. Keep terminal UI details there. Future adapters may
use another terminal without changing role contracts. Do not use Orca tooling or
silently substitute native subagents/background exec sessions for visible workers.

Provide a compact assignment containing:

- Worker name/role, coordinator thread UUID and expected worker model/mode.
- Working repo/worktree/branch and starting SHA; integration destination and PR
  head/target repos and branches, plus code/docs/example destinations.
- Applicable instruction paths (including relevant ancestors of the original
  checkout), authoritative context/plan/issue links, and relevant decisions.
  Highlight the context criteria affecting this delivery and any explicit user
  exceptions; the highlights do not replace reading the relevant source.
- Outcome, task/requirement IDs, owned files/sections, boundaries, checks and
  prerequisite evidence. Do not pass the entire coordinator transcript.
- Any user-selected review exception or suspension, with its scope. Relay it
  explicitly so workers do not apply the default review cycle to that work.
- The absolute path to [the implementer role](references/implementer.md), which
  the worker must read before using `project-implement`.
- Git ownership and the exact user-authorized closure policy, scope and trigger.
  Implementers reuse applicable permission or ask the user directly, then own
  commit/review/push, assigned Linear issue updates and the outcome report.
  Assign one writer per issue when workers share it. The coordinator owns shared
  context/plan documents; PRs and merges require separate authorization.

For ignored local plans, supply their original absolute paths as read-only inputs;
they are not automatically present in a worktree. Do not copy or symlink shared
mutable context into each worktree. Each worker keeps its own build/test outputs.

## Questions and results

Use the [worker message protocol](references/worker-messages.md) for exchanges.
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
Implementers also own their assigned Linear issue's publication checkpoint. On
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
