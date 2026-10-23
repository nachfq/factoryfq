# factoryfq

Portable development workflow skills for AI coding agents. Skills are maintained
in English and follow the user's and project's language conventions. The current
installer and interactive worker adapter target Codex; Herdr is optional.

Start with the [workflow diagrams](docs/workflow.md) for the proposed development
cycle, skill responsibilities, human checkpoints, and worker communication.

## Included workflows

Every skill name starts with `factory-` so it remains recognizable alongside
skills from other sources. Invoke the new names explicitly (for example,
`$factory-project-plan`); the previous unprefixed names are no longer installed.

- `install-codex.py`: the Codex adapter and installer, using Python 3's standard library.
- `skills/factory-git-start-project/SKILL.md`: local folder, Git repository, GitHub remote,
  and repository policy setup.
- `skills/factory-git-commit/SKILL.md`: focused commits following personal and project
  conventions.
- `skills/factory-git-post-commit/SKILL.md`: bounded review and necessary corrections after
  committing.
- `skills/factory-git-pr/SKILL.md`: branch publication, PR creation or updates, and CI status.
- `skills/factory-project-context/SKILL.md`: versioned or locally excluded context storage,
  and explicit repository associations with Linear projects.
- `skills/factory-project-discover/SKILL.md`: project exploration and conversational
  onboarding, maintaining reusable context.
- `skills/factory-project-plan/SKILL.md`: collaborative next-step selection and planning
  in local plans or Linear documents and delivery issues.
- `skills/factory-project-delivery/SKILL.md`: read existing delivery sources and record
  progress through the selected storage provider.
- `skills/factory-project-implement/SKILL.md`: guided blocks or autonomous implementation
  within one delivery, with verification and human review before further work.
- `skills/factory-project-coordinate/SKILL.md`: independent Codex workers with separate
  worktrees, bidirectional questions, and sequential review through a main session.
- `skills/factory-project-review/SKILL.md`: independent delivery review before handoff,
  without requiring a PR or committing unfinished work.
- `config.example.json`: portable example for each machine's local preferences.

The main agent coordinates substantial work and integrates results. Small tasks
stay inline. Custom skills and agent roles can be added when a concrete need arises.

For substantial work, the default is collaborative: agree on one reviewable
delivery, implement and verify it, then return control to the user with the result
and proposed next step. A roadmap does not authorize all deliveries at once.
Explicit requests for autonomous work or multiple deliveries override this default.
Small, clear fixes proceed directly. Commits remain with the user unless delegated.

## Install for Codex

From this checkout:

```sh
./install-codex.py --dry-run
./install-codex.py
```

The installer links `~/.agents/skills/factoryfq` to this checkout's `skills/`
collection. `--skills-dir PATH` selects a different skills parent directory:

```sh
./install-codex.py --dry-run --skills-dir /path/to/skills
```

Codex discovers the skills inside that collection. Adding a
`skills/<name>/SKILL.md` makes it available through the link; start a new session
if the client has not refreshed its catalog. Keep the collection root free of a
`SKILL.md`. The checkout must remain available at the linked path.

Repeated installation with the same link does nothing. Existing files and other
symlinks are preserved unless replacement with a backup is requested:

```sh
./install-codex.py --dry-run --backup
./install-codex.py --backup
```

Backups live under `${CODEX_HOME:-$HOME/.codex}/backups/factoryfq/` (normally
`~/.codex/backups/factoryfq/`), outside this repository. Existing real directories
are never replaced; resolve those conflicts manually. Unrelated skills remain
untouched.

Installation preserves all global and project `AGENTS.md` and `AGENTS.override.md`
files, Codex configuration, credentials, hooks, and session state. No personal or
global agent instructions are installed. Each workflow reads applicable project
instructions and relevant local context independently.

## Machine-local project locations

Copy `config.example.json` to `${XDG_CONFIG_HOME:-$HOME/.config}/factoryfq/config.json`
and fill in the GitHub owners and repository roots for that machine. The installer
does not overwrite or create these preferences. They stay outside Git; no Documents
symlinks or hardcoded storage paths in the skill are required.

Each profile has `github_owner`, `repos_root`, and `ask_subdirectory`. Personal
projects can go directly under their root; grouped organization projects can ask
for a subfolder on each creation. A group explicitly provided in the request is
used without asking again. Missing configuration is clarified before creation.

