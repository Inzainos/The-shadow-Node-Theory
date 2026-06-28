"""
Minimal Markdown -> PDF renderer (reportlab) for SNT documents.
Handles: # ## ### headings, paragraphs, **bold**, *italic*, `code`,
bullet lists (-), and simple pipe tables. Not a full Markdown engine —
just enough for our papers.

Usage: python md_to_pdf.py input.md output.pdf "Title"
"""
import sys
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable)
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Title"], fontSize=15, leading=19, spaceAfter=6)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontSize=12.5, spaceBefore=12,
                    spaceAfter=5, textColor=colors.HexColor("#1a1a1a"))
H3 = ParagraphStyle("H3", parent=ss["Heading3"], fontSize=10.5, spaceBefore=8,
                    spaceAfter=3, textColor=colors.HexColor("#333333"))
BODY = ParagraphStyle("BODY", parent=ss["Normal"], fontSize=9.7, leading=14,
                      alignment=TA_JUSTIFY, spaceAfter=7)
BULLET = ParagraphStyle("BULLET", parent=BODY, leftIndent=14, spaceAfter=3)
SMALL = ParagraphStyle("SMALL", parent=ss["Normal"], fontSize=8.3, leading=11.5,
                       textColor=colors.HexColor("#555555"))
CENTER = ParagraphStyle("CENTER", parent=ss["Normal"], fontSize=9.5,
                        alignment=TA_CENTER, textColor=colors.HexColor("#555555"),
                        spaceAfter=2, leading=13)


def inline(t):
    # 1) protect inline code spans first
    codes = []

    def _stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes)-1}\x00"
    t = re.sub(r"`([^`]+?)`", _stash, t)
    # 2) escape
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # 3) bold then italic (italic must hug non-space, not be part of a glob)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])", r"<i>\1</i>", t)
    # 4) restore code spans
    for i, c in enumerate(codes):
        c = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        t = t.replace(f"\x00{i}\x00", f'<font face="Courier">{c}</font>')
    return t


def build(md_path, out_path, title):
    lines = open(md_path, encoding="utf-8").read().splitlines()
    doc = SimpleDocTemplate(out_path, pagesize=letter, topMargin=0.8*inch,
                            bottomMargin=0.8*inch, leftMargin=0.95*inch,
                            rightMargin=0.95*inch, title=title)
    E = []
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1; continue
        if ln.startswith("# "):
            E.append(Paragraph(inline(ln[2:]), H1))
        elif ln.startswith("## "):
            E.append(Paragraph(inline(ln[3:]), H2))
        elif ln.startswith("### "):
            E.append(Paragraph(inline(ln[4:]), H3))
        elif ln.strip() == "---":
            E.append(HRFlowable(width="100%", thickness=0.6,
                                color=colors.HexColor("#cccccc"),
                                spaceBefore=4, spaceAfter=6))
        elif ln.lstrip().startswith(("- ", "* ")):
            txt = ln.lstrip()[2:]
            E.append(Paragraph("&bull;&nbsp;&nbsp;" + inline(txt), BULLET))
        elif ln.startswith("|"):
            # collect table block
            tbl = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in row):  # skip separator
                    tbl.append(row)
                i += 1
            data = [[Paragraph(inline(c), SMALL) for c in r] for r in tbl]
            if data:
                t = Table(data, hAlign="LEFT")
                t.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a1a")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1),
                     [colors.white, colors.HexColor("#f2f2f2")]),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cccccc")),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ]))
                E.append(t); E.append(Spacer(1, 6))
            continue
        elif ln.startswith("> "):
            E.append(Paragraph(inline(ln[2:]),
                               ParagraphStyle("Q", parent=BODY, leftIndent=12,
                                              textColor=colors.HexColor("#444444"),
                                              fontName="Helvetica-Oblique")))
        elif ln.startswith("*") and ln.endswith("*") and len(ln) > 2:
            E.append(Paragraph(inline(ln), CENTER))
        else:
            E.append(Paragraph(inline(ln), BODY))
        i += 1
    doc.build(E)
    print("PDF written:", out_path)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2],
          sys.argv[3] if len(sys.argv) > 3 else "SNT")
