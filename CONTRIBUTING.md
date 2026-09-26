# Guía de contribución — Shadow Node Theory (SNT)

Gracias por tu interés en **Shadow Node Theory**. Este es un repositorio de
investigación científica: el código, los datos y los documentos teóricos deben
mantener trazabilidad y reproducibilidad. Esta guía describe cómo contribuir.

## Principios

- **La verdad técnica está por encima de la impresión numérica.** Todo resultado
  debe ser reproducible desde fuentes primarias públicas y scripts versionados.
- **Datos reales, no sintéticos.** No se aceptan valores fabricados en el corpus
  activo. Los datos derivados deben citar su fuente primaria en `sources.md`, y
  los archivos fuente externos se anclan (URL, edición, fecha, SHA-256) en
  `data/FUENTES.md`.
- **Inferencia honesta.** Los p-values por caso del corpus están inflados
  (autocorrelación serial en el dominio B; 714 casos no independientes). No
  cites el p por fila sin las salvedades de la auditoría v32 (README → "Audit
  v32").
- **Idioma.** Los documentos del repositorio se escriben principalmente en
  español. Las traducciones al inglés se identifican con el sufijo `_EN`.

## Entorno de desarrollo

```bash
git clone https://github.com/Inzainos/The-shadow-Node-Theory.git
cd The-shadow-Node-Theory
```

### Entorno de runtime

```bash
conda env create -f environment.yml
conda activate snt-env
```

### Entorno de desarrollo

```bash
conda env create -f environment-dev.yml
conda activate snt-dev-env
```

### Alternativa con virtualenv

Si prefieres `venv`, usa:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Actualizar el entorno Conda

```bash
conda env update -f environment.yml --prune
```

## Integración continua

El flujo de CI se encuentra en `.github/workflows/python-package-conda.yml` y usa Miniconda para crear el ambiente `snt-env` desde `environment.yml`.

El pipeline verifica:

- checkout del repositorio
- creación del ambiente Conda
- instalación de dependencias Python
- validación con `flake8`
- compilación de módulos Python activos
- un smoke test con `python reconstruction_real/code/build_aco_v29.py`

Fuera del CI, si tocas el corpus corre también la prueba de regresión y la
auditoría integral:

```bash
pytest reconstruction_real/tests
python reconstruction_real/code/snt_auditoria_integral_v32.py
```

## Estructura del repositorio

Consulta la sección *Repository Structure* del [README](README.md) para el mapa
completo de carpetas. En resumen:

- `reconstruction_real/` — corpus real de 721 casos (introducido en v2.4.0;
  release activa **2.5.2**): datos, código, metodología, `audits/` (auditoría
  integral v32 y prueba discriminante del dominio B) y `tests/`.
- `papers/` — marco teórico activo **v34** (`papers/marco_teorico.md`), linaje en
  `papers/CHANGELOG_marco.md`, y manuscritos/preprints (v30).
- `code/` — utilidades compartidas (`snt_utils.py`, `snt_utils_v32.py`) y scripts
  históricos (v28).
- `data/` — datos fuente y provenance (`FUENTES.md` con URL, edición y SHA-256).
- `genomic_agent/` — SNT Genomic Topologic Analyzer.
- `delta/` — motor de señales cripto y bolsa (independiente).
- `dashboard/` — dashboard interactivo en Streamlit.
- `figures/` — figuras de publicación.
- `archive/` — versiones superadas (no citar).

## Flujo de trabajo

1. Crea una rama descriptiva desde `main` (p. ej. `claude/nueva-validacion`).
2. Realiza cambios pequeños y enfocados.
3. Asegúrate de que los scripts sean reproducibles y conserven sus docstrings.
4. Actualiza `CHANGELOG.md` y, si corresponde, el `README.md`.
5. Abre un Pull Request hacia `main` describiendo el qué y el porqué.

## Convención de commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/es/) con el
asunto en inglés:

- `feat:` nueva funcionalidad o nuevo análisis/dominio.
- `fix:` corrección de errores.
- `docs:` cambios en documentación (README, papers, changelog).
- `data:` cambios en datasets del corpus.
- `refactor:` reorganización sin cambio de comportamiento.
- `chore:` mantenimiento (gitignore, CI, metadatos).

Ejemplo: `docs: update README and add missing repo standards`.

## Estándares de código

- **Python ≥ 3.10.** Sigue PEP 8 y agrega docstrings a módulos y funciones.
- Documenta las fuentes de datos primarias dentro del script o en `sources.md`.
- No incluyas secretos ni datos propietarios (ver `.gitignore`).

## Reportar problemas

Abre un *issue* en GitHub describiendo el problema, el archivo afectado y, si es
un resultado numérico, los pasos para reproducirlo.

## Contacto

Elán Zainos Corona — Fractal Core Research — Tlaxcala, México
GitHub: [Inzainos](https://github.com/Inzainos)
