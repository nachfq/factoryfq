---
name: git-commit
description: Stage, commit, review, and push changes on a suitable working branch when the user asks to commit, unless local-only work is requested.
---

# Commit changes

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

An explicit scoped closure policy also authorizes this workflow when its stated
acceptance trigger and delivery/destination scope hold; see the
[delivery agreement](../project-implement/references/delivery-contract.md).
Reuse that user authorization rather than asking again. Commit only the accepted
content covered by that policy, preserving unrelated staged and working-tree edits;
resolve mixed changes that cannot be safely isolated. The stage-all default below
applies to an unscoped commit request, not to scoped closure. Code approval alone
does not establish such a policy.

A request to commit authorizes this workflow, including a push after verification
and post-commit review, unless the user requests local-only work or no push.
Review-only requests do not authorize staging or committing. Respect explicit scope and previously agreed
file exclusions; never include credentials or machine-local state.

1. Inspect the current branch, status, staged and unstaged changes, and untracked
   files before changing the index. If nothing is staged, include all changes
   (including additions and deletions), except agreed exclusions and ignored files.
   If anything is already staged, ask whether to include all changes or commit
   only what is staged, unless the user already explicitly chose for this request.
   Wait for the answer before changing the index or committing. For staged-only,
   preserve the exact staged content, including partially staged files. If an
   excluded file is staged, leave it out of the commit while preserving its edits.
2. Check that the branch fits the selected changes. Never commit on main, master,
   or the repository's default/integration branch. Use a descriptive working branch
   such as feature/add-login, bugfix/token-expiry, or chore/update-dependencies,
   following project naming conventions. On a base branch, create a suitable branch
   when its name and starting point are clear. If the current working branch is
   unrelated, HEAD is detached, or the correct base is unclear, propose a branch
   and ask before switching; do not rename or move unrelated work implicitly.
3. Group selected changes by functional purpose, keeping related implementation,
   tests, and documentation together. Run relevant checks, reusing valid results
   for unchanged content. Do not bypass hooks or conceal failed checks.
4. Use Conventional Commits: type(scope): description, with an optional scope.
   Write concise English imperative descriptions. Use feat for features, fix for
   bug fixes, and docs, refactor, test, chore, ci, build, perf, or style as appropriate.
   Mark breaking changes with ! and explain the incompatibility in the body.
   Example: feat(skills): add git commit workflow.
5. Stage the selected content and review each final staged diff before committing.
   Preserve all excluded or unselected edits. Do not amend, rewrite history, or
   discard changes unless explicitly requested. Inspect state before retrying a
   failed commit.
6. After successful commits, use [git-post-commit](../git-post-commit/SKILL.md)
   once for this execution, unless the user opts out. Pass the exact commit hashes,
   original objective, exclusions, and checks already run. This includes bounded
   corrections and one follow-up commit when needed, not a recursive commit cycle.
7. Once relevant checks and review are resolved, push the reviewed commits,
   including any verified correction commit, unless local-only was requested.
   Ensure the checks apply to the committed content; results that relied on
   excluded working-tree edits are not verification of the published code.
   Reuse evidence for identical content or verify an isolated checkout when needed,
   preserving local edits; unresolved validation leaves the push pending.
   Verify the intended remote's push URL and working-branch destination; use the
   user's fork when applicable, never infer an upstream publication target.
   Do not push to a default/integration branch. If the destination is missing or
   ambiguous, ask rather than creating a remote or guessing. Inspect the entire
   outgoing commit range; resolve unexpected unreviewed commits before publishing.
   Push an explicit branch ref without force and set tracking on first push.
   On rejection, report the divergence; do not force, rebase, or merge implicitly.
   After a failed or uncertain response, inspect remote state before retrying.
   Verify that the remote branch points to the intended commit. Unresolved checks
   or review findings stop automatic publication; report the local commits and gap.
8. If this work has an explicitly selected delivery, use
   [project-delivery](../project-delivery/SKILL.md) to record the user-reviewed work
   actually published, following source timing and assigned writer ownership.
   Do not discover a delivery for an ordinary commit. If another writer owns the
   record, return evidence to that writer; never duplicate updates. Report failed
   or local-only publication accurately without claiming a published checkpoint.

Report the branch, commit hashes and subjects, verification results, and any
remaining uncommitted changes. Include the push destination and verified result
or why publication is pending. A commit/push request does not create or update a
PR description; use `git-pr` when requested.
