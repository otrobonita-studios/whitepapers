# Stop Discounting the Incredible
### Innovation, quietly starved by perceived limits — until now

*Version 3 — working paper*

---

## The Half-Ask

A UX designer sits down to contribute to a requirement. After thorough user research, stakeholder interviews, and weeks of synthesis, she believes she knows exactly what the product needs. She also knows the team that will build it — she has read their skill composition, their history, their scar tissue — and she knows they cannot deliver it. So she contributes half of what she knows.

Nobody told her to do this. Nobody will ever know she did it. The requirement that reaches the backlog looks complete, reasonable, well-formed. It will be estimated, built, and shipped, and the delivery metrics will record a success. What the metrics cannot record is that the ask was discounted before it was ever voiced.

This paper is about that discount: where it comes from, why it is individually rational and collectively corrosive, and why the moment to correct it is now — because the economics that made the discount feel like realism have quietly moved. The tools that once made testing a ceiling expensive now make exploration cheap. The cost curve has inverted. Most private price lists have not.

---

## The Private Price List

A requirement is never just a description of a need. It is a price quote, written by someone who has already estimated what the ask will cost — in delivery time, in political capital, in the risk of looking unreasonable — and adjusted the ask to a price they believe will be accepted.

The undiscounted version is the requirement at full price: the ask that reflects the actual need, or the actual ceiling of the problem, before anyone quietly shrank it to fit anticipated capacity. Almost no requirement is written at full price. Most are pre-discounted through a private, invisible act of judgment that the writer often does not notice performing. The designer in the opening did not experience herself as suppressing a need. She experienced herself as being realistic.

That is what makes this a habit of mind rather than a process flaw. Process flaws are visible in artifacts and can be audited. This discount happens upstream of every artifact, in the moment before the first word of the requirement is written.

This is anticipatory scope-limiting, and it is distinct from Conway's Law. The system does not merely mirror the organization's communication structure; the ask itself is pre-filtered by a private model of what the team can handle, often before the team is even in the room.

Not every organization discounts. There are environments — space, motorsport, offshore yachting, haute couture, luxury automotive — where the half-ask was never viable. When the requirement is a lap time set by physics, a garment worn by one person on one night, or a system that must function in orbit, the gap between what is needed and what is asked closes to zero by necessity. The cost of the discount is immediate and visible. These industries did not develop the habit this paper describes because they could never afford to. Most organizations are not so fortunate: their discount is invisible, their delivery metrics look clean, and the innovation that was never asked for leaves no trace in any retrospective.

The habit is individually rational and collectively corrosive. Rational, because pushing an ask you expect to be rejected or half-built wastes credibility and political capital. Corrosive, because it creates a ratchet: the team is never stretched, leadership never sees the gap between what users need and what ships, and "we can't do X" becomes true by never being tested. Worse, the discount hides its own cost. An organization whose requirement writers always contribute half will show clean delivery data — reasonable asks, met on time — while a capability gap grows that no metric is tracking. In SAFe terms: the program board fills, PI objectives are met, and the ART velocity looks healthy. What nobody sees is the innovation that never made it to a feature card.

---

## A Thought Experiment

Before the next planning session, try this.

You already know a little about what your team has available. You know which holidays fall inside the increment. You know the sprint length, roughly who is on leave, which two people are half-allocated to something else. You are probably factoring those in — just a little — as you decide what to put forward.

Now argue with yourself. Imagine you had a hundred developers available, in addition to the team you already have. Would that change what you asked for?

If the answer is yes, you have just found your private price list. The holidays were never the interesting part. The interesting part is everything else on that list you did not notice consulting.

The experiment is not hypothetical for much longer. Capacity at that scale — human, agentic, or both — already exists in organizations driving innovation today, and the cost of accessing it is falling faster than most planning habits are updating.

---

## A Canon That Institutionalized the Conditions

The requirement writer does not invent the discount alone. A substantial body of respected literature created the conditions in which it thrives.

