# Read and update a local delivery

Use the existing plan in its selected repository, including ignored files. For a
worker in another worktree, use the assigned source path; ignored files do not
appear automatically in a new worktree. Do not initialize or copy a missing plan.

Resolve `SKILL_DIR` to the `factory-project-delivery` skill directory:

```sh
python3 "$SKILL_DIR/../factory-project-plan/scripts/read_plan.py" --repo "$REPO" list
python3 "$SKILL_DIR/../factory-project-plan/scripts/read_plan.py" --repo "$REPO" show initiative-id
```

Read the applicable repository context and the selected plan's Specs, Technical
approach, tasks and Next delivery. Reconcile the checkpoint with actual code and
prerequisite evidence. A done task is not human acceptance or proof that its code
exists on this branch. Resolve missing prerequisites before dependent work.

For writes, follow the [local plan format](../../factory-project-plan/references/plan-format.md).
Keep mode and one current resume note in Next delivery: applied/reviewed block,
outstanding checks or corrections, and proposed next block. Replace superseded
notes instead of logging each exchange. Partially implemented tasks remain active.

After implementation and required checks, mark verified tasks done but keep Next
delivery on the delivery awaiting human review and the initiative active. Record
acceptance only when the user gives it; do not advance merely because checks pass.
Keep design in the plan and execution evidence alongside its tasks/checkpoint.
Preserve valid completion evidence when another part changes; consult or update
optional history only for consequential decisions, not transcripts.

An independent worker must respect assigned read-only source paths and parent
ownership of shared plan files. Return its progress to the designated writer
rather than modifying a shared plan concurrently. Persist only when that writer
is authorized; report unsaved progress in the conversation meanwhile.

These progress writes do not authorize Git operations. After authorized
publication, record verified commit/destination evidence without claiming that
push means PR creation or merge. Keep ignored context out of Git.
