# Worked example: Sam Okafor (fictional)

Everything here is invented: the person, both employers, the posting and every figure. It shows the whole system on one candidate in a field unrelated to the toolkit's origin.

Read in this order:

1. `profile/locked_truth.md`: what a filled source of record looks like, including forbidden forms, a figure held back for verification, and interview-only material.
2. `profile/tracks.md`: two tracks, each with a headline, a ranked selection and an explicit drop.
3. `Okafor_Sam_Resume_Base_Operations.md`: the Track 1 base. Every figure traces to `locked_truth.md`.
4. `jds/Larkspur_SrDir_Fulfillment.md`: a posting.
5. `jds/Larkspur_SrDir_Fulfillment_Read.md`: the read. Note what it refuses to seed ("cost per order") and why, and what it escalates.
6. `Okafor_Sam_Resume_Larkspur.md`: the tailored resume. Compare it with the base: three changes, no new claims.

Try the tools on it:

```
python3 tools/signal_check.py --config examples/fictional_candidate/profile/tool_config.json examples/fictional_candidate/Okafor_Sam_Resume_Larkspur.md
python3 tools/build_resume_export.py examples/fictional_candidate/Okafor_Sam_Resume_Larkspur.md
python3 tools/parse_check.py examples/fictional_candidate/Okafor_Sam_Resume_Larkspur.md
```

What the example does not show: the cover letter, the weekly sweep and a Tier 3 call. See `method/linkedin_and_cover_letters.md`, `monitoring/SWEEP_RUNBOOK.md` and `method/decisions.md` (D4, D5).
