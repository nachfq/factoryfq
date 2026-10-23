# Preserve and retrieve project research

Use for substantive learning or investigation that is useful to another session
but too detailed for project orientation. Discovery and planning investigations
preserve useful findings as they arise; the user need not request storage separately
once the destination is agreed. Explicit read-only or chat-only requests take precedence.

## One maintained note per coherent topic

Find an existing relevant note before creating one. Organize by question or topic,
not by person, session, or date. Reuse established titles and IDs. Closely related
questions can share a note; split when they answer different retrieval needs.
Skip generic explanations already covered by a useful linked source unless the
project-specific interpretation or reasoning would otherwise be lost.

Use a descriptive title and a short opening answer or summary. Keep scoped findings
and source links, the rationale for alternatives, and consequential open questions.
Distinguish source requirements, verified observations, interpretations, and
explicit user decisions. Include a source/version or verification date when it
matters to validity. Preserve useful reasoning without a transcript or a compulsory
template of empty sections. Notes do not turn recommendations into approved specs.

Replace superseded claims and consolidate overlap instead of appending turn logs.
Preserve relevant evidence and disagreements; a newer note does not automatically
overrule an earlier decision. If findings become part of a plan, link its agreed
contract rather than maintaining competing editable specs in the note.

## Store and link in the selected destination

- **Local:** use `.agent-context/research/<topic>.md` under the existing storage
  policy. Create the directory only when saving a useful note. Link from
  `context.md` with a relative path and a brief project implication.
- **Linear:** list document metadata in the verified project, with pagination,
  and inspect plausible topic matches. For a new note, use `Research: <topic>`
  (topic and prose follow the project's language), attached to that same project.
  Use `save_document` with only the verified project as parent. Recheck for
  duplicates before creation; keep the returned ID and canonical URL. Link from
  `Project context` with a brief project implication. Create no issue or local mirror.

For either destination, read current contents immediately before editing and
preserve unrelated contributions. Prefer focused changes. Concurrent agents should
own separate topics or coordinate one writer for a shared note; fresh reads and
patches do not provide a lock. Reread after a conflict or uncertain write and resolve
conflicting decisions instead of overwriting them. Verify note contents and location
before shortening an overloaded context, then verify its new link. After partial
failure, report what saved and complete only missing steps; do not delete the only
copy of useful findings.

## Retrieve selectively

Start from the relevant links and implications in project context. Open only notes
needed for the current question. If a link is missing, inspect research filenames
and headings locally, or project-scoped document titles/metadata in Linear, before
reading candidate notes. A title-search miss does not establish that their contents
lack the information. Never load all notes or conversations by default. Cite the
actual source and distinguish a missing fact from an undecided question.
