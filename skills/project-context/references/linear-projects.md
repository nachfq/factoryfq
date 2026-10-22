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

## Authorized setup

Only when project creation or repository association is requested, read
[Linear project setup](linear-project-setup.md). Do not load that procedure for
an association lookup.
