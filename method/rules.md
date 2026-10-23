# Rule Set: Long Form

`CLAUDE.md` carries the one-line version of each rule. This file carries the full rule, its check and the reason it exists. Each rule is tagged with its evidence status:

- **[evidence]** backed by published studies, as summarized secondhand (see `why_this_method.md`, section 3)
- **[tested]** enforced by a tool in `tools/` and verified on real resumes
- **[judgment]** practitioner reasoning, adopted after a specific failure. Treat it as a hypothesis your own results can overturn

A draft passes when every check passes or the failure has been escalated to the candidate.

---

## P. Parse: the file survives the machine reader

**P1. One column, conventional headings.** [evidence, tested] Headings in this order: Summary, Experience, Skills, Education. No tables, text boxes, icons, skill bars, or headers and footers holding content.
*Check:* `parse_check.py` confirms the four headings appear in order in the extracted text.
*Why:* applicant tracking systems read plain, text-based resumes more accurately than designed ones. A creative layout is a bet that a human reads first.

**P2. Selectable-text PDF under 2.5 MB.** [tested] DOCX only when the portal asks for it.
*Check:* name, contact line, every role line and every date range come through the text extraction in order and intact.

**P3. Role lines parse cleanly.** [tested] `Title | Employer | Location`, dates on the next line. No em dashes anywhere.
*Check:* `parse_check.py` finds every role line and date line from the markdown, in order, with each date on its own line.
*Why:* em dashes between title and employer split badly in some parsers, and they read as machine-written prose.

**P4. Bullets stay with their role.** [tested] In the plain-text extraction, every role keeps its bullets between its own role line and the next.
*Why:* bold standalone sub-labels inside a role ("Selected contributions:") can be read as new section headers. The label was dropped for this reason.

**Limit:** the parse check uses `pdftotext`, the extraction layer many parsers build on. It is not Workday or Greenhouse specifically. If a portal mangles a submission, look at the portal's parsed preview and adjust the builder.

---

## F. Fit: keyword mapping, not stuffing

**F1. Name the employer's problems before touching keywords.** [judgment] State the two or three problems the hire is meant to solve, in plain language, from the JD. Keywords are then chosen to prove those problems are solved territory for the candidate.
*Check:* the tailoring output opens with that problem statement before any bullet changes.

**F2. Every seeded keyword attaches to a proof.** [evidence] A JD phrase enters the resume only inside a bullet or mandate sentence that describes real work. A keyword with no backing asset stays out, even if the ATS wants it.
*Check:* list each seeded phrase with the sentence that carries it. A phrase with no carrier is cut.

**F3. Seed each keyword once, twice at most.** [evidence] Use the JD's exact phrase once in the body. A second use goes in the Summary or Skills only for a must-have requirement.
*Check:* count repeats. Three or more is stuffing.
*Why:* in the studies summarized in `why_this_method.md`, the resumes with the highest keyword coverage got fewer interviews than those with moderate coverage. Match-score tools push the other way.

**F4. Skills is a claims section.** [judgment] Every tool or method listed must survive "tell me how you used it." JD-specific additions go in the tailored version only, never the base. Hard gaps stay out of keywords; F2 enforces this mechanically.

---

## Q. Proof: quantified impact

**Q1. Every contribution carries a measure.** [evidence] Outcome (X), measured by (Y), through (Z). This is Google's well-known X-Y-Z formula, reordered so the outcome leads.
*Check:* each contribution names a number or a named non-numeric proof.

**Q2. Non-numeric proof is allowed when it is concrete.** [judgment] Valid Y: adopted as an enterprise standard, tied to compensation, a promotion outcome, a named expansion to more accounts or sites. Invalid Y: "improved," "strengthened," "enhanced."
*Check:* could a reference check confirm the Y? If yes, it counts.

**Q3. Use the full metric menu.** [judgment] Revenue is one type. Speed, cost, margin, adoption, scope discipline, quality and talent are others. Pick the type that matches the JD's stated problem (F1). Each track in `profile/tracks.md` names the type that leads.

