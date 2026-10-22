# Codex sessions with a Herdr terminal adapter

This adapter uses Git worktrees, interactive Codex, and `codex queue` for messages.
Herdr only opens and exposes terminals. The user can enter the worker directly.
The CLI round trip was verified locally; inspect installed `--help` when commands
or output schemas differ. Do not change shared daemon settings as a workaround.

## Prepare a worktree

Resolve values from the coordinator's agreed assignment. Use safely quoted shell
arguments or Python `subprocess.run([...], check=True)`, never interpolate prompts
into shell code. Read `git worktree list --porcelain`, branches and remote refs
before creation. Reuse an existing matching worker/session when resuming; on name,
path or branch collisions, inspect rather than replace or invent another worker.

With an existing storage root and verified base SHA:

```sh
git -C "$REPO" worktree add -b "$BRANCH" "$WORKTREE" "$BASE_SHA"
```

Check that the worktree belongs to the intended repository and has the expected
branch and base. Do not combine this with `codex --worktree`, which would create
another managed worktree. Do not copy credentials, ignored build output or `.env`
files to initialize it. Keep generated files and mutable test output per-worktree.

## Open a visible session

Inspect `herdr workspace list`, `herdr agent list` and, when available,
`herdr pane current`. Select the original repo's workspace from verified paths,
not merely the currently focused pane: the user may be working elsewhere. Resolve
ambiguity with the user. If Herdr is absent or no workspace is available, report
that and offer a user-opened terminal with the direct Codex command; do not install
or start a different multiplexer implicitly.

Create one tab in that workspace. Retain `result.tab.tab_id` and
`result.root_pane.pane_id` from `tab create`; the latter is the implementer's
`PANE`, even when an editor split is created. Never infer it from current focus.

Build `PERMISSION_ARGS` as a Bash argument array: `()` when resolved `yolo` is
false, or `(--dangerously-bypass-approvals-and-sandbox)` when true. With Python,
use the equivalent empty or one-element argument list. Use the same resolved
arguments for Herdr, direct terminal launch, and explicit session resume.

```sh
herdr tab create --workspace "$WORKSPACE" --cwd "$WORKTREE" --label "$WORKER" --no-focus
herdr agent start "$WORKER" --kind codex --pane "$PANE" --timeout 20000 -- \
  --model "$MODEL" -c "$REASONING_OVERRIDE" "${PERMISSION_ARGS[@]}"
```

`REASONING_OVERRIDE` is a TOML assignment such as `model_reasoning_effort="high"`,
built from the resolved configuration. Add the bypass flag only when the resolved
`yolo` option is true; do not change global Codex settings. Otherwise, configured
permissions apply and a worker may need user approval to run
Git/build commands or `codex queue`, which accesses Codex state outside its worktree.
Show the blocked pane to the user rather than approve an escalation for them.

Success from `agent start` means an interactive composer is ready, not that a task
has run. Name the Codex chat separately using `/rename WORKER` in that idle composer
(for example via `herdr agent prompt "$PANE" "/rename $WORKER"`). Verify the command
was processed before sending the assignment. Herdr labels alone do not rename
saved Codex chats. If renaming is unavailable, preserve and use the registered UUID.

Submit the complete assignment with `herdr agent prompt "$PANE" "$ASSIGNMENT"`.
Inspect the terminal if startup or submission has an uncertain result; do not
blindly submit twice. Verify Herdr recognizes the expected model/worktree, then
show the user the worker/tab name. The worker's registration supplies its UUID.
Direct terminal fallback: `codex -C "$WORKTREE" --model "$MODEL" -c "$REASONING_OVERRIDE" "${PERMISSION_ARGS[@]}"`;
the user then supplies the same assignment. Never use `exec` as a substitute for
an interactive session the user wants to enter.

## Optional editor layout

Resolve `workers.herdr.layout`: `agent` (missing/default) keeps the single pane;
`agent-nvim-lazygit` opens a 50/50 layout with the implementer left and its editor
right. Reject unknown values rather than guessing. For the split layout, create
it after the tab and before dispatching the assignment:

```sh
herdr pane split --pane "$PANE" --direction right --ratio 0.5 \
  --cwd "$WORKTREE" --no-focus
```

Keep `result.pane.pane_id` from this response as `EDITOR_PANE`. Start Codex only
in the original `PANE`. Both panes must use the same worktree; the editor is for
human review, not another worker. Do not change desktop or editor configuration.

This preset needs `nvim`, `lazygit`, and LazyVim's Snacks integration. Check those
prerequisites before opening the editor. Start Neovim at the fresh editor shell
prompt with this command, which opens the same Git-root view as `Space g g`
after LazyVim finishes loading:

```sh
nvim -c 'autocmd User VeryLazy ++once lua vim.schedule(function() Snacks.lazygit({ cwd = LazyVim.root.git() }) end)'
```

Send it as one shell-quoted command to `herdr pane run`, for example from Python:

```python
editor_args = [
    "nvim", "-c",
    "autocmd User VeryLazy ++once lua vim.schedule(function() "
    "Snacks.lazygit({ cwd = LazyVim.root.git() }) end)",
]
subprocess.run(
    ["herdr", "pane", "run", editor_pane, shlex.join(editor_args)], check=True
)
```

Import `shlex` and `subprocess`; do not join unquoted shell arguments. Verify the
pane's process and visible output with `pane process-info` and `pane read` before
claiming that LazyGit opened. `q` returns to Neovim. Do not use Git actions during
startup verification. Keep the current user focus unchanged.

If dependencies or editor startup fail, report the missing layout component and
continue the authorized implementer launch in its existing pane; do not install
software, restart the worker, or send editor commands into its terminal. Inspect
uncertain results before retrying. On resume, reuse an existing matching layout;
only add a missing editor pane at an idle shell, never duplicate splits or overwrite
an active editor. Direct-terminal fallback does not promise this Herdr layout.

Verified locally with Herdr's split/process/read APIs and LazyVim on 2026-10-09:
the right pane opened LazyGit inside Neovim at the requested repository.

## Bidirectional messages

Use the [worker message protocol](worker-messages.md) for registration, questions
and results. Workers read that protocol directly; this adapter is needed only
for launching, inspecting or resuming terminal sessions.

## Resume and portability

Keep the assignment and registration in the coordinator conversation. No registry,
PID file or session IDs enter Git or Linear. Reuse Git's worktree list and Codex's
saved sessions. A closed terminal can resume its session in the same worktree:

```sh
codex -C "$WORKTREE" "${PERMISSION_ARGS[@]}" resume "$WORKER_THREAD_ID"
```

An exact saved chat name also works when unambiguous; `codex resume --all` is a
fallback picker. In Herdr, open a tab at the existing worktree and launch Codex
with `resume UUID`; do not create a new branch or session. If the coordinator is
replaced by a new session, send workers its new UUID before expecting further
reports. Moving machines transfers configuration, not live sessions or local code.

References: [Codex chat naming/resume](https://learn.chatgpt.com/docs/developer-commands),
[Herdr agents](https://herdr.dev/docs/agents/). CLI messaging and launch behavior
were verified using installed Codex and Herdr; no private server API is required.
