# Delegate within an implementation session

This is native subagent delegation in a shared checkout. For user-requested
independent interactive agents/worktrees, use `factory-project-coordinate` instead;
an unavailable launcher does not authorize silently substituting this mechanism.

For native subagent delegation within this session, the coordinator owns
integration, Git operations, plan updates, and user dialogue.
Handle small tasks directly. For substantial bounded tasks, use fresh native
subagents with the minimum necessary context; prefer a fresh context over the
full planning conversation when supported. No custom agent role or model is
required by this skill. If delegation is unavailable, work directly and report it.

Give each worker the repository path and relevant plan excerpts or links,
assigned delivery/task/requirement IDs, collaboration mode and current checkpoint,
design constraints, prerequisites,
explicit read-only or editing scope, owned files or areas, and expected checks.
Request changed paths, observed
check results, unresolved issues, and a concise explanation of the result.
These native subagents must stay within their assignment, report challenges to the coordinator,
and return without starting another task, spawning workers, changing the plan,
or committing/pushing. They must preserve others' edits in the shared checkout.
For these native subagents, only their coordinator writes delivery records.

In guided mode, scope writers to the current block; delegate bounded read-only
investigation when useful without deciding future blocks for the user. In autonomous
mode, parallelize independent tasks within the active delivery, with disjoint write
ownership. Serialize dependencies and shared-file changes; coordinate broad
formatters, generators, and dependency updates. Stay within the authorized scope
and review boundary: do not start later deliveries while awaiting a required human
checkpoint. An explicitly autonomous milestone permits scheduling its independent
work and continuing through verified dependencies, not ignoring user holds.
Inspect each returned diff before integrating or using it as a prerequisite.
