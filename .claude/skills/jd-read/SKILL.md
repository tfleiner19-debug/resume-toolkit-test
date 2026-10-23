---
name: jd-read
description: Read a job description against the profile and make the tier call (CLAUDE.md Section 2, steps 1-2). Use when the user pastes or links a JD and asks whether to apply.
---

1. Save the JD to `jds/<Company>_<Role>.md` with its source URL and date.
2. Check `profile/locked_truth.md` and `profile/tracks.md` exist and are filled. If not, say what is missing and stop.
3. Name what the person in the seat does most of the time, who it reports to, and whether it does the candidate's kind of work (`method/target_company_framework.md` section 4).
4. Run the six-component standard read: signal vs. noise, hard gaps, soft gaps, tier call with the one assumption that would flip it, tailoring moves if proceeding, adjacent path if present.
5. Tier 3 must name its screen-out mechanism. Without one, default to Tier 2.
6. Name the track and base to use.
7. Save the read to `jds/<Company>_<Role>_Read.md`.
8. Add or update the row in `BOARD.md`.
9. Lead the reply with the tier and the reason in one sentence.
