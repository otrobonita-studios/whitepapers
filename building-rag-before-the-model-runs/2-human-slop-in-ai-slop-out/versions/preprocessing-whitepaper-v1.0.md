# Human Slop In, AI Slop Out

### Preprocessing as the Origin of Retrieval Quality in Retrieval-Augmented Generation

**Author:** Jesper Karlsson / Otrobonita AI Labs
**Date:** August 2026
**Document Version:** 1.0
**Part of the RAG pipeline series:** Data Collection → **Preprocessing** *(this paper)* → Chunking → …
**Sequel:** *Why There Is No Universal Chunking Strategy — Chunking as an Information-Topology Problem* (v2.1)

---

## 1. Opening

### Preprocessing as a hallucination preventer

A retrieval-augmented generation (RAG) system can only answer from what it was given. If the text it retrieves is corrupted, ambiguous, or stripped of the structure that made it meaningful, the model is not merely under-informed — it is actively misinformed, and it has no way to know. Faced with context that has a hole in it, a language model does what it is built to do: it fills the hole with something plausible. That is one of the quietest and most common origins of hallucination, and it is fully determined before the model runs.

Preprocessing is the stage where that damage is either prevented or locked in. It is the work of turning a raw source into clean, structured text an index can trust — and because it happens first, it is the earliest and cheapest place in the entire pipeline to stop a hallucination before it can occur. Every later safeguard, from careful chunking to reranking to prompt design, is working to protect meaning that preprocessing either preserved or destroyed. This paper's argument is that preprocessing deserves to be treated as a correctness stage in its own right, not as janitorial work that precedes the real system.

The claim is easiest to feel with a concrete source. Pull up the declassified *Apollo 7 Onboard Voice Transcription* and the striking thing is how little looks wrong. You might expect a degraded 1968 document to be strewn with *[GARBLE]* placeholders and bracketed guesses. It is not: search the whole transcript for "garble" and you find only a handful of hits, and every one is a crew member or CapCom *saying* it — "you were a little bit garbled, but I think we've got most of it" — not a transcriber flagging lost audio. The pages read cleanly. That is exactly what makes them dangerous. The damage is not loud and self-announcing; it is quiet and structural — a typed "4" open enough at the top that OCR reads the timestamp *…04* as *…0h*, and three columns of time, speaker, and speech held together by nothing but their position on the page.

The people who produced these documents in the 1960s did extraordinary work under impossible conditions. But they were transcribing for human historians, who read charitably and fill gaps from context without noticing they are doing it. They were not transcribing for a vector database, which reads literally and forgives nothing.

Feed that raw text straight into a RAG system and nothing warns it that a timestamp has been corrupted or that two speakers have been braided into a single line. The error is indexed with full confidence precisely because it does not look like an error. When a query later lands on that passage, the hole gets filled — and the hallucination that surfaces at answer time was, in truth, authored back here, at extraction, long before generation began.

This is worth saying plainly, because it inverts a common complaint — and it is meant, in the spirit of this paper's title, as a deliberate provocation:

> Much of what we now dismiss as "AI slop" begins life as **human slop** — upstream, in the source, long before a model is involved. The model did not invent the mess. It inherited it, and amplified it.

That reframing is the subject of this paper. The central claim, stated precisely:

> **Preprocessing is not janitorial work that precedes the real system. It is the stage at which the information structure a retrieval system depends on is either created or destroyed.** The topology that chunking later aligns to — and that faithful generation ultimately rests on — is born here, or it is lost here.

## 2. Two upstream origins of hallucination

Hallucination is usually discussed as a generation-time failure: the model, at the final step, says something untrue. This paper argues that the causes are frequently set much earlier, and that at least two distinct origins live upstream of the model entirely.

**The preprocessing origin — meaning corrupted.** When source text is garbled, ambiguous, or stripped of the marks that disambiguate it, the retrieval system indexes noise as if it were signal. A silently mis-read timestamp is retrieved with the same confidence as a correct one. A speaker label lost during extraction turns a two-person exchange into a single incoherent monologue. The model is then grounded on context that is quietly wrong, and it cannot know that it is. This is the origin this paper claims as its own.

