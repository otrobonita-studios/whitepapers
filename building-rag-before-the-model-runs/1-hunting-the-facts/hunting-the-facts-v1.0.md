# Hunting the Facts

### Sourcing and Acquisition as the First Decision in Retrieval-Augmented Generation

**Author:** Jesper Karlsson / Otrobonita AI Labs
**A part of the series:** Building RAG Before the Model Runs · Paper 1 of 3
**Reading order:** **Hunting the Facts** → Human Slop In, AI Slop Out → A Chunky Size Fits Nobody
**Document Version:** 1.0

---

## 1. Opening: The Frame Decides Everything

Every retrieval-augmented system has an outer boundary it can never cross: it can only ever answer from what someone chose to collect. Preprocessing can rescue a mangled source; chunking can cut it well; retrieval can rank it fairly. None of them can retrieve a document that was never fetched, and none can vouch for one whose origin nobody recorded.

But sourcing does something even earlier than setting a ceiling. **It chooses the camera angle.** The boundary you draw around a corpus — what you decide is "in scope" and what you deliberately leave out — is not a neutral act of collection. It is a claim about what reality the system will represent. And that frame choice cascades downstream in two ways:

1. **What the system CAN answer** is constrained by what's in frame
2. **What kind of system this becomes** — a specialist, a mesh node, or part of something larger — is decided by whether that frame is coherent enough to stand alone

Sourcing is the one stage whose mistakes are strictly invisible downstream — a coverage gap does not throw an error, it simply returns the second-best answer forever, and no one notices the first-best was never in the room. A sourcing decision made carelessly in week one governs the ceiling of everything built on top, and also decides the architecture it will live in.

This paper is about treating that first decision as a first-class engineering problem: not just "did we collect it?" but "**have we been honest about the camera angle we chose, and does that angle fit into a system that stands alone or into a mesh that admits its frame?**"

Two field episodes frame the argument, both worked examples from real builds, and both are about what happens when sourcing choices have architectural consequences.

---

## 2. What sourcing is, and where it sits

Sourcing — acquisition — is everything that turns "the knowledge exists somewhere in the world" into "a raw source is sitting in our ingestion staging area, with a recorded frame." It is the stage *before* preprocessing: preprocessing assumes a raw file is already in hand *and a frame has been chosen*; sourcing is how the file got there and what boundary you drew around it.

In pipeline order the series runs **sourcing → preprocessing → chunking**, and this is the first link. It decomposes into four questions, and a mature pipeline answers all four deliberately rather than by accident:

- **Frame** — *what reality are we representing?* What's in the photograph and what's cropped out? (This is the epistemic choice.)
- **Coverage** — *what* do we collect, and just as importantly, what do we knowingly leave out?
- **Access** — *how* do we fetch it, within the rate limits, licenses, and terms that govern it?
- **Provenance** — *what do we record* about each item, so that later we can trust it, cite it, refresh it, and defend our right to it — AND to defend our choice of frame?

The claim of this paper, stated plainly:

> **Sourcing establishes a frame on reality, and that frame has two consequences: it constrains what the system can answer, and it determines whether the corpus stands alone as a specialist or becomes a routed node in a mesh.** Coverage decides the ceiling of what can be answered; provenance records not just the origin of each source but the coherence of the frame. Both are fixed at acquisition time — cheaply then, expensively or never later.

---

## 3. The Frame: Is This a Specialist or a Mesh Node?

Before coverage, before access budgets, before provenance schemas — the first question is: **What angle are we choosing to represent?**

This is not about "how much data" — it is about *coherence of boundaries*.

### The specialist frame (Apollo, Twain)

A specialist is a RAG that stands alone because its frame is internally consistent and defensible.

**Apollo transcripts** — the frame is *time-indexed, multi-speaker, technical dialogue from a bounded set of missions*. That frame is tight: GET timestamps, speaker codes (CDR, CMP, LMP, CAPCOM), mission phases. Everything sourced shares that structure. The frame is coherent enough that preprocessing can rely on it (timestamps *will* be recoverable; speakers *will* be labeled) and chunking can align to it (temporal windowing makes sense; dialogue turns matter). The system can stand alone: "ask me about Apollo."

