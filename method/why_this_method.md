# Why This Method: An Honest Comparison

**Short answer.** On judgment and truth-control, this is stricter than the common tools and the standard advice. On proven results, it is unproven. It was built and refined during one senior-level search, and no response-rate data exists yet for resumes built under the current rules. The board's outcome columns exist to produce that data for you.

---

## 1. What most approaches do

| Approach | What it does well | Where it goes wrong |
|---|---|---|
| **Keyword match-score tools** (Jobscan and similar) | Shows which JD terms your resume lacks. Fast. Good for cold applications through an ATS | Optimizes toward a coverage target. Jobscan's own guidance is a 75 to 80% match rate. That pushes toward the high-coverage end, which the evidence below associates with fewer interviews |
| **AI resume builders** (Teal and similar) | Job tracker, templates, AI-generated bullets and summaries from a pasted JD | Generates accomplishments from JD language, so many candidates end up with the same smooth bullets. Nothing checks the claims against what you can defend |
| **Standard advice** (quantify everything, X-Y-Z bullets, tailor every resume, one page, ATS-safe format) | Correct as far as it goes. This method keeps all of it except the one-page rule | No rule for *which* proof to cut, *when* tailoring is worth it, or *how to stop* a figure drifting between versions |
| **A professional resume writer** | Strong wording, an outside eye | One-time document. No system for the next 30 applications, and the writer cannot check your numbers either |

## 2. What this method adds

1. **A locked source of truth with forbidden forms.** Every figure has one home, with its status and the forms it must never take ("not $2M, not $2.5M"). *Why it matters:* in the original search, three submitted resumes each carried drifted figures. One transposed two program values, one counted temporary coverage as headcount, one wrote reach as adoption. No common tool catches this, because none of them knows your real numbers.
2. **A hard line between facts and wording (Rule A1).** Claude never generates an accomplishment. *Why it matters:* AI-drafted resumes converge, and a reader cannot rank candidates who all sound alike.
3. **A keyword ceiling instead of a target (F2, F3).** Each JD phrase is used once, twice at most, and only where real work backs it.
4. **A decision before effort (the tiering gate).** Every posting gets Tier 1 (tailor), Tier 2 (send the base cheaply) or Tier 3 (skip). Tier 3 requires a *named mechanism* for the screen-out, not a count of unmet requirements. Before any of that, Claude names what the seat does most of the time. *Why it matters:* the most common false positive is a posting full of your vocabulary whose core job is a discipline you have never practiced. Match scores reward exactly those postings.
5. **Machine-checked bullet rules.** One proof per bullet, a word ceiling, bullet counts, summary limits, and page fill measured on the real PDF layout. The parse check runs on the exported file, not on a preview.
6. **A review loop with an escalation boundary.** Claude fixes phrasing, altitude and tense itself. Anything you might not defend in an interview goes back to you, never into softer wording.
7. **Career-stage calibration.** A four-stage model of what table stakes, good and exceptional look like at each level, so "reads senior" becomes a check rather than a feeling.
8. **Search hygiene.** A job is reported open only when an employer's board feed returned it. That rule came from reporting four "live" leads that were all closed.
9. **A decision log.** `decisions.md` records each rule's origin failure. You can disagree with a rule, and you can see what it was protecting against.

## 3. Evidence base, and its limits

The proof, fit and AI-assist rules lean on a synthesis of third-party studies published by Jeff Su ("Write a Killer Résumé in the AI Era," September 2026, with a written guide at jeffsu.org). Figures as he reports them:

| Finding | Reported figure | Rule it supports |
|---|---|---|
| AI screening reads plain text-based resumes more accurately than designed ones | 87% of hiring managers say so | P1 to P4 |
| Tailoring helps; stuffing backfires | 5.71% interview rate tailored vs. 3.09% untailored; the highest keyword coverage got 21% fewer interviews than moderate coverage | F2, F3 |
| Light AI polish helps; heavy AI drafting flattens candidates | An MIT field experiment found wording help raised hiring probability 8%; separate work found ChatGPT made pitches more alike | A1, A3 |
| Quantified impact beats described responsibility | 75% higher interview rates | Q1 |
| Role-relevant AI skills help when demonstrated | Up to 15 points higher interview selection (Oxford); 60% of hiring managers want AI skills proven, not listed | AI1 to AI3 |

**Limits, stated plainly:**
- These are secondhand summaries. The underlying studies were not independently verified for this toolkit.
- The studies draw on broad applicant pools. Senior hiring runs more through referrals and recruiters, where a human reads first. The parse and keyword rules matter most on cold applications; the proof rules matter on every path.
- Every rule tagged [judgment] in `rules.md` is reasoning from failures in one search, not a study result.

## 4. Where this method is weaker

- **It costs more per application.** A Tier 1 tailoring run with the review loop and checks is slower than pasting into a match-score tool. The tiering gate is the offset: most postings should be Tier 2 or Tier 3.
- **It needs setup.** The locked truth and the bases take a few sessions. Weak inputs produce weak output under any rules.
- **It is calibrated for senior candidates.** The default bullet counts, page budget and mandate structure assume Director level or above. Early-career users should change `profile/tool_config.json` and ignore the mandate paragraph.
- **The parse check is a proxy.** It tests the text extraction most ATS parsers build on, not any specific vendor.
- **The judgment is Claude's.** The review loop and the B8 ranking depend on Claude applying the rules well. Read every draft yourself before you send it.
- **No outcome data yet.** Whether resumes built this way get more callbacks has not been measured. Fill in the Response columns in `BOARD.md` and ask for a comparison after 15 to 20 applications.

## Sources

- [Jobscan: what match rate should I aim for](https://www.jobscan.co/blog/what-jobscan-match-rate-should-i-aim-for/) (75 to 80% guidance)
- [Rezi's review of Teal](https://www.rezi.ai/posts/teal-review) (feature summary: job tracker, JD-based AI bullet generation, match score)
- Jeff Su, "Write a Killer Résumé in the AI Era: 5 New Rules" (YouTube, September 2026) and the written companion at jeffsu.org/resume-ai-era-guide
