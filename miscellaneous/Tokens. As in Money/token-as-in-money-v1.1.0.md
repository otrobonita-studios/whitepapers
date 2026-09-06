# Token… as in Money

### Your bill has never been higher. Tokens have never been cheaper. Both are true, and the second explains the first.

*Otrobonita AI Labs — Whitepaper v1.1.0*

---

## Why this paper, and why now?

Models keep getting better, we are told — and whatever else turns out to be true about that, they get there by spending. They think before they answer, in tokens. They read more context. They call more tools. The capability is bought in exactly the currency your ceiling is measured in.

Which means the better they get, the sooner you hit the roof. And then you sit there, mid-thought, waiting it out.

An earlier paper in this series argued that low token spend is a warning sign: if your spend isn't a problem, you probably aren't using the thing. That was written from a company's chair, where tokens compete with software licences and contractor invoices.

This one is written from the kitchen table, where they compete with groceries. It is about why the roof arrives when it does, and how to get more quality time with your favourite supermodel.

## The thing that looks like a contradiction

Tokens keep getting cheaper. Not slightly — the median frontier model has fallen by roughly 84% since GPT-4 launched in 2023, and the floor for mainstream models now sits around twenty cents per million words-worth of input. By every measure the industry publishes, this is one of the fastest price collapses in the history of computing.

Meanwhile your monthly AI spend went up.

This is not a paradox and nobody is cheating. It is the oldest pattern in resource economics: when something gets cheap, we use much more of it. Cheap tokens mean models that think before answering, in tokens. They mean agents that take fifty steps where a chat took five. They mean uploading the whole folder because why not. Consumption grew faster than price fell, and it grew faster *because* price fell.

There is a second, quieter mechanism. The token is not a fixed unit. Newer model generations count roughly thirty per cent more tokens for the same sentence than older ones did. The sticker price can stand perfectly still while the thing being priced quietly shrinks. No price list shows this.

And a third, which is the one that matters most at the kitchen table: **the price collapse never reaches you.** If you pay a monthly subscription you are not buying tokens at all. You are buying an allowance. The API market got 84% cheaper while consumer tiers went the other way, and the gap between those two facts is where household AI budgets now live.

## Company value, family value

At work, the question is return on investment. Someone builds a business case, the licence competes with other licences, and if it pays for itself it stays.

At the kitchen table the question is different, and no table of figures answers it: **what else would that money have been?** A subscription sits next to the streaming services, the phone plans, the food shop. Nobody runs a business case on it. Somebody just notices, one month, that it adds up.

Families already have a vocabulary for this argument, and it isn't the finance one. It is screen time. What's reasonable, who decides, when does it tip over. AI spending is that same conversation with an invoice attached — and this paper borrows the household vocabulary rather than importing the corporate one.

Worth naming one boundary that runs straight through the middle of it. A parent logs in from home in the evening and has a long, serious, genuinely productive work conversation — on the family subscription, at a consumer tier, against a consumer allowance. That is work paid for out of the household budget. The employer would have got the same tokens cheaper, and often does elsewhere. Nobody decided this. It just happened, the way these things do, and it is worth a family knowing it is happening before they argue about the bill.

## Three piles

Every message you send carries three kinds of weight.

**The setup charge.** Before your question, every message quietly carries the assistant's instructions and a full description of every tool you have connected — what it does, what it accepts, every option. Connect a dozen integrations "just in case" and you are mailing their entire manuals with every single message, whether you use them or not.

**The conversation pile.** This is the big one, and it surprises almost everyone: the assistant remembers nothing between messages. What looks like memory is the whole conversation being re-read from the top, every time. Message twenty re-reads messages one through nineteen. The pile does not grow like a line. It grows like a staircase where every step is longer than the last.

**The attachment tail.** A file you attach is not paid for once. It rides along in every message that follows it. Attach a report in message two of a twenty-message conversation and you have sent that report eighteen times.

For anyone who likes it as arithmetic — the full version lives in the appendix:

> **T ≈ P·n + t·n(n+1)/2 + F·(n−k+1)**
>
> Setup (P) times turns. Plus the pile: average new text per turn (t), summed triangularly. Plus the attachment (F) times the turns it still has to ride along after arriving at turn k.

### What that looks like with real numbers

A modest ten-message conversation. The instructions and tools come to 2,000 tokens. Each exchange adds about 400. You attach a 3,000-token document — call it six pages — on message two.

- Setup: 2,000 × 10 = **20,000**
- Pile: 400 × 10 × 11 ÷ 2 = **22,000**
- Attachment: 3,000 × 9 = **27,000**

**About 69,000 tokens for a ten-message chat**, of which your actual questions are a rounding error. The single largest line is a six-page document you attached once.

Read that last line twice. It is the entire paper.

## What you are actually paying for

One more uncomfortable detail. The assistant's replies are usually the biggest part of the pile — longer than your questions, often by a lot. And they are billed at a premium when written, then charged again as ordinary re-reading in every message that follows.

**Verbosity is paid twice.** Asking for a shorter answer is not politeness. It is a budget decision.

