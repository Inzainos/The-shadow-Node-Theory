# Desbloqueo de pendientes con datos — sesión 2026-10-18

**Naturaleza:** cuatro pendientes "bloqueados" se atacaron consiguiendo o
re-verificando los datos. Dos quedan **resueltos con resultado nuevo**, uno
queda **acotado con evidencia** y uno queda **cerrado como imposible con la
fuente pública**. Ninguno era hipótesis pre-registrada nueva: son follow-ups
declarados post-hoc de pruebas ya publicadas, salvo donde se indica.

## 1. r2_raw del Dominio E3 — RESUELTO (corpus v6 ahora 720/721)

**Pendiente:** el corpus v6 dejó `r2_raw` en NA para los 234 casos de E3
("series crudas OWID no versionadas").

**Qué se hizo:** se descargó de nuevo el archivo completo de OWID
(`raw.githubusercontent.com/owid/covid-19-data/master/public/data/
owid-covid-data.csv`, 98 MB) y el SHA-256 resultó **byte-idéntico al snapshot
anclado del 2026-09-27** (`8473d0f0fdf962e1…`): la edición es exactamente la
que produjo E3. Script `code/e3_r2_raw.py` reconstruye la serie de cada país con
la receta verificada (acumulados, primer día ≥ 100, ventana de 60 días,
t = 1..60), ajusta con `fit_powerlaw` (misma rutina de la auditoría v32) y
registra `r2_raw`.

| Verificación | Resultado |
|---|---|
| SHA-256 del OWID actual vs snapshot 2026-09-27 | **IDÉNTICO** (`8473d0f0…`) |
| Compuerta b (±0.01, criterio de la receta) | 233/234 reproducen (E3_060 East Timor, igual que el run original) |
| r2_log recomputado vs resumen committeado | max \|dif\| = 0.0000 |
| r2_raw nuevo | 233/234 casos (mediana 0.871, rango 0.051–0.982) |

**Corpus v6 actualizado:** `snt_corpus_REAL_v6.csv` ahora con
**r2_raw en 720/721** (solo E3_060 queda NA, conservador: su b no reproduce).
El archivo completo de OWID no se versiona (98 MB; `data/raw_covid/` está en
`.gitignore`), pero cualquier checkout puede reproducirlo: descargar, verificar
el SHA anclado en `FUENTES.md` y correr `e3_r2_raw.py`.

## 2. Corpus de triggers sin filtro WUP ≥ 300k — CERRADO: imposible con la fuente

**Pendiente:** re-probar los disparadores urbanos sin el filtro de
supervivencia (solo ciudades ≥ 300k en 2018).

**Qué se hizo:** se descargó el zip completo `WUP2018-Excel-files.zip` de
population.un.org y el SHA-256 coincide con el anclado
(`80eb71bbabb46cb2…`). Se enumeraron sus **27 tablas**:

- F12 y F22: ciudades ≥ 300k (la que usa el corpus) — la única con series
  por ciudad.
- F17a-d: **agregados por clase de tamaño de asentamiento** (población,
  número, porcentaje) — sin identidades por ciudad.
- F13: capitales; F11: las 30 más grandes; el resto: agregados nacionales.

**Conclusión:** la ONU **no publica series por ciudad < 300k** en el WUP2018 —
no es que falte descargar algo: el dato no existe en la fuente. Quitar el
filtro de supervivencia exigiría censos nacionales país por país (o el dataset
histórico de Reba et al., que termina en 2000 y cambia la ventana de análisis).
El pendiente queda cerrado como **imposible con la fuente pública**, con la
enumeración como evidencia.

## 3. Separación APC — ACOTADA: la diferencia entre cohortes es selección, no periodo

**Pendiente:** separar edad/periodo/cohorte del hazard. La separación completa
es matemáticamente no identificable (`periodo = cohorte + edad`). Lo máximo
alcanzable con datos committeados: comparar **las mismas edades** entre las
cohortes bancarias 1934 y 1970 (observadas en periodos calendario distintos).

Script `apc_separacion_crypto.py` (sección nueva), sobre
`aco_hazard_bandas.csv`:

| Edad (años) | h(1934+edad) | h(1970+edad) | razón 34/70 |
|---|---:|---:|---:|
| 2–32 (jóvenes) | 0.005–0.037 | 0.008–0.060 | **0.25–0.62** |
| 110–148 (viejas) | 0.027–0.032 | 0.030–0.037 | **0.85–0.92** |

Razón mediana: 0.87 (cualquier fin) y 0.82 (solo quiebras). El patrón es
**idéntico en ambos tipos de cierre**: la cohorte 1934 muestra hazard mucho
menor a edades jóvenes — justo donde sus cierres no existen en el archivo FDIC
(no registra cierres antes de 1970: truncamiento izquierdo) — y **converge a
~0.85–0.92 donde ambas cohortes ya están en zona de registro completo**
(edades 70+, ambas post-1970).

**Lectura:** la diferencia entre cohortes a la misma edad es firma de
**selección por truncamiento, no de efecto periodo**. Cuando el registro está
completo para ambas, el hazard a la misma edad casi coincide — consistente con
un modelo de pura edad. La separación APC completa sigue sin ser identificable,
pero el dato disponible **no exige un efecto periodo** en bancos. Caveat
declarado en el script: la comparación es descriptiva, no una identificación.