Hersey and Blanchard's Situational Leadership — still one of the most widely taught leadership frameworks — says explicitly: match your style to the team's competence and confidence, not to the process you would prefer. Skelton and Pais's *Team Topologies* makes team cognitive load a first-class design constraint; work should be shaped to fit what the team can absorb. Mike Cohn's *Agile Estimating and Planning* institutionalizes planning by yesterday's velocity. The Scrum Guide tells teams to pull only what they can commit to in a sprint. SAFe's capacity allocation model builds team load directly into PI Planning as a planning input, not a planning output.

All of this is sound advice for delivery. None of it cleanly distinguishes between adapting the *staging* of a full-price requirement and quietly deleting the full-price requirement before anyone sees it. The literature was written for a world where capacity was expensive and slow to change, so adapting to it was wisdom. Over time the discount became indistinguishable from craft.

It goes further. Karl Wiegers and Joy Beatty's *Software Requirements* lists feasible as a quality attribute of a well-formed requirement. The IIBA's BABOK Guide repeats it. A requirement that exceeds current team capacity is not ambitious in this framework; it risks being graded defective. The professional standard does not set out to teach self-censorship — yet it grades the behavior that produces it.

The requirements field always knew a version of the problem existed. Suzanne and James Robertson's *Mastering the Requirements Process* identifies "undreamed-of requirements" — needs that stakeholders never voice because they assume them impossible or too expensive. That is almost word-for-word the untested ceiling this paper describes. The Robertsons named it. The field noted it. And then, because nobody had a cheap way to test those ceilings, the profession built quality gates — feasibility checks, definition-of-ready checklists, velocity-based planning — that filtered undreamed-of requirements out before anyone senior ever saw them.

Jeff Patton's *User Story Mapping* and Gojko Adzic's *Impact Mapping* push back — both argue for mapping the whole need first and slicing for delivery afterward. Marty Cagan's *Empowered* argues teams should be given problems to solve, not pre-shrunk feature lists. These are important counter-voices. On balance, however, the canon still treats early feasibility as a professional virtue rather than a risk to be managed.

Kahneman's *Thinking, Fast and Slow* supplies the underlying psychology. There is no cognitive bias that reliably inflates the ask. Every well-documented bias pushes downward, and the professional literature, written for an earlier cost regime, reinforces each one.

---

## The Biases That Corrupt the Price

If the discount were a clean, current calculation it might be defensible. It is neither. The private price list is corrupted by predictable biases, and because the pricing happens invisibly, the corruption is never audited.

**Anchoring on past delivery.** New requirements are priced against how long the last similar thing took, even when tooling, staffing, or the problem itself has changed. The anchor is stale but feels like realism. In SAFe environments, story-point velocity from three Program Increments ago becomes the invisible ceiling on what gets written into the next one.

**Availability bias on failure.** One visible failure of an ambitious ask colors requirements for years, while many quiet feasible wins leave no impression. The price list overweights the memorable disaster.

**Status quo framing.** Requirements are written as deltas from the current system rather than from the ideal outcome, so the cost being estimated is the cost of change, not the cost of the capability. Features get written; outcomes do not. A team never asks whether onboarding could go from twenty minutes to two, because everyone assumes that would mean a rewrite — and the rewrite, not the outcome, becomes the thing being priced.

**The cost-of-asking tax.** Every requirement carries a social cost — looking unreasonable, spending credibility with the product manager, appearing to underestimate complexity — that is separate from its delivery cost. Writers optimize against the social price, not the real one. This is the UX designer's half-ask, generalized.

**Skill-composition proxy error.** Feasibility is priced against who is on the team today, rather than what is learnable, hireable, or automatable within the timeframe.

**The requirement-writer's curse.** The person contributing to the requirement often feels responsible if it is not met, so they unconsciously de-risk the ask rather than record the true need. This bias deserves particular attention: the same person who sees the full need is also the one who will carry the political cost of an unmet ask. The incentive is structurally misaligned.

**Premature solutioning.** Requirements written in implementation-shaped language ("add a filter dropdown") rather than outcome-shaped language ("let users narrow results") lock in the old cost model before anyone reconsiders it. SAFe's distinction between features and stories is meant to prevent this; in practice the feature cards often inherit the same constraint-laden framing as the stories beneath them.

