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

Find the repository root and read applicable instructions. Reuse relevant context
and its established source; an explicit destination takes precedence. Use
[project-context](../project-context/SKILL.md) only to resolve a missing source or
association, or perform requested setup. Inspect `.agent-context` explicitly when
needed, since ordinary searches may skip ignored directories. Missing local context
alone does not trigger a Linear search. If no destination is established, resolve local
excluded, versioned, or Linear storage before writing; unavailable Linear access
does not authorize a local fallback. Continue useful read-only exploration while
the choice is pending.

For Linear, verify the repository association and follow the shared
[Linear context document](../project-context/references/linear-context.md) rules
to locate, read, and maintain the document. A request to discover using Linear
authorizes creating or updating useful context in the resolved project; it does
not authorize creating a missing project or association unless that setup was
also requested. If local and Linear copies compete without a clear choice,
resolve which is authoritative before writing. Do not merge or migrate them
implicitly, or create a local mirror of Linear content.

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

## Maintain a concise context document

Once there is useful material and the destination is resolved, create or update
`.agent-context/context.md` for local storage or the selected Linear context
document. Use the project's documentation language. Organize
around durable guidance: a brief orientation, working conventions, maintainer
criteria, repository responsibilities, and authoritative sources. Retain only
cross-delivery decisions or open questions that change future work. Feature-specific
contracts and debates belong in their plan and delivery issue, not here.

Select what to persist, rather than summarizing everything inspected:

- Prioritize knowledge that is hard to recover from the repo: user intent,
  project-specific constraints, maintainer decisions, and why related repos matter.
  Cite the source and scope. Before promoting feedback into a lasting rule, assess
  whether it applies beyond this delivery and is already covered. A clarification
  of one method is not a new project convention; keep it with that feature. Preserve
  a general principle once, without accumulating examples of every correction.
- Keep only enough technical orientation to navigate. Link to authoritative docs
  for APIs, versions, component inventories, and development commands. Retain a
  non-obvious technical constraint when it materially changes future decisions.
- Keep provisional execution details in the conversation and published evidence
  in the delivery issue (or local Tasks/checkpoint). Branch/HEAD, synchronization,
  checks and review status are not project context. Link to a blocker if its
  implication affects future work; do not reproduce its execution history or
  duplicate personal defaults and project instructions.
- Keep potential next initiatives brief and explicitly tentative. Detailed scope,
  task breakdowns, API proposals, and validation plans belong to planning.

Distinguish observed facts, user decisions, hypotheses, and unresolved questions.
Link to repository-relative sources in local context; in Linear, qualify paths
with their repository or use canonical URLs. Keep machine paths out of shared
content. This document is a navigation aid and
current understanding, not a replacement README, code inventory, or chat transcript.

Update the same document as answers arrive. Preserve unrelated useful context,
replace superseded statements, and remove duplication rather than appending a
history of every turn. Do not silently settle conflicting evidence; clarify it
or leave the uncertainty visible. Create no empty research or planning folders.

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
