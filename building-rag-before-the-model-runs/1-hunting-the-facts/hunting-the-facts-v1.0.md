# Hunting the Facts

### Sourcing and Acquisition as the First Decision in Retrieval-Augmented Generation

**Author:** Jesper Karlsson / Otrobonita AI Labs
**A part of the series:** Building RAG Before the Model Runs
**Document Version:** 1.0

---

## Opening: The Frame Decides Everything

Every retrieval-augmented system has an outer boundary it can never cross: it can only ever answer from what someone chose to collect. Preprocessing can rescue a mangled source; chunking can cut it well; retrieval can rank it fairly. None of them can retrieve a document that was never fetched, and none can vouch for one whose origin nobody recorded.

But sourcing does something even earlier than setting a ceiling. **It chooses the camera angle.** The boundary you draw around a corpus — what you decide is "in scope" and what you deliberately leave out — is not a neutral act of collection. It is a claim about what reality the system will represent. And that frame choice cascades downstream in two ways:

- **What the system CAN answer** is constrained by what's in frame
- How precisely the system can select, rank, and qualify evidence is decided by whether that frame is coherent enough for the questions its users will ask
Sourcing is the one stage whose mistakes are strictly invisible downstream — a coverage gap does not throw an error, it simply returns the second-best answer forever, and no one notices the first-best was never in the room. A sourcing decision made carelessly in week one governs the ceiling of everything built on top, and also decides the architecture it will live in.

This paper is about treating that first decision as a first-class engineering problem: not just "did we collect it?" but "have we been honest about the camera angle we chose, and is that angle appropriate for the questions users will actually ask?"

Three field episodes frame the argument. Each comes from a real build, and each shows a different consequence of deciding what belongs inside the corpus and what must remain outside it.

## What sourcing is, and where it sits

Sourcing — acquisition — is everything that turns "the knowledge exists somewhere in the world" into "a raw source is sitting in our ingestion staging area, with a recorded frame." It is the stage before preprocessing: preprocessing assumes a raw file is already in hand and a frame has been chosen; sourcing is how the file got there and what boundary you drew around it.

In pipeline order the series runs **sourcing → preprocessing → chunking**, and this is the first link. It decomposes into four questions, and a mature pipeline answers all four deliberately rather than by accident:

- **Frame** — what reality are we representing? What's in the photograph and what's cropped out? (This is the epistemic choice.)
- **Coverage** — what do we collect, and just as importantly, what do we knowingly leave out?
- **Access** — how do we fetch it, within the rate limits, licenses, and terms that govern it?
- **Provenance** — what do we record about each item, so that later we can trust it, cite it, refresh it, and defend our right to it — AND to defend our choice of frame?

#### The claim of this paper, stated plainly:

Sourcing establishes a frame on reality, and that frame constrains both what the system can answer and which evidence it is likely to retrieve. Specialisation is not an automatic outcome of sourcing, but a narrow and coherent frame permits more detailed expert selection, clearer authority rules, and retrieval behaviour adapted to one domain. The same material in a centralised corpus may compete with passages from different contexts, time periods, or authority levels, increasing retrieval interference and the risk of an answer that is textually supported but wrong for the user's situation. Coverage sets the ceiling of what can be answered; provenance records both the origin of each source and the limits of the frame. Both are fixed at acquisition time — cheaply then, expensively or never later.

## The Frame: Narrowed, Broadened, or Kept Alive

A corpus does not begin with collection. It begins with a decision about which part of reality the system is supposed to represent.

Provenance can establish where an item came from, when it was acquired, and how it was transformed. It cannot establish that the selected material constitutes the correct frame. A perfectly traceable corpus may still be incomplete, misleading, or unsuitable for the questions it is expected to answer.

The three corpora examined during this work produced three different framing outcomes: one was deliberately narrowed, one was deliberately broadened, and one could not honestly be considered complete.

#### Apollo mission transcripts: narrowing the frame

We initially considered a corpus spanning the wider Apollo program. After obtaining API access to the US National Archives and Records Administration (NARA), however, we found no defensible boundary for what “the Apollo program” should include. Mission transcripts, technical reports, photographs, engineering records, administrative material, and later historical interpretation could all plausibly belong in frame. Any stopping point risked appearing comprehensive while remaining arbitrary.

