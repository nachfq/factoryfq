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

## Organize shared understanding

Keep a brief project orientation, shared goals and decisions, and a repository
map linking the associated repos and explaining their responsibilities. Add
repo-specific sections only where there is useful evidence. Start with what is
known from the current repo and the user; do not invent facts or empty sections
for every related repo. Link out to detailed sources. Retain only durable working
criteria and cross-delivery questions; feature-specific contracts and unresolved
API choices stay in their plan/issue. Use the selection and pruning rules in
[project-discover](../../project-discover/SKILL.md#maintain-a-concise-context-document)
for content updates; an exchange with the user does not itself merit a new rule.

Qualify code paths by repository, or link to canonical GitHub sources when known;
do not invent a published URL for unpushed code or store machine-specific paths.
Attribute maintainer feedback and decisions to their source and actual scope.
Discovery from one repo must preserve useful context about the others. A local
constraint must not silently become a project-wide rule. This is current
understanding, not a transcript, backlog, or duplicate technical documentation.

## Write during authorized discovery

`project-discover` owns the content-writing workflow. The main discovery agent
writes; its read-only workers return evidence. Once the project and destination
are resolved, an explicit discovery request using Linear authorizes saving the
result there without asking for approval of every paragraph. A request merely to
find or read context does not. Do not create placeholder documents before there
is useful content, copy local context without a migration request, or change
sharing, project membership, issues, or GitHub synchronization.

Before first creation, recheck project documents to avoid an obvious duplicate.
Call `save_document` with `title: "Project context"`, the verified project UUID
as `project`, and Markdown `content`. Specify only that parent. If another
document has appeared, read and reconcile it instead of creating another copy.

For updates, reread the document immediately before writing. Prefer focused
`patch` operations against the freshly read content and pass the document ID;
omit parent fields so an update does not reparent it. Preserve unrelated edits
and other repositories' sections. Replace superseded statements and remove
duplication instead of appending every discovery turn. If patch anchors fail,
reread and reassess; do not fall back to overwriting a stale full document.

Patches are not a document lock. If concurrent edits conflict over a decision,
pause that revision and resolve the conflict with the user. After an uncertain
write result, reread before retrying, especially before creating another document.
Always read back the saved document, verify project, content and references, and
report its actual URL. Report partial or failed saves honestly; never claim
context was persisted based only on an intended tool call.