**Mark Twain corpus** — the frame is *dense narrative prose and letters, 19th-century vernacular, a complete collected works from Project Gutenberg*. That frame is equally tight: chapter boundaries, letter dates and recipients, consistent OCR/markup. Again, preprocessing knows what to expect, chunking can respect document and narrative hierarchies. It stands alone: "ask me about Twain."

Both frames are *singular*. One angle on one kind of knowledge. That singularity is what lets them be specialists.

### The mesh node frame (ragofrags)

A mesh node is a RAG that **admits its frame is partial and meta-level**, and therefore cannot stand alone.

**ragofrags** — the frame is *knowledge about RAG itself, curated from heterogeneous sources (papers, blogs, docs, posts) across different licenses and scopes*. The frame is **not** "all knowledge about RAG" (impossible). It is "a curated, licensed, defensible subset of what has been written about RAG." That frame is coherent, but it is *self-aware about being partial*. It knows it cannot answer every question about RAG. It knows it is one angle, not the angle.

Because the frame is meta-level and explicitly partial, it cannot work as a specialist — asking "what is RAG?" to ragofrags alone would return a lens, not an answer. Instead, it routes through the mesh: the router asks "is this question about RAG-the-topic, or about RAG-the-practice (Apollo, Twain)?" and routes accordingly. ragofrags is consulted *when relevant*, not asked *directly*.

The frame choice therefore decides the **system architecture**: Is this a specialist you ask directly, or a node in a mesh you consult through a router?

---

## 4. Coverage: what you never collect, you can never retrieve

The failure mode here is the quietest in the entire pipeline, because it produces no artifact to inspect. A missing document is not a corrupted chunk or a bad rank; it is an absence, and absences do not surface in evaluation unless the evaluation was specifically designed to catch them.

This reframes acquisition as a *scoping* decision, not a completeness one. You are not trying to collect everything; you are trying to collect a corpus whose **boundaries you understand and can defend**. Two disciplines make that tractable:

**Separate discovery from harvest.** Walk the source's structure *once* to enumerate what exists — for NARA, that meant traversing the Record Group 255 series tree to list record identifiers — before spending budget pulling full detail. Discovery answers "what is there and is it in scope"; harvest pulls only the parts that pass. Collapsing the two — issuing broad keyword searches and filtering the results client-side — is the single fastest way to burn a query budget on records you were always going to discard.

**Scope to a boundary, not a keyword.** A query filtered to a record group or series burns far fewer calls than a keyword sweep across an entire catalog that you then narrow after the fact. The boundary is also the honest description of your corpus: "Record Group 255, phased by mission" is a coverage statement a reader can evaluate; "we searched for Apollo" is not.

When the budget genuinely cannot cover the scope in one cycle, that is not a failure — it is a **phase boundary**. Ingest one specialty this cycle, the next after the reset, and record where you stopped so the next run is additive rather than a redo. Which brings us to the second half of the problem.

---

## 5. Provenance: the frame made explicit and defensible

A source with no recorded origin is a liability wearing the costume of an asset. But sourcing's real liability is a *frame with no recorded boundaries*. You collected documents, but did you record *why you stopped where you stopped?* Did you record the coherence claim?

The `ragofrags` build treated this as non-negotiable, and the habit is simple to state:

> Every source carries its own provenance as **data, not a footnote**: a URL, a license note, a `retrieved_at` timestamp, and — for anything cloned from a repository — the exact git commit SHA. And the *corpus as a whole* carries a **frame record**: the boundaries of the selection, the scope statement, the architectural decision (specialist or mesh node).

Two consequences follow, and both are worth the discipline.

**Rejection is a first-class outcome.** When a documentation site's license could not be defended, the manifest did not silently drop it — it recorded `status: rejected` with a written reason. A rejection with a reason is reusable knowledge: the next build knows not to re-litigate it, and an auditor can see the decision was made deliberately. A silent omission teaches no one anything and looks, later, exactly like an oversight.

**A manifest is cheaper than a re-hunt.** Persisting what you have already fetched — identifiers, series, fetch dates, frame boundaries — turns an interrupted or resumed acquisition into an *additive* operation instead of a full redo. On a metered API this is not housekeeping; it is the difference between staying inside the monthly budget and blowing through it re-fetching what you already had. The manifest is also the artifact that makes the **frame legible**: it is the difference between "we have ragofrags" and "here are the N sources we hold, by topic/license/date, with explicit boundaries and architectural intent."

