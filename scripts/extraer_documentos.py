#!/usr/bin/env python3
"""Extrae texto buscable de planillas (.xlsx, .xls) y documentos Word (.docx, .doc).

Planillas: una sección por hoja; cada celda como `A1: valor [=fórmula]`. Las imágenes
incrustadas en .xlsx se guardan en material/figuras/ y se referencian en su hoja.
Documentos Word: texto plano convertido con `textutil` (macOS).

Requiere openpyxl (.xlsx) y xlrd (.xls).
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.6g}"
    return str(value).replace("\n", " ").strip()


def formula_text(raw: object) -> str:
    text = getattr(raw, "text", raw)
    return str(text)


def dump_xlsx(path: Path, source_id: str, figures_dir: Path, root: Path) -> list[str]:
    import openpyxl

    values = openpyxl.load_workbook(path, data_only=True)
    formulas = openpyxl.load_workbook(path, data_only=False)
    lines: list[str] = []
    for index, name in enumerate(formulas.sheetnames, start=1):
        lines.append(f"\n===== HOJA {index}: {name} =====\n")
        vsheet, fsheet = values[name], formulas[name]
        for number, image in enumerate(fsheet._images, start=1):
            anchor = image.anchor._from
            cell = f"{openpyxl.utils.get_column_letter(anchor.col + 1)}{anchor.row + 1}"
            target = figures_dir / f"{source_id}-hoja{index}-img{number}.{image.format or 'png'}"
            target.write_bytes(image._data())
            lines.append(f"IMAGEN en {cell}: {target.relative_to(root).as_posix()}")
        for row in fsheet.iter_rows():
            parts = []
            for cell in row:
                raw = cell.value
                if raw is None:
                    continue
                if cell.data_type == "f":
                    cached = vsheet[cell.coordinate].value
                    shown = fmt(cached) if cached is not None else "?"
                    parts.append(f"{cell.coordinate}: {shown} [{formula_text(raw)}]")
                elif text := fmt(raw):
                    parts.append(f"{cell.coordinate}: {text}")
            if parts:
                lines.append(" | ".join(parts))
    return lines


def dump_xls(path: Path) -> list[str]:
    import xlrd

    book = xlrd.open_workbook(path)
    lines: list[str] = []
    for index, sheet in enumerate(book.sheets(), start=1):
        lines.append(f"\n===== HOJA {index}: {sheet.name} =====\n")
        for r in range(sheet.nrows):
            parts = [
                f"{xlrd.formula.cellname(r, c)}: {text}"
                for c in range(sheet.ncols)
                if (text := fmt(sheet.cell_value(r, c)))
            ]
            if parts:
                lines.append(" | ".join(parts))
    return lines


def dump_word(path: Path) -> list[str]:
    if shutil.which("textutil") is None:
        raise RuntimeError("falta textutil para convertir documentos Word")
    result = subprocess.run(
        ["textutil", "-convert", "txt", "-stdout", str(path)],
        capture_output=True, text=True, check=True,
    )
    return ["", result.stdout.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--titulo", required=True)
    parser.add_argument("--ruta", required=True)
    args = parser.parse_args(argv)

    root = args.root.resolve()
    source = root / args.ruta
    figures_dir = root / "material/figuras"
    figures_dir.mkdir(parents=True, exist_ok=True)
    suffix = source.suffix.lower()
    if suffix == ".xlsx":
        body = dump_xlsx(source, args.id, figures_dir, root)
    elif suffix == ".xls":
        body = dump_xls(source)
    elif suffix in (".docx", ".doc"):
        body = dump_word(source)
    else:
        print(f"formato no soportado: {args.ruta}", file=sys.stderr)
        return 1

    header = [f"FUENTE: {args.id}", f"TITULO: {args.titulo}", f"ORIGINAL: {args.ruta}"]
    output = root / "material/extraido" / f"{args.id}.txt"
    temporary = output.with_name(f".{output.name}.tmp")
    temporary.write_text("\n".join(header + body) + "\n", encoding="utf-8")
    temporary.replace(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