**Sunk-cost conservatism.** "We built our workflow around constraint X" remains a reason to write X-shaped requirements long after the constraint is gone.

Every one of these biases pushes in the same direction: downward. The discount compounds.

---

## Two Forms of the Same Discount

So far the discount has been described at the scale of one person and one team: a known need, quietly shrunk. The same habit of mind operates at larger scale, where it takes a more consequential form — not the suppression of a known need, but the failure to ever test what is possible.

Consider a product organization that has lived with a twenty-minute onboarding flow for six years. Nobody has ever asked whether it could be two minutes. Not because anyone measured the effort and rejected it, but because the question was never separable from the answer everyone assumed: a rewrite, a year, a team that does not exist. So the flow gets incrementally improved — nineteen minutes, eighteen — and the two-minute version stays permanently unpriced. The ceiling was never tested. It was inherited.

The same pattern operates at industry scale. No transportation organization sets a short-term goal of cutting fuel consumption by ten percent — not because anyone calculated that ten percent is impossible, but because finding out whether it was possible was always too expensive to attempt. Targets defaulted to the ceiling of past capacity rather than the ceiling of the actual problem. Over time the defaults calcified into industry common sense. Nobody discounted a known need. An entire field simply stopped pricing the question.

These are two forms of the same discount:

**Need-discounting** — I know what I want, and I contribute less because I predict the team cannot deliver it.

**Discovery-discounting** — I do not know what is possible, and I never find out, because the cost of finding out exceeded what the answer seemed worth.

The designer's half-ask and the industry's untested ceiling are the same habit of mind, operating at different scales with different currencies — social capital in one case, R&D budget in the other. In SAFe terms: need-discounting shows up in features and stories; discovery-discounting shows up in the strategic themes and epics that nobody writes because the enabler investment feels unjustifiable against a horizon nobody has tested.

This is what "the incredible" means in this paper's title. Not the impressive. Not the visionary. The incredible is the outcome that was never priced honestly — because either the contributor discounted it, or no one could previously afford to find out whether it was possible.

---

## The Cost Curve Flipped

The economics underneath both forms of the discount have moved. Most price lists have not been updated.

The obvious shift is delivery cost. AI-assisted development, design, and prototyping mean that asks which were previously not worth requesting are now viable. A single BA or product person can stand up a working internal tool in days rather than quarters. The more important shift is subtler: the new tools do not just lower the cost of delivery — they collapse the cost of finding out.

A question like "can we cut fuel consumption ten percent?" no longer requires a funded research program to test. What happens when hundreds of parallel agents work the problem for two weeks? Nobody knows — and that is precisely the point. The question was never askable before, because asking it cost more than the answer seemed worth. Now the exploration itself is cheap, which means every untested ceiling is suddenly testable. Discovery-discounting loses its last rational justification.

The same inversion is visible at the tooling level. For two decades, "buy before build" was the rational default. That asymmetry has collapsed. Off-the-shelf platforms have grown more complex and expensive precisely because they try to serve everyone; organizations pay the license plus the ongoing configuration, plugin, and integration tax of bending a generic tool into their specific workflow. The question is no longer build versus buy; it is who pays the customization tax — once, at build time, or forever, in licensing and workaround time. A default assumption about cost, held confidently for twenty years, has inverted. Most requirement writers are still pricing against the old curve.

One honest caveat is required. Cheap exploration creates its own failure mode: AI-assisted output that outpaces the team's understanding of it — comprehension debt in place of vendor lock-in. Validation, security, compliance, and integration costs do not disappear; in some cases they rise. Generation is cheap; verification is the new bottleneck. The new cost curve is not free. The trade is real and must be managed deliberately. It is still a new trade, and it should be priced as one — not avoided by keeping the old price list.

---

## Restoring Unpriced Discovery

The biases share a common structure: they import the answer to "what is feasible?" into the question "what is needed?" before the question is even asked. The correction is not to argue against each bias individually. The correction is to structurally separate the two questions, and to protect the space between them — the space where unfiltered need lives.