Invoke `$factory-git-start-project` or ask naturally to create a repository, for example:

> Create a private personal repo named demo; only initialize it.

> Create an organization repository named demo in the platform group.

The skill handles repository setup only. It does not research ideas, plan product
work, generate an app, make commits, or push content.
It checks the configured root is available before creating a project beneath it.

New GitHub repositories also get squash-only PR merging. Where supported, the
skill creates a ruleset requiring PRs into `main` with one approval and repository
admin bypass. Public repositories support rulesets on Free; private repositories
require Pro for personal owners or Team/Enterprise Cloud for organizations.
A missing plan is treated as unknown and checked through a read-only API request.
Unsupported protection is reported explicitly; squash settings are independent.
Existing policies are inspected and preserved. See the skill's
[GitHub policy](skills/factory-git-start-project/references/github-policy.md) and JSON payloads.

## Initialize project context

Use `$factory-project-context` in a new or existing repository. It configures
`.agent-context/` and records `versioning` as `local` or `versioned` in
`config.json`. `factory-git-start-project` offers this setup when creating a project.
For example:

> Initialize local, excluded context in this repository.

Local context is excluded through Git's `info/exclude`, without editing the
shared `.gitignore`. Versioned context is eligible for tracking in the repository.
Each repo owns its own context; setup does not create shared storage or symlinks.
No commits are created by setup. Local context and its exclusion must be set up
again on another machine.

Setup creates only the directory and config, preserving any existing content.
Research and planning conversations later create `context.md`, `research/`, and
`plans/` as needed. Those workflows must read `.agent-context` explicitly because
ordinary searches may skip ignored directories. Those conversations can identify
related repositories and record references without copying their context or
putting machine-specific paths in versioned documents. This skill does not yet
define a planner, perform research, or populate those documents.

## Associate repositories with Linear

For Linear-backed work, `factory-project-context` can currently find or create a project
and associate repositories through its Resources links. Questions such as "Does
this repository have an associated Linear project?" use a read-only lookup that
verifies a Resource URL against the Git remote. Ask explicitly to set up or change
an association. It requires an authenticated Linear MCP connection and creates
no mandatory local pointer. See [Linear project associations](skills/factory-project-context/references/linear-projects.md)
for discovery and verification rules. Association does not migrate existing
context or plans. Workflows call `factory-project-context` only for an explicit context
request or a task that needs context not already available. Missing local
context and available Linear tools do not trigger a search on their own.

For repositories whose context belongs in Linear, set a machine-local preference:

```json
"context": {
  "github_owners": { "YOUR_GITHUB_ORGANIZATION": "linear" }
}
```

This is a field in the existing `config.json`, not a separate file. The skill
matches the working repository's GitHub owner case-insensitively. Explicit choices
and established sources take precedence; the preference does not migrate local
context or prove a Linear association. Unconfigured owners do not trigger automatic
Linear searches. An explicit Linear request still works in any repository.

For example, a shortcut question needs no Linear lookup, even in a configured
organization. Planning its next milestone can resolve the associated context.
Within a conversation, agents reuse verified associations and loaded context,
refreshing only what the task needs. Missing context does not start discovery or
create storage automatically.

## Discover a project

Use `$factory-project-discover` to understand a project together and build or refresh
local `.agent-context/context.md` or a `Project context` document attached to its
associated Linear project. For example:

> Help me understand this fork and discuss what we want to do with it.

> Discover this project using Linear to store its context.

The skill reads relevant project evidence before asking focused questions about
your goals, constraints, decisions, and related repos. It uses `factory-project-context`
if storage needs setup, and reuses existing context when available. The current
agent leads the conversation, with bounded research delegated when useful.

For Linear, it verifies the repo association and reads existing project context
before interviewing. The same document holds shared understanding and relevant
repo-specific responsibilities; discovery from either repo preserves the other's
useful context. Updates use fresh reads and focused edits, followed by readback.
There is no local mirror. Competing sources or conflicting decisions are resolved
before writing. See [Linear context document](skills/factory-project-context/references/linear-context.md).

