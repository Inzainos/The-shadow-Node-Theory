# Auditoría de términos SNT — Veredictos

**Fecha:** 2026-11-09
**Pedido por:** Elán Zainos Corona
**Evidencia base:** `EVIDENCIA_TERMINOS.md` (mismo directorio)
**Regla de Elán:** lo que no afecte a la teoría se puede integrar; lo que afecte a términos que existen en la teoría se remueve.
**Estado:** NADA tocado todavía. Las remociones de abajo son propuesta para confirmar antes de tocar el espacio, los documentos o el agente.

## Resumen ejecutivo

**"Luz" no existe en la teoría.** Verificado por grep propio: 0 ocurrencias en `README.md`, `docs/DOMINIOS.md`, `docs/HISTORIA.md` y `CASOS_DE_USO.md` del repo v2.7.5.1 (marco v34). Su única aparición en el repo es una metáfora en `papers/marco_teorico.md:165` ("no es mover la luz, es enfocar la misma sombra"), donde "luz" es el marco de proyección θ, otro sentido. Tampoco es término SNT en el libro (8 apariciones: años luz, luz solar, luz de la Macro-Espiral/Teseracto, luz-materia).

**De dónde salió:** `taxonomia-por-dominio.md` (2026-11-06) crea el esqueleto "flujo, luz, hub, sombra, puente" + ficha por nodo, atribuyéndolo a "repo v2.7.5.1 + definiciones de Elán en chat 2026-11-06". La mitad "repo" está verificada como falsa. La mitad "chat" no es verificable desde archivos — y Elán mismo dice que nunca definió "luz". Para el 2026-11-06 ~23:58 las definiciones de luz ya se trataban como "already defined" (memoria 2026-11-07), y de ahí la plantilla se propagó: espacio §9, `snt_agent.py` (68 ocurrencias de "luz"), Finanzas-mundo y Estado (sección §3 LUZ propia), y salidas del agente.

## Veredictos por término

| Término | Dónde aparece | ¿Afecta a términos existentes? | Veredicto |
|---|---|---|---|
| **Luz** (definicional) | Esqueleto de la plantilla; §9 del espacio ("la sombra se define por lo que cuesta la luz"); `snt_agent.py` (plantilla + umbrales de luz); §3 LUZ de Finanzas-mundo y Estado | SÍ — define a "sombra" (término del repo) y ancla la redefinición de φ en Ueno v2 | **REMOVER como término de la teoría** |
| **Sombra** (4º sentido de la plantilla: "mueve el mismo flujo sin pagar la luz") | `taxonomia-por-dominio.md:16`; plantilla del agente | SÍ — añade un cuarto sentido definido en función de "luz", sobre los tres del repo | **REMOVER la definición de la plantilla**; quedan los tres sentidos del repo |
| **Puente** (rol: "cobra por traducir" + posición de nodo) | Plantilla; fichas por nodo | SÍ — redefine "puente": en el repo solo es "puente construido" (Dominio G, infraestructura, explícitamente "no evidencia") | **REMOVER el rol y la posición**; queda "puente construido" |
| **Flujo** (redefinido como "qué se mide en el dominio") | Plantilla | SÍ — redefine "flujo": en el repo es flujo gradiente de φ y Flujo_total v2.0 | **REMOVER la redefinición**; vuelve el sentido del repo |
| **φ en el modelo Ueno v2** ("trazabilidad normativa… qué actos retiraron luz") | `modelo-ueno-resultados-v2.md` | SÍ — redefinición anclada a "luz" | **REMOVER la redefinición**; φ queda como la define el repo (φ: 𝒞 × T → ℝ⁺, postulada, no medida) |
| **Ficha por nodo** (instrumento entero; categorías naturaleza/patrón: simbionte, parásito, hiberna, etc.) | `taxonomia-por-dominio.md`; fichas del corpus; salidas del agente | NO redefine ningún término del repo (0× "ficha", "simbionte", "hiberna" en el repo) — es instrumento añadido, no redefinición | **INTEGRAR como instrumento derivado**, etiquetado como tal, no como teoría. Sus inferencias ancladas a "luz" ("parásito por luz no pagada") se re-anclan a observables reales o se quitan |
| **Hub** (añadidos: "licencia o legitimidad, punto único de falla") | Plantilla | NO — núcleo canónico intacto; son glosas añadidas | **INTEGRAR como glosa derivada**, etiquetada |
| Tono, R-análogo, Roche-C/R/S, Puente Bayesiano/Flujo Total (§16–§20), agente genómico, `DOMINIOS.md` | Varios | NO — sin conflicto (los de §16–§20 ya van etiquetados "Metáfora (marco pedagógico)") | **SE QUEDAN como están** |

## Lista de remociones (pendiente de confirmación de Elán)