Provenance, in other words, is not paperwork you do after the interesting part. It is the thing that **records the camera angle** — the coherence claim that lets every *later* stage — preprocessing, retrieval, citation, system routing — trust the ground it stands on.

---

## 6. Access: the budget is part of the architecture

The Apollo hunt's real lesson generalizes past NARA's specific limit. Almost every serious source is metered, licensed, or both, and those constraints are not obstacles to route around — they are inputs to the design. A few habits carry across sources:

- **Know what the meter counts.** NARA's cap is on metadata *queries*, not on the digital-object bytes served from its separate media host — so pulling the files themselves is not what drains the budget. Misread the meter and you optimize the wrong thing.
- **Maximize the work per call.** Largest page sizes, fewest round-trips; every avoidable call is coverage you could have bought instead.
- **Ask for more once you know your real numbers.** NARA will consider a higher limit for a stated use case — but the ask is credible only *after* discovery has told you the actual record counts. Guessing the size of your own corpus upfront is not a request an archive can act on.

None of this is exotic. It is simply what it looks like to treat acquisition as engineering: measure the constraint, design within it, and record what you did.

---

## 7. What it costs to skip this — and the hand-off to preprocessing

Sourcing shares the awkward economics of this whole series: it is cheapest to get right at the start and most expensive to fix later. But it has a failure profile all its own. A coverage gap is undetectable without a test built to find it; a frame gap is invisible until a system architect realizes "we built this as a specialist but it's only half a coherent angle." Both are nearly free to prevent at acquisition and painful — sometimes impossible — to repair once the corpus is built, indexed, routed, and in production.

The one decision this paper asks of a team is to stop treating acquisition as the throat-clearing before the real work. **Ask first: is this corpus a specialist or a node in a mesh?** That question determines everything downstream:

- If it's a specialist, the frame must be tight enough that preprocessing can rely on it and chunking can align to it. (Papers 2 and 3 assume this frame coherence.)
- If it's a mesh node, the frame must be explicit enough that a router can know when to consult it, and it must admit its boundaries.

Scope the corpus to a boundary you can name. Separate discovery from harvest. Record provenance as data — both the source metadata AND the frame boundaries. Reject with reasons. Respect the meter as an architectural constraint. Do that, and you hand the next stage something it can actually build on: a bounded, dated, license-clear set of raw sources, each traceable to its origin, and a recorded frame that preprocessing and chunking can rely on.

That hand-off is exactly where the next paper begins. *Human Slop In, AI Slop Out* takes the raw sources this stage collected *within the frame this stage established* and asks what it takes to make them machine-legible without silently corrupting them. Sourcing decides *what angle we're representing and whether we stand alone or route through a mesh*; preprocessing decides *whether the model can read it within that frame*. Neither can fix the other's mistakes — which is the whole reason they are separate papers.

---

*Exemplifier (not required to follow the argument): the sourcing and provenance discipline described here underlies the `ragofrags` corpus — an **interaction-free** specialist-by-design you reach through the mesh at [router.otrobonita.com](https://router.otrobonita.com) rather than on its own page — and the Space Talks corpus at [spacetalks.otrobonita.com](https://spacetalks.otrobonita.com), a specialist whose frame is tight enough to stand alone.*

---

## About This Paper

Disagreement is the point. If part of this is wrong — and some of it will be —
the author would rather hear it than not.

Cite as Karlsson, J. (2026). Hunting the Facts. Otrobonita AI Labs.
otrobonita.com/whitepapers

License Creative Commons Attribution 4.0 (CC BY 4.0). Share it, quote it,
argue with it — attribution is all that is asked.

### The authoring team

- **Jesper Karlsson** — concept, thesis, ideas, structure, and accountability for every final call.
- **Fable 5, GPT 4.5, Grok 4.5, and Gemini 3.6** — drafting support, fact-checking, handling of uncertainty and counter-evidence, independent critique, and adversarial review.

Seven iterations and approximately thirty-two individual feedback loops.

Written in 2026.
