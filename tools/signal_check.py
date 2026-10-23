"""Signal check: Rules B1 to B7 on a resume markdown file, before export.

Companion to parse_check.py. parse_check runs Rules P1 to P4 on the built PDF;
this runs the bullet, headline and page-budget rules on the markdown source, so a
draft fails here before anyone builds or submits it.

    python3 tools/signal_check.py profile/bases/Your_Resume.md
    python3 tools/signal_check.py --config path/to/tool_config.json resume.md

Limits come from profile/tool_config.json (or --config). Exit code 1 if any rule
hard-fails. Warnings do not fail the run; they are the lines a human has to look at.
"""
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULTS = {
    "bullet_counts": [[5, 8], [3, 5], [3, 3], [1, 2]],   # B4, by role position, newest first
    "bullet_words": 30,                                   # B3 standard ceiling
    "bullet_words_allowance": 35,                         # B3 one bullet per role may reach this
    "summary_words": 60,                                  # B7
    "summary_sentences": 4,
    "summary_figures": 2,
    "mandate_words": 60,                                  # architecture: mandate states scope in 60 words or fewer
    "page_min": 1.0,
    "page_max": 1.5,
    "page_max_extended": 2.0,                             # B7: only when current role carries enough proof
    "extended_when_current_role_bullets_at_least": 7,
}


def load_config(path=None):
    cfg = dict(DEFAULTS)
    path = path or os.path.join(ROOT, "profile", "tool_config.json")
    if os.path.exists(path):
        cfg.update({k: v for k, v in json.load(open(path)).items() if not k.startswith("_")})
    return cfg

# A second sentence opening on one of these is a second achievement, not a mechanism (B1).
NEW_PROOF_VERBS = r"(Built|Launched|Rebuilt|Saved|Created|Developed|Designed|Ran|Led|Grew|Cut|Won|Shipped|Architected|Delivered|Set|Established|Introduced|Drove)"
FIGURE = r"(\$[\d.,]+[KMB]?|\b\d[\d,.]*%|\b[\d,]{3,}\b|\b\d+\+)"


def split_sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def words(text):
    return len(re.sub(r"\*\*", "", text).split())


def parse_blocks(md):
    """Return (summary, [(role, mandate, [bullets])]) from the markdown."""
    lines = open(md).read().split("\n")
    summary, roles = [], []
    section = None
    cur = None
    for raw in lines:
        s = raw.strip()
        if s.startswith("## "):
            section = s[3:].lower()
            continue
        if s.startswith("### "):
            cur = {"role": s[4:], "mandate": "", "bullets": []}
            roles.append(cur)
            continue
        if not s or s == "---" or s == "**Selected contributions:**":
            continue
        if s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            continue                                    # provenance note
        if section == "summary":
            summary.append(s)
        elif section == "experience" and cur is not None:
            if s.startswith("- "):
                cur["bullets"].append(s[2:])
            elif not re.match(r"^[A-Z][a-z]{2} \d{4} to ", s):
                cur["mandate"] += (" " + s)
    return " ".join(summary).strip(), roles


def trigrams(text):
    toks = re.findall(r"[a-z][a-z0-9/+.-]*", text.lower())
    return {" ".join(toks[i:i + 3]) for i in range(len(toks) - 2)}


def measure_pages(md):
    """Rendered page fill, using the same layout the export uses."""
    argv = sys.argv
    sys.argv = [argv[0]]
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from reportlab.lib.units import inch
        from reportlab.platypus import BaseDocTemplate
        from reportlab.pdfgen.canvas import Canvas
        spec = importlib.util.spec_from_file_location(
            "bre", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "build_resume_export.py"))
        bre = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bre)
    finally:
        sys.argv = argv

    frame_h = 11 * inch - 2 * 0.55 * inch
    frame_w = 8.5 * inch - 2 * 0.65 * inch
    sink = os.path.join(os.environ.get("TMPDIR", "/tmp"), "_signal_check_sink.pdf")

    cap = {}
    orig = BaseDocTemplate.build
    BaseDocTemplate.build = lambda self, story, *a, **k: cap.__setitem__("s", story)
    try:
        bre.build_pdf(bre.parse(md), sink)
    finally:
        BaseDocTemplate.build = orig

    cv = Canvas(sink)
    total = 0.0
    for f in cap["s"]:
        f.canv = cv
        total += f.wrap(frame_w, frame_h)[1] + f.getSpaceBefore() + f.getSpaceAfter()
    return total / frame_h


