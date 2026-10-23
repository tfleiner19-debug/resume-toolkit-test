# Weekly Opening Sweep: Runbook

Optional. This file is the whole procedure, so a session with no memory of past runs can run the sweep from it alone. It needs Claude with web search and web fetch; a schedule needs Claude Code routines or a similar scheduler.

Framework: `../method/target_company_framework.md`. Vocabulary and settings: `../profile/tracks.md`.

---

## Read this first

**Only an authoritative board feed may source a reported job.** Never report a posting found by web search as open.

Why: a Greenhouse, Lever or Workable job page keeps serving its full description after the requisition closes, and shows the "closed" banner only in the browser. A fetch therefore looks live when it is not, and search indexes lag the boards by weeks. The first live run of this sweep reported four leads from search results, and all four were closed. Board feeds return open requisitions only, so liveness is free and false positives are zero.

---

## Settings (fill in before the first run)

- **Cadence:** [open] *(weekly, Monday morning, is the tested default)*
- **Level floor:** [open] *(Example: Director and above; Senior Manager counts only at companies over about 10,000 people, where the title often carries Director scope)*
- **Geography:** [open] *(Example: remote, plus on-site and hybrid within one region)*
- **Output:** one report per run, in one place
- **Pre-screen:** every surviving hit gets the three pre-screen questions and a tier call

---

## Step 1: Channel B, feed polling. The only source of reported jobs.

Read `board_tokens.json` and fetch one feed per company:

| ATS | Endpoint |
|---|---|
| Greenhouse | `https://boards-api.greenhouse.io/v1/boards/<token>/jobs` |
| Lever | `https://api.lever.co/v0/postings/<token>?mode=json` |
| Workable | `https://apply.workable.com/api/v1/widget/accounts/<token>?details=true` |

Keep every title that carries a search-vocabulary term at the level floor. Everything a feed returns is open.

**Board tokens are often not the company name.** Confirm a token by fetching its feed before storing it.

**Large feeds get cut off, silently.** A fetch tool may stop at a fixed character limit. Lever `mode=json` carries full descriptions and can stop after a handful of postings; big Greenhouse boards stop partway. A cut-off feed hides open roles and makes open roles look closed. So:

- **Lever:** read the board index `https://jobs.lever.co/<token>` instead; it is compact. For very large boards, filter by department: `?department=<name>`.
- **Greenhouse, large boards:** read `https://job-boards.greenhouse.io/<token>?keyword=<term>`, then `&page=2` and on while a page is full.
- If the fetch result says it was cut, call again with the offset it gives.
- **Never mark a posting closed because a feed did not show it.** Confirm with its own posting API (`.../jobs/<id>` on Greenhouse, `.../postings/<token>/<id>` on Lever). An API error alone is not proof either. Call a posting closed only when its API errors **and** it is absent from a complete read of its board.
- List known large boards under `large_boards` in `board_tokens.json`.

**SmartRecruiters and Ashby** have no reachable feed. Report their roles only as unverified leads.

## Step 2: Channel A, vocabulary sweep. Company discovery only.

Run web searches restricted to job-board domains:

```
job-boards.greenhouse.io
boards.greenhouse.io
jobs.lever.co
jobs.smartrecruiters.com
apply.workable.com
```

Build five to seven queries from the narrow vocabulary in `profile/tracks.md`, each pairing a level word with two or three function terms joined by OR. Never add a term from the do-not-search list.

**What to do with a hit:** it proves the company has the function, budgets it at that level, and turns the seat over. It is not a job. Harvest the board token into `board_tokens.json`, add the company to your target list, and let the seat surface through Channel B when it is open. Never report the posting from this channel.

## Step 2c: Channel C, Workday sweep. Unverified leads only.

Workday job pages are indexed by search even though Workday boards cannot be polled. Search with the domain restricted to `myworkdayjobs.com`, two or three queries. Nothing here can be confirmed open: report these hits in their own table, labeled unverified, for the candidate to open and confirm.

## Step 3: Three-stage funnel

**Stage 1, cheap filter, from title, company, URL and snippet alone.** No fetch. Drop on:
- Wrong country. Function vocabulary is global; a Workday URL usually carries a location slug and feed entries carry a location field.
- Below the level floor.
- Wrong geography inside the country.
- No vocabulary term in the title. A match only in the body is the false positive this system exists to remove.
Flag, rather than drop, a title carrying both a target term and a banned one. The body decides those.

**Stage 2, quick read.** Fetch the description and answer the pre-screen: what the seat does most of the time, who it reports to, and whether it does the candidate's kind of work. Check the stated minimums against the hard gaps in `locked_truth.md`. Workday pages vary by employer: always attempt the fetch; only the ones that come back empty go to the candidate unread.

**Stage 3, deep read.** The full Sequence, one JD at a time, for Stage 2 survivors only.

## Step 4: Diff

Compare against `seen_postings.json`. Report only what is new. Write every new item back after reporting, whatever its tier, so it never resurfaces. Add Tier 1 and Tier 2 survivors to `BOARD.md` with status `screened`.

## Step 5: Report

**Two tables that never merge.**

Table one, confirmed open (feed-verified only), ranked:

| # | Role / Company | Location | Pay band | Link |

Table two, unverified leads (Channel C and no-feed boards), unranked, labeled with the reason they are unverified:

| Role / Company | Location | Pay band | Link |

- **State the ranking basis in one line, every run**, even when it has not changed. The candidate can only argue with a basis they can see.
- **Write "not published" or "not readable"** in an empty pay band or location cell. They are different facts, and a blank hides which one applies.
- Below the tables: one short note per ranked row, saying what it is and the one thing that would sink it. Then filtered items as one line each, so the candidate can correct the filter.
- **Never end a sweep silently.** If nothing new cleared, say so in one short report, and name the roles still open and anything that closed.

---

## Known coverage gaps

- LinkedIn, Ashby, SmartRecruiters feeds, Indeed and ZipRecruiter cannot be read.
- Workday boards cannot be polled, so liveness is never confirmable there. Most large corporates run Workday.
- Direct network access from a sandboxed environment (scripts, headless browsers) may be blocked by egress policy. In the original setup, both were tested and both failed. Use the web search and fetch tools.
- Channel B only sees companies in `board_tokens.json`. Coverage grows as Channel A harvests tokens.
- The sweep is strong exactly where LinkedIn is weak (startups and mid-size companies), and the reverse. The manual half never goes away.
