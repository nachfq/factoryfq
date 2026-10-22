# Implement a Linear delivery

Use this reference only for a plan stored in Linear. The shared skill defines
guided and autonomous behavior; storage does not change their review boundaries.
The plan document owns intent and design. Its delivery issue records validated,
published progress. Provisional local work stays in the conversation, with no
local mirror or second tracker.

## Read and select

Reuse relevant context and the verified repo/project association. Use
[project-context](../../project-context/SKILL.md) only if that source or association
needs resolving; recheck when the repo, destination or relevant evidence changes.
Read the project's context document if its contents are not already available
in this session; reading an issue and its plan does not substitute for it.
Follow the
[Linear plan format](../../project-plan/references/linear-plans.md) to locate the
selected plan and issue. An explicit issue ID or URL is a useful entry point:
read that issue and its linked plan, and verify project, plan key, delivery ID,
and repository against the current checkout. A shared project does not authorize
changes in its other repositories.

Read the issue with relations (`get_issue(includeRelations=true)`; if selecting
fields explicitly, include `relations`). Read prerequisite issues only as needed
to establish readiness and prior review. Check their evidence against the actual
checkout: a completed dependency in Linear does not place its code on this branch.
Resolve missing prerequisite code or pending human acceptance before dependent
implementation; do not clear relations or mark dependencies done to proceed.

Reuse a clear user-selected delivery. For a request to continue, inspect its
current checkpoint before selecting later work. Resolve ambiguous selection,
missing acceptance criteria, or conflicting decisions before editing. Status,
assignment, and a ready plan are not execution authorization. Do not create a
replacement plan or issue when an existing artifact is missing or inaccessible.
If Linear is unavailable, report what cannot be read or saved; continue only
authorized work that does not depend on missing information, without a local copy.

## Publication checkpoint

The normal sequence is human validation of the local changes, commit, post-commit
review and relevant checks, successful push, then issue update and one comment.
Use [git-commit](../../git-commit/SKILL.md) when committing is requested; it pushes
after review unless local-only work was requested. Human validation alone is not
a request to commit unless an explicit [closure agreement](delivery-contract.md)
already covers that acceptance trigger, delivery and destination. Reuse applicable
authorization without asking for each step.

Until that sequence completes, keep progress, block feedback, blockers, proposed
next steps, and checks in the conversation. Do not automatically change the
issue's description, checklist, status, or comments on start, block completion,
or readiness for review. If the user requests local-only commits or push fails,
report the pending publication and leave Linear unchanged. An explicit request
to record a blocker or provisional update may override this timing; label the
actual local/unpublished state without claiming completion or publication.

When resuming, read the issue first, then reconcile it with the actual branch,
working tree, and available conversation. The issue describes the last published
checkpoint, not all local edits. Resolve unexplained local work before repeating
or overwriting it; do not infer that unchanged Linear tasks mean no work exists.

After the checkpoint, update only the user-reviewed work included in the pushed
commits. Preserve unrelated tasks and evidence. Reuse stable task IDs; check a
task only when its entire outcome and required checks are satisfied. A reviewed,
pushed block may still be only part of a task or delivery. Maintain a compact
**Execution** section in place with:

- Agreed collaboration mode and the reviewed/published task or block.
- Verified remote branch and commit links, plus relevant repo-relative paths.
- Checks actually run, their outcomes, and remaining checks or corrections.
- Separate facts for implementation verification, independent review, human
  acceptance, push, issue checkpoint and PR/merge where applicable; name pending
  work and its next owner/action. Do not add Linear statuses for these facts.
  A block review is not full delivery acceptance or permission to continue.

Replace superseded checkpoint notes rather than appending transcripts or a
duplicate checklist. Read `list_issue_statuses(team=...)` and use the team's
existing IDs and semantics: a partial published delivery remains in progress;
a fully accepted delivery becomes completed only when the team's other conditions
are satisfied. If merge or further review is required, use the appropriate
non-completed state and name what remains. Do not create statuses, mark other
deliveries complete, or update project status as part of this checkpoint.

## One comment for the published work

After saving the issue, post one short comment covering the reviewed and pushed
batch: what changed, relevant rationale, observed checks, commit links, and the
next step. Follow the project's language. Group related commits into one update;
do not post once for review, again for commit, and again for push. Do not copy the
description or include command logs. Never post project-level updates here.

A request to "post an update" targets the active issue by default. Comments are
selected history; the description is the current published checkpoint. Consult
history only for relevant rationale. Check recent comments for the same event
and commits before posting, reading further when needed. Use
`save_comment(issueId=ISSUE_ID, body=...)` and read back to verify the destination
and content. After an uncertain result, inspect before retrying to avoid duplicates.
Report comment failures separately from saved issue progress or successful push.

## Save safely and verify

Use one writer per issue. An independent implementer owns its assigned issue's
publication checkpoint; its coordinator does not repeat those updates or comments.
If several independent workers share one issue, designate a single writer before
writing. Native subagents return evidence to their coordinator, which writes for
them. Shared context and plan documents remain outside routine issue updates.
Before every update, reread the issue and reconcile other people's changes.
Use `save_issue(id=..., patch=..., state=...)` with only the fields being changed;
omit state if unchanged. Patch the existing checklist and Execution section,
adding the section only if absent. Preserve links, IDs, acceptance criteria,
relations, assignees, labels, project, and unrelated content.

Fresh reads and patches are not a lock. If another writer changes the same task
or decision incompatibly, resolve ownership before overwriting. On failed patch
anchors or an uncertain write result, reread and reconcile before retrying;
do not replace stale full descriptions or create another issue. Read back the
saved issue to verify its state, checkpoint, task evidence, and retained links.
Report unsaved progress or partial updates explicitly.

Ordinary execution does not edit the plan document. An explicitly requested
planning revision can update affected Specs, design, and issue tasks together
through [project-plan](../../project-plan/SKILL.md), preserving valid work. That
is distinct from publishing implementation progress. Do not silently rewrite
requirements to fit the code.

The user handoff includes the issue and plan links, a reviewable diff guide and
actual checks. Do not create per-block issues or routine notification comments,
assign other agents, launch independent sessions, or publish Git changes as a
side effect of updating progress.
