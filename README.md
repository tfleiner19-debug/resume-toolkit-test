# Resume Toolkit

## 1. What this is

This is a rule-based system for building base resumes, tailoring them to job descriptions (JDs) and running a job search, with Claude doing the drafting and the checks. It started as one person's senior-level search. Every rule here was written to fix a real failure, and `method/decisions.md` records what each failure was.

The core idea: **facts come from you, wording comes from Claude, and every claim passes a check before it reaches a recruiter.** Most resume tools generate bullets from the job posting and score you on keyword match. This one forbids generated accomplishments, caps keyword repetition, and decides whether a posting is worth tailoring for before any work starts. `method/why_this_method.md` compares it honestly with the common approaches, including where it is weaker.

## 2. What's in here

| Path | What it holds | Do you edit it? |
|---|---|---|
| `CLAUDE.md` | The operating spec Claude follows every session: the Sequence, review loop, definition of good, rule index | Rarely. Only to change a rule |
| `profile/` | Your facts: locked figures, titles, tracks, experience inventory, tool settings, base resumes | **Yes. This is your folder** |
| `BOARD.md` | Application and tailoring tracker, one row per posting | Yes, or let Claude update it |
| `method/` | Long-form rules with rationale, evidence, career-stage model, target-company framework, decision log | No. Read it to understand why |
| `monitoring/` | Optional weekly job sweep: runbook and feed lists | Only if you use the sweep |
| `tools/` | Export to PDF and DOCX, bullet checks, parse checks, leak scan | No |
| `examples/fictional_candidate/` | A complete worked example on an invented person: profile, base, JD, read, tailored draft | No. Copy its patterns |
| `.claude/skills/` | Shortcuts for Claude Code: onboard, JD read, tailor, weekly sweep | No |

## 3. How it works

1. **Profile.** You answer the onboarding questions. Claude writes your answers into `profile/` and marks gaps as `[open]`.
2. **Tracks and bases.** You pick up to three target directions. Claude builds one base resume per track from your locked facts.
3. **JD read.** For each posting, Claude names what the seat actually does, reads it against your profile and makes a tier call: tailor (Tier 1), send the base with light tuning (Tier 2) or skip with a named reason (Tier 3).
4. **Tailor.** Tier 1 only. Bullet swaps and reframes from your facts, never new claims.
5. **Review and check.** Claude reviews its own draft as a skeptical recruiter, escalates anything you might not defend in an interview, then runs the three tools.
6. **Apply and log.** You submit. The posting's row in `BOARD.md` records the tier, the files and the next step.
7. **Referrals in parallel.** At senior levels a referral gets the resume read; the resume does not get you the referral. `method/target_company_framework.md` section 9 covers where referral time goes.

## 4. Start here

1. Open Claude in this folder and ask: **"What's in here?"** Claude summarizes the repo and reports what is set up.
2. Answer the onboarding questions below. Skip any of them. You can come back later.
3. Ask Claude to build your first base resume.
4. Paste in a JD and ask for a read.

**Claude Code** reads `CLAUDE.md` automatically. The skills in `.claude/skills/` give you `/onboard`, `/jd-read`, `/tailor-resume` and `/weekly-sweep`.

**claude.ai Project instead:** paste `CLAUDE.md` into the project instructions, then upload `method/`, `profile/`, `BOARD.md` and the example folder as project files. The tools need Python, so in a Project, Claude runs them only where code execution is available.

## 5. Onboarding questions (all optional)

Answer in any order, in your own words. Rough answers are fine: Claude asks follow-ups and shows you what it wrote. Each question names the file it fills.

**Where you are**
1. What is your current title, type of employer and industry, and how many years have you worked in your field? → `locked_truth.md` (titles)
2. What is every role you've held, with official title, employer and dates? Does any title not match what you actually did? → `locked_truth.md` (titles), `tool_config.json`
3. What do you run today: budget or revenue, team size, users or customers, and who you report to? → `locked_truth.md` (figures)

**Where you want to go**
4. Which roles are you targeting next? Name up to three directions, such as a bigger version of your current job, the same job in a new industry, or a change of function. → `tracks.md`
5. Which nearby roles would you consider if a posting opened one? → `tracks.md`
6. What are your rules on location and work mode: remote, hybrid, on-site, relocation? → `tracks.md`, sweep settings
7. What are your pay floor and target? This is optional and never goes on a resume. → `tracks.md`

**Your proof**
8. What are your five to ten strongest results? For each, give the number, what you personally did and how it happened. → `experience_inventory.md`
9. Which of those numbers could you defend in an interview without notes, and which are estimates? → `locked_truth.md` (locked vs. verify)
10. Which tools and methods could you explain in two minutes if asked "how did you use it"? → `locked_truth.md` (skills)
11. What gaps keep showing up in postings you want, such as a degree, certification, industry or technical skill? → `locked_truth.md` (hard gaps)

**Limits**
12. What must stay confidential: client names, employer figures, anything under an agreement? → `locked_truth.md` (framing rules)
13. Are any companies off-limits, such as your current employer's clients or competitors? → `tracks.md`
14. How do you explain why you're moving now? → `locked_truth.md` (framing rules)

**How you work**
15. What has happened in your search so far: applications sent, callbacks, feedback? → `BOARD.md` (backfill rows)
16. Can you paste in a current resume and LinkedIn profile? → source material for the bases. Claude never tailors from them directly
17. How do you want to sound? Name phrases you like and phrases you never want to see. → `locked_truth.md` (voice)
18. Do you want a weekly job sweep? Do you use Claude Code or a claude.ai Project? → decides whether the sweep gets set up

**Answer question 9 first if you answer only one.** Separating locked numbers from estimates keeps a stretch claim off your resume, and a stretch claim found in an interview costs more than a missing one.

## 6. Setup

```
pip install -r requirements.txt
# pdftotext, for the parse check:
#   macOS:  brew install poppler
#   Debian/Ubuntu:  sudo apt-get update && sudo apt-get install -y poppler-utils
```

Run order for any resume you plan to submit:

```
python3 tools/signal_check.py profile/bases/Your_Resume.md    # B1 to B7, on the markdown
python3 tools/build_resume_export.py profile/bases/Your_Resume.md   # PDF and DOCX into exports/
python3 tools/parse_check.py profile/bases/Your_Resume.md     # P1 to P4, on the PDF
```

Try them on the example first: `examples/fictional_candidate/Okafor_Sam_Resume_Base_Operations.md`.

## 7. Privacy

`profile/`, `BOARD.md`, `exports/` and `jds/` hold your personal data. Keep this repository private. Before you share a copy with anyone, run:

```
python3 tools/scrub_check.py . --denylist ~/my_denylist.txt
```

Keep the denylist file (your name, employers, clients, figures) **outside** the repository, because the list is itself personal data. Deleting a file from git does not remove it from history: if something leaks into a commit, start a fresh repository.
