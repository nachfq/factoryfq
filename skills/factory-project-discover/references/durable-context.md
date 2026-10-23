# Maintain a concise context document

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
