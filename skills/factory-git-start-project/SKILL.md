---
name: factory-git-start-project
description: Create or connect a local Git repository and its GitHub remote using the user's folder, owner, visibility, and repository policy defaults. Use when the user requests repository setup.
---

# Set up a Git repository

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Set up the requested local folder, Git repository, GitHub remote, and repository
settings. Research, product planning, application scaffolding, and implementation
are outside this skill's scope.

## Resolve location and ownership

Read `${XDG_CONFIG_HOME:-$HOME/.config}/factoryfq/config.json` for this machine's
profiles. Each profile maps `github_owner` to an absolute `repos_root` and an
`ask_subdirectory` preference. Expand a leading `~` in paths. The config contains
local preferences, not credentials; do not copy it into a new repository.

- Select the profile from the user's stated owner or context that clearly
  establishes ownership. If personal versus organization ownership is ambiguous,
  ask before creating local or remote repositories. The current working directory
  alone does not decide ownership of a new project.
- If configuration is missing or the requested profile is absent, ask for the
  owner and root folder. Do not guess paths or silently create a new convention.
- If `ask_subdirectory` is true, use a grouping folder explicitly supplied by the
  user, or ask which group to use. Otherwise use the root directly. A supplied
  destination takes precedence over these defaults.
- Resolve the destination as `repos_root/[group/]repository-name`. Validate that
  the final path stays within the chosen root, including after resolving symlinks;
  reject traversal in names or groups. An explicitly requested different root is
  a new destination choice, not a traversal exception.
- If the configured root is unavailable, report it and request an alternative;
  do not recreate a missing mounted storage hierarchy. Inspect existing target
  folders and remotes before deciding whether to initialize, reuse, or clone.

## Establish the requested scope

Clarify only decisions that affect setup: repository name,
owner, and significant constraints. Use private GitHub visibility by default
unless the user specifies otherwise.

Distinguish brainstorming/research from a request to create a repository. Research
alone does not authorize GitHub writes. When creation is already requested and
the owner, name, and location are clear, proceed without repeating confirmation.
Honor requests to initialize only: do not add scaffolding, dependencies, or plans
as files unless they are part of the requested scope.

For a new project, offer context storage setup alongside these choices: versioned,
locally excluded, or skip for now. Reuse an explicit choice without asking again;
honor requests for Git-only setup. After Git initialization, use
[factory-project-context](../factory-project-context/SKILL.md) if selected. This configures the
repo's own context storage; it does not authorize writing research or plans.

## Initialize or connect the repository

Use the available Git and GitHub tools (normally `git` and `gh`). Check the active
GitHub account and target owner's accessibility. Check for an existing remote repo;
distinguish a genuine not-found result from authentication or network failure.

For a genuinely new destination, initialize Git with `main` and create the private
remote under the explicit `OWNER/NAME`, connecting it as `origin`. With `gh`, use
`gh repo create OWNER/NAME --private --source=DESTINATION --remote=origin`.
Pass dynamic names and paths as safely quoted arguments. Never replace an existing
origin or change an existing repository's visibility just to match defaults.

If the remote already exists, inspect its identity and ask whether to use it when
that is not clear from the request. If creation partially succeeds, inspect the
local and remote state before retrying; do not create alternate repos or remove
files to hide the failure. Stop dependent setup if ownership, access, or destination
cannot be resolved, and report what was actually created.

Leave commits to the user unless delegated. An empty GitHub repo is a valid result;
do not manufacture a commit just to enable a push. Creating or connecting a remote
does not by itself authorize pushing existing local content.

## Configure GitHub defaults

For new GitHub repositories, follow [GitHub policy](references/github-policy.md):
squash-only PR merging, plus an active ruleset for `main` requiring a PR with one
approval and allowing repository administrators to bypass. Apply rulesets only
when available for the repository's visibility and owner plan; a null plan is
unknown, not proof of Free. Verify actual settings and report unsupported or
incomplete protection. For existing repos, apply this only when policy setup is
requested. This setup does not authorize commits, pushes, or changing visibility.

Finish with the local path, GitHub URL and verified visibility when available,
what was created, merge/protection status, and verification. Clearly identify any
incomplete local/remote setup. Do not claim an empty repo is pushed.
