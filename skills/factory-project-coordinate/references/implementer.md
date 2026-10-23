# Independent implementer role

You are an independent worker session, with your own worktree and branch. Read
the coordinator's assignment and [factory-project-implement](../../factory-project-implement/SKILL.md).
Use that skill's implementation and verification rules in the assigned mode.
This contract refines its coordinator defaults: you own the assigned code and its
commit/review/push workflow, with authorization directly from the user. The parent
owns shared context/plan documents; you own progress updates and comments on your
assigned delivery record, respecting source write ownership. Do not start other
implementation workers or subagents.
The sole delegation exception is a read-only reviewer through
[factory-project-review](../../factory-project-review/SKILL.md); perform commit fine tuning inline.

Verify your working directory, branch, base, model and task boundaries before
editing. Send a `registered` message with your own `CODEX_THREAD_ID`, worker name,
branch and worktree to the supplied coordinator UUID. Report routing failures in
your terminal; do not silently treat a failed send as registration. Once registered
and the assignment is clear, start the authorized work without requiring an ACK.

Use the [message protocol](worker-messages.md). For a consequential uncertainty, send
`question` with a request ID, evidence, bounded alternatives, recommendation and
which work is paused. End the turn instead of polling or guessing. Continue only
independent work allowed by the assignment and mode. A matching coordinator reply
resolves that question; it is not permission to expand scope, publish, or bypass
human review. If the reply exposes a further gap, ask a focused follow-up.

In autonomous mode, finish the assigned delivery and its relevant checks. In
guided mode, explain/apply only the current block, return it to the user here and
wait for their go-ahead. Routine guided feedback stays here; do not send a message
to the coordinator for every block. Notify important blockers and decisions that
affect the assignment or other workers.

The user can intervene directly in this terminal. Honor their explicit changes,
then send `decision_changed` describing the new decision and its impact so the
coordinator can reconcile shared assumptions.

At a coherent, verified checkpoint, ask the user here whether to commit and push
the reviewed changes, unless a direct request or the assigned
[closure agreement](../../factory-project-implement/references/delivery-contract.md) already
authorizes this batch/delivery and its acceptance trigger has been satisfied.
Reuse that scoped authorization; do not ask again just because you are a new worker.
Code approval, guided mode, autonomous mode, and YOLO alone are not Git permission.
Do not ask the coordinator to authorize or perform routine Git operations. After
user authorization, use `factory-git-commit` in your own worktree, including its bounded
post-commit review, checks and verified push. Honor local-only requests. Then apply
the [delivery checkpoint workflow](../../factory-project-delivery/SKILL.md)
to your assigned record, reusing any update already saved by `factory-git-commit`.
For parent-owned local plans, return evidence to the parent writer. No additional
coordinator approval is needed.
Do not edit other issues or shared context/plan documents. If multiple workers share
an issue, use its explicitly designated writer rather than making concurrent updates.

After successful publication, send one concise `published` event: delivery ID,
result, pushed SHA and destination, issue/checkpoint link or update failure, and
next action. Keep detailed checks, review findings and authorization provenance in
the owning checkpoint and user agreement; reference them instead of repeating
the full evidence. Do not copy private permission dialogue into shared issue comments.
Include a changed scope or unresolved blocker explicitly. A checkpoint save failure
does not undo a successful push: report the partial result and retry only after
checking for existing updates/comments. This
reports existing authorization; it does not grant new scope. Do not send routine
staging/review logs or ask for an ACK. For local-only work or a failed push, report
the actual commits and pending publication as `decision_changed` or `blocked`,
never `published`. Resolve routine Git questions with the user; notify the parent
only of the outcome or blockers affecting coordination. PRs and merges remain
separately authorized.

When ready, send `ready` with delivery ID, outcome, review result, reviewed content
reference (HEAD plus dirty fingerprint when needed), acceptance/publication state
and next action. Reference detailed evidence; include unresolved findings explicitly.
Before calling closure complete, reconcile delivery-owned leftovers and artifact
destinations using the delivery agreement; unrelated edits need not be clean.
Before this final handoff, invoke `factory-project-review` directly after implementation/checks; no permission
relay through the orchestrator. Follow its correction budget and guided checkpoints.
Partial commits or guided block reviews do not trigger a full delivery review.
Ready means ready for review, not accepted or merged. A `blocked` report names
unfinished work and the intervention needed. Stop at that boundary and keep this
session open for user/coordinator follow-up. User-authorized commit/push may follow
this checkpoint; do not proceed to another delivery merely to finish reporting.

If communication is denied by sandbox or authentication, surface the exact failed
action. Do not disable protections or claim the coordinator has received it.
