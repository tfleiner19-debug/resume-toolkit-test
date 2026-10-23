# Application Board

One row per posting, newest first. Claude adds or updates a row at the end of every JD read and every tailoring run, so the board never depends on anyone's memory.

## Rules

- **Every read gets a row, whatever the tier.** A Tier 3 row names its screen-out mechanism in the Tier column.
- **Closed rows stay**, with the reason in Notes. When a search goes quiet, the closed rows are the evidence. Without them you can only guess whether the problem is the resume, the targeting or the channel.
- **Source says how you found it:** `feed` (an employer board feed returned it, so it was open), `referral`, `recruiter`, `search` (unverified until you open it yourself) or `network`.
- **Outcome columns make the method testable.** Fill in Response and Response date when anything comes back, including a rejection. After 15 to 20 applications, ask Claude to compare response rates by tier, track and source. That is the only real evidence of whether the rules work for you.
- `monitoring/seen_postings.json` is the weekly sweep's de-duplication list. The board is the human record. Claude keeps the two consistent and never reports a posting the board marks closed.
- Status values: `found`, `screened`, `tailoring`, `applied`, `recruiter screen`, `interview`, `offer`, `closed`, `withdrawn`.

## Board

| Date | Company | Role | Source | Tier (reason) | Track | Files | Status | Applied | Response | Response date | Next (date) | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-05 | *Example: Larkspur Outdoor (fictional)* | Senior Director, Fulfillment Operations | feed | 1 (core seat is network operations, a direct match) | Operations | `examples/fictional_candidate/jds/Larkspur_SrDir_Fulfillment.md`, `..._Read.md`, `examples/fictional_candidate/Okafor_Sam_Resume_Larkspur.md` | applied | 2026-01-07 | | | Follow up with recruiter (2026-01-21) | Delete this row when you add your first real one |

## Summary (Claude refreshes on request)

| Measure | Value |
|---|---|
| Applications sent | 0 |
| Responses (any) | 0 |
| Response rate, Tier 1 | n/a |
| Response rate, Tier 2 | n/a |
| Response rate by source | n/a |
