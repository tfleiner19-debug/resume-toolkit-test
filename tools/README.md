# Tools

| Tool | Rules | Runs on | Purpose |
|---|---|---|---|
| `signal_check.py` | B1 to B7 | resume markdown | Bullet, headline and page-budget rules, before export |
| `build_resume_export.py` | P1, P2, P3 by construction | resume markdown | Parse-safe PDF and editable DOCX into `exports/` |
| `parse_check.py` | P1 to P4 | the exported PDF | Confirms name, contact, roles and dates survive text extraction in order |
| `scrub_check.py` | none | a repository copy | Leak scan before sharing: denylist, patterns, binaries |

## Setup

```
pip install -r requirements.txt
# pdftotext: macOS `brew install poppler`; Debian/Ubuntu `sudo apt-get update && sudo apt-get install -y poppler-utils`
```

## Run order for a submission

```
python3 tools/signal_check.py profile/tailored/Your_Resume_Company.md
python3 tools/build_resume_export.py profile/tailored/Your_Resume_Company.md
python3 tools/parse_check.py profile/tailored/Your_Resume_Company.md
```

## What the build enforces

- Single column, one text frame, no tables, text boxes, icons, headers or footers (P1)
- Headings as written in the markdown; keep them Summary, Experience, Skills, Education (P1)
- Selectable-text PDF, typically under 10 KB (P2)
- Role line as `Title | Employer | Location` with dates on the next line (P3)
- PDF and DOCX metadata carry only the candidate's name
- One italic line under the contact line is a provenance note and is stripped from exports

## Settings

`signal_check.py` reads `profile/tool_config.json`: bullet counts by role position (newest first), word ceilings, Summary limits and page budget. Pass `--config <file>` to use another, as the example does.

The page figure is measured on the real reportlab layout the export uses, not estimated from word count.

## Limits

- `parse_check.py` tests `pdftotext` extraction, the layer many ATS parsers build on. It is not any specific vendor. If a portal mangles a resume, check the portal's parsed preview.
- B8 (selection and ranking) cannot be checked by script. It is a manual check.
- `scrub_check.py` catches names, patterns and binaries. It cannot catch a combination of details that identifies someone without naming them. Read the files.

## Known environment quirks

- In some sandboxed containers LibreOffice is installed but cannot convert files. These tools do not use it.
- `pypdf` can fail at import where the system `cryptography` module is broken. Use `pdftotext` instead.
- `apt-get install poppler-utils` may need `apt-get update` first.
- Never hardcode a session-specific temporary path in a tool; it breaks the next session.
