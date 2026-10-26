# PENDIENTES_SNT.md — copia de procedencia (2026-10-26)

> **Nota de procedencia:** este archivo vive originalmente en
> `/home/deamon/PENDIENTES_SNT.md` (fuera del repo) y es del OPERADOR.
> Se copia aquí (observación 7 del `observaciones.md` 2026-10-26) porque
> cinco preregistros y el CHANGELOG lo citan: la copia versionada es la
> referencia estable del contenido que sirvió de base a la ronda
> 2026-10-26. La fuente de verdad sigue siendo el archivo del operador.

---

# Pendientes — Shadow Node Theory (SNT)

**Fecha:** 2026-10-26 · **Base:** `main` en `c4b0eef` + rama `fix/auditoria-ci-claims` (5 commits, sin push)
**Alcance:** lo que quedó sin hacer después de la revisión del repo y de la rama de fixes.

Leyenda: `[ ]` pendiente · **Bloquea** = otra tarea depende de esta · **Decisión** = requiere al autor.

---

## 0. Antes de todo: integrar la rama

- [ ] Hacer `git fetch` del bundle (o `git am` de los parches) y abrir el PR de `fix/auditoria-ci-claims`.
- [ ] Confirmar que el CI pasa **en GitHub** (usa Conda, no el entorno pip donde lo probé). Revisar sobre todo el paso nuevo `pytest reconstruction_real/tests` (~15 s) y que `pyyaml` quede instalado desde `requirements.txt`.
- [ ] Revisar que el paso de humo `build_aco_v29.py` no deje cambios en `figures/` (en mi corrida regeneró `fig_aco_v29_absorption.{png,svg}` con diferencias binarias; las revertí).

---

## 1. Prioridad alta

### 1.1 `rc1_superlineal.py` no se ejecuta — **Decisión · Bloquea 1.2**
- **Síntoma:** `main()` falla también en `main` sin mis cambios.
- **Causa:** el script quedó desfasado respecto de `code/snt_utils_v32.py`.
  - Líneas 252 y 268: `b_est, _, _, _, _ = ajuste_loglog(...)` espera 5 valores; la función devuelve 3 `(b, log a, residuos)`.
  - Línea 269: `b_cal, _ = comparar_modelos(...)` espera 2 valores; la función devuelve un `dict`.
- **Por qué importa:** los `reconstruction_real/data/rc1_*.csv` y el informe `RESULTADOS_RC1_SUPERLINEAL_2026-10-02.md` (que sostiene que `b ≥ 1` no clasifica un régimen) no se pueden regenerar desde ese script.
- **Es un script preregistrado** (commit `1a2ac0e`): no cambiar su lógica sin decidir cómo documentarlo.
- **Acciones:**
  - [ ] Decidir si el script es el vigente o si los CSV salieron de otra versión (buscar en el historial el commit que generó `rc1_calibracion.csv`).
  - [ ] Adaptar las llamadas a la API actual (o restaurar la versión de `snt_utils_v32` que el script esperaba).
  - [ ] Regenerar y comparar contra los `rc1_*.csv` versionados.
  - [ ] Documentar el resultado en `CHANGELOG.md` y en `audits/README.md`.
- **Criterio de cierre:** el script corre de punta a punta y reproduce los CSV (o se documenta la diferencia).

### 1.2 Test de regresión para RC1 — depende de 1.1
- [ ] Agregar un test que fije las cifras de RC1 que cita el README (E3 80,3 %, B 96,8 %, ACO 48,9 %, C 22,6 %, E2_01 94,0 %). Hoy `claims.yaml` ya las verifica contra los CSV, pero no contra el script que las genera.

### 1.3 Sellado externo de los preregistros — **Decisión**
- **Hoy:** los preregistros (`reconstruction_real/preregistro/`) están en commits anteriores a los resultados, pero con fecha de git, que controla el autor.
- [ x] Subir los 10 preregistros a OSF (o a un release de Zenodo) para tener una fecha verificable por terceros.
- [x ] Enlazar el registro externo desde `audits/README.md`.
https://doi.org/10.5281/zenodo.23653089

