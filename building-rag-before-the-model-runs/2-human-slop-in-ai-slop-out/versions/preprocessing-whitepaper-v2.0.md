# Human Slop In, AI Slop Out

### Preprocessing as the Origin of Retrieval Quality in Retrieval-Augmented Generation

**Author:** Jesper Karlsson / Otrobonita AI Labs  
**Date:** August 2026  
**Document Version:** 2.0  
**Part of the RAG pipeline series:** Data Collection → **Preprocessing** *(this paper)* → Chunking → …  
**Sequel:** *Why There Is No Universal Chunking Strategy — Chunking as an Information-Topology Problem* (v2.1)

---

## 1. Opening

### Before retrieval can be good, the source has to become machine-legible

A retrieval-augmented generation (RAG) system is meant to ground a language model in evidence retrieved from a chosen corpus. But grounding is only as trustworthy as the evidence the retrieval pipeline can actually see. If a source is corrupted during extraction, stripped of the structure that disambiguated it, or detached from the scope in which a statement was true, the model may be given evidence that is incomplete, misleading, or simply wrong.

That creates an important distinction. A **generation error** is produced by the model at answer time. A **grounding error** can be created much earlier: the model may faithfully repeat corrupted evidence, or it may invent a plausible bridge across context that preprocessing removed. In both cases the visible failure appears at the end of the pipeline, while an important part of its cause may have been fixed upstream long before generation began.

Preprocessing is where much of that upstream risk is either removed or locked in. It turns a raw source into information a retrieval system can index while preserving the relationships that make the information mean what it means. This paper argues that preprocessing should therefore be treated as a **correctness stage**, not as janitorial work before the real system starts.

The claim is easiest to feel with a concrete source. Pull up the declassified *Apollo 7 Onboard Voice Transcription*. The striking thing is how little looks wrong. A human sees a timestamp, a speaker code, and an utterance and immediately understands that they belong together. But the page does not encode that relationship semantically. It encodes it through position, typography, notation, and convention. A naïve extraction can preserve most of the words while destroying the relationships between them.

That is the central problem of this paper:

> **Preprocessing is the transformation from human-readable information topology into machine-readable information topology.**

Here, *information topology* means the relationships that make isolated pieces of information interpretable: which heading owns a paragraph, which speaker owns an utterance, which timestamp belongs to which event, which department a claim applies to, which revision supersedes another. Humans infer these relationships almost automatically. Retrieval systems need them made explicit.

This is also where the title's provocation comes from:

> Much of what we dismiss as “AI slop” does not begin with AI. It begins upstream, when imperfect human sources, document conventions, scans, exports, and organisational boundaries are handed to machines without enough reconstruction. The model inherits the mess — and can amplify it.

## 2. Where preprocessing sits

For a reader who knows RAG but not every stage, the relevant pipeline can be reduced to one line:

**Sources → Preprocess → Chunk → Index → Retrieve → LLM → Answer**  
**             ↑ this paper**

Collection decides what knowledge enters the system. Preprocessing makes that knowledge machine-legible. Chunking turns it into retrieval units. Indexing makes those units searchable; retrieval selects relevant evidence; the language model generates the answer.

This paper sits at the hand-off between source material and retrieval structure. The companion chunking paper assumes that useful signals — section boundaries, speaker attributions, timestamps, document hierarchy and scope — already exist in machine-readable form. Preprocessing is where those signals are preserved, recovered, reconstructed, or added.

This gives the two papers a simple dependency:

> **Preprocessing makes information topology explicit. Chunking decides how to divide information without violating it.**

The failures are related but distinct. Preprocessing can corrupt or erase meaning before chunks exist. Chunking can fragment meaning even when the source handed to it is perfectly clean. Both can ultimately produce bad grounding, but they do so at different stages and require different remedies.

## 3. What preprocessing actually is

Preprocessing is everything that turns an acquired raw source into a clean, structured representation a retrieval system can safely index. Four operations are useful for understanding the work:

- **Extraction** — lifting content out of its container: text and structure from a PDF, HTML page, scan, transcript, or other source.
- **Cleaning** — separating content from boilerplate, navigation, repeated headers and footers, scan artifacts, and other noise.
- **Normalisation** — making representation consistent: encoding, Unicode, whitespace, punctuation conventions, and other format differences.
- **Structuring & enrichment** — making relationships explicit: sections, hierarchy, speaker labels, timestamps, scope, revisions, and other metadata needed to interpret a statement correctly.

These are not necessarily four isolated conveyor-belt steps. Structuring is the objective that often determines how extraction and cleaning must be performed. If a PDF's three columns encode `timestamp | speaker | utterance`, an extraction method that returns all the words but destroys those relationships has not succeeded merely because the text is legible.