Call that space **unpriced discovery**: the part of the process where the requirement is described before it is costed. Not because constraints are unreal, but because pricing too early is precisely the mechanism of the discount. Unpriced discovery is not naivety. It is a disciplined deferral of the feasibility conversation to the people and the moment where it can actually be acted on. Nobody has forbidden the requirement writer from asking for more; the discipline is to notice the price list and set it down for one conversation.

This is not a call for unconstrained feature creep. It is a call to distinguish *destructive discounting* — suppressing genuine requirements because of fear, stale assumptions, or outdated cost models — from *constructive staging* — acknowledging real constraints while keeping the original intent uncorrupted and visible. The goal is that the gap between need and capacity becomes someone's deliberate decision rather than nobody's private habit.

**Separate the conversation, not the people.** Hold two distinct conversations, never one. The first asks only "what would genuinely solve this?" The second asks "what can we deliver, and by when?" Unpriced discovery lives in the first; feasibility lives in the second. This is a separation of mindsets, not of participants — engineers and architects belong in the first conversation, and their technical insight is often what reveals the real ceiling. What does not belong is the estimation reflex: no velocity talk, no "we tried that," no "the team can't." Those are second-conversation moves, and they need explicit facilitation to keep out of the first.

In SAFe terms this is the distinction between solution intent and PI planning. The common failure mode is that solution intent sessions already inherit the capacity assumptions that PI planning was meant to apply afterward.

**Manage the expectation gap deliberately.** If the first conversation routinely produces asks that the second can fund at only twenty percent, contributor fatigue is inevitable. The remedy is not to abandon the separation; it is to make the gap itself a first-class object of attention. Record the full-price requirement, record the staged version, and treat the difference as an explicit organizational signal — a capability gap, a funding gap, or a prioritization decision. Over time, patterns in that gap become the most honest diagnostic the organization has.

**Make the undreamed-of requirement a deliverable.** The Robertsons named this category decades ago; the profession immediately built gates to filter it out. Reverse that. Make at least one undreamed-of requirement — an ask that assumes current constraints do not apply — a required output of every discovery phase. Not because it will be built, but because the act of writing it recalibrates the contributor's imagination and puts the untested ceiling on record. Some of those ceilings will later be tested and found lower than assumed. That is the organizational learning the discount was hiding.

**Price the exploration separately.** "Find out whether X is possible" was previously bundled into the cost of "deliver X," making the question unaskable without committing to the answer. Separate them. "What would we learn if we let agents work this problem for two weeks?" is now a budgetable line. In SAFe, enabler epics exist for this purpose, yet they are routinely undersized or skipped because the exploration cost feels unjustifiable against an unproven ceiling. Treat ceiling-testing as its own lightweight project type, distinct from delivery.

**Audit the price list explicitly.** When a feasibility judgment surfaces — "that would take months," "this team can't do that," "we tried something similar last PI" — treat it as a hypothesis, not a fact. Ask two questions: when was this last tested, and has the cost of testing it changed? Most price lists are years stale.

**Use creative constraint as a forcing function.** "Solve this as if cost were not a factor." "Design this for an organization ten times the size." "Assume the technology you need already exists — what does the requirement look like?" These prompts separate the requirement from the delivery context long enough to see what the requirement actually is. The resulting full-price requirement may then be staged, phased, or deferred — but it exists, and it is on record.

**Create organizational permission explicitly.** Self-censoring is cultural as well as cognitive. A contributor who has had ambitious asks returned as unrealistic learns not to make them. Protecting unpriced discovery requires an explicit signal: that writing a full-price requirement will not be read as naivety, that the gap between it and the delivered version will not be held against the writer, and that the undreamed-of requirement is a contribution rather than an embarrassment.

Together these practices do not eliminate the feasibility conversation. They relocate it downstream of the requirement, upstream of the delivery plan, and into the hands of people with the authority to change the constraints rather than only work within them. Unpriced discovery is not the abolition of realism. It is the insistence that realism arrives after the need is honestly named, not before.

---

## Addressing the Obvious Objections

Skeptical readers will raise three predictable concerns. Each deserves a direct answer.

### "Isn't this just blue-sky thinking that wastes engineering time?"

No. The full-price requirement is not a commitment to build. It is a record of the true need and a calibrated input to prioritization. The time cost of writing one undreamed-of requirement per discovery cycle is measured in hours, not sprints. The cost of never seeing the gap is measured in years of invisible under-ambition.