Discovery saves useful findings at conversation boundaries without a separate save
request, once storage and language are resolved. Context stays a short orientation
and map; detailed learning lives in maintained topic notes under
`.agent-context/research/` or `Research: <topic>` documents in the same Linear
project. Agents follow relevant links on demand and reuse notes across sessions
and collaborators. Facts, interpretations, and decisions remain distinct. Read-only
and chat-only requests are respected. Discovery creates no placeholder notes,
implementation plan, or code changes. Use `factory-project-plan` next when you
want to choose and plan an initiative.
Saving context in Linear does not create issues or migrate existing plans.

## Plan project work

Start a fresh session and use `$factory-project-plan`, for example:

> Given the project context and our progress, what should we work on next?

The planner explores relevant evidence, recommends options, and discusses the
direction with you. It can also start from a concrete idea or revise an existing
plan. It waits for a direction to be chosen before detailing implementation tasks,
unless you explicitly request a speculative plan. Research is available when
needed, without a mandatory discovery phase.
It remains in planning and leaves implementation for a separate session.

The planner honors the requested destination, reuses the context source for new
plans, and preserves an existing plan's destination during revision. It resolves
competing sources before writing and never silently mirrors or migrates plans.

For local storage, each initiative has `.agent-context/plans/<id>/plan.md` with a
small JSON header and Markdown Specs, Technical approach, Tasks, and Next delivery sections. The
technical explanation connects domain concepts, current behavior, and the proposed
change through a concrete example or flow so the user can assess the design.
Tasks have stable IDs,
dependencies, acceptance and verification information, and form small coherent
deliveries. The next delivery is detailed; later ones can stay coarse. A separate
`log.md` is created only for meaningful historical decisions and evidence. See the
[plan format](skills/factory-project-plan/references/plan-format.md).

The local plan is the source of truth for its state. The reader generates a listing
from headers and opens only a selected plan, excluding logs. From this checkout:

```sh
python3 skills/factory-project-plan/scripts/read_plan.py --repo /path/to/project list
python3 skills/factory-project-plan/scripts/read_plan.py --repo /path/to/project show initiative-id
```

The reader uses only Python's standard library and Git, and writes nothing.
Planning does not commit changes or start implementation. A ready plan records
what can be handed to a new session; execution still requires the user's request.

For Linear, use the same planning conversation, for example:

> Help me choose the next milestone, then build its plan in Linear once we agree.

After choosing a direction, the planner saves a `Plan: <outcome>` document in the
associated project with Specs, Technical approach, and links to delivery issues.
Each issue owns its tasks, acceptance criteria, dependencies, and progress. The
document does not duplicate issue states or checklists. Tasks remain small enough
for human review; unchosen ideas do not generate tickets. A speculative draft is
a document unless draft issues are explicitly requested. See
[Linear plans](skills/factory-project-plan/references/linear-plans.md).

Existing plans and issues are revised in place. Saving is verified by reading back
both the document and its linked issues; partial failures are reported without
blindly recreating artifacts. No local files, assignments, or agent execution are
created by planning. `factory-project-implement` reads local plans or Linear delivery
issues when implementation is requested separately.

## Implement a planned delivery

In a fresh implementation session, identify the local plan and delivery or the
Linear issue. The `factory-project-implement` skill handles requests such as:

> Implement D1 from the selected plan in guided mode. Explain and apply one block,
> then let me review it before continuing.

Or:

> Implement D1 autonomously and return the complete delivery for my review.

Guided mode explains and applies one meaningful block, then waits for your
feedback and go-ahead. Ask to see the proposed code before writing if preferred.
Workers cannot implement later blocks while you review. Autonomous mode completes
the agreed delivery and resolves routine technical choices, asking only when
consequential product or design decisions remain open. It still stops before the
next delivery. If no mode or preference is established, the skill asks once.
You can change modes during the delivery. The implementation entrypoint keeps
scope and context rules visible, then loads only the selected mode. Delegation
instructions are read when delegating; handoff/review instructions when the delivery
is complete; publication procedures when Git closure is authorized. Linear source
reading is separate from issue publication, so starting work does not load the
commenting and status-update procedure.

