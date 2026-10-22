---
name: project-review
description: Independently review a complete implementation delivery against project context, its agreed plan and Git base before handoff or PR creation. Use from an implementer or for an explicit delivery review, including uncommitted work; not for per-commit fine tuning.
---

# Review a delivery

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Review the whole delivery, not just its latest commit. No PR is required. The
implementer invokes a fresh reviewer and owns corrections and user dialogue.
If already acting as the delegated reviewer, follow the
[reviewer role](references/reviewer.md) directly; never launch another reviewer.
Review alone authorizes no source edits, commits, pushes, PRs, or Linear writes.
An explicit request for a new review authorizes that pass even if an earlier
review covered unchanged code; do not substitute the previous result.

## Establish the review target

Reuse the selected delivery and source locations. Read applicable project
instructions, context and plan/issue; use `project-context` when the authoritative
location is unresolved. Follow the [reviewer role](references/reviewer.md)'s
independent-source rule.
Do not start discovery or a new plan.
Preserve scope exclusions and test responsibilities, including guarantees owned
by core libraries, dependencies, tooling or another repository.

Select the review's purpose and destination first: combined integration or the
intended PR target. Use its agreed repository/branch and pin the target commit,
merge base and implementation HEAD; an integration branch is not required for a
PR-only delivery. Do not assume `main` or select a base that hides earlier delivery
commits. If these differ from the assignment, explain and resolve uncertain scope
before review. Inspect the cumulative diff from that merge base and relevant
target-branch changes for integration conflicts. Source review does not prove
that the merged result builds or works. When integration and PR targets differ,
do not claim coverage for both from one diff; publication inspects the actual
outgoing content and reuses only applicable evidence. A changed target does not
automatically authorize another full review or reset the follow-up budget.

Uncommitted work is valid input: include intended staged/unstaged edits and
untracked source files explicitly, excluding credentials, ignored runtime output
and unrelated changes. Record HEAD, selected paths, status and a content fingerprint
of the reviewed diff and included untracked files. A commit SHA alone does not
identify a dirty review target. Freeze edits while the reviewer reads it. If the
target changes, mark the result stale for the affected content rather than claiming
that the new code was reviewed. Do not commit or stash just to create a review target.

## Invoke a fresh reviewer

Read `${XDG_CONFIG_HOME:-$HOME/.config}/factoryfq/config.json` when present. Resolve
`workers.types.reviewer.model` and `reasoning_effort`, defaulting to `gpt-6-astra`
and `high`; an explicit user choice takes precedence. Preserve the implementer
and orchestrator models. This is a native read-only subagent, not an independent
Herdr worker; `workers.yolo` does not configure or broaden its permissions.

Use the harness's native delegation API with a fresh context and explicit model
and reasoning settings. For an API exposing these fields, use `fork_turns: "none"`,
`model`, and `reasoning_effort`. Do not inherit the implementation transcript or
silently substitute a model. If delegation/model selection is unavailable, report
the limitation and let the user choose a supported reviewer or a separate session;
an implementer's self-check is not an independent review.

Provide a bounded assignment:

- Absolute repo/worktree path, branch, pinned target/merge-base/HEAD and dirty
  snapshot details, with the exact paths allowed in this review.
- Agreed delivery/task IDs, objective, acceptance criteria, relevant instruction
  and authoritative plan/context paths or URLs/IDs, exclusions, known decisions
  and explicit user exceptions. Excerpts may orient the reviewer, but must retain
  source locations so it can independently consult the applicable context.
- Checks already run and actual results, plus known gaps; distinguish author
  reports from evidence the reviewer can inspect.
- The absolute path to the reviewer role; read-only scope, no delegation or
  external writes, expected result below, and whether this is the first or follow-up pass.

Keep the worker's own read-only tools available for relevant evidence. No new
worktree is needed for source inspection. Checks that generate files need an
isolated snapshot of the exact reviewed content, prepared by the implementer only
when useful. A clean checkout omitting dirty changes is not that snapshot. Do not
install dependencies or run network/integration suites merely to make a review
look complete; report verification gaps when isolation or prerequisites are absent.

## Evaluate findings and bound corrections

The reviewer checks correctness/regressions, agreed requirements and exclusions,
fit with project-context criteria, integration assumptions, meaningful validation,
and whether the delivery is understandable and reviewable. Evaluate both missing
behavior and unjustified additions. A plan can itself conflict with project
criteria; surface that conflict rather than approving code merely for matching it.
No cosmetic refactors, speculative features, or tests of dependencies/toolchain
guarantees without a concrete new risk.

Require a concise result tied to the pinned target: `no actionable findings`,
`findings`, or `incomplete`, coverage/limitations, and checks actually performed.
Briefly identify the context source and relevant criteria actually checked;
do not paste a checklist or copy the context into the result.
Each finding gets a stable ID, severity, file/line, failure scenario or unmet
requirement, evidence and a bounded correction direction. Questions and uncertain
risks are labeled as such, not presented as proven bugs. No finding quota and no
approval stamp that implies user acceptance, merge readiness or successful CI.

For a standalone review request, return findings without applying corrections.
An already authorized implementer evaluates each finding, fixes supported defects within scope,
and explains rejected findings with evidence. Guided corrections go through the
user's normal block checkpoint; autonomous mode permits in-scope corrections.
Scope/product/API changes follow the existing escalation route. The review does
not authorize additional deliveries, Git publication or skipping human review.

Allow one full pass and at most one focused follow-up for this delivery. Reuse
the reviewer for that follow-up, supplying its finding IDs, dispositions, updated
target and correction diff. It checks those corrections and regressions they
introduce, without restarting the whole review. Declining a finding requires
evidence; unresolved disagreements go to the user/coordinator rather than a loop.
After the follow-up, report remaining defects or unverified fixes explicitly.
Do not reset the budget by spawning another reviewer or after every commit; a new
full pass requires a user request. Later unrelated changes invalidate relevant
review coverage and must be disclosed.

## Return the result

Give the implementer the compact review and finding dispositions. It includes
the reviewed target, relevant checks, unresolved items, and whether corrections
were rechecked in its user handoff and final coordinator report. Full exchanges
stay with the implementer; do not create a new review ledger or post comments to
GitHub/Linear from the reviewer. Existing publication checkpoints can summarize
the review after validated work is committed and pushed. If later commit fine
tuning changes reviewed behavior, disclose the coverage gap; do not silently
start another review cycle. PR creation and merge remain user-requested actions.
