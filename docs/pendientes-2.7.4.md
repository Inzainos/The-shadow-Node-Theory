# Pendientes 2.7.4 – Estado y acciones

Fecha: 2026-11-03
Rama: `fix/pendientes-2.7.4`
Base: `local/doi-v2.7.4` → `main`

## Resumen ejecutivo

Repositorio Shadow Node Theory v2.7.4 con ADENDA 5 sellada DOI 10.5281/zenodo.23684731.
Tests CI pasan: `pytest reconstruction_real/tests` 38 passed.

Pendientes declarados en CHANGELOG/README:
- Consolidación de ajustes de potencia y `snt_utils_v32.py`; bloques puntuales de `logging.basicConfig` fuera de migración.
- `rc1_superlineal.py` desempaquetado de firmas en `main` (corregido en `local/doi-v2.7.4` con importación de `snt`).
- `tela_exogena.py` regenera CSV con diferencias última cifra ~1e-16 por entorno numérico.
- Eje `u` sin definición operativa.
- Campo fricción `φ` postulado, no medido.

## Trabajo realizado

### 1. Revisión de estado
- README v2.7.4, AGENTS.md, CHANGELOG.md, CONTRIBUTING.md, dev-guide.md, SECURITY.md leídos.
- Git: rama `local/doi-v2.7.4` up to date, working tree limpio.
- CI: `.github/workflows/python-package-conda.yml`, `environment.yml`, `requirements.txt`, `pyproject.toml`, `.flake8` verificados.

### 2. Rama de trabajo
```bash
git checkout -b fix/pendientes-2.7.4
```

### 3. Consolidación de logging
Archivos modificados:
- `reconstruction_real/code/tela_exogena.py`
  - Antes: `logging.basicConfig(...)` con StreamHandler + FileHandler.
  - Después: `from snt import configurar_log` y `log = configurar_log("tela_exogena", log_dir=LOG_DIR, log_file="tela_exogena_log.txt")`.
- `reconstruction_real/code/recalculo_trigger_abrupto_gradual.py`
  - Antes: `logging.basicConfig(...)` con FileHandler + StreamHandler.
  - Después: `from snt import configurar_log` y `log = configurar_log("TRIGGER-RECALC", log_dir=LOG_DIR, log_file="recalculo_trigger_abrupto_gradual_log.txt")`.
  - Eliminado `import sys` no usado.
- `reconstruction_real/code/build_comercio_bilateral_cow.py`
  - Antes: `logging.basicConfig(...)` con FileHandler + StreamHandler(sys.stdout).
  - Después: `from snt import configurar_log, sha256` y `log = configurar_log("COMERCIO-COW", log_dir=LOG_DIR, log_file="build_comercio_bilateral_cow_log.txt")`.
  - Eliminado `import sys` no usado.
- `reconstruction_real/code/aco_cohortes_ampliadas.py`
  - Antes: `logging.basicConfig(...)` con FileHandler + StreamHandler(sys.stdout).
  - Después: `from snt import configurar_log, sha256` y `log = configurar_log("ACO-COHORTES", log_dir=LOG_DIR, log_file="aco_cohortes_ampliadas_log.txt")`.
  - Eliminado `import sys` no usado.
- `reconstruction_real/code/npm_pruebas_aco.py`
  - Antes: `logging.basicConfig(...)` con FileHandler + StreamHandler(sys.stdout).
  - Después: `from snt import configurar_log` y `log = configurar_log("NPM-PRUEBAS", log_dir=LOG_DIR, log_file="npm_pruebas_aco_log.txt")`.
  - Eliminado `import sys` no usado.
- `reconstruction_real/code/eje_u_transiciones.py`
  - Antes: función `configure_log()` con `logging.basicConfig(...)`.
  - Después: `configure_log()` usa `snt.configurar_log("EJE-U", log_dir=LOG_DIR, log_file=LOG_FILE.name)`.
  - Import añadido `configurar_log` desde `snt`.
- `reconstruction_real/code/prueba_disparadores_ciudades.py`
  - Antes: `logging.basicConfig(...)` con FileHandler + StreamHandler(sys.stdout).
  - Después: `from snt import configurar_log, sha256` y `log = configurar_log("DISPARADORES", log_dir=LOG_DIR, log_file="prueba_disparadores_ciudades_log.txt")`.
  - Eliminado `import sys` no usado.
- `reconstruction_real/code/modelo_jerarquico_b.py`
  - Antes: `logging.basicConfig(...)` con StreamHandler + FileHandler.
  - Después: `from snt import configurar_log` y `log = configurar_log("modelo_jerarquico", log_dir=LOG_DIR, log_file="modelo_jerarquico_log.txt")`.
  - Eliminado `import sys` no usado.
