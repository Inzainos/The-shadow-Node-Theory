# El parteaguas — notas sobre el tercer documento de Ueno (v3 CORREGIDA)

**Fecha: 2026-11-09. Staging: `~/workspace/ueno-correccion-2026-11-09/parteaguas-notas-v3.md`**
**Base:** `parteaguas-notas.md` (82 líneas) — estructura conservada; solo se corrigen el bloque
"Lo que confirma" (C-24), φ paso 1 (C-28), "triplica" (C-29) y precisiones marcadas [v3].
La sección VERSIÓN 2 del original, que ya estaba actualizada, se conserva verbatim.
**Fuentes:** `modelo-ueno-resultados-v2.md` + `REVISION_DOCUMENTOS_UENO.md` (2026-11-09,
§3.5, C-24, C-28, C-29). No se tocó el original, no se subió nada a GitHub.

**Cambios v3 (resumen):**
- "Lo que confirma": serie vigente 0,0963 → 0,2643 → 0,2357 → 0,2161 → 0,2395; b 0,383/0,436.
  Serie v1 (0,110 → 0,274 → 0,235 → 0,224 → 0,247; b = 0,357) RETIRADA: 0,274 no es ningún
  mes de v2; 0,224 es jun 2026, no ago; 0,247 es sep 2025, no sep 2026.
- φ paso 1 (bloque v1): 65→60, 9 nov 2023 (el "70→60 sin fecha" queda RETIRADO, C-28).
- Intangibles: "triplica" → 2,43× (654.799/269.233; triplicar serían 807.699M). El +654.799M
  sí es v2; el comparador 269.233M no está en v2 (C-29).
- Salvadoras: USD 153M sin FX declarado (151,0M a FX 6.000). Bandera 3 marcada como
  DESACTUALIZADA (la v2 del parteaguas sí usa "malversación").

# El parteaguas — notas sobre el tercer documento de Ueno

Fuente: `~/workspace/user/files/analisis-completo-parteaguas-ueno_2_s54f.md`
Título: "El parteaguas: análisis completo de la concentración, los nodos sombra y el colapso del hub en el caso Ueno Bank". Subido por Elán 2026-11-06 noche, con "Mira".

## Tesis
El colapso no fue un accidente de liquidez. Fue el resultado de una arquitectura en la que el hub captaba fondos públicos y previsionales más rápido que el resto del sistema, los transformaba en activos no realizables y crédito a vinculadas, y sostenía esa arquitectura modificando la norma que debía limitarla. Las tres concentraciones juntas (pasivo, activo, gobernanza) = parteaguas.

## Lo que confirma (v3 — CORREGIDO; el rótulo v1 «sin cambios» queda RETIRADO, C-24)
- R(t) [v3, serie vigente]: 0.0963 (nov 2024) → 0.2643 (nov 2025) → 0.2357 (feb 2026) → 0.2161 (ago 2026) → 0.2395 (sep 2026). b = 0.383 extremo a extremo / 0.436 OLS (ventana dic 2024–nov 2025, t=1 dic 2024, n=12, R² = 0,873). [La serie v1 — 0.110 → 0.274 → 0.235 → 0.224 → 0.247; b = 0.357 — queda RETIRADA (C-24): 0.274 no es ningún mes de v2; 0.224 es jun 2026 (0,2246), no ago 2026; 0.247 es sep 2025 (0,2467), no sep 2026; 0.235 es truncamiento de 0,2357.]
- Megacuentas Gs 3,758,774M = 177.5% del patrimonio (Derechos Fiduciarios 2,105,743M = 99.44%; Intangibles 761,444M = 35.9%; Participaciones 891,586M = 42.1%).
- CDA Gs IPS 1.0% → 8.4% → 19.7% (2023–2025). Resolución 2 nov 2026, solvencia 5.56% vs 12%.