The coordinator reads the saved plan, checks current code and prerequisites, and
uses native subagents for substantial bounded tasks. Writers stay within the
current guided block or autonomous delivery and use separate write areas; the
coordinator integrates and verifies the result. Significant scope or design challenges return to the
user/planner before the affected work continues.

[factory-project-delivery](skills/factory-project-delivery/SKILL.md) owns reading existing context,
plans and execution records and saving checkpoints. Implementation owns code,
collaboration mode and verification; it composes this skill without depending on
a storage provider. Workers read authoritative sources directly. `factory-project-context`
continues to own source lookup/setup, and `factory-project-plan` owns plan creation/revision.

For local plans, Next delivery records the mode and a concise resume note. For
Linear, provisional progress stays in the conversation until the user validates
the changes and they are committed, reviewed, and successfully pushed. Then the
implementer updates the issue's checklist, Execution section, and appropriate
team state, and posts one brief comment with the published changes, checks, commit
links, and next step. A published block does not complete the entire delivery.
Local-only commits or failed pushes leave Linear unchanged. Explicit requests can
record provisional updates without claiming publication. Project-level updates
remain outside this workflow.

The plan document keeps the design. No local mirror or duplicate tracker is
created; a fresh session reconciles the last published issue checkpoint with the
actual working tree. See [Linear delivery](skills/factory-project-delivery/references/linear-delivery.md).
The coordinator handles corrections before moving on and records acceptance only
from the user. It does not start or prepare implementation of later deliveries
while waiting. Wider autonomous work must be explicitly requested. Validation
alone does not request a commit. Commit requests include push by default; PRs,
releases, and merges require separate authorization.

This skill can run in a main implementation session or an independent worker with
the role contract below. It does not automatically launch a planner or other sessions.

## Coordinate independent workers

Ask the main session to coordinate selected issues with independent workers.
`factory-project-coordinate` checks dependencies, accepted prerequisite code, file ownership,
collaboration modes, and the intended integration branch before launching. It
keeps the main model you selected. Parallel execution still returns small deliveries
for sequential human review; dependent or explicitly deferred work is not started
without the corresponding agreement.

Independent workers use the `implementer` role with Sol 6.1 high by default.
Their native read-only `reviewer` uses Astra high. Override either through
`workers.types.<role>` in the same machine-local `config.json`, or per request;
see `config.example.json`. A config entry alone does not define role behavior.

Set `workers.herdr.layout` to `"agent-nvim-lazygit"` for an implementer on the
left and Neovim with LazyGit already open on the right, both in its worktree.
The default `"agent"` keeps one pane. The split preset requires Herdr, Neovim,
LazyGit and LazyVim's Snacks integration; it does not install or configure them.
Press `q` in LazyGit to return to the editor. This applies to new launches or
explicit resumes, leaving running workers unchanged. Other terminal adapters
keep their own layout behavior.

Set `workers.yolo` to `true` to launch workers with Codex's
`--dangerously-bypass-approvals-and-sandbox` flag. `false` (the default) leaves
Codex's configured permissions in effect. This is independent of guided/autonomous
collaboration: guided workers still wait for your feedback on each code block.
Changing this setting affects subsequent launches or explicit resumes, not running
workers. Keep this preference in your machine-local config.

Worktrees live under `workers.worktrees_root/OWNER/REPO/WORKER`. The default root is
`~/.local/share/factoryfq/worktrees`; it must exist before launch and may be a
symlink to a chosen mounted data disk. Set up that link per machine. The installer
does not select disks or migrate worktrees, and launch refuses a missing/broken
root instead of falling back to the home disk.

The current terminal adapter opens a named Codex tab in the repository's Herdr
workspace. You can enter any worker directly. Workers send questions and results
with `codex queue`; the coordinator replies to their session UUIDs. They keep
their worktree and terminal after finishing. Communication relies on the agent
sending the message; there is no additional supervisor or session registry.
With `yolo: false`, configured sandbox approvals also apply to messaging.

Worker branches target the agreed integration branch when PRs are requested.
Implementers ask you directly before committing and pushing their reviewed work.
They run the Git workflow, update progress/state on their assigned Linear issue,
and post one comment after validated work is committed, reviewed and pushed.
They send the coordinator a compact outcome with commits, checks and saved Linear
links, without seeking its approval. Each issue has one writer to avoid duplicate
updates. The coordinator retains shared context/plan document ownership;
PRs and merges remain separately authorized. Worktrees isolate files,
not design decisions: shared changes and integration still need coordination.
Session/worktree references stay in the conversation, outside Git and Linear.
See the [coordination skill](skills/factory-project-coordinate/SKILL.md) and
[launch and resume adapter](skills/factory-project-coordinate/references/codex-herdr.md).

