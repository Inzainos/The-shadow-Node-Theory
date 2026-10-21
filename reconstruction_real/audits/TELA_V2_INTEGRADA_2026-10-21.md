# Tela v2 Integrada — Series Reales donde Existen + Sombra solo donde Faltan

**Fecha:** 2026-10-21
**Script:** `code/tela_de_incertidumbre.py` (v2) sobre
`code/tela_exogena.py`
**Salidas:** `data/tela_de_incertidumbre.csv` (v2: 51,210 puntos),
figuras cimáticas regeneradas, LOO re-medidos
**Rama:** `local/tela-v2-exogena`

## Qué cambió

| | v1 (2026-10-21 mañana) | **v2 (integrada)** |
|---|------------------------|--------------------|
| Casos reales (serie cruda) | 18 (ACO) | **699** (E3 234, B 446, ACO 18, G 1) |
| Sombras | 721 | **41** (A, C, D, E1, E2, F — sin serie cruda versionada) |
| Total | 739 casos / 7,306 puntos | **740 casos / 51,210 puntos** |

Regla de la v2: **serie real donde existe, sombra solo donde falta.** El
script degrada honestamente a v1 si `tela_exogena_series.csv` no existe.

## Nacimiento por dominio (real, log₁₀ m en τ=0)

| Dominio | Nace en (mediana) | Muere en (mediana) | Firma |
|---------|--------------------:|-------------------:|-------|
| E3 | **+2.16** | +3.38 | nace en ~100+ casos (umbral de la receta) — firma de dominio |
| B | +0.09 | +0.17 | nace en la razón PIB real del primer año |
| ACO | **−0.29** | **+0.04** | nace debajo de 1, **converge a m≈1** |
| C/A/E2 | 0.00 | +0.05 a +0.17 | sombras (nacen en 1 por construcción) |
| G | −0.26 | −0.70 | cae (proxy geoquímico Bennu) |
| D, F1 | 0.00 | −2.2 a −4.3 | sombras que caen (b<0) |
| E1, F2 | 0.00 | +4.3 a +6.2 | sombras que vuelan (b alto) |

## Corrección honesta de la lectura del cometa (v1 → v2)

**El "salen del mismo punto" era artefacto de las sombras.** En v1 las
721 sombras nacían exactamente en m=1 (a=1, t=1) y la lectura del
cometa —cabeza-fuente única— heredaba esa construcción. En v2 los casos
reales **nacen en la escala natural de su dominio** (E3 en +2.16
décadas, ACO en −0.29) y el abanico ya nace abierto: IQR 2.05 décadas en
τ=0 (v1: 0.00).

**Lo que SOBREVIVE a la corrección:**
1. **La cabeza persiste**: 60.1% → 54.9% de los casos siguen viviendo
   en la banda de equilibrio m ∈ [0.56, 1.78] — ahora sostenida por
   datos reales (B, C, A), no por construcción.
2. **La estela persiste**: el abanico se abre de 4.72 a 13.38 décadas al
   avanzar la fase — los regímenes extremos siguen separándose.
3. **ACO converge a la cabeza**: |log₁₀ m| mediana 0.292 → 0.071
   (n=18, sin cambio — eran reales desde v1). Nacer debajo de 1 y
   morir en 1 sigue siendo la firma del colapso.

## LOO re-medido sobre la tela integrada

| Prueba | v1 (sombras) | **v2 (integrada)** |
|---------|--------------:|-------------------:|
| Dominio, todos los rasgos | 21.2% | **50.7%** |
| Dominio, solo-forma | 19.8% | 41.9% |
| Tono φ, todos los rasgos | 53.7% | **66.2%** |
| Tono φ, solo-forma | 43.7% | 58.6% |

Por dominio (todos los rasgos): **E3 219/234 = 94%** · A 4/4 · F1 2/2 ·
B 137/446 = 31% · C 3/24 · ACO 4/18.

Por tono: **nula 230/241 = 95%** · alta 248/472 = 52% · variable 7/18.

**Lectura:** las series reales cargan firma de dominio que las sombras
borraban — el nacimiento de E3 en +2.16 (umbral de receta) es
inconfundible. B sigue confundiéndose (sus razones viven donde viven las
de C/E2 — mismo φ alta). ACO como *etiqueta* cayó (4/18) porque sus
trayectorias se parecen a las de B en forma; su firma real es la
**convergencia terminal a m≈1**, no la forma global.

## Limitaciones

- El nacimiento de E3 en +2.16 décadas es semilla de REQUISITO DE
  RECETA (≥100 casos acumulados), no física pura: identifica la receta
  tanto como el dominio.
- B/C/E2 comparten φ y rango: el tono `alta` no es recuperable de la
  forma (52%).
- ACO: n=18; convergencia medida, inferencia no concluyente.
- 41 sombras restantes siguen con m(τ=0)=1 por construcción.

## Reproducir

```bash
python reconstruction_real/code/tela_exogena.py            # 699 series
python reconstruction_real/code/tela_de_incertidumbre.py   # tela v2
python reconstruction_real/code/tela_cimatica.py           # placa + LOO
```

---

*Fractal Core Research · Tlaxcala, México · 2026-10-21*
