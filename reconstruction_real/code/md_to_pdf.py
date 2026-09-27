"""
Minimal Markdown -> PDF renderer (reportlab) for SNT documents.
Handles: # ## ### headings, paragraphs, **bold**, *italic*, `code`,
bullet lists (-), > quotes, and simple pipe tables. Not a full Markdown
engine — just enough for our papers.

Markdown semantics that matter for the manuscripts:
    * consecutive non-blank lines form ONE paragraph (hard-wrapped source
      text is re-flowed), so **bold** / *italic* spans may cross line breaks;
    * a line ending in two spaces (or a backslash) is a hard line break
      inside its paragraph (used by the author/header block);
    * consecutive "> " lines form one quoted paragraph (a bare ">" line
      separates quoted paragraphs);
    * text is set in DejaVu Sans when available, which covers the Greek
      letters, superscripts (10⁻⁹⁷), ≈, ≥, ⊥ and combining marks (b̄) used
      in the papers. The reportlab base-14 Helvetica has none of these
      glyphs (they rendered as "r", "10nnn", "»" in the v30 PDFs).

Usage: python md_to_pdf.py input.md output.pdf "Title"
Log:   reconstruction_real/logs/md_to_pdf_log.txt
"""
import logging
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (HRFlowable, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

ROOT = Path(__file__).resolve().parent.parent.parent
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "md_to_pdf_log.txt"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("MD2PDF")


def _font_dirs():
    """Candidate folders holding DejaVu TTFs (system first, then matplotlib)."""
    dirs = [Path("/usr/share/fonts/truetype/dejavu"),
            Path("/usr/share/fonts/dejavu"),
            Path("/Library/Fonts"),
            Path("C:/Windows/Fonts")]
    try:
        import matplotlib
        dirs.append(Path(matplotlib.get_data_path()) / "fonts" / "ttf")
    except Exception:  # matplotlib is optional here
        pass
    return dirs


def _find_face(fname):
    """First candidate folder that holds `fname`, or None."""
    for d in _font_dirs():
        if (d / fname).exists():
            return d / fname
    return None


def register_fonts():
    """Register DejaVu Sans (+ Mono) with bold/italic mapping.

    Each face is searched independently (some systems ship DejaVuSans and
    -Bold but not the Oblique faces; matplotlib bundles all of them). A
    missing italic face falls back to the upright one of the same weight.
    Returns (regular, bold, italic, bold_italic, mono) font names; falls back
    to the base-14 Helvetica/Courier (no Greek/superscript glyphs) with a
    warning if DejaVu Sans itself is not found.
    """
    faces = {"DejaVuSans": "DejaVuSans.ttf",
             "DejaVuSans-Bold": "DejaVuSans-Bold.ttf",
             "DejaVuSans-Oblique": "DejaVuSans-Oblique.ttf",
             "DejaVuSans-BoldOblique": "DejaVuSans-BoldOblique.ttf",
             "DejaVuSansMono": "DejaVuSansMono.ttf"}
    found = {name: _find_face(f) for name, f in faces.items()}
    if found["DejaVuSans"] is None:
        log.warning("DejaVu Sans no encontrada: se usa Helvetica (sin griego, "
                    "superíndices ni ≈; esos glifos saldrán mal)")
        return ("Helvetica", "Helvetica-Bold", "Helvetica-Oblique",
                "Helvetica-BoldOblique", "Courier")
    fallback = {"DejaVuSans-Bold": "DejaVuSans",
                "DejaVuSans-Oblique": "DejaVuSans",
                "DejaVuSans-BoldOblique": "DejaVuSans-Bold",
                "DejaVuSansMono": None}
    names = {}
    for name in faces:
        if found[name] is not None:
            pdfmetrics.registerFont(TTFont(name, str(found[name])))
            names[name] = name
            log.info("Fuente %-24s <- %s", name, found[name])
        else:
            alt = fallback[name]
            names[name] = names.get(alt, "Courier") if alt else "Courier"
            log.warning("Fuente %-24s no encontrada: se usa %s", name,
                        names[name])
    pdfmetrics.registerFontFamily("DejaVuSans", normal="DejaVuSans",
                                  bold=names["DejaVuSans-Bold"],
                                  italic=names["DejaVuSans-Oblique"],
                                  boldItalic=names["DejaVuSans-BoldOblique"])
    return (names["DejaVuSans"], names["DejaVuSans-Bold"],
            names["DejaVuSans-Oblique"], names["DejaVuSans-BoldOblique"],
            names["DejaVuSansMono"])


FONT, FONT_B, FONT_I, FONT_BI, FONT_MONO = register_fonts()

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Title"], fontName=FONT_B, fontSize=15,
                    leading=19, spaceAfter=6)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName=FONT_B,
                    fontSize=12.5, spaceBefore=12, spaceAfter=5,
                    textColor=colors.HexColor("#1a1a1a"))
