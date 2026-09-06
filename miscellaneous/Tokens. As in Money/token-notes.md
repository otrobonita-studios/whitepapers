# Token… as in Money — running notes

Changes and open questions accumulating since v1.0.0. Nothing here is in the paper yet unless marked APPLIED.

## Applied to v1.0.0 already

- **Screenshot bullet expanded** — "the layout is not the information", messy-text-beats-tidy-picture, plus the exception (charts, tables that collapse as text, a screen you're asking about).

## Pending — candidates for the next version

- **New section: "Where you can use AI for free".** Write it as categories, not a brand list — an assistant built into something you already have, a free tier from one of the majors, a cheap challenger, a model you run yourself. A named list is the most perishable thing the paper could contain and contradicts the decision to keep it free of things that rot. Two points that make it more than a list: (1) free is paid in another currency — usually data, sometimes ads — which matters most if it's the children chatting, and belongs in a paper about family values rather than as a footnote; (2) the ceiling arrives *sooner* on free tiers, tighter quotas and smaller models, so the three piles matter more there, not less — that's the bridge back to the body. Caveat: a self-hosted local model is free in tokens but assumes hardware most households don't have; mark it as a special case. Brand names need verification at publication time. **The punchline: what you pay with is screen time.** A paid subscription wants you to finish; a free, engagement-funded product wants you to stay. Screen time isn't a side effect of free, it's the revenue model — and it's the exact currency families already ration. The ceiling didn't disappear, it moved from the invoice to the clock. No free lunches.

- **New section: "Company value, family value".** The frame that resolves the value question by separating it rather than settling it. At the kitchen table the question is not ROI, it's what else that money would have been — no table answers that, and the paper shouldn't try. Borrow the screen-time vocabulary: families already know how to have this argument, AI spending is the same conversation with a bill attached. Author is not personally a skeptic; the skepticism belongs to the frame, not to him, so it lives in tone rather than in an argument. Strongest single observation available: a parent's long *work* conversations run on the *household* subscription — work use paid from the family budget, on consumer tiers, with consumer allowances. Combined with "the price collapse never reaches the subscriber", the conclusion is that the household is subsidising the employer. Watch the gendering of the example in English; make it a parent.

- **Opening section: "Why this paper, and why now?"** Drafted. Hook is the frustration of hitting the ceiling, not the mechanics. Needs the causal link stated explicitly: models got smarter *by spending more tokens* — reasoning before answering, more context, tool calls — so the intelligence is bought in the same currency the ceiling is measured in, and better models hit the roof sooner. Ends on the quality-time callback: "how to get more quality time with your favourite supermodel." Note the double meaning of "supermodel" (his own service) — kept knowingly. Watch the wording: "spending limits" should be usage allowance for subscribers, and avoid "virtually smarter" / "believed to add value", which read as hedges in English.

- **Format table still unmeasured.** §4 says "an order of magnitude" and "processed twice over" with no measurement behind it. The cheapest fix available: one document through six formats via a token-counting endpoint. Weakest passage in the paper until then.
- **Fable 5.1 cache-read pricing as external validation.** Currently only in the appendix. A vendor pricing frontier cache reads at 2.5% of input instead of 10%, and reporting ~25% savings on typical workloads vs ~45% on agentic ones, is the prefix tax and the conversation pile measured by the people selling them. Arguably belongs in the body.
- **Rounds-as-product could grow.** The "sometimes you want the long conversation" section is currently one short passage. There may be a fuller argument in it: what you buy when the conversation itself is the deliverable, and how to tell which mode you are in before you start.
- **Title/subtitle not final.** "Token… as in Money" with the current subtitle. Formula is not in the title.

## Deliberately declined

- **English-as-advice.** Language packing stays a structural observation, not a user tip. Turning it into advice would convert a systems problem into personal responsibility.
- **Spelling as a checklist item.** Kept as hygiene inside the packing section; not promoted to a habit, to avoid optimisation theatre next to the items that actually move the bill.
- **The service mention.** Supermodels stays out of the paper. Byline only.

## Series

- Third paper candidate: cost visibility as an interface question. "Allocation without visibility is guesswork" is a paper, not a section.

## Files

- `token-as-in-money-v1.0.0.md` — current paper, household edition with builder appendix
- `token-strategy-paper-v0.2.md` — previous, builder-oriented throughout
- `token-strategy-deep-dive.md` — everything, unweighted working material