## 4. Fricción → Δ — ENRIQUECIDO con dos tests nuevos (post-hoc, declarados)

**Pendiente:** "friction → Δ con una cohorte mayor". Dos ampliaciones:

### 4a. ACO n=18 (extensión post-hoc del ordinal de 2008)

Script `friction_aco_18.py`. Se extendió el ordinal de fricción del test
original (pre-arreglo del canal de resolución, 1=desordenado, 6=pre-arreglado)
a los otros 12 casos ACO usando el canal **documentado** de cada uno
(conquista=1, Chapter 11=2-4, subasta §363=4, venta negociada=6,
migración de usuarios=1; tabla con citas en el script).
**La asignación es post-hoc y el autor debe validarla.**

| Test | ρ(F, Δ) | p |
|---|---:|---:|
| Original 2008 (n=6) | −1.000 | ~0.11 |
| **Extensión ACO (n=18)** | **−0.377** | 0.121 (permutación 100k) |
| Dentro de F (n=6) | −1.000 | — |
| Dentro de I (n=4) | **+0.949** | — (dirección opuesta) |
| Dentro de T (n=4) | −0.775 | — |

**Lectura:** la correlación perfecta de 2008 **no generaliza** — era
probablemente suerte de n pequeño. Casos notables contra la dirección:
Nokia (F=6, Δ=1.81) y Blockbuster (F=4, Δ=1.81); a favor: MySpace (F=1,
Δ=2.19).

### 4b. npm n=450 (codificación de fricción PRE-registrada, test post-hoc)

La cohorte npm committeada trae `friccion_a_priori` (fundación=3,
corporativa=2, otra org=1, individual/sin repo=0) — codificada **antes de ver
las series** en el pre-registro NPM 2026-10-02, incluida allí "solo para que un
análisis futuro pueda retomarla". Este es ese análisis (post-hoc, declarado).
Script `npm_followup_cohorte_friccion.py`, punto B:

| Nivel | n | mediana Δ_caida |
|---|---:|---:|
| 0 (individual/sin repo) | 139 | **−0.953** |
| 1 (otra org) | 308 | **−0.732** |
| 2 (corporativa) | 3 | −1.136 |

**Spearman(fricción, Δ_caida) = +0.163, p = 0.0005, n = 450.** La dirección es
la anticipada en el propio pre-registro ("fricción alta → caída suave"): los
paquetes sin respaldo institucional caen más pronunciado. Robusta en el
subgrupo "anunciado" (ρ=+0.363, p=0.038, n=33) y en "sin_clasificar"
(ρ=+0.151, p=0.002, n=416). Caveat: el nivel 2 tiene n=3 y el 3 no aparece en
la cohorte; la comparación efectiva es 0 vs 1.

**Lectura conjunta (4a+4b):** RC-Δ2 queda **débil pero ya no n=6**: la
asociación fricción→forma del colapso es significativa en la cohorte más
grande disponible (npm, dirección anticipada) y no generaliza en el ACO
pequeño. Por ser post-hoc, no actualiza el criterio RC por sí solo; requiere
pre-registro de réplica en otro ecosistema (p. ej. PyPI/CRAN).

## 5. npm hazard decreciente — follow-up: NO es puro artefacto de cohorte

El hallazgo nuevo del 2026-10-02 (hazard decreciente con la edad, ρ=−0.716,
p=0.013 — contrario al de cripto) podía ser mezcla de cohortes (las edades
altas solo las alcanzan los paquetes viejos). Estratificado por cohorte de
nacimiento (mismo script, punto A; el agregado reproduce exacto: ρ=−0.716):

| Cohorte de nacimiento | n | ρ(edad, hazard) dentro | p |
|---|---:|---:|---:|
| ≤ 2017 | 96 | −0.467 | 0.147 |
| 2018–2020 | 165 | −0.342 | 0.408 |
| ≥ 2021 | 189 | **−0.771** | 0.072 |

**La dirección decreciente se mantiene dentro de cada cohorte** (no es puro
artefacto de mezcla), aunque ninguna estrato alcanza significancia individual
por n. El hallazgo queda robusto en dirección, con menos certeza.

---

## Qué NO cambió

- Ningún `b`, ninguna cifra del corpus v5, ningún criterio RC pre-registrado.
- La etiqueta "Roche Radius" sigue retirada; la compuerta AIC sigue vigente.
- RC-Δ2 no se actualiza formalmente (post-hoc); requiere réplica pre-registrada.

## Reproducción

```bash
# 1. E3 r2_raw (requiere data/raw_covid/owid-covid-data.csv, SHA anclado)
python reconstruction_real/code/e3_r2_raw.py
python reconstruction_real/code/corpus_p_exacto_r2_split.py   # regenera v6

# 2. WUP: wget del zip con SHA 80eb71bb… y unzip -l (enumeración arriba)

# 3. APC mismo-edad entre cohortes bancarias
python reconstruction_real/code/apc_separacion_crypto.py

# 4a. Fricción ACO n=18
python reconstruction_real/code/friction_aco_18.py

# 4b + 5. npm follow-up
python reconstruction_real/code/npm_followup_cohorte_friccion.py
```

Todo determinista, sin red salvo las descargas indicadas (verificadas por SHA).

---

*Fractal Core Research · Tlaxcala, México · 2026-10-18*
