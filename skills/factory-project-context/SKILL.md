---
name: factory-project-context
description: Find and verify a repository's existing context location or associated Linear project, or set up local context storage and Linear repository links. Use for explicit context lookup/setup or when project work needs unresolved context; not for unrelated requests, research writing, or planning.
---

# Find or initialize project context

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Locate existing context or configure local storage and repository associations in
Linear. Research and planning workflows populate the context later. Do not
research the project, write speculative context, or create placeholder documents.

## Decide whether and where to look

Resolve context when explicitly requested, when working on a selected Linear issue
or plan, or when missing project goals, constraints or decisions matter to the task.
A general question, self-contained edit, missing local file, or available connector
alone does not justify a Linear query, even in an organization that uses Linear.

Reuse relevant context and verified repository/project associations already in the
conversation. Do not rediscover them for each message. Refresh only the information
needed for the current decision, an explicit refresh, or evidence of a change;
verify current state before mutations as required by the relevant workflow.

An explicit source or selected issue/plan takes precedence; otherwise reuse the
established source, including local context. Only when the source is unresolved,
read `${XDG_CONFIG_HOME:-$HOME/.config}/factoryfq/config.json` if present:
`context.github_owners` maps GitHub owners to the preferred source `"linear"`.
Match owners case-insensitively using the intended working repository's remote
(usually `origin`), not its checkout path or an unrelated upstream. Ambiguous
remotes require clarification before using this preference.

A matching preference selects where to look when context is needed; it neither
triggers a query by itself nor proves a project association. Verify Linear Resources
as described below. Without an explicit/established Linear source or a matching
preference, do not search Linear automatically. Continue with available evidence;
ask for the source only if it is needed to proceed. A missing association or
unavailable connector does not authorize setup, migration or a local fallback.

## Distinguish lookup from setup

Questions about whether a repository has a Linear project or where its context
lives are read-only lookups. Do not create files, change configuration, or create
or edit Linear content. For local context, inspect existing storage and report
what is present without offering setup as a prerequisite to answering.

For Linear lookup or setup, read [Linear project associations](references/linear-projects.md).
Read Git remotes and verify a candidate project's repository Resources before
confirming an association. A matching name or description identifies a candidate,
not an established association. A missing local reference does not invalidate a
verified Linear association. Return the project link and matching repository as
evidence, or explain what remains unverified. For requests to locate or read the
context itself, continue with [Linear context document](references/linear-context.md).
A question only about the project association does not require loading its
documents. Stop after the requested lookup or setup; do not fall through to local
initialization or discovery.

Linear setup establishes the project and repository links only. Use
[factory-project-discover](../factory-project-discover/SKILL.md) when the user requests writing
context. Setup does not migrate existing context or plans. Do not create local
context metadata for this route.

For authorized local setup only, read [local storage setup](references/local-setup.md).
Lookups and Linear workflows do not need that procedure. Preserve existing local
context when associating a repository with Linear; an association alone does not
change which copy is authoritative.