**The chunking origin — meaning fragmented.** Even from clean source text, a poorly chosen chunk boundary severs a fact from the context that gives it meaning. A pronoun is stranded from its referent; a number is cut off from its units; a punchline is separated from its setup. Chunks that are too short, or that carry too little overlap, produce retrieval units that are individually fluent and collectively misleading. This origin is the subject of the companion paper and is treated there in full.

The two are the same failure viewed at different stages. In each case the model is handed context that is missing something, and it closes the gap by inventing. **Preprocessing loses meaning by corrupting the text. Chunking loses meaning by fragmenting it.** This paper owns the first; it points forward to the second.

## 3. Where this paper sits in the series

This paper sits in the middle of the pipeline, and it is worth being exact about the order. A companion paper on **data collection** genuinely comes first: sourcing and acquisition — deciding what is worth ingesting and pulling it in — is a distinct problem, and it precedes everything discussed here. This paper assumes collection has already happened and a raw source is in hand. The **chunking** paper is the sequel: it assumes the work described here is already done. So preprocessing does not come *first* — it comes *after* collection and *before* chunking.

What that middle position turns on is a single dependency. The chunking paper assumes that structural signals — section boundaries, speaker attributions, timestamps, document hierarchy — already exist to be aligned to. It has to assume this; alignment is meaningless without something to align.

But those signals are not found in raw sources. They are *manufactured* during preprocessing: recovered from inconsistent formatting, reconstructed where the original lost them, attached as metadata where they were only ever implicit. Structuring and enrichment is not the tail end of cleanup — it is where a document's information topology is first made explicit and machine-legible.

---

## 4. What preprocessing actually is

Before the examples, a plain definition — because "preprocessing" is often used loosely to mean any dull work that happens before the interesting part.

Preprocessing is everything that turns an acquired raw source into a clean, structured document a retrieval system can index. It sits between *ingestion* (getting the source into the system at all) and *chunking* (splitting it into retrieval units), and it is best understood as four steps working in sequence:

- **Extraction** — lifting the actual content out of its container: text out of a PDF, HTML, or audio transcript.
- **Cleaning** — removing what is not content: boilerplate, navigation, headers and footers, OCR noise.
- **Normalisation** — making the surviving text consistent: encoding, Unicode, whitespace, casing.
- **Structuring & enrichment** — attaching the marks that carry meaning: section boundaries, speaker labels, timestamps. These are the topology signals every later stage depends on.

Two things follow, and they set up the rest of the paper. First, preprocessing is not one action but a short pipeline of its own, and a fault in any step propagates into all of them. Second — the claim this paper defends — the last step is not clerical tidying. **Structuring is where a document's information topology is first made explicit and machine-legible.** It is the point at which meaning is either recovered or lost for good, which is exactly what the two examples below are chosen to show.

---

## 5. Two worked examples

The argument is easiest to see at the extremes. This section places two real corpora at opposite ends of the preprocessing difficulty scale. One is nearly trivial to prepare; the other is among the hardest text a pipeline will meet. Neither is a contrived edge case — both are corpora this project actually ingests.

### 5.1 The hard end: the Apollo 7 onboard voice transcription

Our source is the declassified *Apollo 7 Onboard Voice Transcription* (Manned Spacecraft Center, Houston, December 1968). Two pages from it stand in for two different kinds of preprocessing damage.

**Exhibit A — a transcript page (Day 1, p. 51).** The instructive thing about this page is how *legible* it looks. There is no wall of unreadable garble; a human skims it without effort. The damage is quieter, and precisely the kind an eye forgives and an index does not. Read as five stacked layers, bottom to top:

1. **Physical layer.** A fifty-year-old reproduction: speckle and dust across the page, faint skew, a struck-through *CONFIDENTIAL* header, and a black redaction bar over the footer. Before any character is read, the page is already carrying marks that mean nothing to the conversation.
2. **OCR layer.** The typed "4" is open at the top, so recognition reads the timestamps *00 02 12 04* as *…0h*, *…43* as *…h3*, *…14* as *…1h*. The corruption lands squarely on the ground-elapsed-time values a retrieval system would key on — high confidence, wrong output.
3. **Layout layer.** The page is three columns held together only by visual position: GET timestamp · speaker code · utterance. Extract straight across and *00 01 58 38 · LMP · SPS propellant tank temperature is running 70…* collapses into one line where time, speaker, and speech are indistinguishable. Multi-line utterances smear the braid further down the page.
4. **Notation layer.** The domain conventions carry the meaning: speaker codes (LMP, CDR, CMP, and CC for CapCom/Houston), the *DD HH MM SS* time format, and the "…" that marks a clipped or overlapping transmission — not literal words, but a naïve pipeline ingests them as if they were.
5. **Meaning layer.** The only thing the RAG system actually wants — *who said what, when, about which spacecraft system* — exists nowhere explicitly on the page. It is implied entirely by column position and notation, i.e. by exactly the signals the four layers below have just degraded.

