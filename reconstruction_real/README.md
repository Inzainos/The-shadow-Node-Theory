# SNT Corpus — Reconstrucción con Datos Reales (v3)

## Propósito
Reconstrucción del corpus de Shadow Node Theory usando **exclusivamente datos
primarios reales y trazables**, reemplazando valores que no eran reproducibles
desde fuentes verificables.

## Estado actual: 266 casos reales

| Dominio | Casos | Fuente | Significativos | R² medio |
|---------|-------|--------|----------------|----------|
| B — Países | 258 | Maddison Project 2020 | 85% | 0.41 |
| D — Digital | 3 | HackerEarth 2026 | 100% | 0.88 |
| F — Astronómico | 2 | Open Exoplanet Catalogue | 100% | 0.40 |
| E2 — Depredador-presa | 2 | MacLulich 1937 / Elton 1942 | — | 0.12 |
| C — México N-body | 1 | INEGI 2022 | 100% | 0.87 |

**Total: 266 casos | 85% significativos | CERO valores R² corruptos**

## Garantías de integridad
- Todos los R² ∈ [0,1] (verificado)
- Todos los p ∈ [0,1] (verificado)
- Cada valor de b reproducible desde el script correspondiente
- Sin datos sintéticos ni generados aleatoriamente

## Metodología
Para cada caso:
1. R(t) = métrica_hub(t) / métrica_nodo(t)
2. Linealización log-log: log R(t) = log a + b·log t
3. OLS → b (exponente de satelización)
4. R² real, Durbin-Watson, 95% CI

## Fuentes de datos
- **Maddison Project Database 2020** (Bolt & van Zanden) — PIB per cápita histórico
- **INEGI 2022** — PIB per cápita por entidad federativa (México)
- **HackerEarth 2026** — datos de comportamiento de 4,771 usuarios
- **MacLulich 1937 / Elton & Nicholson 1942** — series lince-liebre Hudson Bay
- **Open Exoplanet Catalogue** — masas planetarias y estelares

## Hallazgo central (verificable)
La satelización (exponente b) varía sistemáticamente según la fricción
institucional. En el dominio B (países), el gradiente por región es claro:
- Convergencia (b<0): Europa, Sudamérica (integración, instituciones fuertes)
- Satelización (b>0): África Subsahariana, Asia Sudeste (mayor divergencia)

## Pendiente de reconstrucción
- A (ciudades históricas): requiere Bairoch 1988 / Buringh (datos en libros)
- C (regiones, resto): OECD/Eurostat
- E1, E3 (biológico): extracción de literatura
- F2-F4 (estelar/galáctico): catálogos SIMBAD/NASA

## Reproducibilidad
```bash
cd code/
python3 expand_dominio_B.py   # regenera los 258 casos del dominio B
```
