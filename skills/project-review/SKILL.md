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

Choose the role before loading further instructions:

- As the implementer or standalone review caller, read the
  [caller workflow](references/caller.md) to pin the cumulative target, configure
  and invoke the reviewer, evaluate findings and return the result.
- As the delegated reviewer, read only the
  [reviewer role](references/reviewer.md); do not invoke another reviewer.

The review target must identify dirty content as well as commits and remain
frozen during review. Honor the selected delivery's exclusions, authoritative
context and explicit user exceptions. Review evidence does not establish human
acceptance or authorize publication. The default budget is one full pass and at
most one focused follow-up; another full pass requires a user request.