That is the deeper criterion throughout this paper: **did preprocessing preserve enough topology for the machine to interpret the information as a human reader would?**

---

## 4. Two worked examples

The easiest way to see the difference is to put two real corpora at opposite ends of the preprocessing spectrum. Both are sources used in this project. One arrives with much of its topology already machine-legible. The other requires substantial reconstruction.

### 4.1 The hard end: the Apollo 7 onboard voice transcription

The source is the declassified *Apollo 7 Onboard Voice Transcription* (Manned Spacecraft Center, Houston, December 1968). A transcript page and its cover illustrate two different preprocessing problems.

**Exhibit A — transcript page, Day 1, p. 51.** The page looks remarkably readable. That is what makes it instructive. The risks are quiet enough that a human eye automatically repairs them.

Read the page as five interacting layers:

1. **Physical layer.** The reproduction contains speckle, skew, struck-through classification markings, and blacked-out material. These marks are visually obvious to a person but can enter machine extraction as content or interfere with recognition.

2. **OCR layer.** Character recognition can silently alter values while leaving the surrounding line perfectly fluent. On the supplied extraction, the open-topped typed `4` produces errors such as:

| Printed page | OCR output |
| --- | --- |
| `00 02 12 04` | `00 02 12 0h` |
| `00 02 12 43` | `00 02 12 h3` |
| `00 02 13 14` | `00 02 13 1h` |

The important property of these errors is not that they look spectacularly broken. It is that they are **locally plausible machine text attached to the wrong value**. An index does not automatically know that the timestamp has been corrupted.

3. **Layout layer.** The page is effectively a table without table borders: `GET timestamp | speaker code | utterance`. A human follows each row visually. A naïve horizontal PDF/OCR extraction can instead flatten or braid the columns, especially when an utterance wraps across several lines. The words may survive while the tuple that gives them meaning does not.

4. **Notation layer.** Domain conventions carry additional information: LMP, CDR, CMP and CC identify speakers; time is represented as ground-elapsed time; ellipses and clipped lines describe characteristics of the recorded conversation. A generic text pipeline cannot assume those marks mean what ordinary prose would imply.

5. **Meaning layer.** *Who said what, when* is present on the page, but the relationships are encoded largely through **spatial position and notation rather than semantic markup**. The preprocessing task is therefore not to invent the information. It is to convert those human-readable relationships into explicit machine-readable structure — for example `timestamp`, `speaker`, `utterance` and, where appropriate, additional domain metadata.

That distinction matters. The source is not “bad data.” It is data whose topology was designed for a human reader.

**Exhibit B — cover page.** Here the problem is reversed. The genuinely useful content is small — document identity, mission, document type, location and date — while much of the page is occupied by a halftone band, rotated FOIA notice, handwritten declassification annotations, stamps, struck-through classification labels, and other administrative marks. A human separates document metadata from administrative history almost instantly. A generic extraction pipeline can index all of it with equal apparent importance.

The Apollo example therefore contains several preprocessing problems at once: recognition, layout reconstruction, notation interpretation, noise rejection, and structural enrichment. Calling all of that “cleaning the PDF” hides the engineering problem.

> **Visual exhibit:** annotate the real p. 51 scan from physical page → OCR → layout → notation → structured meaning, tracing at least one `04 → 0h` corruption and one `timestamp | speaker | utterance` relationship through the stack.

### 4.2 The easy end: Project Gutenberg (Twain)

Now compare the same task with Project Gutenberg's *Adventures of Huckleberry Finn*.

The boilerplate is bounded and labelled. The file provides title and author metadata and a literal machine-findable marker identifying where the ebook begins, with a corresponding end marker. Removing the distribution wrapper can therefore be handled by a stable rule rather than inferred from visual layout.

More importantly, much of the topology is already in the markup. Prose appears as paragraphs; chapters have headings; text is born-digital rather than recovered by OCR. The relationship between a paragraph and its surrounding document structure survives extraction far more naturally than the relationships on the Apollo scan.

There are still preprocessing decisions — whether illustrations belong in the retrieval corpus, how metadata should be retained, how textual conventions should be normalised — but little structural reconstruction is required.

### 4.3 What the pair proves

The difference is not simply “dirty document versus clean document.” It is **how legible the source's information topology already is to a machine**.

- **Apollo:** topology is substantially **spatial and notational**. It has to be reconstructed.
- **Gutenberg:** topology is substantially **semantic and encoded in markup**. It can mostly be preserved.

That leads to the first practical conclusion:

