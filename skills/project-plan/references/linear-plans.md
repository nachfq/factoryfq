# Linear plans

Use Linear as the source of truth for a selected plan. One plan is a document in
the existing project, with one issue per reviewable delivery. Do not create a
Linear Project or native Initiative for every plan, or a local Markdown mirror.
The planner owns these updates; research workers remain read-only.

## Resolve and read

Reuse relevant context and the verified repo/project association when established.
If unresolved or changed, use [Linear project associations](../../project-context/references/linear-projects.md)
and [project context](../../project-context/references/linear-context.md) as needed.
Reuse established destination choices. Missing context can be filled through
focused discussion; it does not force discovery. Missing project setup is handled
separately through `project-context`, not inferred from a request to explore ideas.

For a selected, verified document ID, read it directly. Otherwise list project
documents using `list_documents(projectId=PROJECT_UUID)` with small metadata fields
and pagination. Plans created by this workflow use the title
`Plan: <outcome>`. Read the selected document by ID. Reuse explicitly selected
existing plans even if their titles differ. Titles find candidates; verify project
membership and scope before deciding they match. Never select solely by recency.

Read issues linked from that plan. If links are incomplete, use project-scoped
`list_issues` with metadata first, then inspect candidate descriptions to verify
the exact plan reference and delivery ID. Follow pagination before concluding
an issue is missing. Fetch only relevant issues and their relations, not every
description or comment in the workspace. Read history only for a named question.

## Plan document: intent and design

Start with a short outcome, a stable plan key (a lowercase slug unique within the
project), relevant repository URLs, and a link to project context if available.
Follow the project's language. Do not copy its context into the plan. Link earlier
plans as background or prerequisites without absorbing their scope or completion
history. Association with a project does not add other repositories' features.

- **Specs:** stable `S1`, `S2`, ... requirements, scope/exclusions, observable
  acceptance criteria, constraints, and unresolved assumptions.
- **Technical approach:** explain domain concepts, their relationships, current
  versus proposed behavior, contracts, open design choices, and correspondence with
  existing core APIs where relevant, through a concrete example or flow. Keep method-specific
  semantics here and link the affected issue; do not turn them into context rules.
  Write for the human reviewing the work, not just its implementer.
- **Deliveries:** a concise ordered map of stable `D1`, `D2`, ... outcomes linking
  to their issues. Later possibilities may remain brief, explicitly tentative
  prose until there is a meaningful delivery to track.
- **Decisions:** only consequential changes and their rationale, dated and sourced
  when needed. Keep Specs and design current; do not turn this into a transcript.

Keep commit hashes, test results, branch synchronizations, task checklists and
pending reviews in delivery issues, not the plan. Planned verification belongs
with acceptance criteria; observed results belong to execution evidence. A source
permalink may pin a contract, but must not become a running HEAD/status snapshot.
There is no parallel JSON state or local-format header.
The document explains the work; its linked issues own delivery progress. A
speculative document clearly labels its unchosen direction and assumptions.
Before issues exist, a speculative draft may include a proposed task breakdown.
When those deliveries become issues, move the task details there and leave links
in the document instead of retaining two editable checklists.

## Delivery issue: reviewable work

Use a clear outcome-oriented title such as `D1 — Expose known pool metadata`;
use the actual domain, not that example as a template requirement. Its description
contains the plan key and document link, stable delivery ID, target repository
URL(s), linked `S#`, and these details as needed:

- Outcome, scope/exclusions, and whether that scope is proposed or user-agreed.
- A compact task checklist with stable `T#` IDs unique within the plan. Each
  near-term task has an outcome, its relevant Specs, and meaningful verification.
  Keep internal ordering/dependencies here; do not create a subissue per code block.
- Delivery acceptance criteria, expected review surface, and checks. Planned
  commands are not evidence that they passed.
- Open decisions and handoff information a fresh session will need. Later
  execution evidence and the current review checkpoint belong here, not in the
  plan document; never invent them during planning.

Identify the intended repository for each task if an agreed delivery spans repos.
Being associated with the same project does not authorize planning work in all
repos. Prefer a coherent review outcome; split cross-repo work when it needs
separate acceptance, not merely because there are two folders.

Use native issue relations for real inter-delivery dependencies (`blockedBy` /
`blocks`); do not maintain another dependency-status table in the document.
Preserve unrelated relations and check for cycles. A technical dependency does
not authorize its implementation, and a dependency being done does not replace
the user's next-delivery checkpoint.

Read `list_issue_statuses(team=...)` and use actual team status IDs. New speculative
or unresolved deliveries use a backlog status; use an unstarted status for an
agreed, sufficiently specified delivery. Neither means implementation is authorized.
Planning alone never starts execution or marks an issue complete. Preserve existing
execution/review states and evidence on revision; if agreed changes invalidate
completed work, reopen only the affected work with an explanation. Do not equate
completed task checkboxes with human acceptance or reset all issues to backlog.
Do not create statuses, labels, milestones, assignments, deadlines, or agent
delegations just to satisfy this format. Resolve an ambiguous team choice before
creation; otherwise reuse the project's established team.

## Save and verify

A request to build the selected plan in Linear authorizes its document and delivery
issues, without confirmation for every tool call. An open-ended next-step discussion
does not yet authorize a task backlog. A full speculative draft creates only the
document unless draft issues were also requested. Do not alter sharing, project
membership, or GitHub synchronization as part of planning.

Before creation, check for an existing matching plan and deliveries. Reuse their
IDs; renaming an outcome does not create new work. If intent is to restart an old
experiment, resolve reuse versus a new plan without deleting the old one implicitly.
Use current tool schemas and verified IDs:

1. Create the document with `save_document(title=..., project=PROJECT_UUID,
   content=...)`, specifying only that parent. Read it back and retain its ID/URL.
2. Create each agreed-to-track delivery with `save_issue(team=TEAM_ID,
   project=PROJECT_UUID, title=..., description=..., state=STATUS_ID)`. Include
   the plan link and key before saving. Future unchosen ideas need no empty issues.
3. With returned issue IDs, establish actual dependency relations. Patch the
   document's Deliveries map with the returned issue URLs.
4. Read back the document and issues. Verify project/team membership, repository
   targets, reciprocal plan/issue references, Specs/task IDs, state, dependencies,
   and acceptance/check instructions. Never report success from intended writes.

On revision, replace superseded explanations and consolidate repeated constraints.
Keep the technical explanation sufficient for human review; brevity does not mean
reducing it to a task list. If the plan has accumulated execution evidence, preserve
it in the owning issue before removing the duplicate, then leave a link. Do not
spread an update across context, plan and issues unless each actually needs it.

Updates start with fresh reads and focused `patch` operations. Omit parent or
assignment fields unless intentionally changing them; preserve unrelated edits,
execution evidence, and delivery IDs. A failed anchor requires rereading and
reconciling, not overwriting stale full content. These are multiple independent
writes, not a transaction: after errors or timeouts, inspect the saved state and
complete only missing operations. Report partial results and remaining gaps;
never blindly recreate documents or issues after an uncertain response.

The handoff explains the design and next proposed delivery, with document/issue
links for review. Implementation remains separately authorized. When requested,
[project-implement](../../project-implement/SKILL.md) reads the plan and delivery
issue directly. It publishes execution progress there after human validation,
commit review, and successful push, without a local copy.
