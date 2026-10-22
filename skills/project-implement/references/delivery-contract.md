# Delivery destinations and closure

Use this agreement for a selected delivery, whether implemented directly or by
independent workers. Reuse explicit choices; resolve only missing decisions that
affect the work. Keep it in the delivery issue or local Next delivery section,
with initiative-wide defaults linked once. During discussion, unresolved choices
can stay in the conversation; do not initialize storage just for this agreement.
Changes follow the owning planning workflow, not routine progress updates.

## Destinations before implementation

Distinguish these destinations even when they coincide:

- Working repository/branch and starting base; pin the starting SHA at launch.
- Integration repository/branch, if a combined integration is needed.
- Intended PR head repository/branch and target repository/base, if publication
  is in scope. A PR into a fork and one upstream can have different bases.
- Destination of versioned code, docs and examples: an intended delivery/PR, or
  explicitly local-only validation material with its storage/exclusion choice.

A compact map is enough; no PR number or branch creation is required during
planning. One PR may contain several related artifacts. Local-only work needs
no invented PR. Resolve destinations before producing shared documentation or
integration examples; do not leave them as accidental leftovers. Do not copy
local-only artifacts into publishable branches or change ignore rules implicitly.
Record an agreed destination change in the owning delivery contract and tell
affected workers; an old assignment must not silently remain authoritative.

Review the actual outgoing diff against each intended PR base before opening it.
Combined integration checks do not prove that an isolated upstream PR contains
its prerequisites or excludes sibling deliveries and local-only artifacts.
Report missing dependencies or stale review coverage and resolve the affected
publication path; do not cherry-pick, rebase, merge, or run another full review
implicitly to manufacture readiness. Reuse relevant evidence and run only the
checks needed for the actual outgoing content.

## Reusable closure authorization

Implementation mode and Git authorization are independent. Unless already settled,
agree once whether Git remains per-request or the user authorizes a scoped closure
policy, for example: "For D1–D3, after I accept each delivery, commit, perform
post-commit review, push to the agreed fork branches and update its Linear issue;
ask separately for PR creation or merge." Default to per-request when unspecified;
do not make this question a prerequisite for ordinary implementation.

Record the user's authorized actions, covered deliveries and destinations, and
trigger (such as whole-delivery acceptance). Pass that exact scope to each worker;
a coordinator may relay user authorization but cannot grant it. Reuse it without
asking again while its conditions hold. A guided block approval is not acceptance
of the whole delivery. "Looks good", autonomous mode and YOLO do not create a Git
policy on their own. Material scope/destination changes or revocation require
reconciling the authorization before publishing. A fresh session must recover an
explicit recorded agreement or ask; it must not infer permission from task status.
PRs, merges and releases remain outside this closure unless explicitly authorized.

## Report facts and close the agreed scope

Use a compact checkpoint, not a new state machine or Linear status taxonomy:

> D2: implementation verified · review clear · accepted · pushed `abc123` to
> fork/branch · issue updated · PR pending · next: user requests PR

Name pending, failed, unknown or not-applicable facts honestly. Tie verification,
review and acceptance to the actual content; later substantive changes require
revalidation of affected work. A push is not a merge; a successful push can coexist
with a failed issue update. Detail belongs in the issue/local checkpoint, not in
every worker message or the design document. Before publication, provisional
state stays in the conversation under the existing publication rules.

Before claiming the authorized closure is complete, reconcile delivery-owned
staged, unstaged and untracked changes, artifact destinations, remote publication,
issue update, and PR/integration actions actually requested. List intentional
local-only outputs and unrelated edits separately; a globally clean worktree is
not required. Preserve others' edits. Name any missing action and its owner instead
of calling the whole initiative "done". Closing one delivery does not authorize
the next, a PR, or a merge.
