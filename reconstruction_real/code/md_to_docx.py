"""
Minimal Markdown -> Word (.docx) renderer for the SNT framework documents.
Handles: # / ## / ### headings, | pipe | tables, '- ' bullets, '> ' quotes,
4-space indented code blocks, and inline **bold** / *italic* / `code`.
Not a full Markdown engine — tuned for marco_teorico_v30(.md / _EN.md) and
the SSRN manuscripts (snt_ssrn_v3x_EN.md).

Markdown semantics that matter for the manuscripts:
    * consecutive non-blank lines form ONE paragraph (hard-wrapped source
      text is re-flowed), so **bold** / *italic* spans may cross line breaks;
    * a line ending in two spaces (or a backslash) is a hard line break
      inside its paragraph (used by the author/header block);
    * consecutive "> " lines form one quoted paragraph (a bare ">" line
      separates quoted paragraphs).

Usage: python md_to_docx.py input.md output.docx
Log:   reconstruction_real/logs/md_to_docx_log.txt
"""
import logging
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent.parent
LOG_DIR = ROOT / "reconstruction_real" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "md_to_docx_log.txt"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("MD2DOCX")

# italic must hug non-space and not be part of a glob / identifier
INLINE = re.compile(r"(\*\*.+?\*\*|`[^`]+`"
                    r"|(?<![\w*])\*(?=\S)[^*]+?(?<=\S)\*(?![\w*]))")
BR = "\x01"  # hard-break sentinel inside a joined paragraph


def add_inline(p, text):
    """Add text to paragraph p, rendering **bold**, *italic*, `code`
    and hard line breaks (BR)."""
    for tok in INLINE.split(text):
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            _runs(p, tok[2:-2], bold=True)
        elif tok.startswith("`") and tok.endswith("`"):
            r = p.add_run(tok[1:-1]); r.font.name = "Consolas"; r.font.size = Pt(9)
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            _runs(p, tok[1:-1], italic=True)
        else:
            _runs(p, tok)


def _runs(p, text, bold=False, italic=False):
    """Add text as runs, turning BR sentinels into Word line breaks."""
    parts = text.split(BR)
    for k, part in enumerate(parts):
        r = p.add_run(part)
        r.bold = bold or None
        r.italic = italic or None
        if k < len(parts) - 1:
            r.add_break()


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


def _is_block_start(ln):
    """True if a line opens a new block (ends the current paragraph)."""
    s = ln.strip()
    return (not s or ln.startswith("#") or s.startswith("|")
            or ln.lstrip().startswith(("- ", "* ")) or ln.startswith(">")
            or s in ("---", "***") or ln.startswith("    "))


def flush_table(doc, rows):
    # rows: list of list[str]; drop separator rows like |---|---|
    rows = [r for r in rows if not all(set(c.strip()) <= set("-: ") for c in r)]
    if not rows:
        return
    ncol = max(len(r) for r in rows)
    t = doc.add_table(rows=0, cols=ncol)
    t.style = "Light Grid Accent 1"
    for ri, r in enumerate(rows):
        cells = t.add_row().cells
        for ci in range(ncol):
            txt = r[ci].strip() if ci < len(r) else ""
            cell_p = cells[ci].paragraphs[0]
            add_inline(cell_p, txt)
            if ri == 0:
                for run in cell_p.runs:
                    run.bold = True


def main(src, dst):
    md = open(src, encoding="utf-8").read().split("\n")
    log.info("Entrada: %s (%d líneas)", src, len(md))
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(10.5)

    tbuf, cbuf, qbuf = [], [], []
    n_par = n_tab = n_quote = 0

    def flush_code():
        if cbuf:
            p = doc.add_paragraph()
            r = p.add_run("\n".join(cbuf))
            r.font.name = "Consolas"; r.font.size = Pt(9)
            cbuf.clear()

    def flush_quote():
        nonlocal n_quote
        if qbuf:
            p = doc.add_paragraph(); p.paragraph_format.left_indent = Pt(18)
            add_inline(p, " ".join(qbuf))
            for r in p.runs:
                r.italic = True; r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
            qbuf.clear()
            n_quote += 1

    i = 0
    while i < len(md):
        line = md[i]
        # table rows
        if line.strip().startswith("|") and line.strip().endswith("|"):
            flush_code(); flush_quote()
            tbuf.append([c for c in line.strip().strip("|").split("|")])
            i += 1
            continue
        elif tbuf:
            flush_table(doc, tbuf); tbuf = []
            n_tab += 1

        if line.startswith("    ") and line.strip():      # indented code
            flush_quote()
            cbuf.append(line[4:]); i += 1
            continue
        flush_code()

        if line.startswith(">"):                          # quoted paragraph
            txt = line[1:].strip()
            if txt:
                qbuf.append(txt)
            else:
                flush_quote()
            i += 1
            continue
        flush_quote()

        s = line.rstrip()
        if not s.strip():
            i += 1
            continue
        if s.startswith("# "):
            doc.add_heading(s[2:], level=1)
        elif s.startswith("## "):
            doc.add_heading(s[3:], level=2)
        elif s.startswith("### "):
            doc.add_heading(s[4:], level=3)
        elif s.strip() in ("---", "***"):
            doc.add_paragraph()
        elif s.lstrip().startswith(("- ", "* ")):
            txt = s.lstrip()[2:]
            # indented continuation lines belong to the same bullet
            while (i + 1 < len(md) and md[i + 1].startswith("  ")
                   and not md[i + 1].startswith("    ")
                   and not md[i + 1].lstrip().startswith(("- ", "* "))):
                i += 1
                txt += " " + md[i].strip()
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, txt)
        else:
            # plain paragraph: re-flow hard-wrapped lines
            buf = [line]
            while i + 1 < len(md) and not _is_block_start(md[i + 1]):
                i += 1
                buf.append(md[i])
            p = doc.add_paragraph()
            add_inline(p, _join(buf))
            n_par += 1
        i += 1

    if tbuf:
        flush_table(doc, tbuf)
        n_tab += 1
    flush_code()
    flush_quote()
    doc.save(dst)
    log.info("Bloques: %d párrafos, %d citas, %d tablas", n_par, n_quote, n_tab)
    log.info("DOCX written: %s", dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
