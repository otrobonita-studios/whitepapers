# Token Spenditure as a Performance Indicator

*Why your inference bill is a competitive signal, not a line item to shrink. Token spend should be sky high — the cost should stay reasonable.*

---

**Three terms, deliberately kept apart:**

**Token Spenditure** — the rate at which an organization converts human work into AI work. Spenditure is the tell: it measures how intensely you're actually using AI, and how far you're willing to push past old habits and old workflows to get there.

**Token Cost** — the size of the resulting bill, whether that's a subscription to frontier models or the capital and operating cost of your own infrastructure.

**Token Value** — what those tokens actually produce: decisions made, hours saved, revenue generated, a metric moved. Note the unit: outcomes per token, not tokens. More tokens does not mean more value — a distinction that matters later in this paper. Jensen Huang has put a number on this at the industry level, describing AI data centers as factories where the input is electrons and the output is tokens, and where a single large facility can turn roughly $50 billion of build cost into $300–400 billion of intelligence output a year.

There's a century-old precedent for exactly this shift. Early factories didn't ask how to minimize electricity usage — they asked how much more production electricity could enable, and optimized efficiency afterwards. Nobody ran a successful factory by unplugging machines. Tokens are becoming the same kind of industrial input electricity became: you measure what they enable first, and engineer the unit cost down second. That ordering is the whole argument of this paper.

These are not the same number, and the rest of this paper is about why keeping them separate is the whole point.

## The Claim

If nobody at your company is generating enough Token Spenditure to notice, you're not innovating — you're consuming, lightly.

But Spenditure and Cost are not the same variable, and most organizations confuse them. Feeling cost pain, they throttle usage: fewer agents, shorter context, tighter limits. Wrong fix — that suppresses Spenditure, which is exactly the signal you want to protect. The right posture is the opposite: push Spenditure up, because intensity of use is what parallel reasoning and agent swarms require, while pushing Cost down through architecture. Local inference, purpose-built small models instead of one expensive generalist, smarter retrieval instead of brute-force context — all of it exists to let Spenditure grow without Cost following it in a straight line.

Get this right and the graph shows rising Spenditure on a flat or falling Cost curve. Get it wrong and you either throttle ambition to protect the bill, or scale ambition and quietly bankrupt the project. A competitor who's already decoupled the two is running circles you can't see, at a Cost you'd never notice on their books. And here's the uncomfortable part: they aren't winning because their models are smarter. They're winning because they can afford to think a hundred times more.

What does Spenditure look like as an actual number, not a philosophy? A few auditable proxies: total tokens per employee per month; the share of business workflows where at least one agent participates; tokens spent on novel work (analysis, hypothesis testing, design exploration) versus routine work (summarization, boilerplate); and the ratio of agent-to-agent tokens to human-prompted tokens — a rising ratio means real swarm activity, not just chatbot usage. Pick two or three, put them on the same dashboard as Cost, and the framework stops being rhetoric.

## This Is Already Happening

The intensity shift isn't hypothetical, and the numbers are now public.

Uber handed roughly 5,000 engineers a coding assistant in December 2025 and exhausted its entire 2026 AI budget by April — four months in. Meta's heaviest single user burned 281 billion tokens in one month. Goldman Sachs, in its May 2026 report *Decoding the Agentic Economy*, projects global token consumption multiplying 24× by 2030 to 120 quadrillion tokens per month, and explains why in terms that should sound familiar: an agent continuously monitors its environment, re-reads context as conditions change, calls external tools, verifies its own output across multiple rounds, and often runs around the clock without a human prompting it. That is Spenditure, described by a bank.

The spread between organizations is the real story. The median company spends about $11 per employee per month on tokens. The top one percent spends roughly $7,450 — a factor of six hundred. Meanwhile token prices have fallen something like 98% since early 2024, and enterprise AI bills have gone *up* anyway, with a reported 73% of enterprises exceeding their original AI budgets last year. That is Jevons paradox arriving on schedule: when the unit cost of intelligence collapses, organizations run more agents rather than pocketing the savings.

