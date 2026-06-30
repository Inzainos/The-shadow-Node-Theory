# SNT Corpus -- Reconstruccion con Datos Reales (v5 / v2.5.0)

## Estado: 721 casos REALES en 11 dominios

| Dominio | Casos | Sig. | b mean | R2 mean | Fuente |
|---------|-------|------|--------|---------|--------|
| A -- Ciudades | 4 | 0% | +0.08 | 0.18 | UN Demographic Yearbook |
| B -- Paises | 446 | 84% | +0.09 | 0.35 | Maddison Project 2020 |
| C -- Regiones | 24 | 100% | +0.09 | 0.53 | INEGI 2022 + US Census |
| D -- Digital | 3 | 100% | -1.36 | 0.87 | HackerEarth 2026 |
| E1 -- Invasion | 4 | 100% | +2.89 | 0.81 | OWID COVID-19 spatial |
| E2 -- Depred-presa | 2 | 50% | +0.15 | 0.12 | MacLulich 1937 / Elton 1942 |
| E3 -- Parasito-huesped | 234 | 100% | +0.91 | 0.85 | JHU COVID-19 |
| F1 -- Planetario | 2 | 100% | -1.81 | 0.40 | Open Exoplanet Catalogue |
| F2 -- Estelar | 1 | 100% | +1.27 | 0.48 | Open Exoplanet Catalogue |
| F3 -- Multiplanet | 1 | 100% | +1.26 | 0.90 | Open Exoplanet Catalogue |
| ACO -- Colapso Acoplado | 18 | 94% | +0.60 | 0.87 | ver build_aco_v29.py |

**Total: 721 casos satelizacion + 18 casos ACO | CERO R2 corruptos**| 89% significativos | CERO R2 corruptos**

## Hallazgo central (datos reales)

A nivel de casos individuales en dominios sociales/biologicos (n=714):
**Spearman rho = -0.68, p = 2.5x10^-97**

La friccion institucional predice la satelizacion: dominios con alta
friccion (paises, regiones: b~0.09) vs sin friccion (invasion, epidemias:
b~+0.95). El gradiente es nitido y altamente significativo.

**Mann-Whitney p = 2.4x10^-74**

## Integridad
- Todos los R2 in [0,1] -- verificado
- Todos los p in [0,1] -- verificado
- Cada b reproducible desde datos primarios
- Sin datos sinteticos

## Cambio de v4 a v5
- Dominio B expandido: 258 -> 446 pares de paises (Maddison completo)
- Dominio E3 expandido: 15 -> 234 casos (COVID-19 JHU, 234 paises)
- Spearman actualizado: rho=-0.39 (v4, n=307) -> rho=-0.68 (v5, n=714)

## Notas de honestidad metodologica
- **Dominio A**: solo datos UN modernos (2000-2024), pocos puntos -> no
  significativo. Requiere Bairoch 1988 para casos historicos largos.
- **E1/E3**: modelados como expansion territorial/epidemica (COVID JHU),
  matematicamente equivalentes a invasion. Datos GBIF de especies bloqueados.
- **Dominios fisicos (F)**: siguen ley de potencia pero su "friccion" es
  fisica (Eddington, resonancia orbital), no institucional.

## Fuentes (todas publicas y verificables)
- Maddison Project Database 2020 (Bolt & van Zanden)
- INEGI 2022 (Mexico) + US Census Bureau (estados)
- HackerEarth 2026
- OWID COVID-19 dataset (Johns Hopkins)
- MacLulich 1937 / Elton & Nicholson 1942 (lince-liebre)
- Open Exoplanet Catalogue

## Archivos
- `data/snt_corpus_REAL_v5.csv` -- corpus consolidado (721 casos)
- `data/MASTER_cifras_v5.json` -- todas las cifras del paper
- `data/MASTER_resumen_v5.csv` -- resumen por dominio
- `data/by_domain/` -- CSV individual por dominio con metadatos completos
- `code/expand_dominio_B.py` -- reproduce 446 casos B (Maddison)
- `code/build_dominio_B.py` -- construye dominio B
