# Material y fuentes

Esta carpeta separa originales, archivos pendientes y derivados:

- `entrada/`: bandeja temporal para material todavía no clasificado.
- `catedra/`: originales oficiales; no se editan después de registrarlos.
- `externo/`: bibliografía o recursos complementarios.
- `extraido/`: texto regenerable y buscable, con cortes de página.
- `figuras/`: capturas o diagramas derivados que necesitan inspección visual.

`catalogo.tsv` asigna un ID estable a cada fuente. `checksums.sha256` permite detectar cambios accidentales en originales oficiales. Para registrar una fuente usá `scripts/registrar_fuente.py`; no la copies manualmente a `catedra/`.

IDs sugeridos: `T01` para teoría, `P01` para práctica, `G01` para guías, `B01` para bibliografía y `X01` para material externo. El ID no debe cambiar aunque se renombre el título humano.

## Extracción

`scripts/extraer_fuentes.sh` regenera `extraido/` a partir del catálogo. Los PDF se extraen con `pdftotext` (poppler), con un corte `===== PAGINA N =====` por página. Las planillas y los documentos Word pasan por `scripts/extraer_documentos.py`, que escribe una sección `===== HOJA N =====` por hoja, cada celda con su valor y su fórmula, y guarda en `figuras/` las imágenes incrustadas. Requiere `openpyxl`, `Pillow` y `xlrd` en el Python indicado por `PYTHON` (por defecto `python3`), y `textutil` (macOS) para `.doc` y `.docx`.