def check(md, cfg):
    WORD_CEILING, WORD_ALLOWANCE = cfg["bullet_words"], cfg["bullet_words_allowance"]
    summary, roles = parse_blocks(md)
    fails, warns = [], []
    print(f"\n===== {os.path.basename(md)} =====")

    # ---- B1 / B2 / B3 / B5, bullet by bullet ----
    for pos, r in enumerate(roles):
        label = r["role"].split(" |")[0]
        over = []
        for b in r["bullets"]:
            w, sents = words(b), split_sentences(b)
            if len(sents) > 2:
                fails.append(f"B2 {label}: {len(sents)} sentences ({w}w) - {b[:55]}...")
            if w > WORD_ALLOWANCE:
                fails.append(f"B3 {label}: {w} words, ceiling {WORD_ALLOWANCE} - {b[:55]}...")
            elif w > WORD_CEILING:
                over.append((w, b))
            if len(sents) == 2 and re.match(NEW_PROOF_VERBS + r"\b", sents[1]):
                fails.append(f"B1 {label}: second sentence is a second proof - \"{sents[1][:55]}...\"")
            body = re.split(r"\b(?:by|through|built on|using)\b", b, maxsplit=1)
            if len(body) == 2 and body[1].count(",") >= 2:
                warns.append(f"B5 {label}: mechanism runs to a list - \"...{body[1][:55]}...\"")
        if len(over) > 1:
            fails.append(f"B3 {label}: {len(over)} bullets over {WORD_CEILING}w; only one per role may reach {WORD_ALLOWANCE}")

        # ---- B4 bullet counts, from the architecture ----
        n = len(r["bullets"])
        counts = cfg["bullet_counts"]
        lo, hi = counts[min(pos, len(counts) - 1)]
        if not lo <= n <= hi:
            fails.append(f"B4 {label}: {n} bullets, expected {lo} to {hi} for role {pos + 1}")

        # ---- mandate cap, from the architecture ----
        mw = words(r["mandate"])
        if mw > cfg["mandate_words"]:
            fails.append(f"Mandate {label}: {mw} words, ceiling {cfg['mandate_words']}")

        # ---- B6 mandate machinery must not reappear in the bullets ----
        if r["mandate"]:
            shared = trigrams(r["mandate"]) & trigrams(" ".join(r["bullets"]))
            for s in sorted(shared):
                warns.append(f"B6 {label}: \"{s}\" appears in both the mandate and a bullet")

        avg = sum(words(b) for b in r["bullets"]) / max(len(r["bullets"]), 1)
        print(f"  {label[:18]:18s} mandate={words(r['mandate']):2d}w bullets={n} avg={avg:5.1f}w max={max((words(b) for b in r['bullets']), default=0):3d}w")

    # ---- B7 summary and page budget ----
    top_n = len(roles[0]["bullets"]) if roles else 0
    page_max = (cfg["page_max_extended"]
                if top_n >= cfg["extended_when_current_role_bullets_at_least"] else cfg["page_max"])
    PAGE_MIN = cfg["page_min"]
    sw, ss = words(summary), len(split_sentences(summary))
    sf = len(re.findall(FIGURE, summary))
    print(f"  {'Summary':18s} {sw}w / {ss} sentences / {sf} figures")
    if sw > cfg["summary_words"]:
        fails.append(f"B7 Summary: {sw} words, ceiling {cfg['summary_words']}")
    if ss > cfg["summary_sentences"]:
        fails.append(f"B7 Summary: {ss} sentences, ceiling {cfg['summary_sentences']}")
    if sf > cfg["summary_figures"]:
        fails.append(f"B7 Summary: {sf} figures, ceiling {cfg['summary_figures']}")

    pages = measure_pages(md)
    print(f"  {'Page budget':18s} {pages:.2f} pages (target {PAGE_MIN} to {page_max})")
    if pages > page_max:
        fails.append(f"B7 Page budget: {pages:.2f} pages, ceiling {page_max}")
    if pages < PAGE_MIN:
        fails.append(f"B7 Page budget: {pages:.2f} pages, floor {PAGE_MIN}")

    for w in warns:
        print(f"  WARN  {w}")
    for f in fails:
        print(f"  FAIL  {f}")
    if not fails:
        print("  PASS  B1 to B7")
    return not fails


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = sys.argv[1:]
    cfg_path = None
    if "--config" in args:
        i = args.index("--config"); cfg_path = args[i + 1]; del args[i:i + 2]
    cfg = load_config(cfg_path)
    ok = all([check(md, cfg) for md in args])
    sys.exit(0 if ok else 1)
