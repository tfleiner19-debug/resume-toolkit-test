"""Build a parse-safe PDF and an editable DOCX from one resume markdown file.

    python3 tools/build_resume_export.py profile/bases/Your_Resume.md

Output goes to exports/ at the repository root, or to $RESUME_EXPORT_DIR if set.
Both formats come from the same markdown, so they cannot drift apart.
"""
import re, os, sys
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, ListFlowable, ListItem, HRFlowable)
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get("RESUME_EXPORT_DIR", os.path.join(ROOT, "exports"))

def parse(md_path):
    """Return a flat block list: (kind, text). Provenance note is dropped."""
    lines = open(md_path).read().split("\n")
    doc = {"name": lines[0].lstrip("# ").strip(),
           "headline": lines[1].strip().strip("*"),
           "contact": lines[2].strip(),
           "blocks": []}
    i = 3
    while i < len(lines):
        s = lines[i].strip()
        if not s or s == "---":
            i += 1; continue
        if s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            i += 1; continue                                  # provenance note
        if s.startswith("## "):
            doc["blocks"].append(("h2", s[3:])); i += 1; continue
        if s.startswith("### "):
            j = i + 1
            while j < len(lines) and not lines[j].strip(): j += 1
            doc["blocks"].append(("role", s[4:]))
            doc["blocks"].append(("dates", lines[j].strip()))
            i = j + 1; continue
        if s == "**Selected contributions:**":
            doc["blocks"].append(("label", "Selected contributions:")); i += 1; continue
        if s.startswith("- "):
            doc["blocks"].append(("bullet", s[2:])); i += 1; continue
        doc["blocks"].append(("skill" if s.startswith("**") else "para", s))
        i += 1
    return doc

# ---------------- PDF ----------------
def bold_md(t):
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)

def build_pdf(doc, out):
    F = "Helvetica"; FB = "Helvetica-Bold"; FI = "Helvetica-Oblique"
    S = {
     "name":  ParagraphStyle("name", fontName=FB, fontSize=18, leading=21, spaceAfter=2),
     "head":  ParagraphStyle("head", fontName=FB, fontSize=10.5, leading=13, spaceAfter=2),
     "cont":  ParagraphStyle("cont", fontName=F, fontSize=9, leading=11.5, spaceAfter=9),
     "h2":    ParagraphStyle("h2", fontName=FB, fontSize=10.5, leading=13,
                             spaceBefore=10, spaceAfter=3),
     "role":  ParagraphStyle("role", fontName=FB, fontSize=10, leading=12.5, spaceBefore=7),
     "dates": ParagraphStyle("dates", fontName=FI, fontSize=9, leading=11, spaceAfter=3),
     "label": ParagraphStyle("label", fontName=FB, fontSize=9.5, leading=12,
                             spaceBefore=3, spaceAfter=2),
     "para":  ParagraphStyle("para", fontName=F, fontSize=9.5, leading=12.3, spaceAfter=3),
     "bul":   ParagraphStyle("bul", fontName=F, fontSize=9.5, leading=12.3, spaceAfter=3),
    }
    pdf = BaseDocTemplate(out, pagesize=LETTER,
                          leftMargin=0.65*inch, rightMargin=0.65*inch,
                          topMargin=0.55*inch, bottomMargin=0.55*inch,
                          title=doc["name"], author=doc["name"])
    frame = Frame(pdf.leftMargin, pdf.bottomMargin, pdf.width, pdf.height, id="col")
    pdf.addPageTemplates([PageTemplate(id="single", frames=[frame])])   # P1: one column

    story = [Paragraph(doc["name"], S["name"]),
             Paragraph(doc["headline"], S["head"]),
             Paragraph(doc["contact"], S["cont"])]
    pending = []
    def flush():
        if pending:
            story.append(ListFlowable([ListItem(Paragraph(bold_md(b), S["bul"]), leftIndent=13)
                                       for b in pending],
                                      bulletType="bullet", bulletFontSize=7,
                                      leftIndent=13, bulletOffsetY=-1))
            pending.clear()
    for kind, text in doc["blocks"]:
        if kind == "bullet":
            pending.append(text); continue
        flush()
        if kind == "h2":
            story.append(Paragraph(text.upper(), S["h2"]))
            story.append(HRFlowable(width="100%", thickness=0.6, color="#000000",
                                    spaceBefore=0, spaceAfter=4))
        elif kind == "role":  story.append(Paragraph(text, S["role"]))
        elif kind == "dates": story.append(Paragraph(text, S["dates"]))
        elif kind == "label": story.append(Paragraph(text, S["label"]))
        else:                 story.append(Paragraph(bold_md(text), S["para"]))
    flush()
    pdf.build(story)

# ---------------- DOCX ----------------
def add_runs(p, text, size=9.5):
    for k, part in enumerate(re.split(r'\*\*(.+?)\*\*', text)):
        if not part: continue
        r = p.add_run(part); r.bold = (k % 2 == 1)
        r.font.size = Pt(size); r.font.name = "Arial"

def build_docx(doc, out):
    d = docx.Document()
    sec = d.sections[0]
    sec.top_margin = sec.bottom_margin = Inches(0.55)
    sec.left_margin = sec.right_margin = Inches(0.65)
    st = d.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(9.5)
    st.paragraph_format.space_after = Pt(3); st.paragraph_format.line_spacing = 1.08

    p = d.add_paragraph(); r = p.add_run(doc["name"]); r.bold = True; r.font.size = Pt(18)
    p = d.add_paragraph(); r = p.add_run(doc["headline"]); r.bold = True; r.font.size = Pt(10.5)
    p = d.add_paragraph(); r = p.add_run(doc["contact"]); r.font.size = Pt(9)
    p.paragraph_format.space_after = Pt(9)

    for kind, text in doc["blocks"]:
        if kind == "h2":
            p = d.add_paragraph(); p.paragraph_format.space_before = Pt(10)
            r = p.add_run(text.upper()); r.bold = True; r.font.size = Pt(10.5)
            pb = p.paragraph_format
            from docx.oxml.ns import qn
            from docx.oxml import OxmlElement
            pPr = p._p.get_or_add_pPr(); bdr = OxmlElement("w:pBdr")
            bot = OxmlElement("w:bottom")
            for k, v in (("w:val","single"),("w:sz","6"),("w:space","1"),("w:color","000000")):
                bot.set(qn(k), v)
            bdr.append(bot); pPr.append(bdr)
        elif kind == "role":
            p = d.add_paragraph(); p.paragraph_format.space_before = Pt(7)
            r = p.add_run(text); r.bold = True; r.font.size = Pt(10)
        elif kind == "dates":
            p = d.add_paragraph(); r = p.add_run(text); r.italic = True; r.font.size = Pt(9)
        elif kind == "label":
            p = d.add_paragraph(); r = p.add_run(text); r.bold = True; r.font.size = Pt(9.5)
        elif kind == "bullet":
            p = d.add_paragraph(style="List Bullet"); add_runs(p, text)
        else:
            p = d.add_paragraph(); add_runs(p, text)
    cp = d.core_properties
    cp.author = doc["name"]; cp.title = doc["name"]
    cp.comments = ""; cp.last_modified_by = ""
    d.save(out)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    os.makedirs(OUT, exist_ok=True)
    for md in sys.argv[1:]:
        doc = parse(md)
        base = os.path.basename(md).replace(".md", "")
        build_pdf(doc, os.path.join(OUT, base + ".pdf"))
        build_docx(doc, os.path.join(OUT, base + ".docx"))
        print("built:", os.path.join(OUT, base))
