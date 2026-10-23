# GitHub repository defaults

Apply this policy as part of creating a new GitHub repository, unless the user
opts out. For existing repositories, apply it only when the user requests setup
of these settings; reusing or cloning a repo does not authorize policy changes.
Research-only work performs no writes.

## Policy and payloads

- PRs into `main` require one approval.
- Repository administrators can bypass the ruleset, including direct pushes.
  Use `RepositoryRole` ID `5` with `bypass_mode: always`, not a specific user or
  the organization-admin role.
- PR merging uses squash only. Set this at repository level as well, independently
  of ruleset availability or bypass. It does not prevent admin direct pushes.
- Do not add required CI contexts or other review, deletion, or force-push rules.
  Add checks later when actual CI jobs exist and the user requests them.

Use [main-ruleset.json](../assets/main-ruleset.json) and
[merge-settings.json](../assets/merge-settings.json) as API payloads. Resolve
these paths relative to this skill's directory, not the new project's directory.
Do not copy the payloads into the new repository as scaffolding.

## Availability

Inspect repository visibility, permissions, and the owner's plan when visible.
Do not persist plan assumptions in local profiles.

| Repository | Branch ruleset eligibility |
| --- | --- |
| Public | Free or paid plan |
| Private, personal owner | Pro or applicable paid entitlement |
| Private/internal, organization owner | Team or Enterprise Cloud |
| Non-public with confirmed Free plan | Skip ruleset creation; report unsupported |
| Non-public with missing/null/unknown plan | Unknown, not Free; check availability read-only |

Before POST, use `GET /repos/OWNER/REPO/rulesets?includes_parents=true` with all
pages to inspect existing rules and availability. With an unknown plan, proceed
only if that read succeeds and administrative access is established. An explicit
upgrade-required response means skip creation. Permission, authentication,
rate-limit, and network errors are unresolved access, not evidence of Free;
report them without repeated writes. Never change visibility or subscription
to enable the feature.

Squash-only repository settings are independent of ruleset plan gating. Apply
them when authorized and permitted even when branch rulesets are unsupported.

## Apply and verify

1. Read `GET /repos/OWNER/REPO`. If the three merge settings already match, skip
   the PATCH. Otherwise send the merge-settings payload:

   ```sh
   gh api --method PATCH "repos/$owner/$repo" --input "$skill_dir/assets/merge-settings.json"
   ```

2. For eligible rulesets, inspect existing ruleset details, including inherited
   organization rules. An equivalent active policy needs no new ruleset. Never
   overwrite, delete, or weaken other policies. The bundled payload retains the
   legacy identifier `harness-fq-main` for compatibility; this name is not a
   requirement to replace an equivalent policy. If `harness-fq-main` exists with
   different contents, or other policies affect the requested behavior, report
   the difference for resolution instead of duplicating or replacing it.
   Admin bypass in one ruleset does not bypass other applicable rulesets.

3. If no matching or conflicting policy exists, create the ruleset:

   ```sh
   gh api --method POST "repos/$owner/$repo/rulesets" --input "$skill_dir/assets/main-ruleset.json"
   ```

   Target `refs/heads/main` even for an empty repo. Do not create a commit or
   push merely to materialize the branch. Admin bypass permits the owner's
   initial push when they choose to make it.

4. Read back repository merge settings and the ruleset by its returned ID. Verify
   active enforcement, branch target, main condition, one approval, and admin
   bypass. Inspect `GET /repos/OWNER/REPO/rules/branches/main` to confirm active
   effective rules; this endpoint supports names of branches that do not yet
   exist. If effective rules cannot be verified, say verification is incomplete.

5. Report squash settings and ruleset state separately on partial success.
   After a timeout or uncertain POST, read state before retrying to avoid
   duplicates. Never claim protection merely because a request was sent.

Distinguish applied and verified, already present, skipped as unsupported, and
blocked or unverified. Include the reason when incomplete.

## Sources

- [Availability](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
- [Rulesets REST API](https://docs.github.com/en/rest/repos/rules)
- [Repository settings API](https://docs.github.com/en/rest/repos/repos#update-a-repository)
- [Repository-role IDs](https://github.com/integrations/terraform-provider-github/blob/main/docs/resources/repository_ruleset.md)