## Lo nuevo
- **Phi como secuencia observable (5 pasos):** (1) baja puntaje mínimo de subastas 65 → 60 (9 nov 2023) [v3, C-28: el bloque v1 decía 70 → 60 sin fecha; queda RETIRADO]; (2) elimina límite de patrimonio efectivo (Res. IPS 093-046/2024, 12 nov 2024); (3) permite activar gastos de fusión como activo fiduciario; (4) tolera no desagregar software en subcuenta de transparencia (Res. SB.SG. N° 00105/2024); (5) mantiene reserva supervisora. "Phi se detecta por acumulación, no por un solo acto."
- **Phi contable:** balance 2025 incluyó Gs 2.5 billones de gastos en el fideicomiso de fusión con Visión y clasificación errónea de cartera morosa por Gs 2.6 billones (acta Directorio BCP 19 jun 2026).
- **Circuito de las salvadoras (fechado):** Vinanzas, La Tropa, Aime, Kasas, Sagas pagaban sobregiros/préstamos de Mowi, Grupo Hendy y Grupo M con nuevos créditos del mismo banco. Deudas a ago 2026: G. 905,825M (~USD 153M según cifra citada sin FX — a FX 6.000 son USD 151,0M —, 35% del patrimonio efectivo). Sagas 3,000x su deuda con el resto del sistema; Kasas 800x. Circuito 29 abr 2026: Sagas → Kasas → Vinanzas → Itti → Grupo M. Vinculadas traspasadas a exgerentes/empleados del Grupo Vázquez. Informe Intendencia de Supervisión 8 jun 2026.
- **Memorando Rivarola 10 jul 2026:** recomendó no admitir la venta de cartera morosa de Mowi, Grupo Hendy y Grupo M a Vinanzas para simular cumplimiento del tope 20% a vinculadas.
- **Tres pruebas de identificación de nodo sombra:** desproporción, circularidad, transferencia de control.
- **Nodo sombra = entidad, contrato, norma o ausencia de protocolo.** Ausencia de protocolo del IPS (solo Ley 2334/03) = nodo sombra institucional. Contrato vigente / cláusula de gradualidad (Ley 7609/25 art. 79) = nodo sombra normativo.
- **Consumo del hub en 3 fases:** extrae liquidez → extrae solvencia → extrae legitimidad (captar más fondos públicos para cubrir el hueco sube R(t)).
- **Secuencia del colapso:** previsiones > Gs 1.6 billones → solvencia 5.56%; imposibilidad de reponer encaje legal USD 70M; resolución 2 nov; FGD hasta Gs 228.3M, anticipo hasta Gs 10M en 72h (Ley 7745/2026); 32,000 jubilados, primer pago 17 nov, sin elección inicial de entidad; 120 funcionarios BCP desplegados; balance de exclusión máximo 15 días.
- **Embargo (3 nov 2026):** USD 70M + Gs 1,621,853,458,972 + Gs 58,639,000,000 gastos judiciales, contra U Paraguay S.A., U Holdings S.A.R.L., Grupo Vázquez S.A.E., Federico Miguel Vázquez Villasanti, Juan Manuel Gustale, Diana Leticia Mongelós González y cuatro directores.
- **IPS nuevos datos CGR:** Caja y Equivalentes 2024 en Ueno Gs 665,685,348,380 + USD 12,241,087.73 (líder 2024). CDA USD cierre 2025: USD 27,427,000 = 19.95% del inventario (tres instrumentos USD 15,127,000 + heredado Visión USD 12,300,000). Bonos 2025: Gs 250,000M.
- **Intangibles:** +Gs 654,799M solo en 2025, 2,43× la suma de intangibles de nueve bancos (Gs 269,233M) — NO triplica [v3, C-29: 654.799/269.233 = 2,43; triplicar serían Gs 807.699M. El +654.799M sí es v2; el comparador 269.233M no está en v2]. Participaciones: Gs 10,900M (2024) → 891,586M (2025).
- **Límites Ley 7235/23:** 10% del portafolio total y 20% del patrimonio efectivo; debate si aplica por instrumento o por exposición total (Superintendencia de Pensiones: exposición total).
- **Cuatro dominios con taxonomía completa:** fondos públicos (MEF/Tesoro), IPS/previsional, legal/normativo, bancario/balance/solvencia. Tabla 7x4 en el documento.
- **Comparador nuevo: CAME, México 2025:** 1.3M ahorradores, concurso mercantil feb 2026, intervención CNBV jun 2025, retiro de licencia sep 2025, NICAP categoría 4, IMORA Sofipos 25.41% jun 2026. Banca múltiple mexicana: CCL mediana 261%, CFEN 144% (2T 2026) — riesgo en Sofipos, no en banca múltiple.
- **Tres medidas propuestas:** publicar R(t) por banco y dominio; restaurar límite de patrimonio efectivo sobre exposición total por emisor; protocolo de absorción con reparto competitivo y aleatorio por tipo de cuenta.

