# Linear context document

Use after verifying the repository-to-project association through
[Linear project associations](linear-projects.md). This reference defines how to
find and maintain project understanding, not plans, task state, or issue workflows.
No local pointer, cache, or `.agent-context` directory is required for this route.

## Locate and read

Use one document titled `Project context` attached directly to the verified Linear
project. The title is a discovery convention; prose follows the project's language.
If the user explicitly selects an existing context document with another title,
verify its project and use it without renaming or duplicating it automatically.

List documents scoped to the project's UUID with `list_documents(projectId=...)`.
Request metadata (`id`, `title`, `url`, `project`, `updatedAt`) first, paginate as
needed, and read the selected document with `get_document(id=...)`. Do not search
or load every document in the workspace. Confirm project membership; a document
mentioning the repo somewhere is not sufficient. Use its ID for subsequent reads
and updates in the session, not repeated title searches.

If several documents could be authoritative, resolve the choice before updating.
If none exists, report that the project is associated but its context has not yet
been created. A read-only lookup or ordinary task does not start discovery or
create a document. Failed or incomplete reads do not prove absence. If Linear is
unavailable, disclose that limitation and continue only work that does not need
the missing context; do not silently establish a local replacement.

Read the document before asking onboarding questions or relying on its decisions.
Use it as context, verify facts relevant to the current task, and follow only
relevant references. Do not load all plans, issues, comments, or history as part
of context loading. If a local copy also exists, reuse an explicit source choice;
otherwise clarify the authority before reconciling or writing either copy.

## Authorized persistence

When discovery or an explicit context revision is ready to save useful content,
read [Linear context writing](linear-context-write.md). Do not load writing
procedures for a lookup or merely to use existing project context.
