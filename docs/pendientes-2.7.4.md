# Pendientes 2.7.5 – Estado y acciones

Fecha: 2026-11-04
Rama: `fix/pendientes-2.7.5`
Base: `fix/pendientes-2.7.4` → `main`

## Resumen ejecutivo

Repositorio Shadow Node Theory v2.7.5 en desarrollo sobre base v2.7.4 con ADENDA 5 sellada DOI 10.5281/zenodo.23684731.
Tests CI pasan: `pytest reconstruction_real/tests` 38 passed.
Claims verificados: 39/39 OK.

Pendientes declarados v2.7.4 y ahora v2.7.5:
- Consolidación de ajustes de potencia y `snt_utils_v32.py`; bloques puntuales de `logging.basicConfig` fuera de migración (cerrado en v2.7.4).
- `rc1_superlineal.py` homologado con `snt.configurar_log` (cerrado en v2.7.4).
- `tela_exogena.py` estabilizada numéricamente (cerrado en v2.7.4).
- **Eje `u` sin definición operativa** → nuevo pre-registro con Entropía de Permutación (series cortas) y Dimensión de Correlación (series largas).
- **Campo fricción `φ` postulado, no medido** → definición formal en Axioma 0.1 v2.7.5.

Estado actualizado 2026-11-04:
- Migración de logging a `snt.configurar_log` completada en v2.7.4.
- Estabilización numérica `tela_exogena.py` con `float_format="%.12f"` aplicada en v2.7.4.
- Rama `fix/pendientes-2.7.5` creada desde `fix/pendientes-2.7.4`.
- Definición formal campo `φ` añadida en `papers/marco_teorico.md` Axioma 0.1.
- Pre-registro eje `u` en desarrollo con Entropía de Permutación (series cortas) y Dimensión de Correlación (series largas).

Estado actualizado 2026-11-03:
- Migración de logging a `snt.configurar_log` completada para 11 scripts principales + `rc1_superlineal.py` homologado, y los 17 remanentes adicionales migrados.
- Estabilización numérica `tela_exogena.py` con `float_format="%.12f"` aplicada y CSV regenerados.
- Rama `fix/pendientes-2.7.4` rebased sobre `origin/main` y sincronizada con fix de logger en `snt/utils.py`.

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
Migrados a `snt.configurar_log` en 2026-11-03:
- `reconstruction_real/code/tela_exogena.py`
- `reconstruction_real/code/recalculo_trigger_abrupto_gradual.py`
- `reconstruction_real/code/build_comercio_bilateral_cow.py`
- `reconstruction_real/code/aco_cohortes_ampliadas.py`
- `reconstruction_real/code/npm_pruebas_aco.py`
- `reconstruction_real/code/eje_u_transiciones.py`
- `reconstruction_real/code/prueba_disparadores_ciudades.py`
- `reconstruction_real/code/modelo_jerarquico_b.py`
- `reconstruction_real/code/friccion_por_caso_npm.py`
- `reconstruction_real/code/prueba_discriminante_dominio_B.py`
- `reconstruction_real/code/e3_r2_raw.py`
- `reconstruction_real/code/rc1_superlineal.py` homologado a API canónica.

Migración adicional completada 2026-11-03, los 17 remanentes previos quedan migrados:
- `hackerearth_verificacion.py`
- `covid_E3_series_crudas.py`
- `cointegracion_hub_nodo.py`
- `tela_cimatica.py`
- `reconstruccion_B_hub_comercio.py`
- `md_to_pdf.py`
- `tela_de_incertidumbre.py`
- `build_dominio_G.py`
- `npm_followup_cohorte_friccion.py`
- `build_maddison_mpd2020_csv.py`
- `descargar_binance_klines.py`
- `prueba_hub_temporal.py`
- `md_to_docx.py`
- `generate_readme_figures.py`
- `npm_cohorte_aco.py`
- `hackerearth_entrega_honesta.py`
- `prueba_friccion_dominios_nuevos.py`

Estado: sin archivos `logging.basicConfig` pendientes en `reconstruction_real/code` según lista de remanentes.

### B. Estabilidad numérica tela_exogena
- `DECIMALES_TELA = 12` ya aplicado.
- `float_format="%.12f"` añadido en los cuatro `to_csv` de `tela_exogena.py` el 2026-11-03.
- CSV regenerados; claims 39/39 OK.

Pendiente: documentar tolerancia de última cifra y validar reproducibilidad en CI.

### C. rc1_superlineal firma
- Migrado a `from snt import ajuste_loglog, configurar_log` y llamada canónica `configurar_log("RC1", log_dir=LOG_DIR, log_file=LOG_FILE.name)`.
- Cambio presente en rama `fix/pendientes-2.7.4`, listo para PR a `main`.

### D. Conceptuales
- Eje `u` sin definición operativa.
- Campo fricción `φ` postulado, no medido.

## Próximos pasos sugeridos
1. Documentar tolerancia de última cifra y reproducibilidad de tela_exogena en CHANGELOG.
2. Preparar PR `fix/pendientes-2.7.4` → `main` con claims 39/39 OK y tests 38 passed.
3. Revisar definiciones operativas de eje `u` y campo fricción `φ`.

## Archivos relevantes
- `/home/deamon/The-shadow-Node-Theory/README.md`
- `/home/deamon/The-shadow-Node-Theory/CHANGELOG.md`
- `/home/deamon/The-shadow-Node-Theory/AGENTS.md`
- `/home/deamon/The-shadow-Node-Theory/reconstruction_real/code/tela_exogena.py`
- `/home/deamon/The-shadow-Node-Theory/snt/utils.py`