## Banderas (no resolver por suposición)
1. **ASI:** el documento lo define como "seguro sistémico de absorción" (FGD, transferencia, compensación, capacidad de receptores). El repo SNT tiene un ASI distinto (umbral recalibrado por HackerEarth 0.5 → 0.167, N=4,774). Posible colisión de nombre — preguntar a Elán si es redefinición o concepto distinto.
2. **ACO-A:** el documento lo define como "absorción por oferta competitiva y adjudicación" (estrategia de resolución). En el repo, ACO-A es el marco de colapsos (18 casos, 5 modos). Uso compatible pero más específico — registrar la definición del documento como la operativa para finanzas.
3. **"Malversación" vs mecanismo:** el documento NO usa la palabra malversación. [v3: DESACTUALIZADO — la v2 del parteaguas sí la usa, como denuncia penal presunta del MEF (Gs 250.000M + Gs 123.838M intereses); ver sección VERSIÓN 2 abajo.] Documenta el mecanismo (circuito circular, reclasificación, fideicomiso, tolerancia) y el trigger visible es el ajuste contable (previsiones > Gs 1.6 billones) + encaje USD 70M no repuesto. La clasificación "malversación = trigger exógeno" es de Elán. Ambas encajan si la malversación operó a través de esos circuitos; el embargo nombra a las personas (Grupo Vázquez et al.).
4. **Backcast:** el documento añade peldaños fechados (circuito 29 abr 2026; informe supervisión 8 jun 2026; acta BCP 19 jun 2026; memorando 10 jul 2026) pero la ventana de inicio sigue en nov 2024–mar 2025 (Res. IPS 12 nov 2024; avalancha de fondeo dic 2024–mar 2025 sin crédito). La fusión con Visión (origen del fideicomiso y del convenio heredado) no está fechada en el documento — hueco.

## Qué cambia en el trabajo en curso
- Podcast backcast: incorporar circuito 29 abr 2026, secuencia phi en 5 pasos, tres pruebas, embargo con nombres, primer pago jubilados 17 nov. Ventana de inicio sin cambio (fines 2024, aproximación).
- Tabla maestra: anclajes confirmados; añadir a columnas IPS las cifras CGR 2024 (Caja y Equivalentes) y CDA USD 27.4M cierre 2025.
- Taxonomía: la tabla 7x4 del documento es la taxonomía por dominio más completa hasta ahora; integrarla al espacio cuando toque, con fuente.

---

## VERSIÓN 2 (archivo `analisis-completo-parteaguas-ueno__1__3_xnox.md`, 313 líneas, subido 2026-11-06 ~20:14)

Revisión del mismo informe, +37 líneas. Cambios sustantivos:

### "Cómo leer este informe" (nuevo, tras el resumen)
Tres palabras con sentido preciso, no mezclar: **Fragilidad** (debilidad acumulada antes del colapso), **Trigger** (acto del 2 nov 2026 que la hace visible: resolución del BCP por solvencia), **Cadena** (lo que se desencadena después: congelamiento, garantía, reasignación, denuncias, imputaciones, crisis política). Y: **"El ratio de Roche no se define ni se fecha en este informe. Es el paso siguiente: una aproximación aparte sobre cuándo el sistema entró en zona de ruptura, distinta del trigger del 2 de noviembre."** → El backcast ES esa aproximación aparte.

### Malversación: fuente y distinción (responde la pregunta abierta)
- Calificación oficial del trigger 2 nov: **insuficiencia de solvencia, no malversación**.
- La malversación aparece después como **denuncia penal del MEF (5 nov 2026)** por presunta malversación de **G. 250,000M de la Caja Fiscal + G. 123,838M en intereses** [14] La Nación, contra directivos y contra el presidente. Los G. 250,000M se depositaron en julio de 2025.
- Ministerio Público: **imputación a 27 personas** (4 nov 2026) por conducta indebida en crisis, lesión de confianza, tentativa de estafa y violación de llevar libros [16]. Operaciones 2025–2026 con activos compuestos principalmente con recursos de terceros.
- "En el plano analítico, el 2 de noviembre funciona como trigger de malversación... En el plano jurídico, la malversación permanece como presunta, denunciada e investigada, no como hecho declarado por sentencia."

