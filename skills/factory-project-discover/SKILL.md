---
name: factory-project-discover
description: Explore a project, explain its domain, and preserve useful findings in context and research notes. Use for onboarding, project learning, research, and follow-up discussion before a concrete initiative is defined, in local files or an associated Linear project.
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
research notes before repeating an investigation. Inspect documentation,
entry points, manifests, or checks to understand
what the project does, its main components, and how it is developed and verified.
Use targeted searches to resolve concrete gaps rather than reading the whole repo.
Treat existing context as evidence to check, not unquestionable truth. Describe
documented test commands as such; do not imply they were executed.

## Build understanding with the user

Briefly explain what you understand, with relevant evidence, then ask the next
question that most affects that understanding. Ask one focused question at a time
and let the answer guide the next exploration or question. Do not repeat settled
decisions or ask the user for facts readily available in the repo.
When the user is learning the domain, explain concepts and their relationships
with a concrete example before asking for technical choices. Adapt to follow-up
questions without turning each explanation into a proposed implementation task.

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

## Capture useful findings during the conversation

Discovery includes maintaining shared knowledge. Once storage is selected and
available, save substantive findings, corrections, and unresolved tradeoffs at
natural conversation boundaries, before closing the turn; do not wait for a
separate "save this" request. A repeated explanation or ordinary chat needs no
write. Honor explicit read-only or chat-only requests and resolve missing storage
or language choices before persistence; keep useful exploration moving meanwhile.
For a new project with no established language for documentation and work tracking,
ask the user which language to use before writing the first artifact.
Do not infer that choice from the conversation or an external source such as an RFP;
the conversation may remain in a different language. Reuse an existing convention
or explicit choice without asking again.
Choose the destination by content, not by whichever document is already open:

- **Context:** brief project intent, durable working criteria, repository roles,
  consequential open questions, and links. Follow [durable context](references/durable-context.md).
- **Research note:** explanations, comparisons, source-backed findings, and the
  reasoning behind open alternatives. Own their organization as they evolve:
  consolidate, split, and relink without waiting for the user to direct routine
  maintenance. Follow [research notes](references/research-notes.md).
- **Plan or issue:** agreed specs/design or execution evidence belong to their
  existing workflow; research alone does not authorize creating them.

Do not append detailed learning to context. Keep a short implication and a link
there; consolidate the detail in a topic note. Before finishing, verify that each
new block belongs in its destination and is not duplicated elsewhere. When existing
context contains research detail, preserve it in a verified note before replacing
that detail with its brief implication and link. Keep hypotheses distinct from
requirements and user decisions throughout.

## Close at a useful boundary

Stop when there is enough shared understanding for a meaningful next decision,
or when the user wants to pause; unanswered questions can remain explicit. Read
back changed documents and check their links and consistency with agreed facts.
Trim details that merely duplicate a linked source or record the discovery session;
keep useful decisions and uncertainties rather than targeting an arbitrary length.
Report the saved file path or Linear document URL, what remains uncertain, and a
possible next step. Offer planning around a concrete initiative when appropriate,
without starting it automatically. `factory-project-plan` supports local and Linear plans;
saving context alone does not create or migrate plans or issues.
