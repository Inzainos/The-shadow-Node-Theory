# SNT Corpus — Reconstrucción con Datos Reales (v4)

## Estado: 314 casos REALES en los 11 dominios

| Dominio | Casos | Sig. | b̄ | R̄² | Fuente |
|---------|-------|------|-----|-----|--------|
| A — Ciudades | 4 | 0% | +0.08 | 0.18 | UN Demographic Yearbook |
| B — Países | 258 | 85% | +0.08 | 0.35 | Maddison Project 2020 |
| C — Regiones | 24 | 100% | +0.09 | 0.53 | INEGI 2022 + US Census |
| D — Digital | 3 | 100% | −1.36 | 0.87 | HackerEarth 2026 |
| E1 — Invasión | 4 | 100% | +2.89 | 0.81 | OWID COVID-19 spatial |
| E2 — Depred-presa | 2 | 50% | +0.14 | 0.12 | MacLulich 1937 / Elton 1942 |
| E3 — Parásito-huésped | 15 | 100% | +1.87 | 0.89 | OWID COVID-19 (JHU) |
| F1 — Planetario | 2 | 100% | −1.81 | 0.40 | Open Exoplanet Catalogue |
| F2 — Estelar | 1 | 100% | +1.27 | 0.48 | Open Exoplanet Catalogue |
| F3 — Multiplanet | 1 | 100% | +1.26 | 0.90 | Open Exoplanet Catalogue |

**Total: 314 casos | 86% significativos | CERO R² corruptos**

## Hallazgo central (datos reales)
A nivel de casos individuales en dominios sociales/biológicos (n=307):
**Spearman ρ = −0.39, p = 1.5×10⁻¹²**

La fricción institucional predice la satelización: dominios con alta
fricción (países, regiones: b≈0.08) vs sin fricción (invasión, epidemias:
b≈1.9-2.9). El gradiente es nítido y altamente significativo.

## Integridad
- Todos los R² ∈ [0,1] — verificado
- Todos los p ∈ [0,1] — verificado
- Cada b reproducible desde datos primarios
- Sin datos sintéticos

## Notas de honestidad metodológica
- **Dominio A**: solo datos UN modernos (2000-2024), pocos puntos → no
  significativo. Requiere Bairoch 1988 para casos históricos largos.
- **E1/E3**: modelados como expansión territorial/epidémica (COVID JHU),
  matemáticamente equivalentes a invasión. Datos GBIF de especies bloqueados.
- **Dominios físicos (F)**: siguen ley de potencia pero su "fricción" es
  física (Eddington, resonancia orbital), no institucional.

## Fuentes (todas públicas y verificables)
- Maddison Project Database 2020 (Bolt & van Zanden)
- INEGI 2022 (México) + US Census Bureau (estados)
- HackerEarth 2026
- OWID COVID-19 dataset (Johns Hopkins)
- MacLulich 1937 / Elton & Nicholson 1942 (lince-liebre)
- Open Exoplanet Catalogue

## Archivos
- `data/snt_corpus_REAL_v4.csv` — corpus consolidado (314 casos)
- `data/corpus_v4_resumen_dominios.csv` — resumen por dominio
- `data/by_domain/` — CSV individual por dominio con metadatos completos
- `code/` — scripts de reconstrucción reproducibles
