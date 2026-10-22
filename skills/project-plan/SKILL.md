---
name: project-plan
description: Help choose what to work on next and collaboratively build or revise a plan in local files or Linear documents and delivery issues. Use for planning small, reviewable deliveries or suggesting next steps from project context, not for implementation.
---

# Plan project work

Follow applicable user and project instructions and their language conventions.
Read relevant `.agent-context/context.md` at the repository root when present,
including when ignored by Git; reuse it if already loaded and verify relevant facts.

Act as the planner in this conversation. A starting point can be an idea, a problem,
or simply "what should we do next?" Planning authorizes plan artifacts, not code
changes, commits, or implementation. Keep implementation for a separate session;
this skill does not create or coordinate an implementer agent.

## Resolve the current source

Reuse the established context source and explicit destination; resolve competing
sources before writing. Do not migrate, mirror, or silently fall back from Linear
to local files. Missing discovery is not a gate for a focused planning discussion.
When locating plans or preparing to persist one, read
[plan sources](references/plan-sources.md), then only the selected storage format
when its details are needed. Do not load all references at startup.

## Choose a direction together

Ground suggestions in the user's goals, current code, existing plans, and blockers.
Filter candidate work by this repository's responsibilities, agreed scope, and
work or validation already covered. Related repos provide context; their pending
work does not automatically belong here. Reopen a settled decision or propose
another review only when new evidence or an explicit request warrants it.

For an open-ended request, offer useful options when they exist, explain tradeoffs,
and recommend a next step. Waiting for feedback or choosing no new work is a valid
recommendation: explain what decision or evidence would unblock progress, without
inventing a task or plan to fill the gap. Investigate repo facts yourself; ask
focused questions about intent and consequential choices, letting each answer
shape the next question. Do not repeat settled decisions, impose a fixed interview,
or treat a recommendation as the user's choice.

A request to analyze what to do next starts a comparison and conversation. Present
the evidence and recommendation, then resolve the user's direction before breaking
it into implementation tasks. A saved draft is not evidence of that choice. Any
persisted comparison remains analysis; it need not use the plan's Specs/Tasks
format and must not create delivery issues for an unchosen direction.

Research a named uncertainty when needed. Delegate bounded read-only investigations
when they save context or allow useful parallel work; keep user dialogue here.
If evidence is insufficient to plan implementation, a scoped investigation with a
clear question and expected evidence can itself be the next delivery. Do not
invent implementation tasks before that uncertainty is resolved.

## Develop, revise, and hand off

After the user chooses a direction (or explicitly requests a speculative draft),
read [planning guidance](references/planning.md). Apply project-context criteria
to design, scope, and verification; explain the technical approach before the task
breakdown. Justify the smallest sufficient validation, and agree a bounded delivery
that the human can review. A speculative draft must keep its assumptions and
unchosen direction visible; it does not authorize delivery issues by itself.

When evidence requires a revision, read
[revision and handoff](references/revision-handoff.md) before changing the plan.
Preserve valid work, stable IDs, and evidence-backed states; discuss material scope
changes and do not rewrite durable context to justify a plan.

At the planning handoff, read the handoff portion of that reference, verify saved
artifacts and their links, and explain the behavior, rationale, next delivery, and
unresolved decisions. Planning ends there: readiness is not execution permission.