Even the vocabulary has caught up. Nvidia's Jensen Huang argued at GTC 2026 that engineers should carry annual token budgets worth roughly half their salary — around $250,000 — and said he would be distinctly unhappy to find a $500,000 engineer spending only $5,000 a year on tokens. In June 2026 the Linux Foundation launched the Tokenomics Foundation, backed by Oracle, Google, Microsoft and JPMorganChase, to build open standards for exactly the cost-management problem this paper describes.

None of this proves any single organization's numbers. It establishes the trend line — and that the organizations at the front of it aren't asking whether to spend tokens. They're asking how to afford spending more.

## Salesforce: Doing It Right and Still Struggling

One company deserves a section of its own, because it shows the framework working and failing at the same time.

On the Cost side, Salesforce does exactly what this paper recommends. Salesforce AI Research builds its own models — CodeGen, xGen, xGen-Sales, xLAM — and the stated rationale for xGen-Small could serve as this paper's abstract: deliberately reduce parameter count while extending sequence capacity, achieving long-context understanding without prohibitive inference costs, delivering predictable low cost-to-serve and low energy use. A 9-billion-parameter model that ranks at or near the top among comparably sized peers. Not one expensive generalist for everything — purpose-built small models per task, served on optimized infrastructure with GPU utilization as an explicit engineering target. Textbook decoupling.

The Spenditure is real too: over 22,000 Agentforce deals and 771 million agentic work units in a single quarter, growing 57% quarter over quarter, with agents resolving the large majority of customer queries without human involvement.

And yet Salesforce has changed Agentforce pricing three times in eighteen months — from roughly $2 per conversation, to consumption-based credits at about $0.10 per agent action, and now toward charging per *resolved outcome*. The mechanics leak the difficulty: an action that crosses a 10,000-token threshold is billed as multiple actions, which turns prompt design and context injection into line items. One operations lead's summary is the whole problem in a sentence: they never know what it will actually cost, how much to budget, or how the credits are calculated.

The lesson is not that Salesforce got it wrong. It is that Token Value is genuinely hard, even for an organization with its own research lab and its own models. And the industry is converging on the same answer: HubSpot moved to charging per resolved conversation or generated lead, and ServiceNow is making similar adjustments, on the reasoning that vendors selling *usage* rather than *results* will eventually face a customer revolt. Pricing is migrating from Spenditure to Value — which is either strong validation of this framework or evidence that the market worked it out first. The urgency behind that shift: global AI software spend is projected at roughly $2.59 trillion for 2026, up 47% year over year, while an estimated 94% of engineering leaders report that core ROI metrics are still missing.

## The Warning Bell

The economics are shifting, on a timeline shorter than most roadmaps account for. Apple's M7 Ultra, reported via Bloomberg for a 2028 Mac Studio, is being designed to support up to 1.5 TB of unified memory shared between CPU and GPU — workstation and server-hall territory, the kind of machine that sits in an office rack or an on-prem room, not a bag. Apple is reportedly building AI server variants on the same silicon lineage, and notably skipping M6 Pro and M6 Max entirely to fast-track the AI-focused M7 generation. The stepping stones arrive sooner: an M5 Ultra Mac Studio with 768 GB lands in late 2026. The detail matters less than the direction — commodity hardware capable of serious local inference is coming, fast, and from more than one vendor.

That removes the excuse. "We can't afford to run our own models" stops being true the moment the hardware fits in a server closet instead of a hyperscaler's data center. The honest caveat: large unified memory makes big models *fit*; sustained swarm throughput, model loading, and energy draw are still real constraints, and "runs locally" is not yet "runs free." But marginal cost per query is falling toward electricity and amortization — and you don't have to wait for the 1.5 TB class. Unified-memory desktop nodes in the 128–256 GB range handle local agent swarms today (see the hardware list at the end); the 2028-class machines simply mark the threshold where frontier-scale reasoning moves entirely on-prem. Organizations that internalize this now will be running dense swarms locally within a few years, while the ones waiting for the next API price cut are still metering every call.

