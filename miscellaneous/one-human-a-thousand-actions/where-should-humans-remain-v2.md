# Where Should Humans Remain

*The shift from UX to Autonomous Experience still needs kick-ass design.*

**A discussion paper — a companion to "The Bottleneck Has Moved."**

Jesper Karlsson · Otrobonita AI Labs · Draft v2

---

## IF YOU READ ONE PAGE, READ THIS ONE.

## The Short Version

**The interface is receding. The judgment points remain. Someone has to design them.**

For decades, design answered one question: what should the user see, and what should they do next? Agentic AI makes that the wrong question. Agents take goals, determine steps, and execute — often with no user present at all. The design question inverts: not *what should the human see*, but *where should the human remain*.

**Trust replaces usability as the primary deliverable.** When people can't observe every step, they wonder what's happening behind the curtain. The failure modes sit at both extremes: an agent that asks permission for every micro-action drowns the human in confirmations; an agent that disappears and returns confidently wrong has drifted with nobody watching. The craft lives between.

**The touchpoints are the new screens.** When does the agent surface itself, require approval, merely notify, or work invisibly? Each of these is a designed decision. Made deliberately, autonomy feels like empowerment. Made by accident, it feels like bureaucracy or abandonment.

**The toolchain is reorganizing.** Designers used to hand off wireframes; increasingly they hand off behavior models, escalation rules, and trust protocols. The experience logic is still designed in tools like Figma — but it is realized in orchestration frameworks like LangGraph, where human-approval checkpoints are first-class constructs in the architecture. Designers who understand that layer will shape these systems; designers who don't will be handed systems already shaped.

**Where to start: not where AI is impressive, but where humans want out.** Consent is not a checkbox; it is a feeling of retained control. Don't begin by inserting agents into work people care about owning. Begin with the work they are begging to be rid of. Each despised task an agent absorbs builds the trust budget needed later, when agents touch work people actually care about.

**The harder case: systems that never stop.** Continuous, self-learning agents raise the stakes further. Their coordination model must be allowed — and expected — to evolve, which means touchpoints that lighten as trust accumulates, an interface that is never finished, and a new class of touchpoint entirely: the Specification Gate, where the agent proposes to change its own rules and a named human decides. Sections 7 addresses this case directly, including the additional discovery steps it demands.

**Where it does not work.** Wherever the human's engagement *is* the value — creative direction, relationship-carrying conversations, decisions with legal weight, moments where regulation or ethics demands a human in the seat. Removing the human there isn't automation; it's amputation.

**The connection to the first paper.** "The Bottleneck Has Moved" argued that when execution is cheap, judgment and accountability become the scarce resources — and asked where accountability lives. This paper asks the same question one level down, in the flow itself: where does human judgment physically sit in an agentic workflow? Get the placement wrong and the accountable human of the first paper is accountable in name only.

**Read the open questions before you argue.** How touchpoints decay into rubber-stamping, how to research trust in something users don't observe, and what a well-placed touchpoint even measures as — all named, with candidate answers clearly labeled as candidates, in Section 10.

*This is a hypothesis offered for argument — not a consulting offering, and not a design methodology.*

---

## 0. What This Paper Is, and Isn't

This paper is offered as a point of view — a position to argue with, not a framework to implement and not a methodology with a trademark pending. Its purpose is to make the current understanding of "UX work" feel less inevitable, and to give designers and the decision-makers they report to a concrete way of talking about what changes when the systems they build stop waiting for input.

Everything that follows is deliberately specific. Where the paper sounds confident, read it as precision, not certainty. This is one possible account of design in the agentic era — not the account.

A note on the intended reader: this is written for designers, but it is meant to be *carried* — into leadership meetings, portfolio discussions, and budget conversations. The changes it describes are not decisions a design team can make alone. Where the argument lands, it should land as support for a conversation with the people who allocate money and mandate.

## 1. The Question Inverted

For thirty years, my profession has answered one question: what should the user see, and what should they do next? Screens, flows, affordances, feedback loops. However sophisticated the craft became, the underlying model held constant: the human operates, the interface responds. The human was the driver; the interface was the steering wheel and the dashboard.

Agentic AI breaks that model — not by making interfaces better, but by making the operator optional.

An agent doesn't wait for input. It takes an intent — "monitor these defects overnight," "prepare the compliance summary," "handle my expense reports" — and determines the steps, selects the tools, gathers what it needs, and executes. The human doesn't operate anymore. The human *delegates*. And delegation is a fundamentally different design problem, because for long stretches of the workflow there is no user present at all.

