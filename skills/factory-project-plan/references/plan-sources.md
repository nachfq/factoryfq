# Resolve plan storage and read selectively

Read applicable instructions and reuse relevant context and its established source.
Use [factory-project-context](../../factory-project-context/SKILL.md) only to resolve a missing source
or association, or perform requested setup. Honor the user's selected plan
destination; otherwise reuse the established context source for a new plan and
the existing plan's destination for revisions. If sources compete or the choice
is missing, resolve it before writing. Do not migrate, mirror, or silently fall
back to local files when Linear is unavailable.

For local plans, use the reader below; read [local plan format](plan-format.md)
when creating or revising an artifact, not merely to list existing plans.
For Linear, follow [Linear plans](linear-plans.md) to verify the project,
read its context, and locate documents and delivery issues selectively. Do not
run the local reader or initialize `.agent-context` for the Linear route. Do not
choose an active initiative merely because it is newest. Read relevant history
only when needed to understand a decision.

For local plans, set up missing storage through `factory-project-context` before writing.
Read-only exploration can continue while the destination choice is pending.
Missing discovery is not a gate: gather what this decision needs. Use
[factory-project-discover](../../factory-project-discover/SKILL.md) when the user needs broader project
onboarding rather than a focused next-step discussion.

## Read local plans selectively

Resolve `SKILL_DIR` to the `factory-project-plan` skill directory (not `references/`); the reader requires Python 3 and Git.

```sh
python3 "$SKILL_DIR/scripts/read_plan.py" --repo "$REPO" list
python3 "$SKILL_DIR/scripts/read_plan.py" --repo "$REPO" show initiative-id
```

`list` reads metadata only and generates an index without maintaining a second
state file. `show` reads only the selected `plan.md`, never `log.md`. Both are
read-only and work from a repo root or subdirectory. Search a relevant log by
requirement/task ID when needed instead of loading all initiative histories.
