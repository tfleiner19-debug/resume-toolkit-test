"""Parse check: Rules P1 to P4 on the exported PDF of a resume.

Reads the expected name, contact line, role lines and dates from the markdown
source, then confirms they survive pdftotext extraction intact and in order.
Nothing about the candidate is hardcoded.

    python3 tools/parse_check.py profile/bases/Your_Resume.md [more.md ...]

Looks for the PDF in exports/ (or $RESUME_EXPORT_DIR) under the same base name.
Exit code 1 if any check fails. Needs pdftotext (poppler-utils).
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get("RESUME_EXPORT_DIR", os.path.join(ROOT, "exports"))
HEADS = ["SUMMARY", "EXPERIENCE", "SKILLS", "EDUCATION"]
DATE_LINE = re.compile(r"^[A-Z][a-z]{2} \d{4} to ([A-Z][a-z]{2} \d{4}|Present)$")


def expected(md):
    lines = [l.rstrip() for l in open(md).read().split("\n")]
    name = lines[0].lstrip("# ").strip()
    contact = lines[2].strip()
    roles, dates = [], []
    for i, l in enumerate(lines):
        if l.startswith("### "):
            roles.append(l[4:].strip())
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            dates.append(lines[j].strip() if j < len(lines) else "")
    return name, contact, roles, dates


def in_order(flat, items):
    pos, last = [], -1
    for it in items:
        p = flat.find(it, last + 1)
        pos.append(p)
        if p >= 0:
            last = p
    return all(p >= 0 for p in pos) and pos == sorted(pos), pos


def check(md):
    base = os.path.basename(md)[:-3]
    pdf = os.path.join(OUT, base + ".pdf")
    print(f"\n===== {base}.pdf =====")
    if not os.path.exists(pdf):
        print(f"  FAIL  no PDF at {pdf}. Run tools/build_resume_export.py first.")
        return False
    txt = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
    flat = " ".join(txt.split())
    name, contact, roles, dates = expected(md)
    results = []

    ok, pos = in_order(flat, HEADS)
    results.append(("P1 headings present and in order", ok, "" if ok else str(list(zip(HEADS, pos)))))

    contact_parts = [p.strip() for p in contact.split("|") if p.strip()]
    ok = name.upper() in flat.upper() and all(p in flat for p in contact_parts)
    results.append(("P2 name and contact intact", ok, ""))
    ok, pos = in_order(flat, roles)
    results.append((f"P2 all {len(roles)} role lines, in order", ok, "" if ok else str(pos)))
    ok, pos = in_order(flat, dates)
    results.append((f"P2 all {len(dates)} date lines, in order", ok, "" if ok else str(pos)))
    size_kb = os.path.getsize(pdf) / 1024
    results.append((f"P2 size under 2.5 MB ({size_kb:.0f} KB)", size_kb < 2560, ""))

    results.append(("P3 no em dashes", "—" not in txt, ""))
    bad_dates = [d for d in dates if not DATE_LINE.match(d)]
    results.append(("P3 date lines use 'Mon YYYY to Mon YYYY|Present'", not bad_dates, ", ".join(bad_dates)))
    lines = [l.strip() for l in txt.split("\n")]
    ok = all(any(l == d for l in lines) for d in dates)
    results.append(("P3 dates on their own line", ok, ""))

    rp = [flat.find(r) for r in roles]
    p4 = True
    for i, r0 in enumerate(rp):
        end = rp[i + 1] if i + 1 < len(rp) else flat.find("SKILLS")
        if r0 < 0 or "•" not in flat[r0:end]:
            p4 = False
    results.append(("P4 every role keeps its bullets", p4, ""))

    for label, ok, detail in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}{'  ' + detail if detail else ''}")
    return all(ok for _, ok, _ in results)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(0 if all([check(md) for md in sys.argv[1:]]) else 1)
