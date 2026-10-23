# Read a Linear delivery

Use this reference only for a plan stored in Linear. The calling workflow defines
guided and autonomous behavior; storage does not change its review boundaries.
The plan document owns intent and design. Its delivery issue records validated,
published progress. Provisional local work stays in the conversation, with no
local mirror or second tracker.

## Read and select

Reuse relevant context and the verified repo/project association. Use
[factory-project-context](../../factory-project-context/SKILL.md) only if that source or association
needs resolving; recheck when the repo, destination or relevant evidence changes.
Read the project's context document if its contents are not already available
in this session; reading an issue and its plan does not substitute for it.
An explicit issue ID or URL is a useful entry point:
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

## Resume and write boundary

When resuming, read the issue first, then reconcile it with the actual branch,
working tree, and available conversation. The issue describes the last published
checkpoint, not all local edits. Resolve unexplained local work before repeating
or overwriting it; do not infer that unchanged Linear tasks mean no work exists.

Keep provisional progress in the conversation. Do not update the issue on start,
block completion or readiness for review. Normal persistence requires human
validation, commit, post-commit review/checks and verified push. Local-only commits
or failed pushes leave the issue unchanged. An explicit request to save a blocker
or provisional update may override timing, without claiming publication.

Only when that write boundary is reached, read
[Linear publication](linear-publication.md) for safe updates, state mapping and
comment deduplication. Do not load it merely to start or resume implementation.
If the selected plan/issue cannot be located from established references, consult
[Linear plan format](../../factory-project-plan/references/linear-plans.md) as needed;
reading a delivery does not require loading plan creation procedures.
