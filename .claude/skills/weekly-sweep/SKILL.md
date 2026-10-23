---
name: weekly-sweep
description: Run the weekly job-opening sweep from monitoring/SWEEP_RUNBOOK.md. Use when the user asks for a job sweep or a scheduled sweep fires.
---

1. Read `monitoring/SWEEP_RUNBOOK.md` in full before starting, and follow it step by step.
2. Confirm the Settings block and the vocabulary in `profile/tracks.md` are filled. If not, stop and say what is missing.
3. Report a job as open only when a board feed returned it in this run.
4. Keep feed-verified and unverified results in separate tables.
5. Update `monitoring/seen_postings.json` and add survivors to `BOARD.md`.
6. Always post a report, even when nothing new cleared.
