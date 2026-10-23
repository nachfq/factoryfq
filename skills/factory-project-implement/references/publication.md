# Close an authorized delivery

Read this only for a commit/push request or an applicable scoped closure agreement
whose conditions hold. Code validation alone is not Git authorization. Reuse the
[delivery agreement](delivery-contract.md) to verify scope and destinations without
asking for the same permission again. Independent workers obtain authorization
from the user or reuse the user's recorded agreement, not a new parent approval.

Use [factory-git-commit](../../factory-git-commit/SKILL.md), including its bounded post-commit review
and push by default; honor local-only requests. After successful push of
user-reviewed work, record the checkpoint through
[factory-project-delivery](../../factory-project-delivery/SKILL.md). Reuse any update already saved
by `factory-git-commit`; respect the designated writer and report partial failures.
PR creation, release publication and merge remain separately authorized actions.
Do not start another delivery as a side effect of closure.
