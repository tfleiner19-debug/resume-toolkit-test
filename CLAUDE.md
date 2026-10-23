# Operating Spec: Resume Building, Tailoring and Job Search

Claude reads this file at the start of every session in this repository. It holds the rules that govern a draft. Rationale, evidence and worked examples live in `method/`. Facts about the candidate live in `profile/`.

**Source of record.** `profile/locked_truth.md` holds every figure, title and claim the candidate allows. Where any other file disagrees with it, `locked_truth.md` governs. Never reconstruct its content from memory; open it.

---

## 0. First session: orientation and onboarding

When the candidate asks "what's in here," or opens a session with no clear task:

1. Summarize README sections 1 to 4 in under 150 words.
2. Report setup state, checked from the files and not assumed:
   - which files in `profile/` still contain `[open]` markers or template text
   - whether `profile/tracks.md` defines at least one track
   - how many base resumes exist in `profile/bases/`
   - how many rows `BOARD.md` holds, and how many have a next action that is overdue
3. If `profile/` is still mostly template, offer the onboarding questions in the README. The candidate can answer all, some or none, in any order, one at a time or in a batch.
4. Write each answer into the file the question maps to, then show the candidate exactly what was written. The candidate's answers are facts; your job is placement and wording, never invention (Rule A1).
5. Leave every unanswered item marked `[open]`, so the next session knows what is missing instead of guessing.

**Build order after onboarding:** locked truth, then tracks, then one base resume per track, then the first JD. Never tailor before a base exists, and never tailor from a previously tailored resume.

---

## 1. Who the candidate is

Read `profile/locked_truth.md` (figures, framing rules, titles, skills, hard gaps) and `profile/tracks.md` (target roles, headline per track, current-role selection per track). If either is still template, say so before drafting anything.

---

## 2. Sequence

Run in order. A Tier 3 role gets the call and the reason, not a rewritten resume.

**Before step 1, name what the person in the seat does most of the time.** If that primary activity is a discipline the candidate has never practiced, it is Tier 3 however many secondary phrases match. Matching vocabulary in a posting whose core discipline is a hard gap is the most common false positive this system exists to remove.

1. **Standard read**, six components: signal vs. noise, hard gaps, soft gaps, the tier call with the one assumption that would flip it, tailoring moves if proceeding, adjacent path if present.
2. **Tiering gate.** Every role gets one of three calls.
   - **Tier 1, tailor and apply.** Real fit. Continue the Sequence.
   - **Tier 2, apply cheap.** Plausible stretch: a human reading the resume could credibly call. Send the correct base with light keyword tuning (F2 to F4). Skip steps 3 to 5. No cover letter unless requested.
   - **Tier 3, no-go.** Stop at the call, the reason and any adjacent path.
   Tier 3 requires a **named mechanism** for the screen-out, not a count of unmet qualifications. Valid: a stated minimum naming a discipline the candidate has never practiced, or a stated screening method (AI profile matching, a hard credential filter) run against requirements the resume cannot truthfully carry. Absent a named mechanism, default to Tier 2.
3. **If Tier 1:** name the two or three problems the hire is meant to solve (F1), then map the JD's screening vocabulary to real assets (F2 to F4).
4. **Tailoring moves** against the correct track: specific bullet swaps and reframes only, pulled from `profile/` files. Hold the architecture and that track's current-role selection.
5. **Cover letter** if requested, interpretation first (`method/linkedin_and_cover_letters.md`).
6. **Review loop** (Section 3), then verify against Section 4.
7. **Checks before any submission:** `tools/signal_check.py` on the markdown, `tools/build_resume_export.py`, then `tools/parse_check.py` on the export.
8. **Log it.** Add or update the posting's row in `BOARD.md` at the end of every read and every tailoring run, whatever the tier.

---

## 3. Review loop (run on your own output before returning it)

Read the draft as a skeptical reader at the target level. Never return a first draft. You have autonomy over phrasing, never over truth.

Resolve these yourself, then revise:
1. **Thirty-second read**, as a recruiter seeing it cold. Say in one line what the candidate reads as. If it lands below the target level, find where. Name the career stage it reads at (`method/career_stage_model.md`) against the stage the target role sits at.
2. **Altitude**, bullet by bullet (B1 to B8).
3. **Delivery-language scan.** Convert vocabulary that undercuts level, such as "deliver," "execute," "support," "helped." A cadence figure is rhythm, not accomplishment.
4. **Tense.** Present for ongoing responsibility, past only for completed work.
5. **JD mapping with a ceiling.** Seed a JD phrase only where an asset backs it, once in the body, twice at most. Where an asset completes a multi-layer story the JD asks for, surface it as a proof point most candidates cannot match.
6. **Proof check.** Every contribution carries a measure per Q1 and Q2, pulled from `locked_truth.md`. If none exists, escalate.
7. **Document altitude.** The resume is evidence; the cover letter is interpretation. Operational detail stays out of the letter.

Escalate to the candidate; do not resolve these yourself:
8. **Defensibility.** Any claim they may not defend live in an interview: name it as an interview risk. Never soften it into cleaner wording.
9. **Explainability.** Any sentence they would not say naturally in an interview (A2).
10. **Conflict with `locked_truth.md`.** Stop, state the implication, confirm, then proceed.

---

## 4. Definition of good (final gate)

Verify every line. Fix or flag each failure. Never return output that fails silently.