**Exhibit B — the cover page.** The title page is the opposite failure mode: almost no retrievable content, buried under noise. A halftone dot-screen band, a FOIA *NOTICE* box rotated some eighty degrees, handwritten declassification annotations scrawled diagonally across the header, overlapping stamps. A human reads "Apollo 7 Onboard Voice Transcription, December 1968" in a second; a text pipeline sees a dense field of artifacts around a few real words and, left alone, will happily index the noise.

The point lands before any taxonomy does: *what looks like one text file is five stacked, leaky layers* — and on some pages the content-to-noise ratio approaches zero. Disciplined preprocessing here is not cleanup; it is reconstruction, layer by layer, of information the source no longer cleanly contains.

> **Exhibit to build:** an annotated overlay on the real p. 51 scan — the five bands peeling upward from the physical page to the meaning layer, each captioned with the specific failure it introduces (e.g. *04 → 0h* on the OCR band, the three-column braid on the layout band). Source scans now in hand.

### 5.2 The easy end: Project Gutenberg (Twain)

The same pipeline meets the *Adventures of Huckleberry Finn* Gutenberg edition and has almost nothing to do. Two things make it easy, and both are visible in the source.

First, the boilerplate is *bounded and labelled*. The file opens with the standard Project Gutenberg header — title line, license paragraph, and metadata fields (Author: Mark Twain; Illustrator: E. W. Kemble; release and update dates; credits) — and the body begins at a literal, machine-findable marker: `*** START OF THE PROJECT GUTENBERG EBOOK ADVENTURES OF HUCKLEBERRY FINN ***`, closed by its matching `*** END ***`. Stripping the wrapper is a single stable rule, not a judgement call.

Second, the structure is *already in the markup*. Inspect the rendered chapter and the text sits inside semantic HTML — clean UTF-8 prose in a `<p>` element, chapters under headings — so the paragraph and chapter topology the chunking layer will want is present and legible without reconstruction. There is no OCR layer, no braided columns, no notation to decode. The only real decisions are cosmetic: whether to keep the interleaved illustrations, and how to handle curly quotes and the em-dash in *"Aunt Polly—Tom's Aunt Polly."*

### 5.3 What the pair proves

Set side by side, the two corpora make the paper's structural claim concrete:

> **Preprocessing is corpus-dependent.** The effort that rescues an Apollo transcript — column de-braiding, notation parsing, speaker-turn reconstruction — would be wasted labour on a clean Twain file, and the light boilerplate strip that perfectly serves Gutenberg would leave the Apollo scans in ruins.

This is exactly the argument of the companion chunking paper, moved one stage upstream. There is no universal chunking strategy because information topology varies by corpus; there is no universal *preprocessing* strategy because the **legibility** of that topology varies by corpus first. The exhibits sharpen the point to a single distinction: in the Gutenberg source the structure is already *in the markup* (a `<p>` is a paragraph), whereas in the Apollo scan the structure exists only as *visual position* that extraction destroys and must rebuild. One corpus shows preprocessing can be nearly trivial; the other shows it can be the hardest part of the entire pipeline. A single fixed pipeline cannot be right for both — and most real-world corpora sit somewhere on the line drawn between these two.

## 6. When clean text still lies: contradiction and lost scope

The Apollo case is loss by *corruption* — the words themselves were damaged. There is a second, quieter failure that befalls text which is perfectly clean, and stakeholders meet it far more often: loss by *decontextualization*.

Consider a large organisation whose departments use the same system differently. Operations runs seven processes on System X; engineering runs twelve. Both statements are true — each within its own department. Ingest both into one flat corpus and the boundary that made them compatible is gone. What the retrieval layer now holds is a bare contradiction: *System X supports 7 processes* and *System X supports 12 processes*, side by side, with nothing to say which belongs to whom.