**Q4. Numbers come from `profile/locked_truth.md` only.** [judgment] Nothing invented, rounded or promoted. Unverified figures are flagged.
*Check:* every number traces to a line in `locked_truth.md`.
*Why:* in the original project, three submitted resumes each carried figures that had drifted from the source: a dollar figure transposed between two programs, a headcount that counted temporary coverage, and a reach figure written as adoption. None of them was caught at the time, because there was no single source to check against.

---

## B. Bullet and headline: signal density

**The diagnosis that produced these rules.** [judgment] A senior-level draft ran 1.68 rendered pages and read as prose-heavy and below its level. Words per bullet by role, newest first: 53, 24, 17, 15. The block meant to read as leader carried two to three times the words of the blocks meant to read as builder and delivery foundation. So the altitude ran backwards.

The mechanism was **proof stacking**. The current-role selection named six or more proofs against five or six slots, and tailoring resolved the collision by merging proofs into single bullets instead of cutting one. One bullet carried four separate builds in 85 words. Merging kept every asset and destroyed the scan.

**The tradeoff, decided.** Either the selection list gets shorter or the proof formula compresses. Q1 holds, so the selection list gives way. A single proof in Outcome, measured by, through form fits in one sentence under 30 words. Where brevity and proof collide, proof wins: the bullet keeps its measure, and the bullet with the weakest proof goes whole.

**Where altitude comes from.** Altitude is raised by removing operator detail, not by adding explanatory words. "Own the product roadmap for an enterprise analytics platform" reads more senior than the same line trailed by the tools and rituals used, and it is shorter. That machinery is ATS vocabulary. It belongs in the mandate and in Skills, where it screens at no altitude cost.

**B1. One bullet, one proof.** [tested] A contribution carries exactly one outcome with its measure. A second achievement is a second bullet, is cut, or becomes interview material.
*Check:* state the bullet's single claim in six words. If that needs an "and," it is two bullets. `signal_check.py` flags a second sentence that opens on an achievement verb.

**B2. Headline first, one supporting sentence at most.** [tested] Sentence one carries the outcome and measure. A second sentence may carry the mechanism and nothing else. Never a third.
*Check:* read only the first sentence of every bullet. The case still stands.

**B3. Thirty words per bullet.** [tested] One bullet per role may reach 35. Over 35 is a hard fail.

**B4. Bullet counts are a ceiling to cut to, not a quota to fill.** [tested] Defaults by role position, newest first: 5 to 8, 3 to 5, 3, 1 to 2. Bullets 7 and 8 in the current role must each pass B8 and none may duplicate another's proof type. The counts live in `profile/tool_config.json`.
*Calibration:* the defaults suit a candidate at Director level or above with a long current role. A mid-career candidate might run 4 to 6, 3 to 4, 2 to 3. An early-career candidate might run 3 to 5 per role and stay at one page. These alternatives are judgment, not tested.

**B5. One mechanism, not a work history.** [tested, warning only] Z names the single mechanism that produced the outcome. "Built on a shared data model" is a mechanism. "Built it, pitched it, then set the operating model, workplan and rollout strategy" is scope narration, which belongs in the mandate if anywhere.
*Check:* the clause after "by," "through," "built on" or "using" holds at most one comma.

**B6. The mandate says it once.** [tested, warning only] No phrase from a role's mandate reappears in that role's bullets. Scope lives in the mandate, proof in the bullets.
*Check:* `signal_check.py` reports shared three-word phrases.

**B7. Page budget and a Summary that scans.** [tested] 1.0 to 1.5 rendered pages, up to 2.0 when the current role carries 7 or 8 bullets. The Summary runs to 60 words, four sentences and two figures. It holds positioning, value and mandate only, no named wins, and its figures are scope figures. The reader takes two numbers from a six-second scan; the rest is noise the Experience section carries properly.
*Check:* `signal_check.py` measures pages on the real export layout, not from word count.