### "Won't this produce impossible wish lists and demoralize teams?"

It will if the gap between the two conversations is left unmanaged. The practices above treat the gap as visible and deliberate. Teams are not asked to deliver the impossible; they are asked to help make the trade-off explicit. Psychological safety is protected by the organizational signal that full-price writing is valued, not punished.

### "Doesn't early feasibility keep us honest and focused?"

Early feasibility is valuable — when it is applied at the right moment, by the right people, against current rather than stale data. Importing it into the needs conversation itself is what this paper challenges. The distinction is timing and ownership, not the legitimacy of constraints.

---

## The Habit That Outlived Its Rationale

The designer who contributes half is not failing at her job — she is doing it well by the standards of a reality that is being dismantled. Reading the team, adapting the artifact, pricing the ask against reality: these remain the disciplines of senior practice. What has changed is what reality costs.

The professional canon that codified the discount was built for a world where capacity was genuinely expensive to change, exploration was genuinely expensive to run, and feasibility was a reasonable quality gate because the cost of infeasibility was high. That world has moved. The exploration that once required a funded program now requires a fortnight. The tool that once required a dedicated engineering team now requires a practitioner and an afternoon. The ceiling that an entire industry stopped testing may now be testable before the next PI.

The discount that once passed for realism is now a stale price list, applied by habit, hiding a widening gap between what organizations ask for and what has quietly become possible. Every undreamed-of requirement that stays unwritten, every ceiling that goes untested, every half-ask that reaches the backlog as if it were the honest need — these are the compounding cost of a habit of mind that outlived its rationale.

Stop discounting the incredible.

---

## One-Page Diagnostic: Checking Your Discount Rate

Use these questions in a short retrospective or discovery review. Score each 1–5 (1 = chronic discounting, 5 = unpriced discovery protected). Patterns matter more than absolute scores.

1. When was the last time a full-price (unconstrained) requirement was explicitly recorded, even if later staged?
2. How often do feasibility judgments cite data older than 12–18 months?
3. Are "we tried that" or "the team can't" statements treated as hypotheses to be re-tested, or as settled facts?
4. Does discovery produce at least one undreamed-of requirement as a required output?
5. Is the gap between stated need and delivered scope made visible to someone with authority to close it?
6. Are exploration and ceiling-testing efforts budgeted separately from delivery?
7. Do contributors report that writing ambitious requirements carries social or political cost?
8. How frequently are requirements written in outcome language versus implementation language?
9. When AI or new tooling has changed a cost assumption, how quickly has the private price list been updated?
10. Is there an explicit organizational signal that full-price asking is protected?

A cluster of low scores on 1, 3, 4, 5, and 7 usually indicates need-discounting. Low scores on 2, 6, and 9 usually indicate discovery-discounting.

---

## Further Reading

The literature on requirements, delivery methods, and team capacity was written before the cost curve described here began to invert. The frameworks remain useful as diagnostics of where the habits came from. For what comes next, watch the emerging practice of organizations that are actively testing ceilings they previously assumed fixed.

---

## Appendix Note: Reading the Team

The detailed field guide to team archetypes that appeared in Version 1 has been moved to a companion piece, *Reading the Team*. It retains independent value: senior practitioners form a private price list by diagnosing the team in front of them, often faster than the organization admits the diagnosis. Different root causes — transition, hero-dependency, over-processing, comprehension debt, and others — produce different, often stale, entries on that price list and demand different interventions. The companion piece keeps the main argument focused while giving practitioners a usable diagnostic map.

---

*Version 3. Open questions for further iteration: (1) Anonymized vignettes from practice, including at least one outside software (enterprise operations, finance, or compliance). (2) A single diagram contrasting the discounted path with the unpriced-discovery path. (3) Validation with practitioners who do not already agree — the questions worth asking are "where does this break?" and "have you seen this happen?", not "do you like it?". (4) Whether the practices section should become a standalone methodology paper. (5) Positioning — published whitepaper, conference keynote, or upstream practice supplement for SAFe and product communities.*
