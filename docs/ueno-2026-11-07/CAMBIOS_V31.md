# CAMBIOS_V31

> Nota: en este archivo la ruta local original se escribe como `[ruta-local]/` y su carpeta como `[carpeta-local-original]`, para no reintroducir la ruta local en el repo. Los valores exactos sustituidos se describen en §2. — Corrección v3.1 de Ueno (2026-11-09)

**Orden:** Elán (2026-11-09 ~13:19): que MOLE corrija los 3 problemas que Claude encontró al auditar la rama `docs/ueno-v3-2026-11-07` (commit `ed0e130`), no Claude.
**Base:** copia de `el staging v3 (docs/ueno-2026-11-07/)` (lo que ya está en la rama, carpeta `docs/ueno-2026-11-07/`). Solo cambia lo necesario para los 3 problemas; el resto byte a byte.
**Regla:** NUNCA ASUMAS, SIEMPRE VERIFICA. No se inventaron números ni hechos. No se tocó `main`, ni el espacio SNT, ni los originales en el equipo local.

## 1. Cambios de contenido (21 + 1)

1. **verificar_v3.py** — P1: ruta local retirada; el script debe correr en el repo
   - Antes: `Lee [ruta-local]/[carpeta-local-original]/tabla-maestra-ueno-mef.csv y recomputa:`
   - Después: `Lee tabla-maestra-ueno-mef.csv, en la misma carpeta que este script, y recomputa:`

2. **verificar_v3.py** — P1: CSV junto al script (Claude: FileNotFoundError en repo)
   - Antes: `CSV = os.path.expanduser("[ruta-local]/[carpeta-local-original]/tabla-maestra-ueno-mef.csv")`
   - Después: `CSV = Path(__file__).parent / "tabla-maestra-ueno-mef.csv"`

3. **verificar_v3.py** — P1: os ya no se usa tras el cambio de ruta
   - Antes: `import os`
   - Después: `from pathlib import Path`

4. **rastro-del-dinero-ueno-v3.md** — P2: frase retirada por recomendación de auditoría (Claude)
   - Antes: `**Fractal Core Research — PARAGUAY SÍ SE PUEDE COMPARTIR Y EXPONER (decisión de Elán, 2026-11-07 ~03:17: [frase retirada en v3.1]).** Lo interno y sin publicar es el mapeo MUNDIAL del dinero, no el de Paraguay.`
   - Después: `[línea eliminada] + nota v3.1 al inicio`

5. **REVISION_DOCUMENTOS_UENO.md** — P2: se conserva la auditoría como registro; la cita histórica queda solo en §1.3
   - Antes: `[sin cambio de cuerpo]`
   - Después: `Nota v3.1 al inicio`

6. **podcast/script-v3.txt** — P2: salvaguarda hablable al inicio del guion
   - Antes: `Mole: El dos de noviembre...`
   - Después: `Mole: Antes de empezar: [salvaguarda] El dos de noviembre...`

7. **podcast/script-v3.txt** — P2: atribución explícita USD 146M (fuente: parteaguas § salvadoras / Informe Intendencia 8 jun 2026)
   - Antes: `Mole: Entre septiembre... Ueno desembolsó...`
   - Después: `Mole: Según el informe de supervisión del 8 jun 2026... Ueno desembolsó...`

8. **podcast/script-v3.txt** — P2: atribución explícita traspaso (fuente: parteaguas-notas-v3 L36, Informe Intendencia 8 jun 2026)
   - Antes: `Mowi, Grupo Hendy y Grupo M fueron traspasados...`
   - Después: `Según ese mismo informe de supervisión del 8 jun 2026, Mowi...`

9. **podcast/script-v3.txt** — P2: atribución explícita embargo; nombres conservados porque son los de la orden de embargo
   - Antes: `El tres de noviembre, el juzgado ordenó el embargo preventivo, contra...`
   - Después: `Según la orden de embargo del 3 nov, el juzgado ordenó... Son los nombres que aparecen en esa orden y en la denuncia del MEF del 5 nov.`

10. **podcast/script-v3.txt** — P3: guarda descriptiva en la be de la serie completa
   - Antes: `El número único de toda la serie... esconde los tres regímenes.`
   - Después: `+ guarda: descriptor, no prueba; un solo caso, sin nulo, sin preregistro`

11. **podcast/script-v3.txt** — P3: guarda descriptiva en las bandas Roche
   - Antes: `Las tres cruzadas: colapso completo con trigger legal.`
   - Después: `+ guarda: lectura descriptiva a posteriori; las bandas describen, no validan`

12. **video-largo-ueno/guion-video-largo.txt** — P2: salvaguarda hablable al inicio del guion
   - Antes: `Ueno Bank, Paraguay. La investigación completa...`
   - Después: `+ salvaguarda hablable al inicio (C1a)`

