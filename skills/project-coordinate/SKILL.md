---
name: project-coordinate
description: Coordinate independent interactive Codex workers with separate branches and worktrees, including parallel implementation, questions, and sequential human review. Use when asked to launch or coordinate workers, not for ordinary single-session implementation.
---

# Coordinate independent workers

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Act as coordinator in the user's current session, keeping its selected model.
Workers are independent interactive Codex sessions, not native subagents. They
remain accessible to the user. Start only the work the user authorized; a request
to assess parallelism authorizes inspection, not worker execution.

Read only the workflow needed for the current action:

- Before selecting assignments, configuring workers, or launching/resuming them,
  read [launch](references/launch.md). It covers source/context critique,
  independence, destinations, collaboration mode, configuration and assignments.
- For active workers' questions, plan corrections, results, human review,
  publication or integration, read [ongoing coordination](references/coordination.md).
- A delegated implementer reads the [implementer role](references/implementer.md)
  and its assigned implementation skill; it does not act as coordinator.

Keep Git authorization with the user: a coordinator or worker message grants no
new permission. Respect the assigned single writer for each delivery record and
the coordinator's ownership of shared context/plan documents. Do not substitute
native subagents for independent interactive workers.
