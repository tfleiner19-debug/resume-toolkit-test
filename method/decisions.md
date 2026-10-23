# Decision Log

Each entry is a rule, the failure that produced it, and how to apply it. They come from one real search, with the person's details removed. If you want to overturn a rule, read its failure first: that is what you would be accepting again.

---

### D1. One source of truth for every figure
**Failure.** Three submitted resumes each carried figures that had drifted: a dollar value transposed between two programs, a team size that counted temporary coverage, a reach number written as adoption, a title that never existed, and one role that was not in the career history at all. They had been tailored from each other, not from a shared base.
**Rule.** Every figure lives in `profile/locked_truth.md` with its forbidden forms. Tailor from a base only, never from a tailored resume.
**Apply.** Before any draft, open the file. Never reconstruct a figure from memory or from an earlier resume.

### D2. Proof wins over brevity; cut whole, never merge
**Failure.** A senior draft ran 1.68 pages with 53-word bullets in the current role, because six-plus proofs were merged into five slots. It read as prose-heavy and below level.
**Rule.** One proof per bullet (B1). Where the list outruns the slots, the weakest proof leaves whole.
**Apply.** When a track's selection list names more items than slots, write "drop" in `tracks.md`, never "compress into."

### D3. Altitude comes from subtraction
**Failure.** Senior bullets trailed by tools, rituals and process steps read as operator work.
**Rule.** Machinery goes in the mandate and Skills, where it screens for the ATS at no altitude cost (B6).
**Apply.** If a bullet names a tool, ask whether the tool is the proof. Usually it is the mechanism, at most.

### D4. Tier 3 needs a named mechanism
**Failure.** Gap-counting let a no-go stand in for a prediction. Three no-gos in one day failed for three different reasons, which pointed at sourcing, not at the bar.
**Rule.** A no-go is a forecast about whether a human ever reads the resume, never a judgment about whether the candidate could do the job. It needs a stated minimum or a stated screening method the resume cannot truthfully pass. Otherwise, Tier 2.
**Apply.** State the tier in every read, and name the mechanism in the same sentence as any Tier 3.

### D5. Name the seat's main activity first
**Failure.** Postings matched on vocabulary while their core discipline was a hard gap. One had genuine matches in four of eleven responsibilities; the other seven were hands-on modeling.
**Rule.** Before the Sequence, say what the person in the seat does most of the time. If that is a discipline never practiced, it is Tier 3.
**Apply.** Look next for the adjacent function inside the same organization. It is often the real target.

### D6. Only a feed proves a job is open
**Failure.** A first job sweep reported four leads found by web search. All four were closed. Job-board pages keep serving the full description after a requisition closes, and search indexes lag by weeks.
**Rule.** Report a job as open only when an employer's board feed returned it in that run. Search is for discovering companies, not jobs.
**Apply.** See `monitoring/SWEEP_RUNBOOK.md`. Never mark a job closed only because a feed did not show it, either: large feeds get cut off silently.

### D7. Never end a sweep silently
**Failure.** A scheduled sweep ran, found nothing and posted nothing. The candidate had to ask whether it had run.
**Rule.** Every sweep posts a report, even "nothing new," and names the roles still open.

### D8. Keep a superseded resume beside its rebuild
**Rule.** A superseded resume is rebuilt under current rules at its name and the original is kept as `_old.md`.
**Why.** The pair shows how the rules change the output. It is **not** evidence about why an old application went quiet: a rebuild is what you would send now, not what went out.

### D9. When the search goes quiet, hold every explanation loosely
**Failure.** A no-callback stretch was blamed on how the current title read. An audit then found enough figure and altitude errors in the same submissions to explain it just as well.
**Rule.** Treat each explanation as a hypothesis. The board's closed rows and outcome columns are the evidence.

### D10. The operating spec stays lean
**Failure.** The project's instructions grew past the platform's character limit because evidence and history kept being added to them.
**Rule.** Only rules that govern a draft go in `CLAUDE.md`. Evidence, rationale and history go in `method/`. Facts go in `profile/`.
**Apply.** Before adding to `CLAUDE.md`, ask whether the addition is a rule or a reason. Reasons go here.

### D11. No "current" copy of a moving spec
**Rule.** Never keep a file named "current" that duplicates a live spec. The first stale read costs more than the copy saves. Snapshot deliberately at a milestone, with a date in the filename.

### D12. Confidential clients are never a warm channel
**Failure.** The current employer's client roster was proposed as a warm target tier. The candidate's agreement restricted soliciting clients, and the candidate did not own those relationships.
**Rule.** Check agreements before building any target tier from work relationships. Map former colleagues, not accounts.

### D13. Titles stay official
**Rule.** Prior titles appear exactly as held, on every track. Never swap in a better-reading title, even a close one. A background check compares titles, and an interviewer may know the employer's ladder.

### D14. Headline wording is the candidate's
**Failure.** A default headline qualifier was invented and rejected.
**Rule.** Claude proposes, the candidate decides. Never ship an invented qualifier.

### D15. One-time savings are never annualized
**Rule.** A result from one month on one workstream stays that size. Annualizing it is the overclaim most likely to be tested in an interview.

### D16. Reach is not use
**Rule.** "Made available to N people" is reach. Write it as adoption, usage or current reach only with usage data, and use past tense if the product is retired.
