# Configure and launch assigned workers

Read only when launching or explicitly resuming authorized workers, after the
[assignment checks](launch.md) are settled. Assessing parallelism alone does not
authorize a launch. Reuse established inputs rather than repeating questions.

## Configure and launch

Read `${XDG_CONFIG_HOME:-$HOME/.config}/factoryfq/config.json`. The optional `workers`
object has `worktrees_root`, boolean `yolo`, and `types.<role>.{model,reasoning_effort}`. Defaults are
`~/.local/share/factoryfq/worktrees`, role `implementer`, model `gpt-6.1-sol`, and
reasoning `high`. Explicit per-task choices override configuration, then defaults.
Do not change the coordinator's model or silently substitute an unavailable model.
This launcher creates independent `implementer` sessions. The separate
[project-review](../../project-review/SKILL.md) workflow defines a native read-only
`reviewer`, configured under `workers.types.reviewer`. A config entry alone does
not create a new worker capability.

`workers.yolo` defaults to `false`: preserve Codex's configured permissions.
When `true`, launch workers with `--dangerously-bypass-approvals-and-sandbox`.
This controls execution permissions only; guided checkpoints, scope and publication
rules still apply. Reject non-boolean values rather than interpreting string truthiness.
Changes apply on launch or explicit resume, not to already running sessions.

`workers.herdr.layout` selects `agent` (default, one pane) or
`agent-nvim-lazygit` (implementer left, Neovim with LazyGit right, same worktree).
Apply only through the Herdr adapter; explicit task preferences override config.
The editor layout does not change worker permissions or collaboration mode.

The worktrees root must already exist and be writable. It may be a symlink to a
larger disk; a missing/broken link or unmounted destination is a setup problem,
not permission to create storage elsewhere. Use `ROOT/OWNER/REPO/WORKER`, deriving
repository identity from the intended Git remote. Resolve ambiguous identity.
Validate name components and path containment, including symlinks; never accept
path traversal. Use a short stable name such as `issue-123-pools` for the worktree,
terminal and Codex chat, with branch `work/issue-123-pools`.

Read [Codex and Herdr sessions](codex-herdr.md) when launching or
resuming sessions. Keep terminal UI details there. Future adapters may
use another terminal without changing role contracts. Do not use Orca tooling or
silently substitute native subagents/background exec sessions for visible workers.

Provide a compact assignment containing:

- Worker name/role, coordinator thread UUID and expected worker model/mode.
- Working repo/worktree/branch and starting SHA; integration destination and PR
  head/target repos and branches, plus code/docs/example destinations.
- Applicable instruction paths (including relevant ancestors of the original
  checkout), authoritative context/plan/issue links, and relevant decisions.
  Highlight the context criteria affecting this delivery and any explicit user
  exceptions; the highlights do not replace reading the relevant source.
- Outcome, task/requirement IDs, owned files/sections, boundaries, checks and
  prerequisite evidence. Do not pass the entire coordinator transcript.
- Any user-selected review exception or suspension, with its scope. Relay it
  explicitly so workers do not apply the default review cycle to that work.
- The absolute path to [the implementer role](implementer.md), which
  the worker must read before using `project-implement`.
- Git ownership and the exact user-authorized closure policy, scope and trigger.
  Implementers reuse applicable permission or ask the user directly, then own
  commit/review/push, assigned Linear issue updates and the outcome report.
  Assign one writer per issue when workers share it. The coordinator owns shared
  context/plan documents; PRs and merges require separate authorization.

For ignored local plans, supply their original absolute paths as read-only inputs;
they are not automatically present in a worktree. Do not copy or symlink shared
mutable context into each worktree. Each worker keeps its own build/test outputs.
