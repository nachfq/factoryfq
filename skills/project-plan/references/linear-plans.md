# Linear plans

Use Linear as the source of truth for a selected plan. One plan is a document in
the existing project, with one issue per reviewable delivery. Do not create a
Linear Project or native Initiative for every plan, or a local Markdown mirror.
The planner owns these updates; research workers remain read-only.

## Resolve and read

Reuse relevant context and the verified repo/project association when established.
If unresolved or changed, use [Linear project associations](../../project-context/references/linear-projects.md)
and [project context](../../project-context/references/linear-context.md) as needed.
Reuse established destination choices. Missing context can be filled through
focused discussion; it does not force discovery. Missing project setup is handled
separately through `project-context`, not inferred from a request to explore ideas.

For a selected, verified document ID, read it directly. Otherwise list project
documents using `list_documents(projectId=PROJECT_UUID)` with small metadata fields
and pagination. Plans created by this workflow use the title
`Plan: <outcome>`. Read the selected document by ID. Reuse explicitly selected
existing plans even if their titles differ. Titles find candidates; verify project
membership and scope before deciding they match. Never select solely by recency.

Read issues linked from that plan. If links are incomplete, use project-scoped
`list_issues` with metadata first, then inspect candidate descriptions to verify
the exact plan reference and delivery ID. Follow pagination before concluding
an issue is missing. Fetch only relevant issues and their relations, not every
description or comment in the workspace. Read history only for a named question.

## When creating or changing a plan

After the direction is selected, or an explicitly speculative draft is requested,
read [Linear plan writing](linear-plan-writing.md) for document and issue structure,
authorization boundaries, persistence, revisions, and saved-state verification.
Do not load writing procedures merely to locate or read a plan.
