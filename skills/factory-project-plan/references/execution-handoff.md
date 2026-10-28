# Prepare an agreed plan for execution

Read when the user requests implementation of a selected plan or milestone,
especially when it is still a draft or lacks delivery records. The main session
owns this transition through `factory-project-plan`; assigned workers report gaps
to their coordinator rather than creating shared plans or issues themselves.
Planning alone still does not authorize implementation.

## Prepare the authorized scope

Read the current context, plan, delivery records and actual checkout. Reuse the
user's choices; do not repeat the discovery interview. Match the execution request
to named outcomes. A request to complete an agreed milestone authorizes its bounded
deliveries and the planning records needed to execute them, not unchosen ideas.
Resolve missing consequential decisions; routine task detail can be completed
within the agreed design. Record changed agreements in their owning artifacts.

Use the selected source's writing procedure before code edits or worker dispatch:

- **Linear:** follow [Linear plan writing](linear-plan-writing.md). Find and reuse
  existing issues, or create one per agreed delivery with its tasks, criteria and
  actual dependencies. Move task detail out of the draft into those issues and
  link them from the plan. Read back and verify the saved records. Creating planned
  work does not require a commit or push; the publication rule applies to later
  execution updates, not issue creation. An issue is not implemented or accepted
  merely because execution was authorized.
- **Local:** follow [local plan format](plan-format.md). Complete the authorized
  deliveries' tasks, checks and handoff in the existing plan; create no second tracker.

If required records cannot be prepared, report the missing step and pause affected
execution rather than silently using a document-only or local fallback. Partial
saves must be reconciled before retrying. Keep later, unchosen work tentative.

## Select the execution workflow

Keep the current conversation as coordinator when the user wants to continue here:

- For independent/full agents or separate interactive worktrees, use
  [factory-project-coordinate](../../factory-project-coordinate/SKILL.md).
- For direct implementation, including ordinary native subagent delegation, use
  [factory-project-implement](../../factory-project-implement/SKILL.md).

Autonomous scope does not select an agent mechanism. Honor an explicit mechanism;
if it cannot be launched, explain the blocker before proposing a substitute.
Do not describe native subagents as independent interactive sessions.

Carry the authorized deliveries, guided/autonomous mode and human review boundary
into the assignments. Default to human review after each delivery. An explicit
request to complete a milestone autonomously permits continuing through its
deliveries after prerequisite verification and required independent review, with
human acceptance pending at the agreed boundary. Existing user-requested holds and
guided checkpoints still apply. Parallelize only genuinely independent work;
verified prerequisites and available code still govern dependent work.

Execution permission does not grant commits, push, PRs, merges or deployment.
Resolve Git/base prerequisites through the selected workflow before launch.