So the design question inverts. It is no longer *what should the human see?* It is *where should the human remain?*

That question sounds philosophical. It is intensely practical. Every agentic workflow contains a finite number of moments where a human could see, approve, correct, redirect, or veto. Choosing those moments — their placement, their frequency, their weight — is now the core of the design job. Everything else in this paper follows from taking that claim seriously.

### What "designing" means when there's no screen to design

To be precise about what changes and what doesn't: visual and interaction craft do not disappear. Agents still need surfaces — status views, approval prompts, summaries, escalation alerts — and those surfaces deserve the same rigor as ever. What changes is what sits upstream of the surfaces. The primary design artifact is no longer the sequence of screens; it is the *coordination model* — the specification of when the system acts alone, when it reports, when it asks, and when it stops. The screens serve the model, not the other way around.

This is why the subtitle of this paper is not a joke. The shift from UX to autonomous experience does not make design less necessary. It makes bad design harder to see until it's expensive — because a badly designed agentic flow doesn't look ugly; it looks fine right up until trust collapses.

## 2. Trust Is the Deliverable

When a person can observe every step of a tool's operation, trust is a byproduct: the tool behaves, visibly, and confidence follows. When a person delegates to an agent and looks away, that mechanism is gone. Psychological distance creeps in. Users of agentic systems consistently report the same unease: *what is it doing right now? How would I know if it went wrong?*

Trust, which used to be a byproduct of a well-crafted interface, becomes the primary deliverable. And it fails in two symmetrical ways.

**Failure mode one: the confirmation-loop parody.** The agent asks permission for everything. Every file it touches, every message it drafts, every step it takes generates a dialog. This feels safe to the people building it — every action is authorized! — but it reduces autonomy to theater and transfers the full cognitive load back onto the human, now with extra clicking. Users of these systems don't feel in control; they feel like they've been made the clerk of a machine that was supposed to be *their* clerk.

**Failure mode two: silent drift.** The agent disappears for an hour and returns with something confidently, fluently wrong — having misread the intent somewhere around step four, with nobody watching and no checkpoint where the misreading could surface. The output isn't just wrong; it's wrong *with momentum*, because subsequent steps were built on the misreading. One experience like this costs more trust than fifty successes earn.

The craft lives between these extremes, and it is genuinely craft — not a policy setting. Researchers at Amazon have started describing workflows as *coordination curves*: a mapping of how human involvement rises and falls across a task, revealing the natural peaks (framing the intent, judging the result) and the long valleys where the agent runs alone. Those valleys are exactly where design matters most, because they are where the second failure mode breeds. The related idea of *responsive salience* — an agent adjusting how visible and interruptive it makes itself based on context and stakes — points at the same insight from the other side: visibility itself is now a designed, dynamic property, not a fixed one. Tellingly, in early testing of responsive salience, several participants did not notice the adaptation until researchers pointed it out — which suggests that when coordination is well calibrated, it feels seamless rather than intrusive.

### A vocabulary of touchpoints

If touchpoints are the new screens, they deserve at least the beginnings of a taxonomy. Four levels of weight, from heaviest to lightest:

| Touchpoint | The human... | Use when... | Overuse produces... |
|---|---|---|---|
| **Approval gate** | must act before the agent proceeds | consequences are hard to reverse or carry external weight | confirmation-loop parody |
| **Escalation** | is summoned when the agent detects ambiguity or risk | the agent can recognize the boundary of its own competence | alert fatigue; escalations ignored |
| **Notification** | is informed, but the agent proceeds | awareness matters, intervention rarely does | noise; notifications filtered to a folder nobody opens |
| **Agentic task** | can reconstruct what happened, after the fact | routine work within established trust | nothing — but *underuse* here destroys auditability |

Two design principles fall out of the table. First, **weight must match stakes** — an approval gate on a trivial action teaches users that gates are noise, which is precisely how the important gate eventually gets clicked through blind. Second, **the taxonomy is dynamic, not static** — a flow that requires approval gates in month one should be earning its way down to notifications by month six, as demonstrated reliability accumulates. A touchpoint architecture with no path toward lighter weight isn't cautious; it's frozen.

