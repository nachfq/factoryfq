---
name: project-discover
description: Explore a project and talk with the user to build or refresh reusable context in local files or an associated Linear project. Use for project onboarding or understanding how to move forward before a concrete initiative is defined.
---

# Discover a project

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Build a useful shared understanding through bounded exploration and conversation.
The agent in the user's conversation leads discovery; delegate only scoped,
read-only investigations when they materially help. Discovery does not require
an implementation goal and does not authorize code changes, commits, or a work plan.

## Orient before interviewing

Find the repository root and reuse existing context and its established source.
Inspect `.agent-context` explicitly when needed because searches may skip ignored
files. Missing local context alone does not trigger a Linear lookup. When the
source is unresolved, or before saving context, read
[context storage](references/context-storage.md). Resolve competing destinations
before writing; unavailable Linear access does not authorize local fallback.
Read only references needed for the current stage, not all references at startup.

Read existing context, the README, and a focused file listing. Follow relevant
documentation links and inspect entry points, manifests, or checks to understand
what the project does, its main components, and how it is developed and verified.
Use targeted searches to resolve concrete gaps rather than reading the whole repo.
Treat existing context as evidence to check, not unquestionable truth. Describe
documented test commands as such; do not imply they were executed.

## Build understanding with the user

Briefly explain what you understand, with relevant evidence, then ask the next
question that most affects that understanding. Ask one focused question at a time
and let the answer guide the next exploration or question. Do not repeat settled
decisions or ask the user for facts readily available in the repo.

Explore the user's relationship to the project, intended outcomes, current
priorities, constraints, and undocumented decisions as relevant. Ask about related
repositories when that relationship remains unclear; confirm their identity and
inspect only what helps explain the connection. Local context belongs to its repo;
a Linear project can hold shared context for its associated repositories. Keep
shared goals separate from repo-specific responsibilities and constraints. Record
what a related repo provides and when to consult it instead of copying its docs.

Adapt depth to uncertainty and consequences, without a fixed questionnaire or
mandatory number of rounds. Do not invent choices or prematurely turn possibilities
into commitments. A research subagent returns evidence and decision gaps to this
conversation; it does not conduct a separate user interview. External research is
useful for a named gap, not a required onboarding step.

## Persist durable understanding

Once useful material exists and its destination is resolved, read
[durable context](references/durable-context.md) before creating or updating it.
Keep intent, constraints, maintainer criteria, repository responsibilities, and
links to authoritative sources. Distinguish facts, decisions, hypotheses, and
open questions. Feature contracts and execution evidence belong in their delivery;
context is a concise navigation aid, not a transcript or code inventory.

## Close at a useful boundary

Stop when there is enough shared understanding for a meaningful next decision,
or when the user wants to pause; unanswered questions can remain explicit. Read
back the saved document and check its references and consistency with agreed facts.
Trim details that merely duplicate a linked source or record the discovery session;
keep useful decisions and uncertainties rather than targeting an arbitrary length.
Report the saved file path or Linear document URL, what remains uncertain, and a
possible next step. Offer planning around a concrete initiative when appropriate,
without starting it automatically. `project-plan` supports local and Linear plans;
saving context alone does not create or migrate plans or issues.
