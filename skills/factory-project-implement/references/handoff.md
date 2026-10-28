# Review and hand off a completed delivery

Read this after the selected delivery and its checks are complete, or when an
explicit review request arrives. It does not apply to each guided block.

## Independent review

After completing the selected delivery and its checks, use
[factory-project-review](../../factory-project-review/SKILL.md) before the final user/coordinator handoff,
unless the user opts out or valid review evidence covers the identical target.
An explicit request for another review requires reading the current review skill
and invoking that pass; an earlier clean result does not satisfy the request.
Invoke the reviewer directly with fresh context; no orchestrator approval is needed.
This reviews the cumulative delivery, including uncommitted work when present,
not each guided block or partial commit. Respect its one full pass and at most one
focused follow-up. Assess findings, apply in-scope corrections in the agreed mode,
and disclose unresolved issues. Review does not authorize commit/push or replace
user acceptance. `factory-git-post-commit` remains a separate bounded commit fine-tuning step.

## User handoff

Finish with the implemented outcome, a short technical explanation, an ordered
guide to the important diff, checks and results, and any limitations or decisions
still needed, plus the independent review target, outcome and remaining findings.
Include the authoritative plan and task references and how the user can
try the change. Present one integrated review surface, not a stream of worker reports. All workers for
the delivery must have returned or been stopped before this review handoff.

Report verification, review, acceptance and publication as separate facts, with the
remaining action. At the agreed boundary, wait for human review; acceptance is
recorded only when the user gives it. Within an explicitly autonomous milestone,
retain this delivery's summary and reviewed evidence, then continue through
authorized work once its prerequisites are verified. Present the deliveries in
order at the final handoff, without claiming they are human-accepted. For requested
corrections, reopen affected tasks, fix and verify in the agreed mode, and present
the same delivery again. Otherwise propose later work without starting it.
When commit/push is requested or an applicable closure agreement's trigger is met,
read [publication](publication.md). Do not load Git procedures just to hand off code.