### 1.4 Release v2.7.1 en Zenodo y `CITATION.cff` — **Decisión**
- **Hoy:** el DOI `10.5281/zenodo.19446521` archiva v2.5.0; el manuscrito r32 se basa en v2.6.1.
- [ x] Hacer el release v2.7.1 y activar la integración GitHub–Zenodo para releases futuros.
- [ x] Actualizar `CITATION.cff` con el DOI nuevo.
- [ actualizar con la version 2.7.1] Confirmar en SSRN (abstract `6418778`) qué versión del manuscrito está publicada; el repo indica que la carga de r32 estaba pendiente.

### 1.5 URL del repositorio de Genomic — **Decisión (requiere un dato)**
solo mencionar a uno versionado en github hasta terminar actualizaciones y pruebas
- [ ] Pasar la URL del repo de `genomic_agent`.
- [ ] Sustituir `/home/deamon/genomic_agent` en `README.md` (línea ~483), `AGENTS.md` y `CLAUDE.md`.

---

## 2. Reproducibilidad e infraestructura

### 2.1 Binarios pesados → Git LFS o DVC — **Decisión**
- **Hoy:** `.git` pesa 49 MB. Archivos grandes: `figures/Fig1–Fig4.tif` (~6 MB c/u), `data/COW_Trade_4.0.zip` (12 MB), `reconstruction_real/data/tela_exogena_series.csv` (5,9 MB), `data/binance_cierres_diarios.csv.gz` (3,8 MB).
- [ ] Elegir LFS o DVC.
- [ ] Mover los archivos (los checksums ya están en `data/FUENTES.md`).
- [ ] Verificar que el CI sigue funcionando sin descargar los binarios que no necesita.

### 2.2 Lockfile
- [ ] Generar `conda-lock` o `pip-compile` y fijar versiones de numpy, scipy, pandas y statsmodels.
- **Motivo:** `tela_exogena.py` regenera los CSV con diferencias de ~1e-16 al cambiar de entorno numérico (ver 2.3); sin lockfile no hay igualdad byte a byte entre máquinas.

### 2.3 Reproducibilidad de `tela_exogena.py`
- [ ] Decidir la política: (a) fijar entorno y exigir igualdad exacta, o (b) tolerancia relativa documentada (el test de la auditoría ya usa `rtol=1e-9`).
- [ ] Si es (b), redondear a un número fijo de decimales al escribir los CSV para que los diffs de git sean estables.

### 2.4 Semillas — revisión manual
- **Hoy:** 20 scripts usan RNG; la búsqueda automática solo encontró uno sin semilla (`matriz_mexico_ncuerpos.py`, ya corregido). Fue un grep, no una lectura.
- [ ] Revisar a mano los 20 scripts con `np.random`, `default_rng` o `random`.
- [ ] Verificar que cada simulación pre-registrada fija su semilla y que la semilla aparece en el informe.

### 2.5 `environment-dev.yml` sin configuración
- [ ] Elegir un solo conjunto (propuesta: `ruff` + `pytest`) y configurarlo, o quitar `pre-commit`, `black`, `isort`, `mypy` y `tox`, que hoy no tienen configuración.

---

## 3. Calidad de código

### 3.1 Paquete `snt/` — **Decisión (cambio invasivo)**
- [ ] Crear `pyproject.toml` y un paquete `snt/` instalable con `pip install -e .`.
- [ ] Consolidar duplicados: `fit_power_law` / `ajustar_ley_potencia` (×3), `sha256` (×11), `configurar_log` (×6).
- [ ] Unificar `code/snt_utils.py` (80 líneas, solo lo usa `Legacy/`) con `code/snt_utils_v32.py` (568 líneas); quitar el sufijo de versión del nombre.
- [ ] Eliminar los `sys.path.insert` + `# noqa: E402` de los scripts y tests.

### 3.2 Lint residual
- [ ] 34 avisos `F541` (f-strings sin placeholders).
- [ ] ~1 600 avisos E/W con `--max-line-length=120` (la mayoría `W503` y `E702`). Cosmético; decidir si se activa `ruff format`.

### 3.3 Separar lo que no es SNT
- [ ] Mover `delta/` (motor de señales cripto/bolsa) y `dashboard/` a repos propios, como se hizo con Genomic.

