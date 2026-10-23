# profile/

Your facts live here, and only here. Everything else in the repository is method.

| File | Holds |
|---|---|
| `locked_truth.md` | Every figure, title, framing rule, skill and hard gap. The source of record |
| `tracks.md` | Target directions, headline per track, current-role selection per track, search settings |
| `experience_inventory.md` | Raw results, scope, review themes, interview stories |
| `tool_config.json` | Bullet counts and page limits for `tools/signal_check.py` |
| `bases/` | One base resume per track. Tailor from these only |
| `tailored/` | Tailored resumes, one per application. Never tailor from these |

**Never push this folder to a public repository.** If you share this toolkit, share a copy without your `profile/`, and run `tools/scrub_check.py` on it first.

**Base resume format.** Copy `examples/fictional_candidate/Okafor_Sam_Resume_Base_Operations.md`. The tools rely on its shape: name on line 1, headline on line 2, contact on line 3, `## Summary`, `## Experience`, `### Title | Employer | Location` with dates on the next line as `Mon YYYY to Mon YYYY` or `Mon YYYY to Present`, then `## Skills` and `## Education`. One italic line after the contact line is a provenance note: it records the base's version and is stripped from exports.