That second principle has a governance implication worth stating for the decision-makers this paper hopes to reach: *who decides when a touchpoint lightens?* That is a real decision with real risk attached, and it should be owned deliberately — by the accountable human of the companion paper's model, not drifted into by whoever last edited the configuration.

### The asynchronous review problem

One property of agentic touchpoints has no precedent in screen design: the human may arrive at them *hours after the work began*. An agent that started a task at nine in the morning may pause at an approval gate at one in the afternoon, summoning a human who has long since moved on to other things. The approval itself might take thirty seconds; rebuilding the context to make it *meaningful* might take ten minutes — and under deadline pressure, the human will skip the rebuilding and approve on faith.

Every interrupting touchpoint therefore needs a **context recovery surface**: a compact answer to "what was I asked, what did the agent do, what changed, and what exactly am I approving?" A ten-second summary, the specific diff, the agent's rationale for pausing — designed as deliberately as the gate itself. A gate without context recovery is not oversight. It is a signature line.

## 3. The Toolchain Is Reorganizing Underneath Us

Here is what I find genuinely exciting, and slightly vertiginous: the artifacts we produce are changing.

We used to hand off wireframes and interaction specs. Increasingly we hand off behavior models, escalation rules, trust protocols, prompt libraries, and evaluation criteria. The deliverable is less "here is the screen" and more "here is when the system steps back and lets a human decide — and here is how we'll know it's working."

And there is now a real pipeline forming between the design layer and the execution layer:

**The design layer.** The experience logic — the coordination model, the touchpoint placement, the escalation conditions — still gets designed where designers live: in Figma and its siblings, in journey maps, in service blueprints. The blueprint just maps something new: not the user's path through screens, but the *interleaving* of human and agent activity across a workflow. Which lane is the human in, and when?

**The orchestration layer.** That logic gets *realized* in agent orchestration frameworks — LangGraph being the clearest current example, alongside the broader LangChain ecosystem and its competitors. In these frameworks, agent workflows are built as explicit graphs: nodes, states, conditional branches, loops. And — this is the part every designer should sit with — **human-in-the-loop checkpoints are first-class constructs in these frameworks.** An interrupt-and-wait-for-approval is not a hack bolted onto the side; it is a native construct, configured per tool: this action requires approval, that one allows editing, this one is safe to run unattended. Execution state is checkpointed during the pause, so the workflow resumes exactly where it stopped — whether the human answers in a minute or a day.

Read that again from a designer's chair. The escalation point you sketch in a design file has a direct counterpart in the orchestration code. The approval gate in your service blueprint maps to a configurable interrupt in the graph. Design intent and implementation haven't mapped onto each other this directly since the early days of the web — with one honest caveat: this mapping is *becoming* real rather than already universal. The frameworks support it natively; the practice of designers specifying it and engineers implementing it faithfully is still young, and the translation loss is still real in most organizations. That is an argument for designers engaging with the layer now, not a claim that the pipeline is finished.

I am not arguing that designers must write orchestration code (though some will, and the current generation of conversational build tools is collapsing that distance fast). I am arguing that the coordination model is a design deliverable, that it must be specified with the same precision we once spent on interaction states, and that a designer who can read an orchestration graph can *verify* their touchpoint architecture survived implementation. That verification is not optional. A trust protocol that exists only in the design file is a trust protocol that doesn't exist.

**What this demands of design leadership, concretely:** budget and time for designers to learn the orchestration layer; a seat for design in the architecture discussions where graphs get shaped; and a revision of what "design handoff" means in the hiring profile and the review criteria. None of these are free. All of them are cheaper than retrofitting trust into a system that shipped without it.

## 4. Where to Start: Not Where AI Is Impressive, but Where Humans Want Out

Every organization asks the same question: where do we begin with agentic flows? The instinct is to start with something visible and impressive — a customer-facing agent, a flagship feature, a demo that makes the board lean forward. The instinct is wrong, and it is wrong for a reason that is specifically a *design* reason: it ignores consent.

Many people are still wary of AI — and their wariness is reasonable, earned by every system that overpromised. Consent is not a checkbox in an onboarding flow; it is a *feeling of retained control*, and it is the substrate every touchpoint in Section 2 is built on. Insert an agent into work people care about owning, and every touchpoint reads as surveillance or usurpation. Insert an agent into work people despise, and the same touchpoints read as service.

So: **start where the pain is sharpest and the consent is cheapest.**