### ASI redefinido (resuelve la bandera #1)
"ASI designa el Índice de Soberanía Atómica. **No es un seguro ni un mecanismo de absorción.** Es una medida de cuánto control conserva la unidad atómica cuando el hub falla." Unidad atómica: depositante individual, jubilado, OEE, o titular que no puede dividir su exposición sin perder su función. ASI alto: puede elegir banco, retirar/transferir sin permiso del hub, acceder a información veraz, recuperar en plazo. ASI bajo: cautivo por convenio, sin elección inicial, fondos congelados, depende de decisión discrecional. Evaluación: ASI bajo en tres unidades (jubilados reasignados sin elección; ahorristas con fondos congelados; organismos dependientes de la denuncia/proceso penal). "Una absorción puede ser ordenada en términos sistémicos y, al mismo tiempo, dejar un ASI bajo." Queda pendiente si este ASI es el mismo del repo SNT (umbral HackerEarth 0.167) — el documento v2 ya no lo define como seguro, que era la colisión.

### Nueva sección 1.4: trigger 2 nov (fragilidad acumulada, detonador, no causa)
- Sep 2025–may 2026: **~USD 146M** a Mowi, Grupo Hendy y Grupo M por encima del tope 20%, a sola firma, sin garantías [17].
- 5 jun 2026: Superintendencia notifica exceso en límite a vinculadas; banco corrige 15 jun; 24 jul: pide incorporar otras empresas al grupo vinculado y recalcular exposición [18].
- Ratio de capital total declarado: **15.01% (mar 2026), 14.5% (jun), 13.85% (sep)** — ocultaba la fragilidad real [19][22].
- Inspección 31 oct confirma hallazgos → previsiones → solvencia 5.56% [22].
- 30 oct: IPS en **9.70%** de su cartera en Ueno, al borde del máximo 10%; sin nuevas colocaciones en 2026 [20].
- Cadena: congelamiento, cierre de servicios, garantía, reasignación, denuncias, imputaciones, detenciones y **crisis política** [21].
- Cadena penal: 3 nov detención de ocho directivos; 4 nov imputación a 27; después denuncia MEF. Cadena política: **renuncia y juicio político al presidente** (Santiago Peña, según [21] El Cronista).

### Phi corregido y fechado
- Paso 1: **9 nov 2023**, puntaje mínimo de subastas de **65 a 60** (v1 decía 70→60 sin fecha).
- Paso 2: 12 nov 2024, elimina límite de patrimonio efectivo **y baja la calificación exigida de A-Py con tendencia fuerte a A genérica**.

### Otros
- Resumen: en septiembre el banco todavía declaraba 13.85%; fuente BCP oficial [15] añadida.
- Sección 9.1 reestructurada en fragilidad / trigger / cadena. 9.3 reescrita con ASI. Conclusión: tercera medida ahora incluye preservar ASI en cada unidad atómica.
- Nuevas fuentes [14]–[22]: La Nación, BCP, ABC (imputación y USD 146M), El Economista, Última Hora, El Cronista (x2), Perspectivas.
- Corrección menor: cita [4]→[2] en sección 3.2.

### Qué cambia en el trabajo en curso
- **Podcast (ya entregado):** dos líneas quedan desactualizadas por la v2: (a) "El parteaguas NO usa la palabra malversación" — la v2 sí la usa, como denuncia penal presunta del MEF (G. 250,000M + G. 123,838M); (b) el cruce del ratio de Roche el 2 nov — la v2 dice que el ratio de Roche es una aproximación aparte, distinta del trigger, es decir, el backcast mismo. Recomendado: actualización (regrabar episodio o grabar episodio corto de corrección). Decisión de Elán pendiente.
- **Tabla maestra (Elán la corrige):** peldaños nuevos fechados candidatos para sus notas: USD 146M sep 2025–may 2026; ratios de capital 15.01/14.5/13.85; IPS 9.70% al 30 oct; phi paso 1 fechado 9 nov 2023 (65→60).
- **ASI:** la bandera se resuelve en el documento (v2 lo redefine); queda solo verificar si coincide con el ASI del repo.