H3 = ParagraphStyle("H3", parent=ss["Heading3"], fontName=FONT_B,
                    fontSize=10.5, spaceBefore=8, spaceAfter=3,
                    textColor=colors.HexColor("#333333"))
BODY = ParagraphStyle("BODY", parent=ss["Normal"], fontName=FONT,
                      fontSize=9.7, leading=14, alignment=TA_JUSTIFY,
                      spaceAfter=7)
BULLET = ParagraphStyle("BULLET", parent=BODY, leftIndent=14, spaceAfter=3)
SMALL = ParagraphStyle("SMALL", parent=ss["Normal"], fontName=FONT,
                       fontSize=8.3, leading=11.5,
                       textColor=colors.HexColor("#555555"))
CENTER = ParagraphStyle("CENTER", parent=ss["Normal"], fontName=FONT,
                        fontSize=9.5, alignment=TA_CENTER,
                        textColor=colors.HexColor("#555555"),
                        spaceAfter=2, leading=13)
HEAD = ParagraphStyle("HEAD", parent=SMALL, fontName=FONT_B,
                      textColor=colors.white)
QUOTE = ParagraphStyle("Q", parent=BODY, leftIndent=12, fontName=FONT_I,
                       textColor=colors.HexColor("#444444"))


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
        t = t.replace(f"\x00{i}\x00", f'<font face="{FONT_MONO}">{c}</font>')
    return t


BR = "\x01"  # hard-break sentinel, survives inline() escaping


def _join(buf_lines):
    """Join raw paragraph lines: space-join, but keep Markdown hard breaks."""
    out = ""
    for k, raw in enumerate(buf_lines):
        hard = raw.endswith("  ") or raw.rstrip().endswith("\\")
        txt = raw.strip()
        if txt.endswith("\\"):
            txt = txt[:-1].rstrip()
        out += txt
        if k < len(buf_lines) - 1:
            out += BR if hard else " "
    return out


def para(txt, style):
    """Paragraph with inline markup and hard breaks rendered as <br/>."""
    return Paragraph(inline(txt).replace(BR, "<br/>"), style)


def _is_block_start(ln):
    """True if a line opens a new block (ends the current paragraph)."""
    s = ln.lstrip()
    return (not ln.strip() or ln.startswith("#") or s.startswith("|")
            or s.startswith(("- ", "* ")) or ln.startswith(">")
            or ln.strip() == "---")


def build(md_path, out_path, title):
    lines = open(md_path, encoding="utf-8").read().splitlines()
    log.info("Entrada: %s (%d líneas)", md_path, len(lines))
    doc = SimpleDocTemplate(out_path, pagesize=letter, topMargin=0.8*inch,
                            bottomMargin=0.8*inch, leftMargin=0.95*inch,
                            rightMargin=0.95*inch, title=title)
    E = []
    n_par = n_tab = n_quote = 0
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
            # indented continuation lines belong to the same bullet
            while (i + 1 < len(lines) and lines[i + 1].startswith("  ")
                   and not lines[i + 1].lstrip().startswith(("- ", "* "))):
                i += 1
                txt += " " + lines[i].strip()
            E.append(Paragraph("&bull;&nbsp;&nbsp;" + inline(txt), BULLET))
        elif ln.startswith("|"):
            # collect table block
            tbl = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in row):  # skip separator
                    tbl.append(row)
                i += 1
            # header row in white bold (the SMALL grey text was invisible
            # on the dark header background)
            data = [[Paragraph(inline(c), HEAD if k == 0 else SMALL)
                     for c in r] for k, r in enumerate(tbl)]
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
                n_tab += 1
            continue
        elif ln.startswith(">"):
            # consecutive "> " lines = one quoted paragraph; bare ">" splits
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                txt = lines[i][1:].strip()
                if not txt:
                    if buf:
                        E.append(Paragraph(inline(" ".join(buf)), QUOTE))
                        n_quote += 1
                        buf = []
                else:
                    buf.append(txt)
                i += 1
            if buf:
                E.append(Paragraph(inline(" ".join(buf)), QUOTE))
                n_quote += 1
            continue
        else:
            # plain paragraph: re-flow hard-wrapped lines
            buf = [lines[i]]
            while i + 1 < len(lines) and not _is_block_start(lines[i + 1]):
                i += 1
                buf.append(lines[i])
            txt = _join(buf)
            if (len(buf) == 1 and txt.startswith("*") and txt.endswith("*")
                    and len(txt) > 2):
                E.append(para(txt, CENTER))
            else:
                E.append(para(txt, BODY))
            n_par += 1
        i += 1
    doc.build(E)
    log.info("Bloques: %d párrafos, %d citas, %d tablas", n_par, n_quote, n_tab)
    log.info("PDF written: %s", out_path)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2],
          sys.argv[3] if len(sys.argv) > 3 else "SNT")