Time reporting might be the most universally hated activity in professional life. Nobody's identity is invested in it. Nobody fears losing control over it — they never wanted control in the first place; the control was imposed on them by an administrative system. An agent that quietly makes time reporting disappear does not trigger resistance. It triggers gratitude. Expense claims, status-report compilation, meeting minutes, calendar tetris, compliance attestations — same category: high pain, zero ownership, low stakes if the agent stumbles, and a human review step that feels like a two-minute favor rather than a burden.

There is now empirical backing for this instinct. In a recent enterprise study of UX principles for agentic systems, the top-ranked principle — human control — carried a striking criterion: participants held that an agent should work autonomously only on low-impact, time-consuming, manually intensive tasks, and 95% required human confirmation before any critical business decision. The consent on-ramp is not a rhetorical device. It is what the intended users of these systems are asking for, in their own ranking.

This on-ramp does three jobs at once:

**It builds the trust budget.** Every despised task an agent absorbs is a deposit. When agents later begin touching work people *do* care about — analysis, drafting, decisions — the organization spends from that budget. Organizations that skip the on-ramp arrive at the meaningful work with an empty account and wonder why adoption stalls.

**It is the design lab.** Low-stakes flows are where a design team learns the touchpoint craft — how heavy the approval gate should be, how fast trust accumulates, how quickly notifications become noise — while the cost of getting it wrong is a mangled timesheet rather than a mangled customer relationship. The taxonomy in Section 2 is not learned from a paper. It is learned from watching real colleagues interact with real agents on work they don't love.

**It surfaces the bottleneck honestly.** The companion paper argued that when execution becomes cheap, the constraint moves to judgment and accountability. The on-ramp makes that visible at small scale, safely: the moment the tedious work is absorbed, the question of *what the freed attention is for* — and who is answerable for the agent's output — arrives on schedule. Better to meet that question over time reports than over customer commitments.

**What the first ninety days might look like.** Concretely, for the decision-maker who leaves this section persuaded: pick one or two despised processes from the bottom-left of the delegation map. Design the coordination model for those flows — every touchpoint, its weight, and its context recovery surface — before writing orchestration code. Instrument the touchpoints from day one: intervention rates, response times, dismissal patterns. Define in advance what "trust is building" looks like as a measurement, not a feeling. Review at week six and week twelve — not for delivery metrics, but for whether the touchpoint weights are still right and what the humans in the loop say has changed. That review, not the launch, is where the organization learns whether it is ready for the second flow.

The biggest pain point is the most natural place to start. Not because it is easy. Because it is *wanted* — and wanted is the only foundation trust compounds on.

## 5. Where This Does Not Apply

A model claimed to work everywhere is a model no experienced practitioner will trust anywhere. So, plainly: the "remove the human from the loop wherever possible, touchpoints for the rest" logic of this paper collapses in several places.

**Where engagement is the value.** Creative direction, coaching, teaching, relationship-carrying conversations — contexts where the human's presence *is* the product. An agent can assist around these; designing the human out of them isn't automation, it's amputation. The design question there is the mirror image of this paper's: not "where should the human remain" but "how does the agent stay out of the way."

**Where the law or ethics puts a human in the seat.** Medical judgment, credit decisions, employment decisions, safety-critical operation — domains where regulation increasingly *mandates* meaningful human oversight. Here touchpoints are not a design nicety; they are a compliance surface, and "meaningful" is the operative word: an approval gate that humans click through blind satisfies the letter and violates the point. (The rubber-stamp problem returns in Section 10, because it is the hardest one.)

**Where the workflow is genuinely novel every time.** Touchpoint architecture assumes recurring flows in which trust can accumulate. One-off, high-ambiguity work — early-stage strategy, crisis response — offers no repetition for trust to compound on. There, the human doesn't remain at designed points; the human simply drives, with agents as instruments.

**Where the users didn't choose the agent.** The consent on-ramp of Section 4 assumes the humans in the loop have some stake in the agent's success. Where an agent is imposed on people who bear its risks without sharing its benefits — the classic deployment failure — no touchpoint placement rescues the design, because the problem isn't placement. It's legitimacy.

## 6. The Bottleneck Argument, One Level Down

"The Bottleneck Has Moved" argued that development capacity is no longer the scarce resource — judgment and accountability are — and proposed one named human per value stream, owning a verification system rather than personally re-checking everything.