## How densely the words pack

The system does not charge by idea, or by word. It charges by fragments it recognises, and some writing packs into fewer fragments than others.

The largest factor by far is language. English is the cheapest encoding these systems know. Most Western European languages cost roughly one and a half to two times as many tokens for exactly the same meaning; some writing systems considerably more. That is not only money — it is room. A Swedish user runs out of space in a conversation sooner than an English one, for the same amount of thinking, on the same subscription.

This is a property of how the systems were trained, not a personal failing, and it is not advice. Nobody should abandon their working language to save fragments. The correct conclusion runs the other way: **if you work in a language that packs poorly, everything else in this paper matters more, not less.** You are already paying a premium on every idea, so paying for the same paragraph nineteen times costs you more than it costs an English speaker.

Spelling and formatting belong to the same family and are much smaller. Unusual spellings split into more fragments, but a handful of typos will not move your bill. The real cost is indirect: an unclear question buys a clarifying question or a wrong answer, and that extra exchange then rides the pile for the rest of the conversation. Write normally because it saves you a round trip, not because it saves you fragments.

## Three questions, in order

The whole strategy fits on a napkin.

1. **How long will this conversation live?** That sets the pile. New topic, new chat.
2. **What is sitting at the front, and when did the file arrive?** That sets the setup charge and the attachment tail.
3. **How densely do the words pack?** Language, then format, then spelling.

The first two move the bill. The third trims it.

### As habits

- **Start a new chat when the subject changes.** The single most effective habit available. An old conversation is a bill you keep paying.
- **Attach late, not early.** Ask your questions first. Attach when the file is actually needed.
- **Paste the text instead of uploading the PDF.** A PDF page is often processed twice over — once as a picture, once as text. Same content, a fraction of the cost, and read more reliably.
- **Never screenshot text.** The layout is not the information. A model reads what looks to you like an ugly wall of pasted text considerably better than a tidy picture of the same words — and the picture costs more. Select, copy, paste. The exception is when the layout genuinely *is* the information: a chart, a table that collapses into nonsense as text, a screen you are asking about. Then the picture earns its price.
- **Attach the pages, not the report.** Three relevant pages beat a two-hundred-page appendix on cost and on answer quality alike.
- **Ask for shorter answers.** Billed high once, then re-billed forever.
- **Connect tools sparingly at the start, then leave them alone.** Every connected tool is described in full on every message. But disconnecting mid-conversation has its own cost — it throws away the discount your stable setup had earned. Choose at the beginning; don't tidy up halfway through.
- **When a long conversation drifts, ask for a summary and start fresh with it.** Keep the conclusions. Drop the accumulated weight.

Notice what the list does not say. It never says ask less, or ask smaller. A well-formed question with the right context attached *should* cost more than a lazy one. What it eliminates is the re-asking — the four follow-ups needed because the first attempt was careless, each of which is then paid for again in every message that follows.

## And the free ones?

There are four ways to use these systems without a subscription, and they age differently, so here they are as kinds rather than brands: an assistant already built into something you own, a free tier from one of the major labs, a cheap challenger trying to buy its way into your habits, and a model you run on your own machine. The last one is genuinely free in tokens and assumes hardware most households do not have, so treat it as a special case rather than a suggestion.

Two things to know before the family settles on free.

**The ceiling arrives sooner, not later.** Free tiers come with tighter allowances and usually smaller models. Everything in this paper therefore applies more there, not less. A free user who attaches a PDF in message two will be sitting at the roof before lunch.

**And free is paid for in another currency.** Usually your conversations, used to improve the product. Sometimes advertising. But the deepest one is this: a paid subscription wants you to finish, and a free, engagement-funded product wants you to stay. **Screen time isn't a side effect of free. It is the revenue model** — and it happens to be the exact currency families were already rationing.

The ceiling didn't disappear. It moved from the invoice to the clock.

## And sometimes you want the long conversation

Here is the honest exception, and it undoes half of the above on purpose.

Everything so far assumes you want an answer. Sometimes you want a conversation — to think out loud, to be argued with, to arrive somewhere over twenty rounds that you could not have reached in three. In that mode the number of rounds is not overhead. It *is* the product. A model that hands you the right answer in one exchange has, from this angle, sold you rather less than you wanted.

So spend it. Just know which one you are buying. The waste this paper is about is paying for twenty rounds and getting three rounds' worth of thinking — because nineteen of them went on re-reading a PDF you attached at the start and forgot about.

## What nobody shows you

Every one of these interfaces hides the accumulating weight completely.

You connect twelve integrations "just in case" and nothing tells you what that costs, per message, forever. You attach a report in the second message and nothing mentions that it will travel with you for the rest of the conversation. The information exists. It is simply never shown.

Which costs is it reasonable for a person to see and steer, and which are fairly hidden away? Every piece of advice in this paper assumes someone who can see numbers that no interface displays. That is not a token problem wearing an interface costume. It is an interface problem wearing an infrastructure costume.

---

# Appendix — for people who build things

The same model, stated for practitioners, plus the parts that only apply when software is doing the typing.

### The model

