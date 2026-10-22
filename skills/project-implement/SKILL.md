---
name: project-implement
description: Implement or revise one planned delivery from local files or Linear in guided or autonomous mode, returning the result for human review.
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

When launched as an independent worker by `project-coordinate`, first read its
[implementer role](../project-coordinate/references/implementer.md). That assignment
defines reporting and ownership: keep shared context/plan documents with the parent;
own progress updates and comments on your assigned Linear issue after publication.
Handle commit/review/push with direct user authorization or a recorded, scoped
user agreement relayed in the assignment whose conditions hold. Report the
outcome to the parent instead of asking it for Git approval.
Do not interpret the coordinator defaults below as permission to spawn more agents;
the role permits only its bounded independent delivery review.

## Select the authorized delivery

Read applicable instructions and `.agent-context/context.md`, if present. Resolve
the selected plan's existing source through [project-context](../project-context/SKILL.md)
when needed. Reuse established choices; clarify competing sources before writing.
Do not migrate or mirror a plan as part of implementation.

Read the applicable project context, including for a Linear delivery, or reuse
its relevant contents already read in this session. A known link or assignment
summary alone is insufficient. Apply its criteria to implementation choices;
reconcile consequential conflicts with the plan instead of treating a task as
an automatic override. Respect explicit user exceptions and the criteria's scope.

For Linear, follow [Linear implementation](references/linear-implementation.md)
to read the plan and issue. Update its progress and post an issue comment only
after the user validates the work and it is committed, reviewed, and pushed.
Keep provisional progress in this conversation. Do not initialize local context
or run the local reader for this route.

For local plans, use the existing reader, resolving `SKILL_DIR` to this skill's
directory:

```sh
python3 "$SKILL_DIR/../project-plan/scripts/read_plan.py" --repo "$REPO" list
python3 "$SKILL_DIR/../project-plan/scripts/read_plan.py" --repo "$REPO" show initiative-id
```

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
selected delivery? Record the choice in local Next delivery or, for Linear, in
the conversation until the publication checkpoint permits saving it to the issue.
The user can change modes mid-delivery;
preserve completed work and adjust the next checkpoint. Autonomous
mode alone never authorizes additional deliveries or Git publication.

### Guided

Work through one small, meaningful code block at a time: a function, type, or
connected change the user can understand in one review, not an arbitrary line
count or an entire delivery disguised as a block. Briefly explain its purpose,
how it fits the design, and the code about to change. By default, apply that block,
run the checks meaningful at that point, and return control with file links and
an explanation of the important code and choices. Disclose any intentionally
incomplete integration; do not describe a partial block as a verified delivery.

If the user wants review before writing, present the proposed code or diff and
wait for confirmation before applying it. In either variant, discuss and correct
the current block and wait for the user's go-ahead before beginning the next.
A question about the code is not permission to advance. Do not implement future
blocks in the background while the user reviews. All writers for the current
block must have returned or been stopped before handing control back.

Keep the resume note current in local Next delivery or the conversation for
Linear: reviewed/applied block, outstanding checks or corrections, and proposed
next block. Keep a partially implemented task
active; a block review does not imply completion or acceptance of the whole
delivery. Replace this note as work advances instead of logging every exchange.

### Autonomous within the delivery

Complete the selected delivery, including integration, checks, and in-scope fixes,
without asking for approval of each code block. Resolve technical unknowns through
targeted inspection or research and follow existing conventions for routine
implementation choices. Bring consequential unresolved choices back to the user
under the discovery rules below. Present the integrated result for review when
the delivery is complete, then stop before another delivery.

## Inspect and coordinate

Inspect the branch, working tree, relevant code, and prerequisite evidence. Preserve
existing edits and distinguish them from this delivery's changes. Resolve actual
overlaps or incompatible work before writing; do not reset, stash, or switch away
someone else's work. Check plan assumptions against the current code.

For native subagent delegation within this session, the coordinator owns
integration, Git operations, plan updates, and user dialogue.
Handle small tasks directly. For substantial bounded tasks, use fresh native
subagents with the minimum necessary context; prefer a fresh context over the
full planning conversation when supported. No custom agent role or model is
required by this skill. If delegation is unavailable, work directly and report it.

Give each worker the repository path and relevant plan excerpts or links,
assigned delivery/task/requirement IDs, collaboration mode and current checkpoint,
design constraints, prerequisites,
explicit read-only or editing scope, owned files or areas, and expected checks.
Request changed paths, observed
check results, unresolved issues, and a concise explanation of the result.
These native subagents must stay within their assignment, report challenges to the coordinator,
and return without starting another task, spawning workers, changing the plan,
or committing/pushing. They must preserve others' edits in the shared checkout.
For these native subagents, only their coordinator writes Linear documents and issues.

In guided mode, scope writers to the current block; delegate bounded read-only
investigation when useful without deciding future blocks for the user. In autonomous
mode, parallelize independent tasks within the active delivery, with disjoint write
ownership. Serialize dependencies and shared-file changes; coordinate broad
formatters, generators, and dependency updates. Do not delegate tasks from later
deliveries or start their preparatory implementation while awaiting human review.
Inspect each returned diff before integrating or using it as a prerequisite.

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
in-scope fixes; report failed, skipped, or unavailable checks honestly. For local
plans, update states and evidence using the
[local plan format](../project-plan/references/plan-format.md). For Linear, report
provisional outcomes in the conversation; defer description, checklist, state,
and comment writes until the publication checkpoint in the reference above.

In either mode, once implementation and checks are complete, present the delivery
as awaiting user review. For local plans, mark verified tasks done, keep Next
delivery on this delivery, and keep the initiative active. For Linear, leave the
saved issue unchanged until reviewed work is committed and pushed. Do not advance
to later work or claim acceptance before user review. Report actual blockers and
unfinished checks instead of claiming a review-ready result.

## Review the delivery independently

After completing the selected delivery and its checks, use
[project-review](../project-review/SKILL.md) before the final user/coordinator handoff,
unless the user opts out or valid review evidence covers the identical target.
An explicit request for another review requires reading the current review skill
and invoking that pass; an earlier clean result does not satisfy the request.
Invoke the reviewer directly with fresh context; no orchestrator approval is needed.
This reviews the cumulative delivery, including uncommitted work when present,
not each guided block or partial commit. Respect its one full pass and at most one
focused follow-up. Assess findings, apply in-scope corrections in the agreed mode,
and disclose unresolved issues. Review does not authorize commit/push or replace
user acceptance. `git-post-commit` remains a separate bounded commit fine-tuning step.

## Present the completed delivery and stop

Finish with the implemented outcome, a short technical explanation, an ordered
guide to the important diff, checks and results, and any limitations or decisions
still needed, plus the independent review target, outcome and remaining findings.
Include the plan path or Linear plan/issue URLs and how the user can
try the change. Present one integrated review surface, not a stream of worker reports. All workers for
the delivery must have returned or been stopped before this review handoff.

Report the delivery agreement's compact factual checkpoint and remaining action.
Wait for user review; after acceptance, execute any already-authorized closure
whose conditions hold without asking for the same permission again. For requested corrections,
reopen affected tasks at the appropriate checkpoint, fix and verify them, and
present the same delivery again. Record acceptance only when the user gives it;
propose the next delivery without starting it. Validation alone does not request
a commit unless an explicit scoped closure policy already authorizes it at that
checkpoint. Use `git-commit` for that authorization or a direct request; it reviews and pushes
by default; honor local-only requests. After successful push of user-reviewed work,
update Linear through its publication checkpoint. PR creation, release publication,
and merge remain separately authorized actions.