This paper is the same argument at the next level of magnification. Zoom into any one of those value streams and the question recurs: *within this workflow*, where does the accountable human's judgment physically sit? If the approval gates are in the wrong places — too heavy where stakes are low, absent where they're high — the accountable human is either drowning in confirmations and rubber-stamping them, or discovering problems after they've shipped and answering for decisions they never saw.

Put sharply: **touchpoint design is what makes the accountability model of the first paper real rather than rhetorical.** The org chart says who is answerable. The coordination model determines whether they ever had a genuine chance to exercise the judgment they're answerable for. One is governance; the other is design; and the second is the load-bearing one.

This is also why the scarce design resource has changed. It is no longer screen real estate or interaction polish. It is *the placement of human judgment* — a budget of attention that must be spent where it buys the most safety and the most trust, and nowhere else.

## 7. Designing Continuous & Self-Learning Agentic Systems

Most of what has been said so far applies to any agentic workflow. Continuous, self-learning systems raise the stakes further. When an agent does not simply execute a task and stop, but keeps running, observing, and adjusting itself over weeks and months, the design problem changes character.

The coordination model is no longer a static arrangement of touchpoints. It becomes a living system that must be allowed — and expected — to evolve. Trust is no longer earned once; it is maintained or eroded across hundreds of small interactions. And the human's role is no longer only to approve or correct individual outputs, but to shape the agent's future behaviour through those approvals and corrections.

Conventional product discovery is poorly equipped for this. It assumes a relatively stable problem space, a fixed set of user needs, and an interface that, once shipped, changes only through deliberate releases. Agentic systems that learn violate all three assumptions. What follows is therefore not a complete methodology, but a proposed set of additional discovery and design steps that appear necessary once systems become continuous and adaptive.

### Why ordinary discovery is not enough

Traditional research asks what people need and how they currently work. That remains useful. It does not, however, answer the questions that determine whether an agentic system will be accepted or quietly rejected:

What will people actually hand over? How much interruption will they tolerate before they start rubber-stamping or disengaging? What proof do they require before acting on something a machine has surfaced? How should the system's behaviour be allowed to change as trust accumulates?

These are not secondary questions. They are the primary design constraints.

### Proposed additional discovery steps

The following steps are offered as a working set. Some are assembled from emerging research; two are, as far as the author can tell, new. They are listed in rough dependency order.

**1. Coordination zone triage.** Before detailed research begins, classify candidate workflows according to the relationship between human and agent: done-with-me, done-for-me, or done-under-me. Only the first two require careful touchpoint design. A done-under-me flow has no approval gates to budget for. Conventional discovery has no equivalent step because conventional software offers only one zone: done-by-me.

**2. Delegation and anxiety mapping.** Identify not only what people can delegate, but what they are willing to delegate, and where anxiety concentrates. The output is a simple quadrant that reveals where a first version can safely live. Autonomy that looks efficient on paper often fails when it touches work people feel defines their competence or responsibility.

**3. Interrupt budget profile.** Quantify interruption tolerance before placing a single gate. How many meaningful interruptions can this role absorb per day or per week before attention collapses into rubber-stamping? Fatigue is widely observed; it is almost never budgeted. Treating the interrupt budget as a design constraint rather than a post-mortem finding is one of the clearest practical disciplines this domain currently lacks.

**4. Trust baseline and verification audit.** Establish what proof a given person or role needs before treating an agent's output as actionable. The gap between "the system produced an answer" and "I am prepared to act on it" is where many agentic initiatives die quietly.

**5. Evaluation pre-commitment.** Because standardised metrics for agentic experience do not yet exist, teams must define in advance what they will measure: intervention rate, escalation precision, time-to-detection of drift, trust trajectory over time, and the rate at which touchpoints can safely be lightened. Without this pre-commitment, teams end up measuring whatever the system happens to emit.

**6. Coworker anchoring.** In environments with strong co-determination traditions (and increasingly elsewhere), the affected workforce is not merely a user group to be researched. It is a consultation partner. Monitoring boundaries, escalation rights, and the conditions under which the system may change its own behaviour should be agreed, not simply announced. Skipping this step produces systems that are technically compliant and socially stillborn.

These steps do not replace classical discovery. They sit alongside it, addressing the distinctive properties of systems that act, persist, and adapt.

### Designing for a system that is never finished

A continuous, self-learning agent does not ship a final interface. It ships a starting coordination model and a set of rules for how that model may evolve.