1. **Espacio SNT §9 (y sección Ueno):** quitar "luz" del esqueleto ("flujo, luz, hub, sombra, puente" → "flujo, hub, sombra" + puente solo donde sea "puente construido"); quitar la frase "la sombra se define por lo que cuesta la luz en ese dominio" y las filas Luz/Puente de las fichas, o moverlas a un glosario "Vocabulario del caso Ueno" (recomendación del inspector, registrada en la evidencia).
2. **`snt_agent.py` (agente Kaggle):** quitar "luz" de la plantilla (definiciones, umbrales de luz) y de las salidas ("Naturaleza: parásito (por observables: luz no pagada)" → re-anclar a observables reales). El agente es privado, así que el cambio no afecta nada público.
3. **`taxonomia-por-dominio.md`:** corregir la atribución falsa a "repo v2.7.5.1" y quitar "luz" de las 4 definiciones por dominio.
4. **Finanzas-mundo y Estado (§3 LUZ):** NO se borran los datos. Se renombran las secciones a lo que realmente miden: competitividad/provisionamiento (Finanzas-mundo: "luz no pagada" = provisionamiento; Estado: "luz" = licitación competitiva/rendición de cuentas). Los números quedan intactos.
5. **`modelo-ueno-resultados-v2.md`:** reescribir la definición de φ sin "luz".

## Lo que se integra (con etiqueta de derivado)

- **Ficha por nodo** como instrumento de taxonomía por dominio (trabajo de verificación, no teoría del repo). La propia `taxonomia-721-casos.md` ya es honesta al marcar "Luz: GAP" en todos los dominios del corpus — esa honestidad se mantiene.
- **Hub**: glosas añadidas etiquetadas como derivadas.

## Limitaciones de la auditoría

- El chat del 2026-11-06 no se revisó (no disponible en archivos); la atribución "definiciones de Elán en chat" no es verificable desde archivos. Elán mismo dice que nunca definió "luz" — su palabra cierra ese punto.
- No se revisaron los notebooks de Kaggle subidos ni otros derivados fuera de la lista (p. ej. `efipem-snt/`, podcast/video de Ueno).
- La inspección del espacio fue solo lectura; no se tocó el espacio.

## Actualización 2026-11-09 ~10:51 — definición del autor

Elán definió "luz" él mismo: **"La luz es la energía cinética que libera un sistema complejo que está en movimiento y no está en decaimiento todavía o que no entra en el ACOA."**

Con esto, "luz" deja de ser invento del agente y pasa a ser **término definido por el autor**. El veredicto cambia: **luz pasa de REMOVER a DEFINIR**, pendiente de resolver:

1. **Colisión con "energía productiva residual" (README:313):** el repo ya dice que el hub "absorbe energía productiva residual y aumenta masa gravitacional". ¿La "energía cinética liberada" (luz) es la misma energía vista desde el otro lado (el sistema la libera, el hub la absorbe), o son dos cosas distintas? Si es la misma, la definición de luz queda anclada al hub; si son distintas, hay que distinguirlas explícitamente.
2. **Relación con φ (campo de fricción):** README:33, Capa 3 — Campo de fricción φ, postulada por dominio. En física la fricción disipa energía cinética: si luz es energía cinética liberada y φ es fricción, φ se opone a la luz. Esa lectura es coherente, pero Elán no la afirmó explícitamente — hay que confirmarla o descartarla.
3. **"Decaimiento" vs "entrar al ACO-A":** la definición une dos condiciones con "o". ¿Son la misma condición (decaimiento = entrar al ACO-A) o dos distintas? Si son distintas, un sistema podría estar en decaimiento sin entrar al ACO-A y seguir teniendo luz — hay que precisar.
4. **La "sombra" de la plantilla hay que reescribirla:** "mueve el mismo flujo sin pagar la luz" con la nueva definición significaría "mover flujo sin liberar energía cinética", lo cual es físicamente raro (el movimiento libera energía cinética). La definición de sombra no puede quedarse como estaba.

Los demás veredictos (puente como rol, redefinición de flujo, redefinición de φ en Ueno v2, ficha como instrumento derivado) quedan igual hasta que Elán decida.

## Actualización 2026-11-09 ~10:52 — luz por nodo, puente como ER = EPR

Elán refinó la definición: **luz es la energía que libera cada nodo individualmente**. ~~De ahí vienen el ASI y el breach o el puente.~~ **CORREGIDO por Elán 2026-11-09 ~11:11 y reafirmado ~12:05 ("para que no se vuelva a invertir"): la dirección es al revés — el ASI crea la luz (ASI → luz, nunca luz → ASI). La luz es la energía cinética que libera el sistema/nodo; el ASI es lo que la produce, lo que hace brillar al nodo.** El puente lo mete como **ER = EPR** (registrado como "ER igual a PR"; se lee como la conjetura Maldacena-Susskind: puente Einstein-Rosen = entrelazamiento EPR — por confirmar con Elán). **Entrelazamiento cuántico entre sistemas (versión SNT):** cuando dos nodos/sistemas entran en contacto, dependiendo de la cercanía entran en entrelazamiento; entre más tiempo pase, más enlaces y más fuerte se hace.