13. **video-largo-ueno/guion-video-largo.txt** — P2: atribución explícita embargo; nombres conservados porque son los de la orden
   - Antes: `Contra U Paraguay... Son nombres de documentos públicos...`
   - Después: `Según la orden de embargo del 3 nov 2026, contra... Son los nombres que aparecen en esa orden y en la denuncia del MEF del 5 nov.`

14. **video-largo-ueno/guion-video-largo.txt** — P3: guarda descriptiva en las bandas Roche
   - Antes: `Las tres bandas cruzadas significan colapso completo con trigger legal.`
   - Después: `+ guarda descriptiva: un solo caso, a posteriori, sin nulo ni preregistro`

15. **video-largo-ueno/guion-video-largo.txt** — P3: guarda descriptiva en la meseta
   - Antes: `Después la deriva se detuvo: la be es cero punto cero tres uno, sin tendencia medible.`
   - Después: `+ guarda: la meseta solo respalda sin tendencia, no una estructura`

16. **video-resumen-ueno/guion-video.txt** — P2: salvaguarda hablable al inicio del guion
   - Antes: `Ueno Bank, Paraguay. En noviembre...`
   - Después: `+ salvaguarda hablable al inicio (intro)`

17. **video-resumen-ueno/guion-video.txt** — P3: guarda descriptiva en la be y las bandas
   - Antes: `Es un descriptor de la ventana, no una prueba de mecanismo...`
   - Después: `+ guarda: meseta solo respalda sin tendencia; un solo caso, a posteriori, sin nulo ni preregistro`

18. **modelo-ueno-resultados-v3.md** — P3: guarda descriptiva en las bandas
   - Antes: `## 10. Las bandas determinan el colapso`
   - Después: `+ Guarda v3.1 tras el encabezado §10`

19. **modelo-ueno-resultados-v3.md** — P3: guarda descriptiva en las conclusiones
   - Antes: `## 11. Qué muestran los modelos`
   - Después: `+ Guarda v3.1 tras el encabezado §11`

20. **modelo-ueno-resultados-v3.md** — P3: guarda descriptiva en el backcast
   - Antes: `## 13. El backcast v3`
   - Después: `+ Guarda v3.1 tras el encabezado §13`

21. **modelo-ueno-resultados-v3.md** — P3: guarda descriptiva en b=0.8234
   - Antes: `El ajuste de toda la serie (b ≈ 0.82...) resume tres regímenes...`
   - Después: `+ autocorrelación fuerte, sin n_eff ni nulo: descriptor, no prueba`


22. **rastro-del-dinero-ueno-v3.md** — P2: atribución explícita al embargo en §4.
   - Antes: `**Gs 2.1005 billones** en total ... Contra U Paraguay S.A., ...`
   - Después: `... Según la orden de embargo del 3 nov 2026, contra U Paraguay S.A., ...`

## 2. Sustituciones de rutas locales (Problema 1, 22 archivos tocados)

Regla aplicada, en este orden: la ruta de staging local → `docs/ueno-2026-11-07/`; la carpeta local original → `docs/ueno-2026-11-07/` para los archivos que están en esta carpeta del repo; `mef-informe-bancos/` y `auditoria-terminos/` → con la nota `(no incluido en el repo)` porque no están en la rama; las fuentes subidas por el autor → `fuentes del autor (no incluidas en el repo)`; cualquier resto de ruta del equipo local → `el equipo local`.
En la auditoría (`REVISION_DOCUMENTOS_UENO.md`, registro histórico) las rutas de su tabla de inventario se actualizaron a la ubicación de cada archivo en el repo; eso no cambia sus cifras ni sus citas de línea.