This has direct consequences for design. Touchpoint weight should be allowed to lighten as demonstrated reliability accumulates — and the change should be visible and explained, not silent. Labels, friction, and information density can shift with trust: a button that once said "Review & Approve" may later say "Looks right?" for categories that have earned it. The system should surface, briefly, what it has learned: "Based on your recent responses, competitor pricing alerts have been moved from approval gates to notifications." The coordination curve itself can be shown over time, with a ghost of the original curve as comparison. Design becomes something the human can watch evolving, rather than something done to them.

The governing principle is simple: the system may change its behaviour, but it must not change silently. Every meaningful adaptation should be legible. Opacity in the learning process destroys the very trust the adaptations are meant to serve.

### The Specification Gate

Every touchpoint described so far governs a single action — approve this output, clarify this ambiguity, note this event. A continuous, self-learning system introduces a qualitatively different kind of touchpoint: one where the agent proposes to change its own rules.

When the system observes that competitor pricing alerts have been approved without modification fourteen times in a row, it may propose promoting them from approval gates to notifications. That proposal is not an operational decision. It is a governance decision — a change to the system's own specification. And it belongs at a named, deliberately weighted moment in the human-agent relationship: the **Specification Gate**.

The Specification Gate is the human-in-the-loop moment for documentation, not just for output. When the agent proposes a rule change and the human approves, all downstream artifacts change together: the requirements increment, the touchpoint matrix updates, the interface specification reflects the new behaviour, and the audit log is sealed with the human's name, the decision, and the rationale. The accountable human of the companion paper is not just approving outputs — they are governing a system that is attempting to rewrite its own operating model.

This has one critical design implication that distinguishes it from every other touchpoint: **rubber-stamp decay here is not a quality problem. It is a governance failure.** A human who clicks through a Specification Gate without reading it has not merely missed an error in an output. They have ceded control of the system's future behaviour — and remain, on the record, accountable for what that behaviour subsequently produces.

The design response is therefore different from other gates. Specification Gates should be infrequent by design, never batched, always accompanied by a plain-language summary of what changes and what the system observed to propose it, and always require an explicit rationale from the human approving them — not a single click, but a confirmation that carries the weight of the decision it represents.

In a self-learning system, the interface is never finished. The Specification Gate is where that fact becomes a governance instrument rather than a liability.

### A note on ambition

The steps above are a proposal, not a proven method. They are offered because the current alternative — forcing continuous agentic systems through discovery processes designed for static software — is visibly inadequate. Organisations that treat interrupt budgets, delegation anxiety, and evolving touchpoint weight as first-class design concerns will make fewer expensive mistakes than those that discover them only after deployment.

The accountable human of the companion paper still needs well-placed judgment points. In a self-learning system those points must themselves be allowed to move — carefully, visibly, and under governance that the humans affected can recognise as legitimate.

## 8. What This Demands of Management

Conceding real costs builds more credibility than omitting them.

- **Touchpoint design must be budgeted as design work, not configuration.** If the coordination model is an afterthought assigned to whoever writes the orchestration code, the touchpoints will be placed by default. Defaults optimize for the demo, not for month six.
- **Designers need access to the orchestration layer** — training time, tool budget, and a seat in architecture discussions. This is a small line item against the cost of retrofitting trust later.
- **The consent on-ramp requires patience that quarterly demos punish.** Starting with time reporting produces no board-meeting fireworks. Leadership must be willing to measure the on-ramp by trust built and lessons learned, not by headline impact — and to say so out loud, so the teams doing the unglamorous work know it counts.
- **Research budgets must follow the question.** Usability testing assumed an observable interaction. Researching trust in a system users *don't* observe requires different methods and longer horizons; funding models built around week-long usability studies will systematically underfund exactly the evidence this shift needs.

### The leadership decision agenda

For the meeting this paper is carried into, four decisions — not discussion topics, decisions — that should leave the room owned and dated:

**Who owns touchpoint evolution?** Lightening a gate to a notification as trust accumulates is a risk decision. Name its owner, the criterion it is decided on, and where it is recorded. For self-learning systems, this owner is the person standing at every Specification Gate.

**What is the rubber-stamp policy?** Decide now what the organization does when gate-approval times collapse below reading speed — because they will. Detection, response, and consequence, agreed before the first gate ships.

**How is the consent on-ramp measured?** Agree the trust-budget signals — intervention rates, touchpoint promotion rate, participant sentiment — and the review cadence, so the on-ramp is judged on what it is for rather than on delivery theatrics.