- Correct track, with that track's current-role selection.
- Every figure matches `locked_truth.md` exactly (Q4). No rounding, no promotion of an estimate.
- Tense follows the rules recorded for each figure in `locked_truth.md`.
- No overclaims: nothing on the candidate's "never claim" list, no reach figure presented as adoption, no growth attributed to a role that did not produce it, no annualized one-time savings, no double-counted revenue.
- Any career transition framed structurally, never as dissatisfaction.
- Hard gaps acknowledged where the JD demands them, and absent from keywords.
- Cover letter leads with interpretation, not a credential recap.
- Voice: point first, verb front-loaded, short declaratives with one longer sentence for rhythm. No em dashes, no filler, no AI-sounding constructions. Candidate overrides in `profile/locked_truth.md` (voice section) win.
- Parse-safe (P1 to P4) and signal-safe (B1 to B8), both tool-verified where a tool exists. Every contribution carries a measure or concrete proof (Q2). No orphan keywords (F2, F3). AI claims per AI1.
- `BOARD.md` row written.

---

## 5. Resume architecture

The standard structure for every track; content selection is governed by track.

- **Levels step down in altitude on purpose.** The current or most senior role reads as leader, the one before as builder, earlier roles as delivery foundation. The reader should see a leader built on real delivery strength.
- **Senior blocks (current role, and the prior role if it was also senior):** a mandate paragraph, then bullets. **Earlier blocks:** plain bullets, no mandate.
- **Mandate** states scope, never accomplishment, in 60 words or fewer: three to five short declaratives, each front-loaded with Lead, Own, Manage or Direct, covering in order the programs or business owned with locked figures, platform or system ownership, team scope, stakeholder altitude, reporting line. Present tense for the current role, past for prior roles.
- **Contributions** are proof, not scope. Each follows Outcome, measured by, through (Q1) and the B rules. Default counts by role position are in `profile/tool_config.json`.
- **Failure mode:** a mandate that states scope while a bullet restates it. The mandate is what they run. Contributions are what they achieved.
- **Current-role selection by track** lives in `profile/tracks.md`. When a track's list names more items than it has slots, drop the weakest item whole. Never fold it into another bullet (B1).

---

## 6. Rule index

Operative summaries. Full text with rationale and checks: `method/rules.md`. Open it before applying a rule you are unsure of.

**P. Parse**
- P1. One column. Headings in order: Summary, Experience, Skills, Education. No tables, text boxes, icons, skill bars or header and footer content.
- P2. Selectable-text PDF under 2.5 MB. DOCX only when the portal asks.
- P3. Role lines read "Title | Employer | Location", dates on the next line. No em dashes.
- P4. Bullets stay attached to the right role in a plain-text paste.

**F. Fit**
- F1. Name the employer's problems before touching keywords.
- F2. Every seeded keyword sits inside a bullet or mandate sentence describing real work.
- F3. One use per JD phrase in the body, two at most.
- F4. Skills is a claims section: every item must survive "tell me how you used it." Hard gaps stay out of keywords.

**Q. Proof**
- Q1. Every contribution follows Outcome (X), measured by (Y), through (Z).
- Q2. Valid non-numeric Y: adoption as an enterprise standard, tie to compensation, a promotion outcome, a named expansion. "Improved," "strengthened" and "enhanced" do not count. Test: could a reference check confirm it?
- Q3. Match the metric type to the JD's stated problem.
- Q4. Numbers come from `locked_truth.md` only.

**B. Bullet and headline** (`tools/signal_check.py` enforces B1 to B7)
- B1 and B2. One proof per bullet. Sentence one is outcome and measure; an optional second sentence carries mechanism only.
- B3. 30 words per bullet; one per role may reach 35.
- B4 and B5. Drop the weakest item whole, never merge two proofs. One mechanism, not a work history.
- B6. Keyword machinery lives in the mandate and Skills, never inside a contribution.
- B7. 1.0 to 1.5 pages, up to 2.0 when the extra length is current-role proof. Summary: 60 words, 4 sentences, 2 figures; positioning, value and mandate only, no named wins. Where brevity and proof collide, proof wins: cut a bullet, never its measure.
- B8. Selection and ranking: eligible, required by track, altitude, distinct proof type, unique (A3). Rank by the reader's problem. Cut the weakest whole.

**AI. AI proof** (applies when the candidate claims AI work)
- AI1. Shipped work leads with its measured result. In-progress work states purpose only.
- AI2. Every AI tool in Skills has a bullet showing a build behind it.
- AI3. Proof is the interview walkthrough, under two minutes. No resume Projects section at senior level.

**A. AI-assist boundary** (how you work)
- A1. The candidate supplies the result, their contribution and how it happened. Never generate accomplishments from titles or JD language.
- A2. Every sentence must be something the candidate would say naturally in an interview.
- A3. Each contribution contains at least one detail a peer at the same level could not claim.

---

## 7. House rules

- Markdown is the source of record. PDF and DOCX are generated by `tools/build_resume_export.py`, never hand-edited.
- A superseded resume is not deleted. Rebuild it under current rules at its name and keep the original beside it as `_old.md`, so the two can be compared. A rebuild is what you would send now; it is not evidence about why an old application went quiet.
- Never report a job as open unless an authoritative board feed returned it in that run (`monitoring/SWEEP_RUNBOOK.md`).
- Facts and evidence go in `profile/` and `method/`. Only rules that govern a draft go in this file. Keep it lean; it is read every session.
- `profile/` and `BOARD.md` hold personal data. Never push them to a public repository. Run `tools/scrub_check.py` before sharing any copy of this repo.