- `README_UENO_V3.md`: `el staging v3 (docs/ueno-2026-11-07/)` → `docs/ueno-2026-11-07/` (×1)
- `README_UENO_V3.md`: `[ruta-local]/[carpeta-local-original]/auditoria-terminos/` → `auditoria-terminos/ (no incluido en el repo)` (×1)
- `README_UENO_V3.md`: `[ruta-local]/[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `REVISION_DOCUMENTOS_UENO.md`: `[ruta-local]/[carpeta-local-original]/auditoria-terminos/` → `auditoria-terminos/ (no incluido en el repo)` (×1)
- `REVISION_DOCUMENTOS_UENO.md`: `[ruta-local]/[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `REVISION_DOCUMENTOS_UENO.md`: `[ruta-local]/user/files/` → `fuentes del autor (no incluidas en el repo)` (×1)
- `REVISION_DOCUMENTOS_UENO.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×25)
- `VERIFICACION_UENO_V3.md`: `el staging v3 (docs/ueno-2026-11-07/)` → `docs/ueno-2026-11-07/` (×1)
- `VERIFICACION_UENO_V3.md`: `[ruta-local]/[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `VERIFICACION_UENO_V3.md`: `[carpeta-local-original]/auditoria-terminos/` → `auditoria-terminos/ (no incluido en el repo)` (×1)
- `VERIFICACION_UENO_V3.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×2)
- `VERIFICACION_V3.md`: `[ruta-local]/[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `backcast-roche-notas-v3.md`: `el staging v3 (docs/ueno-2026-11-07/)` → `docs/ueno-2026-11-07/` (×1)
- `backcast-roche-notas-v3.md`: `[ruta-local]/user/files/` → `fuentes del autor (no incluidas en el repo)` (×1)
- `finanzas-mundo-snt.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `forecast-ueno-2026-11-06.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `modelo-ueno-resultados-v2.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `modelo-ueno-resultados.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `modelo-ueno-valores-v2.csv.NOTA.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `modelo-ueno-valores.csv.NOTA.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `parteaguas-notas-v3.md`: `el staging v3 (docs/ueno-2026-11-07/)` → `docs/ueno-2026-11-07/` (×1)
- `parteaguas-notas-v3.md`: `[ruta-local]/user/files/` → `fuentes del autor (no incluidas en el repo)` (×1)
- `podcast/topics-v3.md`: `el staging v3 (docs/ueno-2026-11-07/)` → `docs/ueno-2026-11-07/` (×1)
- `rastro-del-dinero-ueno-v3.md`: `el staging v3 (docs/ueno-2026-11-07/)` → `docs/ueno-2026-11-07/` (×1)
- `tabla-maestra-NOTAS-v1.md`: `[ruta-local]/[carpeta-local-original]/mef-informe-bancos/` → `mef-informe-bancos/ (no incluido en el repo)` (×2)
- `tabla-maestra-NOTAS-v1.md`: `[ruta-local]/[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×3)
- `tabla-maestra-NOTAS-v1.md`: `[ruta-local]/user/files/` → `fuentes del autor (no incluidas en el repo)` (×1)
- `tabla-maestra-NOTAS-v1.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `tabla-maestra-NOTAS.md`: `[ruta-local]/[carpeta-local-original]/mef-informe-bancos/` → `mef-informe-bancos/ (no incluido en el repo)` (×2)
- `tabla-maestra-NOTAS.md`: `[ruta-local]/[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×3)
- `tabla-maestra-NOTAS.md`: `[ruta-local]/user/files/` → `fuentes del autor (no incluidas en el repo)` (×1)
- `tabla-maestra-NOTAS.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `tabla-maestra-ueno-mef-v1.csv.NOTA.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `tabla-maestra-ueno-mef.csv.NOTA.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `ueno-acoa-tela-cimatica-incertidumbre.md`: `[ruta-local]/[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `ueno-acoa-tela-cimatica-incertidumbre.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `ueno-huella-cimatica-NOTA.md`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `video-largo-ueno/guion-video-largo.txt`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)
- `video-resumen-ueno/guion-video.txt`: `[carpeta-local-original]/` → `docs/ueno-2026-11-07/` (×1)

## 3. Decisiones y límites (para el padre / Elán)

- **Nombres de personas físicas conservados solo donde son los de la orden de embargo** (modelo v3 §13, rastro §4, forecast, parteaguas, y los dos guiones con embargo): todos con atribución explícita a la orden de embargo del 3 nov 2026 y/o a la denuncia del MEF del 5 nov 2026. En ningún guion se sustituyó un nombre por su rol, porque en los tres casos el nombre aparece como parte de la lista del embargo, no como afirmación suelta del locutor.
- **Traspaso Mowi / Grupo Hendy / Grupo M:** atribuido en el podcast al Informe de la Intendencia de Supervisión del 8 jun 2026 (fuente: parteaguas-notas-v3, circuito de las salvadoras). No se afirmó como hecho propio.
- **USD 146M (podcast):** atribuido al informe de supervisión del 8 jun 2026, recogido en el parteaguas. No se cambió la cifra.
- **Frase retirada:** **0 ocurrencias en todo el staging tras el scrub del padre antes del push.** La cita histórica que quedaba en `REVISION_DOCUMENTOS_UENO.md:41` (§1.3, tabla de inventario) fue sustituida por "[anotación personal retirada en v3.1]"; la nota v3.1 al inicio de la auditoría explica el retiro. En todos los documentos v3.1 la frase está retirada.
- **Video guiones: números v2 pendientes.** Los guiones de video largo y resumen son copias de registro con los números v2 del guion original (30 meses, meseta +0.031, +511,865M). La v3.1 solo les añadió atribución, salvaguarda y guarda descriptiva; NO actualizó sus números a v3, porque eso queda fuera de los 3 problemas de Claude. Si se van a hablar, hay que actualizar sus cifras a v3 antes.
- **Audio del podcast:** sigue sin regrabar (episodio-v2.mp3 con números v1). El guion v3.1 está listo; la regrabación es decisión de Elán.
- **No se añadió ningún hecho nuevo ni se cambió ningún número.**
