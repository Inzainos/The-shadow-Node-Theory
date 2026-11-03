# Plan por partes – Pendientes 2.7.4

Objetivo: cerrar pendings técnicos declarados en CHANGELOG/README sin romper reproducibilidad.

## Fase 0 – Preparación
- Rama base: `fix/pendientes-2.7.4` sobre `local/doi-v2.7.4`.
- Tests de referencia: `pytest reconstruction_real/tests` 38 passed.
- Documentación base: `docs/pendientes-2.7.4.md`.

## Fase 1 – Consolidación de logging
Objetivo: eliminar `logging.basicConfig` disperso, usar API `snt`.

### 1.1 Inventario
Generar lista completa de archivos con `logging.basicConfig`.
Ya detectados 28+ en `reconstruction_real/code/`.

### 1.2 Migración estándar
Por archivo:
- Reemplazar bloque `logging.basicConfig(...)` por:
  ```python
  from snt import configurar_log
  log = configurar_log("<nombre_modulo>", log_dir=LOG_DIR, log_file="<archivo>.log")
  ```
- Si el script ya usa `logging.getLogger`, conservar nombre.
- Mantener formato `%(asctime)s | %(levelname)-7s | %(message)s`.

### 1.3 Priorización
1. `tela_exogena.py` – DONE
2. Scripts de auditoría v32: `snt_auditoria_integral_v32.py`, `verificar_claims.py`
3. Scripts de reconstrucción por dominio: `build_aco_v29.py`, `expand_dominio_B.py`, etc.
4. Resto de `reconstruction_real/code/`.

Criterio de aceptación: `grep -r logging.basicConfig reconstruction_real/code` → 0 hits.

## Fase 2 – Estabilización numérica tela_exogena
Objetivo: diffs deterministas entre entornos.

### 2.1 Salidas actuales
- `DECIMALES_TELA = 12`
- `.round(DECIMALES_TELA).to_csv(...)`

### 2.2 Mejora
- Añadir `float_format="%.12f"` en escrituras CSV críticas:
  `tela_exogena_series.csv`, `tela_exogena_casos.csv`, `tela_exogena_estadisticas.csv`, `tela_exogena_probabilidad.csv`.
- Documentar tolerancia 1e-9 en tests.

### 2.3 Validación
- Regenerar salidas, comprobar diff idéntico en dos entornos.
- Tests `tela` continúan pasando.

## Fase 3 – Unificación API de ajuste
Objetivo: asegurar uso canónico de `snt.ajuste_loglog`.

### 3.1 Verificación
- `rc1_superlineal.py` ya usa `from snt import ajuste_loglog`.
- Revisar `rc1_dominios_restantes.py`, `build_comercio_bilateral_cow.py` etc.

### 3.2 Corrección
- Eliminar definiciones locales duplicadas de `ajuste_loglog`.
- Importar desde `snt` y `snt_utils_v32` según corresponda.

Criterio: `grep -r "def ajuste_loglog" reconstruction_real/code` → solo en librerías, no en scripts.

## Fase 4 – Consolidación sha256 / utilidades
Objetivo: usar `snt.sha256` centralizado.

- Buscar copias de función sha256.
- Reemplazar por `from snt import sha256`.

## Fase 5 – Cierre y PR
- Actualizar `CHANGELOG.md` con cambios.
- Actualizar `reconstruction_real/claims.yaml` si cambia salida.
- PR `fix/pendientes-2.7.4` → `main`.
- CI verde: flake8, compileall, smoke test, pytest.

## Fase 6 – Pendientes conceptuales
No bloqueantes para PR técnico:
- Definición operativa de eje `u`.
- Medición de campo fricción `φ`.

Se documentan en `papers/marco_teorico.md` en iteración separada.

## Entregables por fase
- Fase 1: lista de archivos migrados, PR parcial.
- Fase 2: CSV estables, diff report.
- Fase 3: informe de API unificada.
- Fase 4: auditoría sha256.
- Fase 5: PR mergeado, CHANGELOG actualizado.

## Riesgos
- Cambios de logging pueden alterar orden de handlers si el logger ya existe → usar `if not logger.handlers`.
- Formato fijo a 12 decimales aumenta tamaño CSV, pero dentro de tolerancia.

Inicio con Fase 1.2 a partir de `tela_exogena.py` ya completado.