Note what did **not** go wrong. Neither source was inaccurate; neither was garbled. The failure was entirely in preprocessing — the scope, *which department this claim holds for*, was never captured as a field, so two claims that were never really in conflict were filed as though they were.

> A contradiction in a RAG corpus is rarely the sign of a bad source. It is usually the sign of a missing metadata field.

It comes in two flavours, each with a different missing field:

- **Lateral (scope).** Department, region, product variant, customer tier. Both claims are true at once; they belong to different boundaries. Missing field: *scope*.
- **Temporal (version).** Revision 1 of an instruction versus revision 3, where the later supersedes the earlier and only the current one applies unless history is explicitly requested. Missing field: *effective date / revision*.

The consequences are worse than steady wrongness, for two reasons. First, the system fails **inconsistently**: whichever chunk happens to rank higher wins, so the same question returns "7" today and "12" tomorrow. Inconsistent wrongness erodes trust faster than reliable wrongness, because a user cannot even learn where to be careful. Second — and this is the mechanism from §1 again — handed two flattened claims, the model may **invent a reconciliation**: *"System X supports 7 core and 5 optional processes,"* a confident figure true in no department at all. The gap it fills is the missing scope; the fill is a fabrication that sounds more authoritative than either real answer.

The fix lands exactly where this paper already points — the **structure & enrich** step. Preprocessing must attach the boundary (`scope: engineering`, `effective_date: 2025-03`) so the retrieval layer can either filter to the asker's context or, better, return both claims *with their scopes intact*: "For operations, seven; for engineering, twelve." Stated that way it is not a contradiction at all — it is a complete, correct answer. Retrieval does the filtering, but it can only filter on metadata that preprocessing created. Preprocessing therefore creates not only structural topology but **scope topology**: the boundaries within which each claim is true.

This also points at a preventive architecture. Rather than pour every department's knowledge into one pile and hope metadata sorts it out afterward, partition the corpus by knowledge boundary — system, process, part-family — so incompatible scopes never share a store to begin with. (This is the stance behind Otrobonita's *Rag of Rags*: minted specialists scoped by boundary, "not one RAG per bolt, and not one masterbrain." Partitioning by scope is contradiction prevention by construction.)

## 7. What it costs to skip this

Preprocessing has an awkward profile for anyone deciding where to spend effort: it is invisible when it works, and nearly invisible when it fails. A broken preprocessing step rarely throws an error. It ships a clean-looking answer that happens to be wrong — the failure mode most corrosive to trust, because nothing flags it and nothing crashes.

That is the whole severity argument in one line:

> Preprocessing is the cheapest stage to get right and among the most expensive to get wrong, because every stage downstream inherits its output. A shortcut here is paid back many times over — in confident wrong answers, in eroded user trust, and in debugging that begins at the wrong end of the pipeline.

The one decision this paper asks of a stakeholder is not technical. It is to drop the assumption that preprocessing is a solved, one-size step you can simply "run." The two examples show why that assumption is expensive: the same pipeline that is almost free on a clean Gutenberg text has to perform real reconstruction on an Apollo scan. Preprocessing effort must be **budgeted per corpus, at ingestion time** — before a delivery date is promised, not discovered after.

A rough rule of thumb for triage:

- **Clean, born-digital, well-marked-up sources** (Gutenberg-like): preprocessing is a rounding error. Proceed.
- **Scanned, multi-column, notation-heavy, or OCR'd sources** (Apollo-like): preprocessing is likely the single largest and riskiest line item in the build — and the cheapest place in the entire system to prevent a hallucination.

Everything above is settled before a single chunk is cut. What preprocessing hands downstream — clean text with its structure made explicit — is exactly what the chunking paper assumes it already has. Get this stage wrong and no amount of clever chunking, reranking, or prompting downstream can recover what was already lost.

---

*Parked for the technical companion (deliberately out of scope for this stakeholder-length paper):*
- *A fuller taxonomy of preprocessing loss, mapping each step — extract, clean, normalize, structure — to the specific downstream failure it induces.*
- *The "just auto-detect the corpus type" objection, and why it understates the problem (mirrors the chunking paper's objection-handling).*
- *Proposed evaluation: measuring preprocessing quality independently of downstream retrieval.*