- `reconstruction_real/code/friccion_por_caso_npm.py`
  - Antes: `logging.basicConfig(...)` con StreamHandler + FileHandler.
  - Después: `from snt import configurar_log` y `log = configurar_log("friccion_por_caso", log_dir=LOG_DIR, log_file="friccion_por_caso_log.txt")`.
  - Eliminado `import sys` no usado.
- `reconstruction_real/code/prueba_discriminante_dominio_B.py`
  - Antes: `logging.basicConfig(...)` con FileHandler relativo y StreamHandler(sys.stdout).
  - Después: define ROOT/LOG_DIR, usa `snt.configurar_log("DISCRIM", ...)` y elimina `import sys`.
  - Log ahora en `reconstruction_real/logs/prueba_discriminante_log.txt`.
- `reconstruction_real/code/e3_r2_raw.py`
  - Antes: `logging.basicConfig(...)` con FileHandler + StreamHandler(sys.stdout).
  - Después: `from snt import configurar_log, sha256` y `log = configurar_log("E3-R2RAW", log_dir=LOG_DIR, log_file="e3_r2_raw_log.txt")`.
  - Eliminado `import sys` no usado.
- `reconstruction_real/code/rc1_superlineal.py`
  - Antes: importaba `configurar_logging as configurar_log` y llamaba `configurar_log(LOG_FILE)`, firma desajustada.
  - Después: import `from snt import ajuste_loglog, configurar_log` y llamada `configurar_log("RC1", log_dir=LOG_DIR, log_file=LOG_FILE.name)` usando API canónica.
  - Homologada firma a `snt.configurar_log`.
- `reconstruction_real/code/tela_exogena.py` — estabilización numérica
  - Añadido `float_format="%.12f"` en los cuatro `to_csv` de salidas:
    `tela_exogena_estadisticas.csv`, `tela_exogena_probabilidad.csv`, `tela_exogena_casos.csv`, `tela_exogena_series.csv`.
  - Reduce diferencias de última cifra ~1e-16 en regeneraciones.
- Compilación OK.
- Tests `tela` 9 passed, suite completa 38 passed.

Impacto: scripts migrados a logger centralizado de `snt`. Reduce duplicación de `logging.basicConfig`.

### 4. Verificación
```bash
pytest reconstruction_real/tests -q   # 38 passed
pytest reconstruction_real/tests -k tela   # 9 passed
```

## Pendientes técnicos abiertos

### A. Logging / sha256 disperso
Scripts con `logging.basicConfig` puntual:
`reconstruction_real/code/recalculo_trigger_abrupto_gradual.py`,
`build_comercio_bilateral_cow.py`, `aco_cohortes_ampliadas.py`, `npm_pruebas_aco.py`,
`eje_u_transiciones.py`, `prueba_disparadores_ciudades.py`, `modelo_jerarquico_b.py`,
`friccion_por_caso_npm.py`, ... 28+ casos detectados.

Acción propuesta: migrar a `snt.configurar_log` / `snt.configurar_logging`.

### B. Estabilidad numérica tela_exogena
- `DECIMALES_TELA = 12` ya aplicado.
- Salidas usan `.round(DECIMALES_TELA).to_csv(...)` sin `float_format`.
- Diferencias ~1e-16 persisten por BLAS/numpy.

Acción propuesta: añadir `float_format="%.12f"` en escrituras CSV críticas y documentar tolerancia.

### C. rc1_superlineal firma
- En `main` existía definición local de `ajuste_loglog` y `configurar_log`.
- En `local/doi-v2.7.4` ya migrado a `from snt import ajuste_loglog, configurar_logging`.
- Pendiente traer cambio a `main` vía PR.

### D. Conceptuales
- Eje `u` sin definición operativa.
- Campo fricción `φ` postulado, no medido.

## Próximos pasos sugeridos
1. Continuar migración masiva de logging a `snt`.
2. Estabilizar salidas CSV de tela_exogena con formato fijo.
3. Preparar PR `fix/pendientes-2.7.4` → `main`.
4. Documentar decisiones de estabilidad numérica en CHANGELOG.

## Archivos relevantes
- `/home/deamon/The-shadow-Node-Theory/README.md`
- `/home/deamon/The-shadow-Node-Theory/CHANGELOG.md`
- `/home/deamon/The-shadow-Node-Theory/AGENTS.md`
- `/home/deamon/The-shadow-Node-Theory/reconstruction_real/code/tela_exogena.py`
- `/home/deamon/The-shadow-Node-Theory/snt/utils.py`