Cambios a los veredictos:
- **Puente: pasa de REMOVER a DEFINIR.** Si puente = entrelazamiento (ER = EPR), tiene sentido preciso. Pero hay que desambiguarlo del "puente construido" del repo (Dominio G, infraestructura): mismo término, dos sentidos. La definición de puente como entrelazamiento debe escribirse explícita y separada.
- **Luz: DEFINIR (refinada).** Ahora es por nodo individual. **Dirección corregida (Elán 11:11, reafirmada 12:05): el ASI crea la luz (ASI → luz), nunca luz → ASI.** Pendiente: ¿la "energía productiva residual" que absorbe el hub (README:313) es la luz que liberan los nodos? ¿Cómo produce el ASI la luz — qué mecanismo conecta ASI = δH·α/F con la energía cinética liberada?
- **Breach: término nuevo por definir.** Elán lo mencionó junto al ASI y al puente ("de ahí viene el ASI y el breach o el puente") sin definirlo. No existe en el repo como término SNT (verificar).
- **Breach vs bridge — ACLARADO (Elán, 2026-11-09 ~10:56):** la ruptura (breach) es cruzar el Muro de los 5 Eventos, positivo o negativo; al cruzarlo se crea un bridge (puente). Breach ≠ puente: el breach es el evento (el cruce), el puente es lo que se crea (el enlace ER = EPR). Veredicto puente: DEFINIR como entrelazamiento creado al cruzar el muro.
- **Puente, ruptura, colapso, salto, switchover — ACLARADO (Elán, 2026-11-09 ~10:59, en español porque los términos en inglés confunden):** el puente es el vínculo mientras los sistemas/nodos están todavía juntos en el sistema. La ruptura inicia positiva o negativamente. Negativo (colapso): el puente se rompe (la comunicación puede seguir, pero empieza la ruptura); cuando termina el colapso, el puente finaliza. Positivo (salto/leapfrog): el vínculo también se rompe, porque el nodo chico supera al grande — analogía Oracle Data Guard: base standby + base primaria; el satelizado (el más grande) es la primaria; cuando el chico da el salto y supera al grande, switchover: la standby se vuelve primaria y la primaria standby.
- **Tensión por resolver:** antes Elán dijo que al cruzar el muro "se crea un bridge"; ahora dice que al cruzarlo el puente/vínculo "se rompe". Hipótesis por confirmar: en el positivo el puente viejo se rompe y se crea uno nuevo con los roles invertidos; en el negativo el puente solo termina. También pendiente: ¿después del switchover se crea un nuevo puente con roles invertidos?
- **Pregunta abierta:** ¿la fuerza del entrelazamiento sigue la forma t^b de R(t)? Si los enlaces se hacen más fuertes con el tiempo, la forma temporal es la misma ley de potencia — hipótesis por confirmar, no afirmación.

## Actualización 2026-11-09 ~10:55 — hub central, disonancia, decaimiento, fractura

Elán: en el ámbito con hub central, **el hub central distribuye o redistribuye la energía entre todos sus nodos**. Regla: **ningún nodo puede ser mayor que el hub central ni superarlo**; si lo hace, entra en **estado de disonancia**. La disonancia empieza a **descentralizar los flujos de poder** y el sistema puede entrar en **decaimiento** o en **fractura**.

- Esto responde en parte la pregunta 1 de la actualización anterior: el hub redistribuye la luz que liberan los nodos (además de absorber energía productiva residual, README:313).
- **Conexión con R(t) por confirmar:** la regla suena a R(t) ≥ 1 como condición de estabilidad (R = métrica_hub / métrica_nodo). Pero en Ueno R corre 0.096–0.24 (todo < 1): ¿la R de Ueno va orientada al revés, o el umbral de disonancia no es R = 1?
- **Términos nuevos por definir:** disonancia (estado), descentralización de flujos de poder, fractura (¿distinta de colapso? La teoría tiene 5 modos de colapso en ACO-A), decaimiento (régimen; aparece también en la definición de luz — ¿decaimiento = entrar al ACO-A?).

## Siguiente paso

Elán confirma la lista de remociones (o la corrige) y entonces se aplican: espacio, `taxonomia-por-dominio.md`, `snt_agent.py`, Finanzas-mundo/Estado (renombres) y `modelo-ueno-resultados-v2.md`.