## Why It Takes Dozens or Hundreds of Agents, Not One Chatbot

Meaningful gains from agentic AI rarely come from a single well-prompted assistant. The largest gains usually emerge when dozens or hundreds of specialized agents attack a problem from different angles, reconciled by a synthesis layer. **One chatbot is a demo.** Many agents fetching data, testing hypotheses, and cross-checking each other — that's a system that moves a metric. The Spenditure in these architectures comes mostly from the parts a serial chatbot doesn't have at all: reflection loops, cross-validation, and consensus between agents.

Moving a real metric generates real Spenditure, a lot of it. If your Spenditure isn't climbing, your swarm probably isn't big enough to matter. If your Cost climbs at the same rate as Spenditure, your architecture isn't doing its job. A few problems, spread across industries so the pattern reads as general:

- **Heavy transport / fuel efficiency** — shaving a few percent off fleet consumption needs agents continuously testing routing, load, and maintenance timing against live data, not a quarterly script.
- **Pharmaceutical discovery** — parallel agents screening candidates and cross-referencing literature outperform any single research assistant; the search space is too large for serial reasoning.
- **Energy grid balancing** — matching renewable volatility to demand needs constant, distributed forecasting between many local agents, not periodic central calls.
- **Logistics and supply chain routing** — the same swarm logic applied to shipping, containers, and warehouse allocation, where the data never stops moving.
- **Content and recommendation at scale** — genuine personalization needs many lightweight agents reasoning per-user in parallel, not one generic model.

Several of these domains already run continuous algorithmic optimization — route solvers, demand forecasters, recommender models. The distinction matters: those systems optimize within a fixed problem formulation someone wrote down years ago. An agent swarm can reformulate the problem, pull in a data source nobody thought to connect, and question the assumption underneath the solver. That reformulation work is where the new Spenditure goes, and it's why the token bill in these domains *should* reach the boardroom. If it hasn't, the swarm isn't running yet — you're still optimizing the old model.

## Proof, Not Theory

The Factory — ten agents, five models, running ideation through delivery on a single workstation-class GPU — was built specifically because cloud-API-scale Cost would have made it uneconomical. The constraint drove the design: each model sized to its task rather than one frontier model for everything; local inference for the high-volume, always-on stages; frontier APIs reserved for the few steps where quality genuinely pays for itself. The pipeline runs continuously, so Spenditure stays high, while Cost sits at hardware amortization plus electricity rather than per-token billing. The system exists in its current form *because of* that pressure — the constraint was the innovation engine, not an obstacle to it.

## The Risk

Push this framework too hard and it can turn against itself in two ways.

First, decoupling Cost from Spenditure takes real infrastructure — custom silicon, local clusters, proprietary optimization pipelines — and that infrastructure is itself a capital-intensive game. Chase Token Cost down far enough and the advantage concentrates in whoever can afford to build it, tilting the field toward the same handful of infrastructure owners this framework was meant to help you compete with. Optimization, left unchecked, can entrench monopoly rather than break it.

Second, Token Value is the easiest of the three numbers to misrepresent. A model optimized purely to produce more tokens per dollar can look efficient on paper while quietly producing less useful output per token — verbose, redundant, or busywork tokens that inflate Spenditure and depress Cost without moving anything real. "Congratulations, your agents generated forty billion tokens arguing with each other" is a failure state, not a milestone. Measure Value against actual outcomes, not against token count, or the other two numbers will lie for you.

