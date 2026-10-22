# Resolve context storage

Find the repository root and read applicable instructions. Reuse relevant context
and its established source; an explicit destination takes precedence. Use
[project-context](../../project-context/SKILL.md) only to resolve a missing source or
association, or perform requested setup. Inspect `.agent-context` explicitly when
needed, since ordinary searches may skip ignored directories. Missing local context
alone does not trigger a Linear search. If no destination is established, resolve local
excluded, versioned, or Linear storage before writing; unavailable Linear access
does not authorize a local fallback. Continue useful read-only exploration while
the choice is pending.

For Linear, verify the repository association and follow the shared
[Linear context document](../../project-context/references/linear-context.md) rules
to locate and read the document. Before persisting changes, read
[Linear context writing](../../project-context/references/linear-context-write.md). A request to discover using Linear
authorizes creating or updating useful context in the resolved project; it does
not authorize creating a missing project or association unless that setup was
also requested. If local and Linear copies compete without a clear choice,
resolve which is authoritative before writing. Do not merge or migrate them
implicitly, or create a local mirror of Linear content.
