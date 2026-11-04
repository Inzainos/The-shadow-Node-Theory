# Resultados — eje u Permutación/DimCor v2.7.5

**Pre-registro:** `reconstruction_real/preregistro/PREREGISTRO_EJE_U_PERMUTACION_DIMCOR_2026-11-04.md`
**Script:** `eje_u_permutacion_dimcor.py`
**Fecha:** 2026-11-04

## Procedencia
SHA-256 inputs registrados en log.

## Nota de implementación
Esta corrida reconstruye `R(t) = PIBpc_hub / PIBpc_nodo` desde Maddison MPD2020 para Dominio B y estima Dimensión de Correlación para Cripto con ventana 200.

## Resumen Dominio B (real)
- Casos: 446
- Mediana Spearman θ1/θ2: 0.929
- Mediana IQR: 0.169
- Invarianza pasa: True
- Variación pasa: True

## Resumen Cripto D2
- Casos: 19
- Elegibles: 19
- Mediana D2: 0.730
- Mediana IQR D2: 0.227

## Próximos pasos
- Calcular métricas por ventana deslizante para compuertas de invarianza A–D completas y decisión pre-especificada.
- Refinar estimador D2 con muestreo adaptativo y rango r optimizado.