This objection already has a name, and the critique deserves to be met head-on rather than waved past. *Tokenmaxxing* — treating token consumption as a proxy for productivity — is a real and documented failure mode, and the evidence against naïve volume-chasing is not trivial: data drawn from some 22,000 developers reportedly shows bugs up 54% and code churn up 861% in high-AI-adoption environments. A reader encountering this paper's argument for high Spenditure is entitled to ask whether it is tokenmaxxing with a better vocabulary.

It isn't, and the distinction is precisely the three-needle split. Tokenmaxxing is Spenditure treated *as* the outcome. This framework treats Spenditure as an input that is worthless unless Value moves — which is why Value carries the veto, why the unit is outcomes per token, and why teams reporting 60–90% token reductions through better agent architecture are demonstrating the thesis rather than contradicting it. Falling Cost at constant Value is a win. Rising Spenditure at flat Value is the failure the critics correctly identify. Anyone who reads this paper as permission to burn tokens has read exactly half of it.

## Hardware Available Right Now

You don't have to wait for 2028. Unified-memory desktop machines already make local agent swarms economically viable:

- **NVIDIA DGX Spark** — roughly $3,000–4,700. 128 GB unified CPU+GPU memory, full CUDA stack, runs fully offline; handles 70B models without quantization, and two units can be paired for 256 GB. Throughput per agent is modest, which sounds disqualifying until you remember the architecture this paper argues for: asynchronous background agents care about task completion over hours, not streaming latency for human eyes. A swarm doesn't need any single agent to be fast — it needs many agents to be always on and nearly free.
- **NVIDIA DGX Station** — the bigger sibling, a proper desktop workstation rather than a hand-sized box. More power, more cost, aimed at teams doing heavier fine-tuning rather than inference alone.
- **A high-end gaming PC (RTX 5090-class)** — more raw GPU throughput per dollar, and doubles as a video/render rig. But no unified memory: capped by VRAM, which rules out the model sizes a unified-memory box handles comfortably.

For organizations serious about Spenditure rather than curious about it, the unified-memory route is the honest bridge. The gaming-PC route makes sense only if the real bottleneck is graphics work rather than agent inference.

## Two Postures, Side by Side

| | Legacy posture (throttled) | Decoupled posture (optimized) |
|---|---|---|
| **Primary goal** | Minimize the inference bill | Maximize AI integration density |
| **Architecture** | One frontier model, API calls | Swarms of specialized models + routing, local where it counts |
| **Cost behavior** | Scales linearly with ambition | Flat or falling while Spenditure climbs |
| **Failure mode** | Low ambition, no transformation | Token inflation — vanity Spenditure (mitigated by outcome tracking) |
| **What the board sees** | A cost line to cut | Three needles: Spenditure, Cost, Value |

## The Bottom Line

Three needles: Token Spenditure, Token Cost, Token Value. Rising Spenditure with rising Cost and flat Value means you're spending your way to a result — expensive, and eventually unaffordable. Rising Spenditure with flat or falling Cost, and Value pulling ahead of both, means you've built something that scales its own thinking and pays for itself while doing it.

If you want the whole framework in one line, treat it as a conceptual equation, not literal mathematics:

**Organizational Intelligence ≈ (Token Spenditure × Token Value) ÷ Token Cost**

Read Value as outcomes, never as token count — otherwise the equation rewards exactly the busywork it's meant to expose. Push the numerator up. Engineer the denominator down. Everything else in this paper is commentary on those two moves.

Three things this short paper deliberately leaves open, each large enough to deserve its own: how to attribute Token Value to outcomes when effects are lagged and multi-causal; what has to change in workflows, review loops, and trust calibration before high Spenditure is even possible; and how organizations that can't build private clusters achieve the same decoupling through open models, efficient fine-tunes, and shared infrastructure. Naming them is not the same as solving them — but a framework that pretended they were solved would be worth less than one that doesn't.

In ten years, organizations won't be measured by how many employees they have. They'll be measured by how much thinking they can afford. Token Spenditure is simply the first attempt to measure that.
