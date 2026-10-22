---
name: git-pr
description: Push a working branch and create or update its GitHub pull request, reviewing the full change and reporting CI status. Use when asked to open or update a PR.
---

# Publish a pull request

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

A request to open or update a PR authorizes pushing its committed changes and
creating or editing that PR. A request only to draft or review does not authorize
remote writes. Do not commit local edits, merge, enable auto-merge, force-push, or
change repository policies as part of this workflow.

1. Read project instructions and the PR template. Inspect branch, status, remotes,
   and the target GitHub repository. Resolve head and base explicitly: use the
   user's current explicit head/base choices, otherwise the agreed publication
   target (head/target repository and branch). Use the remote's default branch only
   when no PR base was selected.
   Do not substitute an integration branch for a distinct upstream PR target.
   Ask only when the target
   is ambiguous, such as an unclear fork destination. Do not publish a PR from a
   base branch or detached HEAD. If the base does not exist, report the missing
   setup rather than inventing history.
2. Fetch relevant remote refs and review all commits and the complete diff from
   the merge base to the proposed head, not just the latest commit. Confirm the
   change fits the requested scope and contains its prerequisites; combined
   integration checks do not prove each isolated PR works. Account for all intended
   code/docs/examples and exclude agreed local-only validation artifacts.
   Surface unexpected commits or sensitive files
   before publication. Local staged, unstaged, and untracked changes stay untouched
   and outside the PR. If the requested change depends on them, resolve that gap
   with the user before publishing. Do not create an empty PR.
3. Verify the committed content with relevant checks, reusing valid results for
   the same content. Do not attribute checks on a dirty working tree to committed
   code; use an isolated checkout when needed or state what remains unverified.
   Report failures accurately. For a known blocker, propose a draft PR rather than
   presenting the change as ready; honor an explicit draft request.
4. Find an open PR for the exact head repository/branch and base before creating
   one. Push any unpublished commits to the intended remote without rewriting
   history; if the branch already matches, reuse it without a redundant push.
   If the push is rejected, inspect and report the divergence rather than forcing
   it. If a remote operation has an uncertain outcome, read back before retrying.
5. Create the PR or update the matching one to reflect the full resulting change.
   Use a concise Conventional Commit title in English and follow the project's
   language and template for the body. Explain the problem, resulting behavior,
   verification actually performed, and material limitations. Scale detail to the
   change; preserve human-written notes, issue links, and review checklist state.
   Do not invent issue-closing intent or mark unchecked work complete. With gh,
   pass multiline bodies through a temporary file and --body-file.
6. Verify the PR URL, head SHA, base, and draft state. Inspect CI for that head SHA
   and report passed, failed, pending, absent, or unavailable checks distinctly.
   Pending or absent checks are not success. Report the current snapshot without
   waiting indefinitely; monitor to completion only when requested. Do not fix CI
   or start another implementation cycle as part of PR publication.

Return the PR link, head/base branches, what was published or updated, verification
and CI status, and any local changes left out. Report partial success explicitly.
