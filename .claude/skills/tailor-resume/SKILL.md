---
name: tailor-resume
description: Tailor a base resume to a Tier 1 job description, run the review loop and the three checks (CLAUDE.md Section 2, steps 3-8). Use after a JD read returns Tier 1, or Tier 2 for light keyword tuning.
---

1. Confirm a read exists in `jds/` with a Tier 1 or Tier 2 call. If not, run the jd-read skill first.
2. Copy the track's base from `profile/bases/` to `profile/tailored/<Last>_<First>_Resume_<Company>.md`. Never start from another tailored file.
3. Tier 1: state the two or three employer problems (F1), map JD vocabulary to real assets (F2 to F4), then make specific bullet swaps and reframes from `profile/` only. Hold the architecture and the track's current-role selection.
   Tier 2: keyword tuning only, under F2 to F4. No structural changes.
4. Run the review loop in `CLAUDE.md` Section 3 on your own draft. Revise. Do not return a first draft.
5. Run, in order: `python3 tools/signal_check.py <file>`, `python3 tools/build_resume_export.py <file>`, `python3 tools/parse_check.py <file>`. Fix any failure and re-run.
6. Verify against `CLAUDE.md` Section 4, line by line.
7. Update the row in `BOARD.md` (status, track, files).
8. Reply with: the track used, the changes made and why, every item escalated under review loop items 8 to 10, and the check results.