**B8. Selection and ranking.** [judgment, manual] A bullet must pass five checks, in order:
1. **Eligible:** it carries a measure from `locked_truth.md`.
2. **Required:** the track's selection list names it.
3. **Altitude:** a proof at the target career stage beats one at the stage below (`career_stage_model.md`).
4. **Distinct:** it shares no proof type or mechanism with another bullet.
5. **Unique:** it passes A3.
Rank by the reader's problem, as each track defines it. Cut the weakest bullet whole. No script can detect proof type, so this check is Claude's and the candidate's.

### Before and after (fictional)

> **Before (78 words, four proofs).** Cut order cycle time from six days to two across three distribution centers by redesigning pick paths and wave planning. Rolled out a new warehouse management system to 400 staff on schedule. Built the vendor scorecard now used across the network, and reduced carrier cost 9% through a rebid. Also launched a cross-training program that lowered overtime during peak.
>
> **After (19 words).** Cut order cycle time from six days to two across three distribution centers by redesigning pick paths and wave planning.
>
> The other three proofs do not shrink; they leave. The carrier rebid competes for its own slot. The system rollout and the cross-training program become interview material, or bullets on a track where they lead.

> **Before (44 words, mechanism sprawl).** Turned the returns process into a resale channel worth $1.4M a year by building the grading standard, pitching it to finance, then setting the operating model, staffing plan and rollout schedule it runs on.
>
> **After (22 words).** Turned returns into a resale channel worth $1.4M a year, built on a grading standard now used at every site.
>
> The measure survives whole. The how-list goes, because it restated scope the mandate already carries.

---

## AI. AI skill proof (when the candidate claims AI work)

**AI1. Shipped work leads with its measured result; in-progress work states purpose only.** [evidence, judgment] No efficiency claim without a before-and-after number the candidate can defend.

**AI2. Tools in Skills need a bullet behind them.** [judgment] Every AI tool listed appears in, or is implied by, a contribution.

**AI3. Proof is the interview walkthrough.** [judgment] At senior levels a resume Projects section reads junior, and employer work often cannot be shown. The standard is a clean verbal walkthrough of one build in under two minutes: the problem, the design, the control step, the measured result.

**Fit by function.** AI work converts fully only where the target role's function is the one the AI changed. Count it as a strength in a function-transformation seat; expect it to be read as a side skill elsewhere.

---

## A. AI-assist boundary: how Claude works

**A1. Facts before wording.** [evidence] For any new or rebuilt bullet, the candidate supplies the raw result, their specific contribution and how it happened. Claude drafts from those notes. It never generates accomplishments from job titles or JD language.
*Why:* a field experiment found light AI help with spelling, grammar and wording raised hiring probability, while other work found AI-drafted pitches more alike and harder to rank. The facts are what make a candidate rankable.

**A2. Interview-explainability test.** [judgment] Every sentence must be something the candidate would say naturally in an interview.
*Check:* read each contribution aloud as an interview answer opener. If it sounds written, it fails.

**A3. Distinctiveness over polish.** [evidence, judgment] A specific, slightly rough detail beats a smooth generic line.
*Check:* each contribution contains one detail a peer at the same level could not claim.

---

## Prompt patterns

**Employer-problem read (F1)**
> From this JD, name the two or three business problems this hire is meant to solve. Plain language, one sentence each. Then list the JD phrases that describe each problem. Do not map to my experience yet.

**Metric discovery (Q3)**
> For each contribution in my base resume, name the metric types that would prove it (speed, cost, margin, revenue, adoption, scope, quality, talent). Ask me questions to find real numbers. Do not suggest figures.

**Wording pass (A1, Q1)**
> Rewrite each bullet as Outcome, measured by, through. Use only facts and numbers from my notes and locked_truth.md. Do not add or change any fact or figure. Flag any sentence I would not say naturally in an interview.

---

## Not adopted, and why

- **A resume Projects section** at senior levels. It suits early-career candidates. Senior proof goes in the interview walkthrough or a linked case document.
- **Keyword coverage targets** such as a match-rate percentage. The evidence shows a penalty at the top of the range but gives no safe threshold, so F3 caps repeats instead.
- **Revenue as the default metric.** It leads only where the reader's problem is commercial (Q3).
- **One page as a universal rule.** Proof beats brevity at senior levels; B7 sets a budget instead.
