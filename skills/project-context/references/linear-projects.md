# Linear project associations

Use the authenticated Linear MCP to find or establish repository links on a
project. This covers read-only lookup and authorized setup, not context migration,
planning, or issue creation. A lookup never authorizes writes. Reuse explicit user choices for
workspace, team, project, and repositories; clarify missing consequential choices.
Do not hardcode company, project, or repository IDs in this skill.

## Identify repositories

Read the checkout's Git remotes. Normalize GitHub SSH and HTTPS URLs to
`https://github.com/OWNER/REPO`, removing a terminal `.git` and trailing slash.
Compare GitHub owner/repository identity case-insensitively. Do not use local
checkout paths as identity or include credentials from remote URLs.

Use the intended working repository, usually the user's fork. Do not substitute
an upstream repository because it shares the codebase. If remotes leave ownership
unclear, resolve that before creating an association. Include related repositories
only when requested or already agreed.

## Find and verify an association

Project Resources hold repository links using this convention:

- Label: `Repository: OWNER/REPO`
- URL: `https://github.com/OWNER/REPO`

Multiple repositories may belong to one project. Match the normalized URL, not
the label or project name alone. Existing links with another label can be
candidates; confirm their intended role before treating them as a new association.
An incidental GitHub source citation does not automatically select a project.

The currently tested MCP interface has these constraints:

- `list_projects(query=...)` searches project names. A repository URL query did
  not find a project whose Resources contained that exact URL. Do not use an
  empty name-search result as proof that a repository has no association.
- `list_projects` does not expose Resources in its selectable fields or a
  repository-URL filter. Request small metadata fields (`id`, `uuid`, `name`,
  `url`) and inspect candidates with `get_project(includeResources=true)`.
- `get_project` returns link Resources with `type`, `id`, `label`, and `url`.

If the user names a project, resolve it directly and verify its links. Otherwise,
list projects in the agreed team/workspace scope, follow pagination, and inspect
their Resources. Name search can prioritize candidates but cannot establish an
exhaustive result. If the scan is incomplete, report that limitation rather than
claiming uniqueness or absence. If multiple projects match, let the user choose
the one relevant to the current work. Do not select by recency or similar name.

The association lives in Linear. No required local pointer or cache is created.
This convention identifies a project. For context lookup, continue with
[Linear context document](linear-context.md); selecting an issue is separate.

For a lookup, report the verified project URL and the Resource URL matching the
Git remote. If only the name or description matches, report a candidate rather
than confirming an association. Mention absent local metadata only if relevant
to the user's question; it is not required evidence for a Linear association.

## Create or associate when authorized

Check for existing matching projects before creation to avoid duplicates. Use
`save_project` with the agreed `name`, verified team ID in `addTeams`, and `links`
as an array of `{title, url}` entries using the convention above. A concise
summary and repository responsibilities may describe the agreed scope; do not
invent a roadmap, deadlines, or ownership. Use the team's default status unless
the user requested another one.

For an existing project, first read its Resources and preserve unrelated content.
Inspect the available update semantics before modifying its links; this workflow
has verified creation with multiple links, not whether an update appends or
replaces them. Skip already matching links. If a mutation fails or times out,
read the resulting state before retrying creation or link insertion.

Read the saved project back with `includeResources=true`. Verify its team and all
requested repository URLs, and return the project URL and identifier. Record no
credentials, machine paths, or private project content in the factoryfq repository.
Project visibility follows Linear access controls; links do not configure GitHub
issue synchronization or grant repository access.

Report partial success accurately. Project creation and association do not mean
context, plans, or tasks have been migrated. Existing local artifacts remain
untouched until migration is agreed.