> **Preprocessing is corpus-dependent.** A pipeline appropriate for Gutenberg can destroy Apollo; the reconstruction needed for Apollo would be unnecessary work for Gutenberg.

This is the same principle developed one stage later in the companion chunking paper. There is no universal chunking strategy because information topology varies by corpus. There is no universal preprocessing strategy because the **machine-legibility of that topology varies first**.

Most organisational knowledge sits somewhere between these extremes.

## 5. When clean text still lies: scope and version

OCR and layout make the preprocessing problem visible, but perfectly extracted text can still lose meaning.

Consider an illustrative enterprise case. Operations uses System X for seven processes; engineering uses it for twelve. Both statements are accurate within their respective departments. If the two statements enter a flat corpus without their organisational scope, retrieval sees:

*System X supports 7 processes.*  
*System X supports 12 processes.*

Nothing is wrong with either sentence. What disappeared is the boundary within which each sentence is true.

This is another form of topology — not spatial this time, but **organisational**.

Two common variants are especially important:

- **Lateral topology — scope.** Department, region, product variant, customer tier, system, process family. Two claims can both be current and correct because they apply within different boundaries.
- **Temporal topology — version.** Revision 1 versus revision 3, an old policy versus its replacement, or a value whose meaning depends on an effective date.

Genuine source contradictions of course exist. But many **apparent** contradictions in enterprise RAG are created when scope or version information is discarded. What looks downstream like conflicting knowledge may actually be incomplete representation.

The consequence is particularly awkward for retrieval. One chunk may rank above the other on one query, while a slightly different query reverses them. The user experiences a system that appears to change its mind. Worse, a language model presented with both flattened claims may manufacture a reconciliation — for example, “seven core and five optional processes” — that exists in neither source.

The remedy begins before retrieval. Preprocessing can attach boundaries such as `scope: engineering`, `effective_date: 2025-03`, or a revision identifier. Retrieval can then filter or return the claims with their boundaries intact:

*For operations, seven. For engineering, twelve.*

This is why the definition of preprocessing used here extends beyond text cleanup. **For RAG, preprocessing is not finished when the characters are clean. It is finished when the boundaries required to interpret those characters are machine-readable.**

Some architectures go further and partition knowledge by those boundaries rather than relying exclusively on metadata inside one store. That is one possible design response, and the idea behind Otrobonita's *Rag of Rags* work: specialist knowledge systems scoped by meaningful boundaries rather than one undifferentiated “master” corpus. Whether physical partitioning, metadata separation, or a hybrid is appropriate is an architectural decision; the prerequisite is the same — the boundaries must first be recognised.

## 6. What it costs to skip this

Preprocessing has an awkward profile for anyone allocating time and budget: it is almost invisible when it works, and often remains invisible when it fails. A damaged preprocessing step may not throw an error. It can simply deliver clean-looking retrieval evidence whose meaning has changed.

That creates a debugging trap. Teams naturally investigate the visible end of the system — the model, prompt, retrieval parameters, reranker, or chunk sizes — even when the defect was introduced during source preparation. Downstream tuning can sometimes compensate for upstream loss, but it cannot **reliably reconstruct information it was never given**.

The stakeholder decision is therefore not “which preprocessing tool should we run?” It is whether preprocessing effort has been assessed **per corpus before ingestion is treated as solved**.

A useful triage rule is:

- **Clean, born-digital, well-marked-up sources** *(Gutenberg-like)* — topology is already largely machine-legible; preprocessing may be inexpensive.
- **Scanned, multi-column, notation-heavy, OCR-derived, historically layered, or context-dependent sources** *(Apollo-like)* — preprocessing can become one of the largest and riskiest parts of the RAG build.
- **Organisational knowledge spanning scopes and revisions** — text cleanliness alone is insufficient; scope and temporal boundaries need to survive ingestion as structure or metadata.

The larger lesson is simple:

> **Human slop in does not inevitably produce AI slop out. But preventing it requires treating preprocessing as information engineering, not housekeeping.**

Everything downstream depends on what crosses this boundary. Chunking can preserve topology only after preprocessing has made that topology available to preserve. Retrieval can filter by scope only after scope exists as a field. A model can ground an answer faithfully only in the evidence the system successfully reconstructed and retrieved.

That is why preprocessing belongs in the correctness architecture of RAG.

---

*Parked for the technical companion (deliberately out of scope for this stakeholder-length paper):*

- *A fuller taxonomy of preprocessing loss, mapping extraction, cleaning, normalisation and structuring to downstream failure modes.*
- *The “just auto-detect the corpus type” objection, and why automatic classification does not remove corpus-specific preprocessing requirements.*
- *Evaluation methods for measuring preprocessing quality independently of downstream retrieval and generation.*
