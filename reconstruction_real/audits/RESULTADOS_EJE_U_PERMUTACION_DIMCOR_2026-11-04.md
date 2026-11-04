# Resultados — eje u Permutación/DimCor v2.7.5

**Pre-registro:** `reconstruction_real/preregistro/PREREGISTRO_EJE_U_PERMUTACION_DIMCOR_2026-11-04.md`
**Script:** `eje_u_permutacion_dimcor.py`
**Fecha:** 2026-11-04

## Procedencia
SHA-256 inputs registrados en log.

## Alcance Cripto
Los primeros 30 pares pertenecen a la cohorte preregistrada; los otros
30 son una extensión exploratoria posterior al pre-registro. Se reportan
separados. Las cifras previas de D2 quedan invalidadas porque usaban un
estimador distinto del especificado.

## Nota de implementación
Esta corrida reconstruye `R(t) = PIBpc_hub / PIBpc_nodo` desde Maddison MPD2020 para Dominio B y estima Dimensión de Correlación para Cripto con ventana 200.

## Resumen Dominio B (real)
- Casos: 446
- Mediana Spearman θ1/θ2: 0.930
- Mediana IQR: 1.283
- Invarianza pasa: True
- Variación pasa: True

## Cripto D2 — combinación exploratoria
- Casos: 60
- Elegibles: 60
- Mediana D2 emb2: 1.653
- Mediana IQR u^D2: 1.367
- Mediana Spearman emb2/emb3: 0.939

## Cohortes Cripto
- `preregistrada`: 30/30 elegibles; mediana D2 emb2 1.652, IQR u^D2 1.367, Spearman emb2/emb3 0.939.
- `extension_exploratoria`: 30/30 elegibles; mediana D2 emb2 1.653, IQR u^D2 1.370, Spearman emb2/emb3 0.938.

## Estimadores
- `u^PE` se calcula como número efectivo de patrones (`exp(PE × log(m!))`):
  m=3 para la métrica primaria y m=4 para la comparación de invarianza.
- D2 se estima por regresión lineal de `log C(r)` sobre `log r` en 11 radios
  equiespaciados entre `0.05σ` y `0.3σ`; ambos embeddings usan los mismos
  radios por ventana, con `σ` de la serie en esa ventana.

## Próximos pasos
- Calcular métricas por ventana deslizante para compuertas de invarianza A–D completas y decisión pre-especificada.