---

## 4. Documentación

- [ ] **README:** mover la sección «Evolución» a `docs/HISTORIA.md` y dejar arriba solo estado actual, tabla de evidencia y cómo reproducir. Hoy pesa 28 KB.
- [ ] **README:** aclarar que el «8 de 8, p = 0,0039» de las ciudades es el valor **mínimo alcanzable** con n = 8 en un Wilcoxon unilateral (1/256), no un resultado particularmente fuerte.
- [ ] **CHANGELOG:** partirlo por año (hoy 96 KB).
- [ ] **Claims:** ampliar `claims.yaml` (hoy 30 cifras). Sin claim todavía: 8/8 de ciudades, npm (ρ = +0,114, IC95), hazard (ρ = −0,716), ACO abrupto vs gradual (p = 0,101 y 0,938), hub comercial (ρ = −0,153; p = 0,125 y 0,78), B 446/446 pendientes reproducidas, fricción por dominios (ρ = −0,556; −0,131), HackerEarth (AUC 0,836 y 0,893).
- [ ] Revisar que el `AGENTS.md` y `CONTRIBUTING.md` describan igual el flujo (el primero ya menciona pytest en CI; el segundo no).

---

## 5. Ciencia pendiente (no son fixes: son pruebas nuevas)

### 5.1 Nulos para ACO-A
- **Pregunta:** ¿la convergencia de `|log₁₀ m|` hacia 0 (0,292 → 0,071, n = 18) es una firma del colapso o regresión a la media?
- **Cómo:** simular pares de series AR(1) con la misma autocorrelación y la misma regla de selección por colapso, y medir si también convergen a `m ≈ 1`.
- **Salida esperada:** preregistro + script + informe en `audits/`.

### 5.2 Cointegración hub–nodo
- [ ] Aplicar Engle-Granger o Johansen a las series de B, E3 y ACO **antes** de interpretar `R(t)` y `b`. Es el control estándar contra regresión espuria en razones de series con tendencia.

### 5.3 Modelo jerárquico de `b` por dominio
- [ ] Ajustar un modelo mixto o bayesiano (MixedLM o PyMC) con partial pooling, en lugar de tratar 721 filas como casos independientes. Con n_eff mediano de 2,2 en B, esto maneja la dependencia explícitamente.

### 5.4 Prueba prospectiva de ACO-A
- [ ] Congelar hoy una cohorte nueva (candidatos ya en el repo: `hazard_crypto.py`, cierres de Binance, npm).
- [ ] Escribir la predicción por escrito (Δ y convergencia a `m ≈ 1`) y sellarla externamente (ver 1.3).
- [ ] Evaluar después del corte, sin cambiar los criterios.

### 5.5 Prueba alternativa para el tono φ
- **Hoy:** la forma de la trayectoria no distingue el tono φ de una asignación aleatoria de tonos a dominios (`audits/TELA_CLASIFICACION_BASELINE_2026-10-25.md`).
- [ ] Si se quiere sostener φ, hace falta una prueba que no sea una etiqueta constante por dominio: medir φ por caso (continuo) o usar dominios nuevos con φ asignado **antes** de ver los datos.

---

## 6. Hallazgos ya documentados (no requieren acción, solo conocerlos)

- La clasificación de la tela por dominio (50,7 %) queda por debajo de la línea base mayoritaria (60,5 %); la exactitud balanceada (55,6 %) sí supera el azar (11,1 %).
- E3 acierta 94 % en esa clasificación en buena parte por la receta de selección (umbral de nacimiento), no por dinámica.
- Los preregistros están en commits previos a los resultados; falta sellado externo (1.3).
- La auditoría integral v32 se reproduce idéntica (57 cifras; 29 con estado REPLICA) y ahora está bajo test.

---

## Orden sugerido

1. Integrar la rama (sección 0).
2. 1.1 → 1.2 (RC1).
3. 1.5 y 1.4 (datos que solo tú tienes).
4. 1.3 (sellado externo) antes de cualquier prueba prospectiva nueva.
5. 5.1 y 5.2 (las pruebas que más pueden cambiar una conclusión).
6. 2.x y 3.x en paralelo cuando haya tiempo.
