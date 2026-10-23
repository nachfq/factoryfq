# Maintain a Linear context document

Read only when authorized to create or update context. Resolve the authoritative
document through [Linear context document](linear-context.md) first; reuse already
verified source selection. Lookup alone does not authorize persistence.

## Organize shared understanding

Keep a brief project orientation, shared goals and decisions, and a repository
map linking the associated repos and explaining their responsibilities. Add
repo-specific sections only where there is useful evidence. Start with what is
known from the current repo and the user; do not invent facts or empty sections
for every related repo. Link out to detailed sources. Retain only durable working
criteria and cross-delivery questions; feature-specific contracts and unresolved
API choices stay in their plan/issue. Use the selection and pruning rules in
[durable context](../../factory-project-discover/references/durable-context.md)
for content updates; an exchange with the user does not itself merit a new rule.

Qualify code paths by repository, or link to canonical GitHub sources when known;
do not invent a published URL for unpushed code or store machine-specific paths.
Attribute maintainer feedback and decisions to their source and actual scope.
Discovery from one repo must preserve useful context about the others. A local
constraint must not silently become a project-wide rule. This is current
understanding, not a transcript, backlog, or duplicate technical documentation.

## Write during authorized discovery

`factory-project-discover` owns the content-writing workflow. The main discovery agent
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
