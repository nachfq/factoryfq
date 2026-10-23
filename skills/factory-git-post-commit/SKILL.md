---
name: factory-git-post-commit
description: Review newly created commits for concrete defects and omissions, making a bounded correction commit only when needed. Use after factory-git-commit or when post-commit review is requested.
---

# Review committed changes

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Review the exact commits supplied by the coordinator against the original
objective. If invoked separately, resolve the requested commits first; do not
assume the whole branch is in scope. A review-only request permits findings, not
edits or commits. The factory-git-commit workflow authorizes the bounded corrections below.

This is commit fine tuning, not an end-to-end review of the feature branch. Keep
the supplied commits as its scope; use `factory-project-review` separately for a cumulative
delivery review. Always report the outcome, including when no correction is needed.

1. Inspect committed diffs and relevant surrounding code, documentation, and tests.
   Handle an initial commit as a diff against the empty tree. Record the branch,
   HEAD, and existing staged/unstaged/untracked changes before making corrections;
   local edits are not evidence of what was committed.
2. Decide whether the change needs correction. Look for introduced defects,
   documentation made inaccurate by the change, and missing meaningful checks of
   changed behavior. Require concrete evidence and impact. Skip cosmetic rewrites,
   speculative improvements, unrelated debt, and documentation without a reader
   need. If nothing actionable is found, report that and stop without a commit.
3. For substantial or risky changes, use a fresh native subagent for a read-only
   review. Provide the objective, exact hashes, relevant constraints, and completed
   checks; request concise findings with evidence, or an explicit clean result.
   Keep simple changes inline. The coordinator evaluates findings and owns fixes.
4. Make only small corrections within the original objective and exclusions.
   Report larger design or scope changes for discussion instead of implementing
   them. Preserve all pre-existing local edits; if a correction overlaps them and
   cannot be isolated safely, report it and ask how to proceed. Do not stash,
   reset, or discard the user's work to make room for corrections.
5. Run checks targeted to the corrections. Confirm HEAD and branch still match the
   reviewed state before committing; if they changed, stop and report the mismatch.
   Create at most one follow-up commit containing only these corrections, using
   Conventional Commits and a concise English subject. Preserve unrelated staged
   content and verify the exact commit diff; never stage all remaining changes.
   If isolation is uncertain, ask rather than include unrelated content.

Stop after this correction and validation pass. Do not invoke factory-git-commit again,
review the follow-up recursively, amend, push, or expand the task. Report reviewed
hashes, findings, checks and limitations, any correction commit, and deferred work.
When called by `factory-git-commit`, return to that coordinator; it owns the subsequent
push after successful review. A standalone review does not authorize a push.