The transcripts offered a narrower and more defensible boundary. They form a bounded class of time-indexed, multi-speaker technical dialogue, with recurring timestamps, speaker codes, mission phases, and OCR problems. Those properties made them particularly useful for examining preprocessing and chunking: whether extraction preserves speaker and temporal structure, and whether retrieval units follow conversational rather than merely textual boundaries.

We initially included transcripts from the Mercury and Gemini programs as well. Much of this material consisted of degraded typewritten originals from the early and mid-1960s, affected by ink bleed, inconsistent reproduction, damaged pages, and difficult OCR conditions. Restoring enough of it to support dependable retrieval would have become a substantial archival project in its own right.

That effort was disproportionate for a system intended primarily to demonstrate RAG preprocessing and chunking problems. Rejecting most of the material was therefore not a failed collection attempt. It was a useful sourcing outcome: the condition of the records changed the defensible scope of the corpus.

We consequently framed the corpus as **Apollo mission transcripts**, not **the Apollo program**. From a retrieval perspective, that choice produces a deliberately limited system. It cannot serve as a general authority on Apollo, and it was never intended to. Its purpose is to expose specific upstream problems clearly enough that preprocessing and chunking strategies can be inspected, compared, and challenged.

The resulting corpus can be explored at [spacetalks.otrobonita.com](https://spacetalks.otrobonita.com/).

#### Mark Twain and Samuel Clemens: broadening the frame

The initial sourcing for the Mark Twain corpus was more straightforward. Project Gutenberg had already digitised and organised a substantial portion of the relevant public-domain literature, making it a practical starting point for acquisition.

The difficult decision was not where to find the books, but what the corpus was meant to represent. A corpus framed around **Mark Twain** could reasonably contain only works published under that name. A corpus framed around **Samuel Clemens** could also include correspondence, autobiographical material, journalism, speeches, biographical records, contemporary accounts, and works published under other names.

We decided to look beyond the pen name and include the person behind it. Python acquisition scripts were therefore created to collect relevant material from the Internet Archive and Wikisource in addition to Project Gutenberg.

This broadened the corpus from the output of a named author to documentary evidence about Samuel Clemens as a writer and historical person. It also changed the retrieval problem. The system had to distinguish between primary works, letters, editions, biographical accounts, commentary, and material that merely mentioned him.

The broader frame offers more kinds of answer, but it also introduces more opportunities for ambiguity and contradiction. Provenance therefore becomes part of the answer rather than merely a hidden property of the index. A passage written by Clemens, a later editor’s note, and a biographer’s interpretation may concern the same event without carrying the same evidential weight.

The resulting corpus can be explored at [mark.otrobonita.com](https://mark.otrobonita.com/).

#### Rag Of Rags: maintaining a living frame

**Rag Of Rags** began as an agentic acquisition process across internet sources about retrieval-augmented generation. Unlike the Apollo and Twain/Clemens corpora, its subject does not settle. Libraries change, practices mature, claims become obsolete, and new evidence appears. Its sourcing process therefore cannot honestly be described as complete.

The system is intended to include an agent that periodically revisits registered sources and proposes additions, updates, or removals while preserving the provenance and review history of each change. Automation can identify candidates for revision, but it should not silently rewrite the accepted knowledge base. A proposed change remains a research decision: what changed, which source supports the change, what should be superseded, and who accepted it?

Much of this knowledge may already be represented in a general-purpose model, but only up to its training boundary and not necessarily with sufficient precision, provenance, or consistency. This becomes especially consequential when organisations adopt older or smaller models. Their capabilities may remain adequate for the task while recently acquired knowledge effectively disappears from the system.

A maintained specialist corpus separates the currency of the knowledge from the age of the model. Sources can be added, corrected, challenged, or withdrawn without retraining the underlying model, and those changes remain visible to reviewers.

The arrangement also gives the organisation explicit control over the system instructions governing how the corpus is interpreted and used. Those instructions do not replace model training, but they can materially affect retrieval behaviour, evidential standards, uncertainty handling, source selection, and the form of the final answer. The maintained sources, their provenance, the retrieval policy, and the system instructions together determine much of the system’s observable behaviour.

Rag Of Rags has no general-purpose graphical interface. It serves primarily as a demonstration of how a specialist, domain-specific RAG can remain deliberately limited in scope while being maintained and made available to the relevant users or systems.

## Acquisition inside organisations

Public archives make the mechanics of acquisition unusually visible. Within an organisation, the same decisions are often distributed across systems that were never designed to form a coherent knowledge corpus.

Potential sources include Teams channels, meeting transcripts, expert debriefs, SharePoint libraries, production databases, ticketing systems, operational documentation, source repositories, and records held in legacy applications. Each source carries different access rules, retention periods, ownership expectations, formats, and evidential limitations.

The challenge is not simply to connect these systems. A collection process must determine which channels and meetings are authoritative, whether informal discussion should be treated as evidence, which database states require historical preservation, and whether an expert’s explanation supplements or contradicts the formal record.

Expert debriefs are particularly valuable when operational knowledge has never been documented, but they also illustrate why collection and verification cannot be separated. Memory is selective. Terminology changes. Different experts may describe the same process differently. The debrief must retain its speaker, date, context, and relationship to other evidence if later users are to judge it responsibly.

Production databases present another problem. Their current state may answer what is true now while erasing how and why it became true. A useful corpus may therefore require snapshots, event histories, schemas, data dictionaries, and documentation of the business processes that produced the records—not simply access to the latest rows.

Agentic access to legacy systems remains one of the largest practical obstacles to keeping organisational RAG systems relevant. Older systems may lack stable APIs, searchable exports, usable identity integration, or reliable metadata. Access may depend on graphical interfaces, proprietary formats, fragile reports, or undocumented procedures known by only a few employees.

An agent can assist with discovery, extraction, comparison, and monitoring, but access alone does not establish meaning or authority. The organisation still has to decide what may be collected, what should be trusted, what requires human review, and which absences must remain visible.

Keeping a RAG relevant is consequently not a one-time ingestion task. It is an ongoing research and governance process. The system must know not only where its information came from, but also why those sources were selected, what was excluded, which parts may have become stale, and who remains responsible for changing the frame.

## Coverage: what you never collect, you can never retrieve

The failure mode here is the quietest in the entire pipeline, because it produces no artifact to inspect. A missing document is not a corrupted chunk or a bad rank; it is an absence, and absences do not surface in evaluation unless the evaluation was specifically designed to catch them.

This reframes acquisition as a scoping decision, not a completeness one. You are not trying to collect everything; you are trying to collect a corpus whose **boundaries you understand and can defend**. Two disciplines make that tractable:

**Separate discovery from harvest.** Walk the source's structure once to enumerate what exists — for NARA, that meant traversing the Record Group 255 series tree to list record identifiers — before spending budget pulling full detail. Discovery answers "what is there and is it in scope"; harvest pulls only the parts that pass. Collapsing the two — issuing broad keyword searches and filtering the results client-side — is the single fastest way to burn a query budget on records you were always going to discard.

**Scope to a boundary, not a keyword.** A query filtered to a record group or series burns far fewer calls than a keyword sweep across an entire catalog that you then narrow after the fact. The boundary is also the honest description of your corpus: "Record Group 255, phased by mission" is a coverage statement a reader can evaluate; "we searched for Apollo" is not.

When the budget genuinely cannot cover the scope in one cycle, that is not a failure — it is a **phase boundary**. Ingest one specialty this cycle, the next after the reset, and record where you stopped so the next run is additive rather than a redo. Which brings us to the second half of the problem.

## Provenance: the frame made explicit and defensible

A source with no recorded origin is a liability wearing the costume of an asset. But sourcing's real liability is a frame with no recorded boundaries. You collected documents, but did you record why you stopped where you stopped? Did you record the coherence claim?

The ragofrags build treated this as non-negotiable, and the habit is simple to state:

Every source carries its own provenance as data, not a footnote: a URL, a license note, a retrieved_at timestamp, and — for anything cloned from a repository — the exact git commit SHA. And the corpus as a whole carries a frame record: the boundaries of the selection, the scope statement, its intended users and questions, its authority rules, and its maintenance obligations.

Two consequences follow, and both are worth the discipline.

**Rejection is a first-class outcome.** When a documentation site's license could not be defended, the manifest did not silently drop it — it recorded status: rejected with a written reason. A rejection with a reason is reusable knowledge: the next build knows not to re-litigate it, and an auditor can see the decision was made deliberately. A silent omission teaches no one anything and looks, later, exactly like an oversight.

**A manifest is cheaper than a re-hunt.** Persisting what you have already fetched — identifiers, series, fetch dates, frame boundaries — turns an interrupted or resumed acquisition into an additive operation instead of a full redo. On a metered API this is not housekeeping; it is the difference between staying inside the monthly budget and blowing through it re-fetching what you already had. The manifest is also the artifact that makes the **frame legible**: it is the difference between "we have ragofrags" and "here are the N sources we hold, by topic/license/date, with explicit boundaries and architectural intent."

Provenance, in other words, is not paperwork you do after the interesting part. It is the thing that records the camera angle — the coherence claim that lets every later stage — preprocessing, retrieval, citation, and answer generation — trust the ground it stands on.

## Access: the budget is part of the architecture

The Apollo hunt's real lesson generalizes past NARA's specific limit. Almost every serious source is metered, licensed, or both, and those constraints are not obstacles to route around — they are inputs to the design. A few habits carry across sources:

- **Know what the meter counts.** NARA's cap is on metadata queries, not on the digital-object bytes served from its separate media host — so pulling the files themselves is not what drains the budget. Misread the meter and you optimize the wrong thing.
- **Maximize the work per call.** Largest page sizes, fewest round-trips; every avoidable call is coverage you could have bought instead.
- **Ask for more once you know your real numbers.** NARA will consider a higher limit for a stated use case — but the ask is credible only after discovery has told you the actual record counts. Guessing the size of your own corpus upfront is not a request an archive can act on.
None of this is exotic. It is simply what it looks like to treat acquisition as engineering: measure the constraint, design within it, and record what you did.

## What it costs to skip this — and the hand-off to preprocessing

Sourcing shares the awkward economics of the whole series: it is cheapest to get right at the start and most expensive to fix later. But it has a failure profile all its own. A coverage gap is undetectable without a test built to find it; a frame gap is invisible until users ask questions the selected sources were never capable of answering responsibly. Both are nearly free to expose at acquisition and painful — sometimes impossible — to repair once the corpus is built, indexed, and in production.

The one decision this paper asks of a team is to stop treating acquisition as the throat-clearing before the real work. Ask first: what part of reality is this corpus intended to represent, and is that frame defensible for the questions its users will ask? That decision shapes everything downstream:

- A narrow, coherent frame can support detailed expert selection, domain-specific authority rules, and retrieval tuned to the distinctions that matter inside that field.
- A broad or centralised corpus must control retrieval interference between sources from different contexts, time periods, and authority levels; otherwise apparent relevance can displace the evidence appropriate to the user's situation.
Scope the corpus to a boundary you can name. Separate discovery from harvest. Record provenance as data — both the source metadata AND the frame boundaries. Reject with reasons. Respect the meter as an architectural constraint. Do that, and you hand the next stage something it can actually build on: a bounded, dated, license-clear set of raw sources, each traceable to its origin, and a recorded frame that preprocessing and chunking can rely on.

That hand-off is exactly where the next paper begins. Human Slop In, AI Slop Out takes the raw sources this stage collected within the frame this stage established and asks what it takes to make them machine-legible without silently corrupting them. Sourcing decides what angle we are representing and whether that angle is defensible for its intended use; preprocessing decides whether the model can read the selected evidence without losing its structure or meaning. Neither can fix the other's mistakes — which is the whole reason they are separate papers.

## About This Paper

Disagreement is the point. If part of this is wrong — and some of it will be — the author would rather hear it than not.

Cite as Karlsson, J. (2026). Hunting the Facts. Otrobonita AI Labs. otrobonita.com/whitepapers.

License Creative Commons Attribution 4.0 (CC BY 4.0). Share it, quote it, argue with it — attribution is all that is asked.

### The authoring team

- **Jesper Karlsson** — concept, thesis, ideas, structure, and accountability for every final call.
- **Fable 5, GPT 4.5, Grok 4.5, and Gemini 3.6** — drafting support, fact-checking, handling of uncertainty and counter-evidence, independent critique, and adversarial review.
5 iterations and approximately twenty individual feedback loops.

Written in July 2026.
