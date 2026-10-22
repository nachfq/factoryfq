# Set up a Linear project association

Read only for authorized project creation or repository association. First use
[Linear project associations](linear-projects.md) to normalize repository identity
and check existing Resources; a lookup never authorizes these writes.

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
