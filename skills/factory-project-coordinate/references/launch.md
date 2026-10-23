# Select, configure and launch workers

## Select and bound the work

Read applicable instructions and reuse relevant context and its established source.
Use `factory-project-context` only to resolve a missing source or association, or requested setup.
Read the selected plan, issues, current code, Git state, and prerequisite evidence.
Read the applicable project context if not already available in this session;
knowing its location is not knowing its criteria. Check the proposed assignments
against those criteria, and resolve consequential conflicts before dispatch.
Use [factory-project-plan](../../factory-project-plan/SKILL.md) for consequential revisions, including
its context-exception and verification decisions; do not defer unresolved planning
conflicts to implementers or reviewers. This is not a mandatory new planning phase.
Explicit requests to implement named deliveries are sufficient scope.

Check whether the work is actually independent: agreed interfaces, prerequisite
code, testability, and file ownership. Do not manufacture parallelism or treat
worktrees as protection against incompatible API changes. Resolve shared interfaces
before launch; assign shared files by section or serialize their changes. A task
explicitly deferred in the plan needs an agreed scheduling revision before launch.

For each worker, state its outcome, task IDs, owned files/sections, exclusions,
checks, and collaboration mode. Reuse the user's preference; if unspecified, ask
once for guided or autonomous implementation of the selected scope. Guided workers
stop after each block for the user; autonomous workers complete only their assigned
delivery. Read-only review by the coordinator is not the user's acceptance.

Resolve the [delivery destinations and closure agreement](../../factory-project-implement/references/delivery-contract.md)
before launch. Choose a verified starting commit containing accepted prerequisites
for each worker, using a shared base where needed. Distinguish work branches,
combined integration and intended PR targets, including upstream versus fork.
Give shared docs/examples an explicit destination. Do not include uncommitted edits
implicitly or reset the main checkout. Check CI triggers against the actual PR bases.

## Launch when authorized

When actually launching or explicitly resuming workers, read
[worker launch](worker-launch.md) for configuration, paths, terminal adapter and
assignment payload. Do not load session commands merely to assess parallelism.
