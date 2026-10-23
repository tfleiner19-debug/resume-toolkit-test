"""Scrub check: scan a copy of this repository for personal data before sharing it.

    python3 tools/scrub_check.py <repo_dir> --denylist <path_outside_repo>
    python3 tools/scrub_check.py <repo_dir> --denylist <path> --include-profile

Layers:
  1. Denylist: every term in the denylist file (one per line, # for comments),
     matched case-insensitively. Keep the denylist OUTSIDE the repository: the list
     is itself personal data.
  2. Patterns: email addresses, phone numbers and LinkedIn profile URLs, except the
     reserved fictional forms (example.com/.org/.net, 555-01xx numbers,
     linkedin.com/in/example...). Dollar figures are listed as warnings for a human
     to confirm they are illustrative.
  3. Binaries: any PDF, DOCX, image, archive or compiled file fails, because document
     metadata carries names that a text scan cannot see.
  4. Git history: if the directory is a git repository, every commit author and
     committer name and email is checked against the same denylist and patterns.

profile/, BOARD.md, jds/ and exports/ are skipped unless --include-profile is given,
since they are meant to hold the owner's data. Share a copy without them.
A clean pass is necessary, not sufficient: also read every file for details that
identify someone without naming them. Exit code 1 on any failure.
"""
import os
import re
import subprocess
import sys

TEXT_EXT = {".md", ".txt", ".py", ".json", ".yml", ".yaml", ".toml", ".cfg", ".gitignore", ""}
BINARY_EXT = {".pdf", ".docx", ".doc", ".pptx", ".xlsx", ".png", ".jpg", ".jpeg", ".gif",
              ".zip", ".tar", ".gz", ".pyc", ".dotx", ".rtf", ".heic", ".webp"}
PERSONAL = {"profile", "jds", "exports"}
PERSONAL_FILES = {"BOARD.md"}
SKIP_DIRS = {".git", "__pycache__", "node_modules"}

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")
PHONE = re.compile(r"(?<!\d)(?:\+?1[ .-]?)?\(?(\d{3})\)?[ .-](\d{3})[ .-](\d{4})(?!\d)")
LINKEDIN = re.compile(r"linkedin\.com/in/([A-Za-z0-9_-]+)", re.I)
DOLLAR = re.compile(r"\$\s?\d[\d,.]*\s?(?:[KMB]|million|billion)?\b", re.I)
FICTIONAL_DOMAINS = ("example.com", "example.org", "example.net")


def load_denylist(path):
    terms = []
    for line in open(path, encoding="utf-8"):
        t = line.strip()
        if t and not t.startswith("#"):
            terms.append(t)
    return terms


def walk(root, include_profile):
    for d, dirs, files in os.walk(root):
        rel = os.path.relpath(d, root)
        top = rel.split(os.sep)[0]
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS
                   and (include_profile or rel != "." or x not in PERSONAL)]
        if not include_profile and top in PERSONAL:
            continue
        for f in files:
            if not include_profile and rel == "." and f in PERSONAL_FILES:
                continue
            yield os.path.join(d, f), os.path.join(rel, f) if rel != "." else f


def main(argv):
    if not argv or argv[0].startswith("-"):
        sys.exit(__doc__)
    root = argv[0]
    include_profile = "--include-profile" in argv
    deny = []
    if "--denylist" in argv:
        dl = os.path.abspath(argv[argv.index("--denylist") + 1])
        if os.path.commonpath([dl, os.path.abspath(root)]) == os.path.abspath(root):
            print("FAIL  the denylist is inside the repository. Move it out; it is personal data.")
            return 1
        deny = load_denylist(dl)
    else:
        print("WARN  no --denylist given: only pattern and binary layers run.")

    fails, warns, scanned = [], [], 0
    deny_res = [(t, re.compile(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", re.I)) for t in deny]
    for path, rel in walk(root, include_profile):
        ext = os.path.splitext(path)[1].lower()
        if ext in BINARY_EXT:
            fails.append(f"BINARY  {rel}: binary or document file. Ship none; metadata can carry names.")
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except UnicodeDecodeError:
            fails.append(f"BINARY  {rel}: not UTF-8 text.")
            continue
        scanned += 1
        for n, line in enumerate(text.split("\n"), 1):
            for term, rx in deny_res:
                if rx.search(line):
                    fails.append(f"DENY    {rel}:{n}: matches a denylist term")
            for m in EMAIL.finditer(line):
                if not m.group(1).lower().endswith(FICTIONAL_DOMAINS):
                    fails.append(f"EMAIL   {rel}:{n}: {m.group(0)}")
            for m in PHONE.finditer(line):
                if not (m.group(2) == "555" and m.group(3).startswith("01")):
                    fails.append(f"PHONE   {rel}:{n}: {m.group(0)}")
            for m in LINKEDIN.finditer(line):
                if not m.group(1).lower().startswith("example"):
                    fails.append(f"LINKEDIN {rel}:{n}: {m.group(0)}")
            for m in DOLLAR.finditer(line):
                warns.append(f"DOLLAR  {rel}:{n}: {m.group(0).strip()}  (confirm it is illustrative)")

    if os.path.isdir(os.path.join(root, ".git")):
        log = subprocess.run(["git", "-C", root, "log", "--all", "--format=%an <%ae> | %cn <%ce>"],
                             capture_output=True, text=True).stdout
        for line in sorted(set(log.splitlines())):
            hit = any(rx.search(line) for _, rx in deny_res)
            hit = hit or any(not m.group(1).lower().endswith(FICTIONAL_DOMAINS) for m in EMAIL.finditer(line))
            if hit:
                fails.append(f"GIT     commit identity: {line}")
        print(f"Git identities checked: {len(set(log.splitlines()))}")

    print(f"Scanned {scanned} text files under {root}"
          f"{'' if include_profile else ' (profile/, jds/, exports/, BOARD.md skipped)'}.")
    print(f"Denylist terms: {len(deny)}")
    for w in warns:
        print("WARN  " + w)
    for f in fails:
        print("FAIL  " + f)
    print("PASS  no personal data found by the automated layers." if not fails
          else f"{len(fails)} failure(s).")
    print("Next: read every file for details that identify someone without naming them.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