## Review a delivery before opening a PR

At the end of a planned delivery, the implementer invokes `factory-project-review` directly
with a fresh native reviewer, the agreed plan/constraints and the whole diff against
the pinned integration base. It includes intended uncommitted files when needed;
no PR, extra implementation branch or commit is required to request an opinion.
Source inspection is read-only; checks that generate files require an isolated
snapshot of the exact reviewed content. Reviewer availability/model limitations
are reported instead of silently replacing independence with self-review.

The reviewer looks for concrete correctness, scope, integration and validation
problems. The implementer evaluates findings and owns fixes; guided corrections
still pass through you. One full review and at most one focused follow-up keep the
process bounded. Remaining disagreements or verification gaps are reported.
The orchestrator receives a compact final result, not every exchange.

The reviewer writes neither code nor Linear/GitHub comments. The implementer includes
its review outcome in the usual issue update after human validation, authorized
commit/review/push. Review is distinct from your acceptance, publication and merge;
PR creation remains a separate request. `factory-git-post-commit` keeps its narrower role
of checking and fine-tuning the newly created commits.

## Commit changes

When asked to commit, the skill stages all changes if the index is empty, except
agreed exclusions and ignored files. If anything is already staged,
it asks whether to include everything or commit only the staged content, unless
that choice was explicit in the request. It checks that the working branch fits
the changes and avoids main and other base/integration branches.
Commits use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
with concise English subjects, grouped by functional purpose, and relevant checks.
Review-only requests do not stage or commit. A commit request includes pushing the
reviewed result by default; request local-only work to skip push. Rewriting history
still requires an explicit request.

After committing, `factory-git-commit` runs `factory-git-post-commit` once on the commits it created,
unless asked to skip it. The coordinator reviews simple changes directly and uses
a fresh read-only subagent for substantial or risky changes. Concrete defects or
omissions can produce one corrective commit; a clean review produces none.
Corrections preserve local changes left out of the original commits. Larger issues
are reported for discussion, and the corrective commit does not trigger another
review cycle. After successful checks and review, the coordinator pushes the
reviewed working branch and verifies the remote commit. It resolves unexpected
outgoing commits or an ambiguous destination before pushing and never force-pushes
on rejection. For an explicitly selected Linear delivery, the validated and pushed
work then updates its issue. A standalone review-only request does not authorize
edits, commits, or push. Opening or updating a PR remains a separate request.

## Publish a pull request

Ask to open or update a PR, or invoke `$factory-git-pr`. It reviews the full committed
change against the intended base, pushes the working branch, and creates or updates
the matching GitHub PR. Titles use Conventional Commits; descriptions follow the
project's language and template and explain the outcome and actual verification.
It reports CI for the published head and leaves uncommitted changes untouched.
Drafting or reviewing alone does not publish. It does not merge, enable auto-merge,
force-push, or automatically fix CI failures.

## Edit and try

Edit the relevant `skills/<name>/SKILL.md`, inspect the diff, and start a new
Codex session to load the changed skill. Try a bounded workflow in a disposable
repository and check its scope, permissions, project context, and output against
the request. The link exposes the current working copy, including uncommitted edits.

On another machine, clone this repository and run the installer. Later Git pulls
update the linked content. After moving the checkout, rerun with `--backup` to
replace an obsolete link. The installer targets Linux/macOS.

To uninstall, remove only the `factoryfq` symlink pointing to this checkout from
the selected skills directory. Restore a previous skill link or file from its
backup if needed. No agent instructions or Codex configuration need restoring.

Keep credentials, machine-specific configuration, history, and runtime state
outside Git. An optional future UI can sit above these workflows; the current
repository does not integrate or install a dashboard.

## Verify local tooling

```sh
python3 -m unittest discover -s tests -v
```

Tests use temporary Codex homes and repositories; they do not modify your personal
configuration or project plans.