**What is the minimum design investment in the orchestration layer?** A number: training days, tool budget, and whose calendar absorbs it. An unfunded intention is a decision to place touchpoints by default.

## 9. Open Questions

A paper earns trust by naming what it hasn't answered. Several of these are exactly where the author hopes readers push back hardest.

**The rubber-stamp decay.** Every approval gate degrades. Humans habituate; the hundredth approval gets a fraction of the attention the first one did, and the gate silently converts from a judgment point into a latency tax — while still *recording* that a human approved, which is worse than no gate at all, because it launders accountability. What keeps attention honest at a gate over months is an open design question, and in the author's view the hardest one in the space. Two speculative patterns are worth testing, offered here to be argued with rather than adopted. *Synthetic injection:* periodically insert deliberate, low-risk errors into the approval queue and measure whether they are caught — the gate's health becomes observable rather than assumed. *Progressive friction:* require the approver to identify *what* they are confirming ("line item three looks right") rather than offering a single global button — attention becomes structurally necessary rather than optional. Both carry costs; both are cheaper than discovering, after an incident, that a gate had been decorative for months.

**Researching the invisible.** Our research methods evolved for observable interaction: watch the user, see where they struggle. How do you usability-test a valley in the coordination curve — a stretch where, by design, nothing is visible? Longitudinal trust measurement, incident-anchored interviews, and instrumented touchpoint analytics all seem like pieces; none is yet a practice. The field needs its equivalent of the think-aloud protocol, and doesn't have it.

**Metrics for a well-placed touchpoint.** Click-through and task-completion don't capture what matters here. The current empirical literature is explicit that no standardised metrics or assessment methodologies yet exist for human-agent interaction quality — which means teams must author their own. As a provisional, clearly-labeled starter set: *intervention rate* at gates (persistently near-zero means the gate is theater; persistently high means the agent isn't ready), *escalation precision* (what fraction of escalations the human judged worth being summoned for), *time-to-detection* when the agent errs, *approval latency* as a decay signal (sub-reading-speed approvals flag a dying gate), and *touchpoint promotion rate* (how fast trust is legitimately accumulating). These are candidates, not standards. Until the measurement question is settled, touchpoint design will be argued by intuition, and intuition is exactly what loses budget debates.

**The skill-transfer question.** This paper cheerfully asserts that interaction designers can become coordination designers. Some will. But the craft draws on systems thinking, probability, and a tolerance for specifying behavior rather than appearance — muscles adjacent to, not identical with, classical UX strengths. What the transition path looks like, and what happens to excellent visual craftspeople in a field that needs fewer screens, deserves more honesty than a single open question — but it starts by being named.

**Touchpoints across agent-to-agent chains.** This paper assumes one human, one agent crew. Real systems increasingly chain agents across team and even organizational boundaries. Where the human touchpoints belong when *no single human* owns the full chain — whose approval gate governs a handoff between two value streams — is unresolved here, and connects directly to the architectural-consistency question the companion paper flags as its own largest gap.

## 10. Closing Thought

The point of this paper is not that any particular touchpoint taxonomy is right. The point is that the question it forces — *where should humans remain when systems no longer wait for them?* — is coming regardless of what any design team decides. Every agentic system that ships is answering it, mostly by accident. And the self-learning systems now arriving answer it repeatedly, revising their own answer as they run.

The interface is receding; the judgment points remain; and they will be designed either deliberately or by default. In continuous systems, they will then be *re*-designed — by the system itself — under governance that is either legible or absent.

Deliberately is a craft. It should be ours.

If this argument is wrong, it would be useful to know exactly where — that's what it's for.

---

## About This Paper

Jesper Karlsson is a UX and product designer, and founder of Otrobonita AI Labs. He has spent three decades in human–computer interaction, enterprise design systems and software development, most recently building autonomous agentic production systems.

This paper is a companion to *The Bottleneck Has Moved* (otrobonita.com/whitepapers), which asks where accountability lives when execution is no longer scarce. This one asks where the human remains once the answer is "with one named person." A third paper, on the design and governance of self-improving systems in full, is in preparation.

Disagreement is the point. If part of this is wrong — and some of it will be — the author would rather hear it than not.

**Contact** otrobonita.com · otrobonita.com/whitepapers · jesper@otrobonita.com
