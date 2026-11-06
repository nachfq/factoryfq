# Define behavior with the user

Use while an idea, brainstorm, RFP or existing requirement still needs a shared
behavioral definition. Default to guided conversation; honor an explicit request
for a full draft or delegated definition, labeling unapproved assumptions. An
autonomous implementation preference does not make definition autonomous.

## Guide one meaningful decision at a time

Start with a short map of what is already agreed and what needs definition for
this scope: intended outcome, users, main journey, rules, relevant failures or
limits, exclusions and evidence of success. Reuse known decisions. This is a
navigation aid, not a mandatory questionnaire or a demand to specify the whole
product. Choose the next topic by its impact on the intended outcome.

Explain the current topic through a concrete situation, offer alternatives and
a recommendation when useful, then ask one focused question. Adapt vocabulary
and depth to demonstrated familiarity and the user's role; do not require a
product or sales user to choose libraries or infrastructure to describe a need.
Explain necessary technical consequences in terms they can evaluate. Investigate
facts yourself and leave technical design choices for design unless they constrain
the behavior or were explicitly selected by the user.

Use representative examples of input/action/outcome to discover rules and resolve
ambiguities. Explore rejection, error, state transitions or boundaries when they
change the contract; avoid exhaustive scenario matrices. Separate source obligations
(with relevant RFP/source links), user decisions, recommendations and unanswered
questions. An analogy or brainstorming suggestion is not an approved feature.

After a coherent decision block, summarize the behavior, a confirming example,
exclusions and material uncertainties. Ask for confirmation or correction and
return control before advancing to another block. An explicit user decision is
already agreement; do not ask for its approval again. A question, tentative answer,
silence or a request for explanation does not approve the agent's proposal. An OK
applies to the block just discussed, not an entire unseen spec or implementation.

## Save agreements incrementally

Once a block is agreed, save it without a separate "save this" request, using the
established source and language. Read the applicable local/Linear writing guidance
at that point. Reuse the initiative's existing Specs; a definition-only draft can
contain partial Specs and open questions without design, tasks or delivery issues.
Create the initial artifact only when there is useful agreed content or an explicit
draft request. Do not create a second spec, approval ledger or local Linear mirror.

Read fresh before patching; preserve unrelated contributions, stable requirement
IDs and execution evidence. Mark proposals and unresolved questions separately
from agreed behavior. Do not silently amend an agreed requirement while explaining
an alternative. On correction, confirm consequential changes, update the affected
requirements/examples and identify any existing design/tasks that need revision.
Verify the saved block and briefly report its location, what changed and the next
open topic. Do not reload the whole knowledge base or append a transcript.

Keep this progress map in the existing spec/handoff, not a second checklist. A pause
can leave a useful partial definition; leave a concise resume point. Research detail
belongs in linked topic notes, not in the agreement. Context receives only durable
orientation changes, not every product decision.

## Move to design when appropriate

A useful spec lets the user recognize the agreed journey, observable outcomes,
important limits and what remains undecided. Resolve questions that change the
next delivery's behavior or scope; defer unrelated uncertainty explicitly. Match
detail to risk rather than chasing completeness or a fixed page count.

Offer design and delivery planning once enough is agreed. Specification approval
alone does not request tasks, issue creation, code or workers; an existing explicit
request covering those steps can authorize continuing. Only then use
[planning guidance](planning.md), preserving the user's collaboration preference.
Define acceptance examples before choosing test mechanisms; this does not impose
TDD, a new test suite or one automated test per requirement.
