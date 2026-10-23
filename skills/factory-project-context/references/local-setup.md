# Set up local context storage

Use only for an authorized local setup, after selecting this repository and route.

## Resolve the choices

- Identify the repository root and inspect its `.agent-context` directory and
  `config.json`. Reuse matching setup without replacing content. If the path is
  a symlink or incompatible file, report it rather than modifying its target.
- For new context, ask whether it should be **versioned** or **local** unless the
  user already chose. Each repository owns its own context.

## Create storage and apply its policy

Create `.agent-context/` and only this metadata file initially:

```json
{"versioning": "local"}
```

Use `"versioned"` for the other choice. Store this as `.agent-context/config.json`.
Reuse an existing valid config. Missing or conflicting policy needs clarification,
not an automatic reset. Repeating setup must preserve content and policy.

- **Local:** exclude `/.agent-context` in the repo's local Git
  exclude file. Find the correct file with
  `git -C REPO rev-parse --path-format=absolute --git-path info/exclude`;
  do not assume `.git` is a directory. Preserve existing rules and append the
  exact rule only if absent, on its own line. Do not edit `.gitignore` or global
  Git configuration.
- **Versioned:** leave the directory eligible for tracking;
  do not stage or commit it. If another ignore rule hides it, report that
  conflict rather than silently changing unrelated rules.

## Verify and hand off

Confirm the config and verify ignore behavior with `git check-ignore -v` and
`git status --short --untracked-files=all`. Local context must be ignored;
versioned context files must be
eligible for tracking. Report partial setup accurately if a step fails.

Report the context directory and policy. Later workflows use `context.md` for
current project context, `research/` for useful findings, and `plans/` for evolving
plans, creating them only when there is content to write. They should access
`.agent-context` explicitly because ordinary searches may skip ignored paths.
Related repositories can be referenced in that content without sharing storage;
keep machine-specific paths out of versioned documents. Leave discovery of those
relationships and writing conventions to the workflows that populate the context.
