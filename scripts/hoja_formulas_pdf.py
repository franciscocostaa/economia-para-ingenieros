#!/usr/bin/env python3
"""Genera output/pdf/hoja-de-formulas.pdf desde wiki/repaso/hoja-de-formulas.md.

Una carilla A4 apaisada por sección `##` (valor tiempo del dinero y proyectos),
pensada para imprimirse en una sola hoja a doble faz. Usa Google Chrome headless.
Las viñetas que empiezan con ⚠ se resaltan en ámbar y las que empiezan con ✔ en verde.
Uso: python3 scripts/hoja_formulas_pdf.py          (hoja general)
     python3 scripts/hoja_formulas_pdf.py --andy   (wiki/repaso/hoja-de-formulas-andy.md,
                                                    a dos columnas por carilla)
El texto anterior al primer `##` no se imprime.
"""
import html, re, subprocess, sys, tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MD = RAIZ / "wiki/repaso/hoja-de-formulas.md"
PDF = RAIZ / "output/pdf/hoja-de-formulas.pdf"
MD_ANDY = RAIZ / "wiki/repaso/hoja-de-formulas-andy.md"
PDF_ANDY = RAIZ / "output/pdf/hoja-de-formulas-andy.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4 landscape; margin: 7mm 8mm; }
body { font-family: "Chalkboard SE","Comic Neue","Segoe Print",sans-serif; font-size: 8pt;
  line-height: 1.2; color: #1a1a1a; margin: 0;
  background: repeating-linear-gradient(#fffdf5 0 15px, #e9e6d9 15px 16px); }
section { page-break-after: always; }
section:last-child { page-break-after: auto; }
.cab { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid #222; margin-bottom: 3px; }
h2 { font-size: 15pt; margin: 0; }
.cab span { font-size: 7.5pt; color: #555; }
h3 { font-size: 10pt; margin: 5px 0 1px; color: #0b3d2e; }
ul { margin: 0 0 2px 0; padding-left: 0; list-style: none; }
li { margin: 1px 0; padding: 1px 6px; text-indent: 0; }
li.warn { background: #fdeecf; border-left: 3px solid #d98a00; border-radius: 3px; }
li.ok { background: #e4f2d8; border-left: 3px solid #4f9a1f; border-radius: 3px; }
p.warn { background: #fdeecf; border-left: 3px solid #d98a00; border-radius: 3px; padding: 2px 6px; margin: 2px 0; }
p.ok { background: #e4f2d8; border-left: 3px solid #4f9a1f; border-radius: 3px; padding: 2px 6px; margin: 2px 0; }
.pill { background: #cfe8b8; border-radius: 4px; padding: 0 5px; font-weight: 600; margin-right: 5px; white-space: nowrap; }
table { border-collapse: collapse; width: 100%; margin: 2px 0 3px; font-size: 7.5pt; }
th { background: #cfe8b8; text-align: left; font-weight: 600; }
th, td { border: 1px solid #b7cfa3; padding: 1.5px 5px; vertical-align: top; }
code { font-family: Menlo, monospace; font-size: 7pt; background: #eef2e6; padding: 0 2px; border-radius: 2px; }
p { margin: 2px 0; }
p.pie { font-size: 7.5pt; color: #444; }
.cols { column-count: 2; column-gap: 9px; column-rule: 1px dashed #b7cfa3; }
.cols h3 { break-after: avoid; }
.cols table, .cols li, .cols p { break-inside: avoid; }
"""

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    return t

def bullet(t):
    cls = " class='warn'" if t.startswith("⚠") else " class='ok'" if t.startswith("✔") else ""
    m = re.match(r"\*\*([^*]+)\*\*\s*·\s*(.*)", t)
    if m:
        return f"<li{cls}><span class='pill'>{inline(m.group(1))}</span>{inline(m.group(2))}</li>"
    return f"<li{cls}>{inline(t)}</li>"

def render(md, cols=False, rotulo="Hoja de fórmulas · Segundo parcial"):
    lines = md.splitlines()
    while lines and not lines[0].startswith("## "):
        lines.pop(0)
    cierre = "</div></section>" if cols else "</section>"
    out, i, n_sec = [], 0, 0
    total = sum(1 for l in lines if l.startswith("## "))
    def abrir(h):
        nonlocal n_sec
        n_sec += 1
        return (f"<section><div class='cab'><h2>{inline(h)}</h2>"
                f"<span>{rotulo} · cara {n_sec}/{total}</span></div>" + ("<div class='cols'>" if cols else ""))
    while i < len(lines):
        l = lines[i]
        if l.startswith("# ") and not l.startswith("## "):
            pass
        elif l.startswith("## "):
            if n_sec: out.append(cierre)
            out.append(abrir(l[3:]))
        elif l.startswith("### "):
            out.append(f"<h3>{inline(l[4:])}</h3>")
        elif l.startswith("- "):
            out.append("<ul>")
            while i < len(lines) and lines[i].startswith("- "):
                out.append(bullet(lines[i][2:])); i += 1
            out.append("</ul>"); continue
        elif l.startswith("|"):
            filas = []
            while i < len(lines) and lines[i].startswith("|"):
                filas.append(lines[i]); i += 1
            celdas = lambda f: [c.strip() for c in f.strip().strip("|").split("|")]
            out.append("<table><tr>" + "".join(f"<th>{inline(c)}</th>" for c in celdas(filas[0])) + "</tr>")
            for f in filas[2:]:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in celdas(f)) + "</tr>")
            out.append("</table>"); continue
        elif l.strip():
            if l.startswith("⚠"): cls = " class='warn'"
            elif l.startswith("✔"): cls = " class='ok'"
            elif re.match(r"(τ = |P = |Fuentes|Rótulos|CT neto)", l): cls = " class='pie'"
            else: cls = ""
            out.append(f"<p{cls}>{inline(l)}</p>")
        i += 1
    out.append(cierre)
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(out)}</body></html>"

def main():
    andy = "--andy" in sys.argv[1:]
    md, pdf = (MD_ANDY, PDF_ANDY) if andy else (MD, PDF)
    rotulo = "Hoja de fórmulas de Andy · Segundo parcial" if andy else "Hoja de fórmulas · Segundo parcial"
    htmltxt = render(md.read_text(encoding="utf-8"), cols=andy, rotulo=rotulo)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(htmltxt); src = f.name
    pdf.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", f"file://{src}"], check=True, capture_output=True)
    print(f"PDF generado: {pdf}")

if __name__ == "__main__":
    sys.exit(main())