**T = P·n + t·n(n+1)/2 + F·(n−k+1)**

P is prefix size (system prompt plus tool and schema definitions), n is turns, t is average new tokens per turn, F is payload size, k is the turn at which the payload arrives.

Three terms, three growth curves — linear, triangular, and linear in remaining turns — and therefore three different remedies. Most cost discussions apply the wrong remedy to the wrong layer: caching offered as an answer to context bloat, compaction offered as an answer to an oversized prefix.

**What T is and is not.** It counts input tokens under unmanaged conditions. It is not an invoice. Output and reasoning tokens are billed separately and higher and are not in the equation. A stable prefix is billed at a discount after the first write. Compaction makes the middle term piecewise. It is also a billing curve, not a compute-complexity curve — unrelated to the O(n²) attention cost inside a single forward pass, despite the shared exponent.

**Stateless, but no longer uniformly retransmitted.** Three things that used to be identical are separating: model memory (still absent), wire retransmission (no longer universal — some APIs chain on a previous-response identifier and hold state server-side), and billed tokens (the context is still processed). Keep them apart when reasoning about a specific vendor.

### The prefix

Tool definitions are not names in a list — each carries a full schema. Mid-sized connectors expose thirty to sixty tools each. Caching is how you price the prefix: large, stable, at the front, read at a fraction of base input after the first write. One vendor now prices frontier cache reads at 2.5% of input rather than the usual 10%, and reports that this cuts typical workloads by around a quarter and agentic ones by nearly half — which is, in effect, the prefix tax and the conversation pile measured by the people selling them.

The fragility is specific: change a connected tool mid-session, reorder the list, or leave a timestamp at the top, and the prefix invalidates and the write premium is repaid. Hence: stable content first, volatile content last.

The quality argument outranks the cost argument. Schemas for tools that are never called degrade tool selection. More tools do not make an agent more capable; they make the choice harder.

### The agentic multiplier

In a chat the human is the rate limiter — you type, you read, you pause, and patience caps n at around thirty. An agentic loop has no such brake. Turns fire as fast as the API responds, every tool result is appended, the volume is machine-generated, and t grows as the session goes, so the curve steepens rather than merely continuing.

Fan-out is the naive case, not the necessary one. An orchestrator that clones a transcript to five subagents carries five piles; a competent one passes a task slice and gets a summary back. The patterns that actually break the triangle in production:

- Tool-result budgets — cap what one call may append, truncate with a pointer.
- Artifact stores instead of pasted files — the transcript carries paths, not contents.
- Subagent isolation with summary-back — slices in, conclusions out, never a cloned transcript.
- Explicit "what leaves the room" — the return value is what the parent pays for from then on.

### Four axes, in order of what to try first

1. **Price — caching.** The first move, not the clever one. Cheaper curve, same shape; cached content still occupies the window.
2. **Volume — compaction.** Summarise older context at a threshold and drop what precedes it. The only mechanism that actually breaks the triangle. Lossy by construction.
3. **Relocation — progressive disclosure.** Context editing, memory, retrieval, artifact stores, skills, deferred tool loading. All one idea: keep a pointer in context, not the content. Metadata in context, body on disk.
4. **Internalisation — fine-tuning the prefix into the weights.** Usually beaten by a cached, versioned, shared prefix plus retrieval. If pursued, split by volatility and auditability rather than size: tone and terminology are stable and statistical; policy changes quarterly, must be deterministic, and must be auditable. You can point at a document. You cannot point at a weight.

Diagnostic order: large prefix and short sessions → caching and prefix hygiene. Long sessions with growing t → compact and budget tool results. Large payload arriving early → relocate it. Only then internalisation, and only after asking whether the workload should have been interactive at all.

### Restrictive and transformative measures

Restrictive measures remove a degree of freedom to avoid solving an architecture problem: blocking uploads, capping conversation length, flattening a prompt into a fine-tune. They work, and they show up in the budget immediately — and in user behaviour a quarter later. Block PDF uploads and people paste broken text, screenshot pages (more expensive than the original), or leave for a consumer tool with no data agreement. **A blocked format in a tool people must use is a shadow-IT generator.**

Transformative measures remove the cost without removing the capability: convert at ingest, deduplicate by document hash, and set quotas by exposure rather than size — a payload's true cost is its size times the turns that follow it.

### Limitations

Analytical, not validated against production billing. Additivity holds for tokens, not for money. The closed form assumes constant t and a single payload, both of which understate agent sessions. Coefficients are vendor- and version-specific and stale on publication; the mechanics are not. Self-hosting, batch processing and long-context tiers are out of scope, which leaves one architectural question unasked: whether a given workload should have been interactive at all.

### Terms

**The setup charge** *(the prefix tax)* — what you pay every turn for capability you may never use.
**The conversation pile** *(the conversation triangle)* — the triangular cost of remembering by re-reading.
**The attachment tail** *(the payload multiplier)* — a document's cost is its size times the turns that follow it.
**Progressive disclosure** — metadata in context, body on disk.
**Restrictive and transformative** — removing the capability, or removing the cost.
