Shadow Node Theory:
Invarianza de Escala en el Algoritmo de Satelizacion de Nodos
Evidencia en Multiples Dominios y una Capa Universal de Colapso Orbital (ACO-A)
Elan Zainos Corona (Captain 1n2a1n05)
Fractal Core Research — Tlaxcala, Mexico
Pre-print v2.5.0 (marco v30) — 2026 — No arbitrado
| Clasificacion JEL | N00 (Historia Economica General) · C14 (Estimacion semi-parametrica) · O18 (Desarrollo Regional) |
|---|---|
| Palabras clave | Shadow Node Theory · invarianza de escala · preferential attachment · ley de potencia · friccion institucional · colapso orbital acoplado (ACO-A) · funcion de hazard · churn prediction · leapfrog cognitivo |
| Dataset principal | Corpus real v30 de 721 casos (reconstruction_real/) · Maddison Project · INEGI Mexico 1993-2022 · zerve_hackathon_dataset.csv (HackerEarth 2026) · Yahoo Finance, NOAA GOES, NASA/ZTF, CoV-Spectrum (capa de colapso) |
| Codigo disponible | shadow_node_verification_v2.py — analisis cuantitativo completo con datos Maddison |
| Zenodo DOI | https://doi.org/10.5281/zenodo.19446521 (v2.5.0) |
| GitHub | https://github.com/Inzainos/The-shadow-Node-Theory |
| Conflicto de intereses | El autor es ciudadano de Tlaxcala, nodo sombra del caso mesoamericano analizado. El sesgo potencial se mitiga mediante uso exclusivo de fuentes cuantitativas externas verificables. |





# Abstract / Resumen
Elan Zainos Corona · Fractal Core Research · Tlaxcala, Mexico · elan.zainos.corona@gmail.com
DOI: https://doi.org/10.5281/zenodo.19446521 · SSRN: https://ssrn.com/abstract=6418778
Resumen
NOTA DE VERSION (v30): esta version actualiza el preprint al corpus real de 721 casos (reconstruido 100% desde fuentes primarias verificables; reemplaza el corpus previo de 502 casos que contenia valores sinteticos) e integra una Capa Universal de Colapso Orbital Acoplado (ACO-A). Cifras maestras: friccion institucional predice el exponente de satelizacion b (Spearman rho=-0.68, p=2.5e-97, n=714); separacion de regimenes bio-sin-friccion (b~+0.95) vs economico-con-friccion (b~+0.09), Mann-Whitney p=2.4e-74. La capa de colapso anade un eje ortogonal Delta, una capa de hazard h(tau)>0, una taxonomia de modos de colapso (friccion x trigger x piso/techo) y un Principio de Minima Friccion, con evidencia en cinco dominios reales (finanzas, historia, cripto, biologia, astronomia). La hipotesis de la proporcion aurea (H-phi) fue probada y REFUTADA en 4 rondas (incl. control placebo); queda excluida de los claims principales.

Este trabajo presenta la Shadow Node Theory (SNT), que consolida el Modelo de Triple Resolucion (v2.0) y formaliza la satelizacion de nodos en tres escalas de resolucion distintas con dinamicas propias: el Sistema Micro (Nodo Atomico / individuo), el Sistema Meso (Red Fungica intra-nacional), y el Sistema Macro (colision de superorganismos entre naciones). La hipotesis central original se mantiene: cuando dos nodos de poder orbitan en proximidad critica, el nodo con mayor ventaja acumulada sateliza al nodo historico mediante un algoritmo cuya dinamica sigue una ley de potencia invariante a la escala temporal y al sustrato. La SNT v2.0 extiende este hallazgo con tres contribuciones nuevas: (1) la formalizacion del Modelo de Triple Resolucion que establece las condiciones de aplicabilidad del modelo binario segun la escala de analisis; (2) la verificacion empirica de la taxonomia de cinco niveles con datos INEGI 2022 para las 32 entidades federativas de Mexico, confirmando una distribucion de ley de potencia (b=-0.473, R2=0.838, p<0.001) consistente con las predicciones de preferential attachment; y (3) la vectorizacion de trayectorias para ocho entidades mexicanas (1940-2022) que documenta los primeros casos de leapfrog exitoso dentro del sistema nacional — Queretaro (b=-0.155, p<0.01) y Nuevo Leon (b=-0.058, p<0.001) — como instancias empiricas de convergencia mediante salto dimensional.

Se analizan cinco casos en tres dominios. Historico-demografico: Brujas-Amberes (trigger: sedimentacion Canal Zwin, c.1490) y Toledo-Madrid (trigger: decreto Felipe II, 1561). Economico historico: Portugal vs NW Europa (trigger: Union Iberica 1580, datos Maddison GDP pc USD 2011) y Tlaxcala-Puebla (trigger: Real Cedula 1535, serie larga 1550-2022). Digital: usuarios HackerEarth Canvas (409,287 eventos, Fractal Core Framework 2026).

El analisis cuantitativo revela una taxonomia de dos velocidades. Triggers abruptos (Brujas, Toledo): exponente b medio = 0.717, R2 > 0.87, p < 0.001. Triggers graduales (Portugal, Tlaxcala): exponente b medio = 0.122. Diferencia de velocidad: 5.9x. En el dominio digital, el Fractal Gap muestra una discontinuidad de 7,478x en VDR. El modelo GradientBoostingClassifier alcanza ROC-AUC = 0.9994. El 5-Event Wall es el umbral de activacion detectable en la primera sesion. El predictor dominante de retencion es la adopcion del agente AI, interpretado como leapfrog cognitivo: el equivalente digital de la ruptura asintotica.

Abstract
This paper presents Shadow Node Theory (SNT), proposing that when two power nodes orbit in critical proximity, the node with greater accumulated advantage satellizes the historical node through a predictable power-law algorithm. The central hypothesis: this algorithm operates invariantly across temporal scales and substrates — the same mathematical pattern appears in 16th-18th century historical systems, long-run economic data (Maddison Project 2023), and real-time digital behavioral data (4,774-user dataset, 2026).

Quantitative analysis reveals a two-speed taxonomy. Abrupt triggers (Bruges, Toledo): mean exponent b = 0.717, R2 > 0.87, p < 0.001. Gradual triggers (Portugal, Tlaxcala): mean exponent b = 0.122. Speed ratio: 5.9x. In the digital domain, the Fractal Gap shows a 7,478x discontinuity in VDR. The GradientBoostingClassifier achieves ROC-AUC = 0.9994. The 5-Event Wall is the activation threshold detectable within the first session. The dominant retention predictor is AI agent adoption — the digital equivalent of asymptotic breakout (cognitive leapfrog).



# 1. Introduccion
La pregunta que motiva este trabajo es simple en su enunciado y compleja en su respuesta: cuando dos sistemas humanos compiten por los mismos recursos en el mismo espacio geografico o funcional, existe un patron matematico predecible que determina cual de los dos termina satelizando al otro? Y si ese patron existe, opera de la misma forma en sistemas separados por siglos y en dominios tan distintos como la demografia urbana medieval y el comportamiento de usuarios en una plataforma de inteligencia artificial?

La hipotesis de este trabajo es afirmativa. Llamamos Shadow Node Theory (SNT) al modelo que formaliza esta idea. La teoria postula que cuando dos nodos de poder orbitan en proximidad critica, el nodo con mayor ventaja acumulada sateliza al nodo historico mediante un algoritmo predecible cuya dinamica sigue una ley de potencia. El nodo satelizado no desaparece: queda funcionalmente subordinado. Sus recursos fluyen hacia el nodo dominante, su capacidad de decision se reduce, y su divergencia se amplifica de forma no lineal.

## 1.1 El problema de la invarianza de escala
El fenomeno de la satelizacion entre centros de poder ha sido abordado por la geografia economica (Krugman, 1991), la teoria de dependencia (Prebisch, 1950), y la historia economica cuantitativa (Maddison, 2001; Bolt y van Zanden, 2024). Cada tradicion estudia una instancia especifica en un dominio particular. Lo que este trabajo propone es que existe un algoritmo matematico comun subyacente a todas esas instancias, invariante a la escala temporal y al sustrato. Esta hipotesis es falsificable: si los exponentes de la ley de potencia son estadisticamente distintos entre casos con mecanismos completamente diferentes, la hipotesis queda refutada. Los resultados reportados muestran que los exponentes convergen en dos clases: b ~ 0.72 para triggers abruptos y b ~ 0.12 para triggers graduales, con diferencia de velocidad de 5.9x que emerge de los datos.

## 1.2 Antecedentes teoricos
La SNT se construye sobre tres cuerpos de literatura. Primero, redes libres de escala: Barabasi y Albert (1999) demostraron que en redes con preferential attachment la distribucion de grados sigue una ley de potencia. Los nodos con mas conexiones atraen mas conexiones nuevas, generando concentracion 80/20. Este mecanismo es matematicamente identico al que la teoria identifica en los sistemas de competencia. Segundo, historia economica cuantitativa: el Maddison Project Database, Costa-Palma-Reis (2015), Ringrose (1973), y Gelderblom (2013) son las fuentes empiricas primarias. Tercero, sistemas complejos aplicados: Schelling (1971) mostro que preferencias individuales debiles producen segregacion agregada extrema. Simon (1955) propuso el modelo de crecimiento proporcional, reconocido mas tarde como caso especial de preferential attachment.

## 1.3 La brecha en la literatura
No existe hasta donde sabemos un trabajo que integre estos tres cuerpos para formular una teoria unificada de satelizacion aplicable a multiples dominios y escalas temporales, y que la verifique cuantitativamente en casos historicos reales con datos Maddison, series demograficas historicas y datos conductuales digitales en tiempo real. La brecha que este trabajo llena es triple: formalizacion matematica del algoritmo como ley de potencia con exponente calculable y comparable; identificacion de la taxonomia de velocidades segun el tipo de trigger; demostracion de que el mismo patron aparece en datos digitales en tiempo real con la misma estructura matematica.



# 2. Marco Teorico Formal
## 2.1 Definiciones
Nodo: unidad de analisis que concentra recursos (capital, poblacion, decision institucional, capacidad computacional) e intercambia esos recursos con otras unidades dentro de un sistema.

Proximidad critica: condicion en que dos nodos compiten por los mismos recursos en el mismo espacio funcional, de forma que el crecimiento de uno implica perdida relativa del otro.

Nodo sombra: nodo que posee recursos historicos previos pero enfrenta desventaja acumulada creciente respecto al nodo dominante.

Satelizacion: proceso por el cual el nodo sombra pierde autonomia funcional progresiva. Sus recursos fluyen hacia el nodo dominante, su capacidad de decision se reduce, y su divergencia se amplifica en el tiempo.

Trigger: evento o proceso que supera el umbral de activacion. Puede ser abrupto (decreto, colapso de infraestructura, vacio institucional) o gradual (acumulacion de ventaja durante decadas o siglos).

Umbral de activacion: nivel de ventaja relativa del nodo dominante a partir del cual el proceso se vuelve estadisticamente irreversible sin intervencion exogena. La teoria predice este umbral entre el 10% y el 15%.

## 2.2 Hipotesis central
H1: La divergencia entre nodo dominante y nodo sombra, medida como R(t) = valor_dominante(t) / valor_sombra(t), sigue una ley de potencia de la forma R(t) = a * t^b, donde t es el tiempo desde el trigger, a es el coeficiente de escala, y b es el exponente de divergencia.

Predicciones verificables: P1 — la ley de potencia ajusta mejor que un modelo lineal (R2 significativo); P2 — b > 0 en todos los casos (la brecha crece); P3 — los exponentes b de casos con el mismo tipo de trigger son estadisticamente similares; P4 — en todos los casos existe un punto donde la ventaja del nodo dominante supera el 10-15%, y ese punto precede o coincide con la divergencia acelerada.

## 2.3 Criterios de refutacion
RC1: El ajuste de ley de potencia no es significativo (p > 0.05) en la mayoria de los casos.
RC2: Los exponentes b de casos con el mismo tipo de trigger tienen CV intra-clase > 0.60.
RC3: Algun caso muestra convergencia espontanea (el nodo sombra cierra la brecha sin intervencion exogena).
RC4: En el dominio digital, la distribucion de comportamiento es gaussiana, no de ley de potencia.



# 3. Metodologia
## 3.1 Diseno general
Diseno comparativo-historico con verificacion cuantitativa. Cinco casos en tres dominios. Comparabilidad garantizada mediante: ratio R(t) = nodo_dominante / nodo_sombra como variable dependiente uniforme; tiempo desde el trigger como variable independiente; mismo modelo funcional (ley de potencia) aplicado a todos los casos.

## 3.2 Criterios de seleccion de casos
Trigger identificable con fecha aproximada documentada en literatura academica primaria.
Al menos cuatro puntos de datos en la serie temporal post-trigger.
Los dos nodos en proximidad critica (competencia por los mismos recursos).
Caso documentado en fuentes academicas independientes de este trabajo.
Trigger de naturaleza distinta a los otros casos, para maximizar la diversidad de mecanismos.

## 3.3 Fuentes de datos
Brujas-Amberes (1300-1589): poblacion total estimada. Fuentes: Nicholas (1992) y Gelderblom (2013) para Amberes; Van der Wee (1963) para la transicion. Incertidumbre +/-20%.

Toledo-Madrid (1528-1787): poblacion total. Fuentes: Ringrose (1973) para 1528-1661; INE Espana para datos posteriores. Datos Toledo 1600-1787 son estimaciones de Ringrose basadas en registros parroquiales.

Portugal vs NW Europa (1535-1980): GDP per capita en USD internacionales 2011 PPP. Fuente: Maddison Project Database 2023 (Bolt y van Zanden). Nodo dominante = promedio Paises Bajos y Reino Unido. Decision respaldada por Costa, Palma y Reis (2015).

Tlaxcala-Puebla (1550-2022): estimaciones Maddison Mexico 1550-1820 calibradas con datos INEGI 1993-2022 (ancla: ratio Puebla/Tlaxcala = 1.49 en 1993). Ventaja inicial estimada en 12% post-Real Cedula 1535.

HackerEarth 2026: 409,287 eventos de 4,774 usuarios. Pipeline Fractal Core V3. Variables: VDR, CSI V3, 284 features de eventos. Fuente: zerve_hackathon_dataset.csv (Captain 1n2a1n05, 2026).

## 3.4 Pipeline de analisis
Construccion de la serie de ratios R(t) para cada punto de datos disponible.
Calculo del tiempo t desde el trigger (t = ano - ano_trigger, t minimo = 1).
Ajuste de ley de potencia en espacio logaritmico: log(R) = log(a) + b * log(t).
Calculo de R2 en escala original y correlacion Pearson en log-log con p-value.
Identificacion del ano en que el nodo dominante supera umbral del 10-15%.
Calculo de velocidad de divergencia post-trigger (cambio en ratio por ano, primeros 100 anos).

## 3.5 Limitaciones metodologicas
(1) Datos pre-1820 con incertidumbre significativa (+/-20% en datos medievales). (2) N pequeno: cuatro casos historicos no permiten inferencia estadistica robusta sobre la distribucion de exponentes. (3) Portugal R2 bajo por proceso oscilatorio con perturbaciones exogenas (oro brasileno). (4) Caso digital: riesgo de causalidad inversa (usuarios Elite podrian tener habilidad previa distinta). (5) Sensibilidad del exponente a la definicion del trigger en casos graduales. Todas estas limitaciones se detallan en la seccion 7.



# 4. Resultados por Caso
Se aplico el pipeline de analisis descrito en la seccion 3 a los cuatro casos historicos. Los resultados del caso digital se presentan en la seccion 6.

## 4.1 Brujas — Amberes (1300-1589)
| Año | Brujas (miles hab.) | Amberes (miles hab.) | Ratio A/B | t desde 1490 |
|---|---|---|---|---|
| 1300 | 46 | 5 | 0.109 | t=-190 |
| 1375 | 42 | 10 | 0.238 | t=-115 |
| 1450 | 38 | 18 | 0.474 | t=-40 |
| 1500 | 30 | 45 | 1.500 | t=+10 |
| 1520 | 22 | 65 | 2.955 | t=+30 |
| 1560 | 15 | 105 | 7.000 | t=+70 |


Parametros: a=0.238, b=0.739, R2=0.868, r Pearson (log-log)=0.958, p<0.001. Umbral 10-15% superado en 1500 (ventaja 50%). Velocidad divergencia post-trigger: 0.042 ratio/ano. El mecanismo fue exclusivamente fisico-geografico: la sedimentacion del Canal Zwin elimino el acceso maritimo de Brujas para barcos de gran calado. La pegajosidad institucional documentada por Gelderblom retardo la migracion del comercio financiero aproximadamente 20 anos despues del comercio de mercancias.

## 4.2 Toledo — Madrid (1528-1787)
| Año | Toledo (hab.) | Madrid (hab.) | Ratio M/T | t desde 1561 |
|---|---|---|---|---|
| 1528 | 31,930 | 5,000 | 0.157 | t=-33 |
| 1561 | 56,270 | 15,000 | 0.267 | t=0 |
| 1600 | 40,000* | 55,000 | 1.375 | t=+39 |
| 1661 | 25,000 | 120,000 | 4.800 | t=+100 |
| 1787 | 15,000* | 156,672 | 10.445 | t=+226 |


(*) Toledo 1600-1787: estimaciones Ringrose basadas en registros parroquiales. Parametros: a=0.188, b=0.694, R2=0.924, r Pearson=0.983, p<0.001. Mejor ajuste del conjunto. Umbral superado en 1600 (ventaja 37.5%). Velocidad: 0.045 ratio/ano. El decreto de 1561 convirtio al nodo mas pequeno de Castilla en el nodo dominante mediante la transferencia del control sobre el flujo de recursos del sistema. Toledo no colapso por falta de meritos historicos sino por perdida de acceso al flujo de decision del poder imperial.

## 4.3 Portugal vs NW Europa (1535-1980)
| Año | Portugal GDP pc | NW Europa GDP pc* | Ratio NW/PT | t desde 1580 |
|---|---|---|---|---|
| 1535 | 1,290 | 2,388 | 1.851 | t=-45 |
| 1600 | 1,258 | 2,981 | 2.368 | t=+20 |
| 1700 | 1,572 | 2,895 | 1.841 | t=+120 |
| 1750 | 2,184 | 3,240 | 1.483 | t=+170 |
| 1800 | 1,459 | 3,764 | 2.580 | t=+220 |
| 1913 | 1,992 | 7,333 | 3.681 | t=+333 |


(*) Promedio Paises Bajos + Reino Unido. USD internacionales 2011 PPP. Fuente: Maddison Project Database 2023. Parametros: a=1.231, b=0.060, R2=0.123, p=0.277. El R2 bajo no invalida el caso: refleja que el proceso fue oscilatorio, no monotónico. El oro brasileno produjo recuperacion parcial en 1750 (ratio cae de 2.37 a 1.48) que rompe el ajuste lineal en log-log. La tendencia de largo plazo es inequivocamente divergente: ratio de 1.85 en 1535 a 3.68 en 1913. Dato clave del Maddison: en 1535 Paises Bajos ya tenia GDP pc de 3,110 USD vs 1,290 de Portugal. La brecha era de 2.4x antes del trigger politico de 1580.

## 4.4 Tlaxcala — Puebla (1550-2022)
| Periodo | Evento clave | Ratio Pue/Tlax (est.) | Velocidad del cambio |
|---|---|---|---|
| 1535 | Real Cedula — Puebla ciudad principal | 1.12 | Trigger |
| 1700 | Consolidacion colonial | 1.24 | +0.12 en 165 anos |
| 1873 | Bypass ferroviario | 1.21 | Plateau colonial |
| 1940 | Industrializacion Puebla | 1.35 | +0.14 en 67 anos |
| 1993 | Dato directo INEGI | 1.49 | +0.14 en 53 anos |
| 2022 | Dato directo INEGI | 1.55 | +0.06 en 29 anos |


Parametros serie larga: a=0.642, b=0.184, R2=0.567, r Pearson=0.753, p<0.001. La amplificacion maxima ocurre en 1940-1993 (industrializacion de Puebla: VW 1964, Hylsa, petroquimica). Datos INEGI directos: correlacion migracion-divergencia r=0.9646; ratio IED Puebla/Tlaxcala 2022 = 25.5x; 14.5% de la fuerza laboral tlaxcalteca trabaja fuera del estado.



# 5. Discusion: La Taxonomia de Dos Velocidades
## 5.1 El hallazgo central
| Clase | Casos | b medio | R2 medio | Vel. ratio/año | Descripcion |
|---|---|---|---|---|---|
| Abruptos | Brujas, Toledo | 0.717 | 0.896 | 0.044 | Satelizacion super-lineal |
| Graduales | Portugal, Tlaxcala | 0.122 | 0.345 | 0.002 | Satelizacion sub-lineal acumulativa |


La diferencia de velocidad de 5.9x entre clases emerge de los datos sin ser supuesta en el modelo. El CV intra-clase para triggers abruptos es 0.04 (casi identicos). Para triggers graduales, 0.52 (consistente pero con varianza mayor por las perturbaciones exogenas documentadas en ambos casos: oro brasileno en Portugal, cambios en politica industrial en Tlaxcala).

## 5.2 Interpretacion cualitativa
En los triggers abruptos, el evento genera una discontinuidad inmediata en los flujos de recursos: la corte se traslada, el canal se sella. El flujo es unidireccional y rapido porque la fuente del recurso se mueve de forma definitiva. En los triggers graduales, no hay discontinuidad sino una asimetria sostenida que se acumula: Portugal pierde autonomia decisional gradualmente, Tlaxcala pierde capital humano e inversion gradualmente. La perdida no es de infraestructura sino de opciones estrategicas disponibles.

## 5.3 Implicaciones para la intervencion temprana
La taxonomia permite estimar la ventana de intervencion antes de que el proceso complete su ciclo. En triggers abruptos, la ventana es estrecha: los primeros 20-40 anos post-trigger son criticos. Para 1640 el colapso de Toledo era irreversible sin intervencion sistemica mayor. En triggers graduales, la ventana es mas larga pero el proceso es igualmente irreversible si no se actua. La clave es identificar el trigger gradual mientras el ratio es bajo y antes de que el preferential attachment haya generado suficiente inercia para autosostenerse.



# 6. Validacion en Dominio Digital: HackerEarth 2026
## 6.1 El experimento
Validacion de la SNT en datos de comportamiento de 4,774 usuarios de HackerEarth Canvas: 409,287 eventos, 141 tipos, dataset zerve_hackathon_dataset.csv. Pipeline Fractal Core Framework V3 (Captain 1n2a1n05, 2026). Pregunta: la misma dinamica de preferential attachment que produce satelizacion en sistemas historicos produce una distribucion discontinua (Fractal Gap) en comportamiento de usuarios?

## 6.2 El Fractal Gap
| Cohort | N | % | CSI V3 rango | VDR medio | Ratio vs Basic |
|---|---|---|---|---|---|
| Elite | 24 | 0.5% | 55.62 – 74.76 | 47.86 | 7,478x |
| Intermediate | 306 | 6.4% | 18.57 – 55.62 | 40.85 | 6,484x |
| Basic | 4,444 | 93.1% | 0 – 18.57 | 0.0063 | baseline |


La discontinuidad de 7,478x en VDR entre Elite y Basic no es un gradiente explicable por diferencias de habilidad. Es una brecha cualitativa del mismo tipo que la observada entre Amberes y Brujas en 1560. El modelo GradientBoostingClassifier entrenado sobre 284 features de eventos alcanza ROC-AUC = 0.9994 en test y ROC-AUC = 1.0000 en validacion cruzada de 5 folds.

## 6.3 El 5-Event Wall
El Survival-Style Chart muestra que el pico de probabilidad de churn ocurre exactamente en los primeros 5 eventos. Despues de ese punto, la probabilidad cae abruptamente para los usuarios que cruzan el umbral. Este patron tiene la misma estructura que el umbral del 10-15% en los casos historicos: por debajo del umbral el sistema no ha generado suficiente inercia para autosostenerse; por encima el preferential attachment toma el control. La diferencia es la escala temporal: el umbral historico se define en anos, el digital en eventos de una sesion.

## 6.4 El ranking SHAP y el leapfrog cognitivo
El hallazgo mas original de la seccion es el ranking de importancia SHAP. Los dos predictores dominantes de retencion son agent_accept_suggestion (importancia ~0.5) y agent_worker_created_ratio (~0.4), ambos eventos de delegacion al agente AI. Credits_used tiene importancia 0.001. El modelo dice que el usuario que se queda no es el que consume mas sino el que delega mas al agente.

Denominamos leapfrog cognitivo al mecanismo por el cual el usuario deja de operar como ejecutor de tareas y empieza a operar como orquestador de agentes. Este salto es el equivalente digital de la ruptura asintotica descrita en la seccion 2 del marco teorico: el nodo que delega procesamiento a un agente externo opera en una dimension donde la ventaja acumulada del nodo Elite en herramientas especificas no es el factor determinante.

La validacion digital confirma que el algoritmo de satelizacion no requiere siglos para operar. Opera en semanas en el dominio conductual digital con la misma estructura matematica que en el dominio historico. La invarianza de escala temporal es real y medible.



## 6.5 Extension al Dominio Empresarial
El caso HackerEarth 2026 no fue solo una validacion digital del modelo binario — fue la primera demostracion empirica de la SNT aplicada a un sistema empresarial complejo. La plataforma Canvas con sus 4,774 usuarios constituyo un ecosistema cerrado con todas las caracteristicas del sistema Meso: un hub (la plataforma y sus mecanismos de ranking), nodos Elite que concentraban el valor, y nodos Basic que proveian actividad sin retener valor proporcional. El Fractal Gap de 7,478x en VDR entre ambos estratos es la distribucion de Pareto en su forma mas extrema.

El modelo es aplicable a cualquier empresa que tenga bases de datos de sus operaciones. La condicion no es el sector ni el tamano sino la disponibilidad de datos que permitan medir los flujos entre nodos. Para detectar satelizacion interna se requieren cinco metricas: volumen de datos generados por nodo, actividad sostenida, tiempo de respuesta ante nuevas demandas, diversidad funcional y resiliencia ante fallos. Estas cinco metricas producen el Composite Score Index Empresarial (CSIE).

El hallazgo mas importante del caso HackerEarth — que el predictor dominante de retencion es la adopcion del agente AI — es transferible al dominio empresarial: los equipos que orquestan herramientas de IA escapan de la satelizacion cognitiva; los que siguen ejecutando linealmente son absorbidos por el sistema.



# 7. SNT v2.0: Modelo de Triple Resolucion Sistemica
La SNT v2.0 extiende el modelo binario original en tres escalas de resolucion con dinamicas propias, actores distintos y reglas de competencia incompatibles entre si. La taxonomia de cinco niveles y la verificacion empirica con INEGI 2022 confirman que el sistema nacional mexicano opera bajo preferential attachment. La vectorizacion de trayectorias para ocho entidades (1940-2022) documenta los primeros casos de leapfrog exitoso dentro del sistema: Queretaro (b=-0.155, p<0.01) y Nuevo Leon (b=-0.058, p<0.001).

## 7.1 Resolucion Micro: El Sistema Atomico
La escala base de procesamiento y supervivencia. El Nodo Atomico opera bajo dinamica lineal y autopoyetica. Sus recursos se dividen en Cuantitativos (RQ, extractables: capital, tiempo, infraestructura) y Cualitativos (RL, inherentes: conocimiento, habilidades, madurez). Los RL no pueden ser extraidos directamente pero se degradan por falta de practica cuando la escasez de RQ impide su mantenimiento. El leapfrog requiere dos dimensiones en paralelo: Intrapersonal (DI, base obligatoria) y Profesional (DP, salto visible). Sin DI suficiente el salto es temporal — el nodo no puede mantener la nueva posicion.

## 7.2 Resolucion Meso: La Red Fungica Intra-nacional
Ecosistema cerrado delimitado por frontera geopolitica o jurisdiccion institucional. El Hub Central administra la red mediante extraccion continua de energia residual de los Nodos Sombra. La jerarquia no es fija por identidad sino por funcion productiva. El Hub es practicamente inamovible desde adentro — desplazarlo requiere redisenar toda la red. La respuesta inmunologica se activa por la direccion del crecimiento, no por el tamano: si el nodo crece para servir al sistema no hay amenaza; si crece para reorganizarlo, se activa mediante captura regulatoria o adquisicion. El Hub puede expandir su red mediante absorcion silenciosa, acuerdo pacifico o expropiacion — en ese orden de preferencia por costo energetico.

## 7.3 Resolucion Macro: La Colision de Superorganismos
Competencia entre redes fungicas completas. No existe un hub central que arbitre. La posicion relativa se determina por Masa Gravitacional (MG): PIB total, densidad poblacional, nivel tecnologico y area territorial. El freno real a la expansion agresiva no son los organismos reguladores internacionales sino la red interna de nodos del superorganismo. Entre dos superorganismos de masa comparable, el que ejecuta el leapfrog primero termina con ventaja a largo plazo. El Nodo Atomico nunca escapa completamente del sistema Macro: su existencia legal y tributaria esta anclada al superorganismo donde reside.

## 7.4 Principios de Interaccion entre Escalas
Principio de Transmision en Cascada: los eventos de escala Macro impactan los tres sistemas en cascada descendente — primero Macro, luego Meso, finalmente Micro. La velocidad de transmision depende del nivel de independencia dimensional de cada nodo.

Principio de Velocidad Escalar: TC_micro en horas a meses (IA: 1.2 mil millones de usuarios en 3 anos; HackerEarth: ciclo en 13.5 horas). TC_meso en meses a anos (empresas: 1-5 anos normal, 11 dias bajo presion COVID). TC_macro en decadas a generaciones (internet: 30 anos; M-Pesa: 4 anos como caso excepcional). Diferencia de 10-100x entre cada nivel. La velocidad es la ventaja estructural del Nodo Atomico.



# 8. Verificacion Empirica SNT v2.0: Matriz de N-Cuerpos — Mexico
La taxonomia de cinco niveles se verifica con datos INEGI 2022-2023 para las 32 entidades federativas. Nivel 0 (CDMX): 1 entidad, 14.8% del PIB nacional. Nivel 1 (9 atractores secundarios): 41.0%. Nivel 2 (8 bypass logisticos): 20.2%. Nivel 3 (11 nodos sombra): 16.8% con el mayor numero de entidades. Nivel E (3 anomalias exogenas): 4.3%. El ajuste de ley de potencia confirma que el sistema sigue preferential attachment: b=-0.473, R2=0.838, p<0.001.

El gradiente compuesto de Tlaxcala es el hallazgo mas importante de la v2.0: el modelo binario media w_ij(Tlaxcala->Puebla) = 26.2k MXN. La matriz N-cuerpos revela w_ij(Tlaxcala->CDMX largo alcance) = 216.8k MXN. Gradiente compuesto total: 243.0k MXN. El modelo binario subestimaba la satelizacion de Tlaxcala en un factor de 9.3x. El 89.2% de la extraccion va directamente a CDMX saltando al intermediario. Atacar solo la relacion Tlaxcala-Puebla es resolver el 10.8% del problema.

La vectorizacion de trayectorias para ocho entidades (1940-2022) revela dos grupos naturales. Satelizacion (b>0): Chiapas (b=0.229, R2=0.839), Oaxaca (b=0.176), Guerrero (b=0.176), Veracruz (b=0.181), Tlaxcala (b=0.147), Puebla (b=0.116). Convergencia (b<0): Queretaro (b=-0.155, R2=0.782, p<0.01) y Nuevo Leon (b=-0.058, R2=0.935, p<0.001). Estos dos son los primeros casos documentados de leapfrog exitoso dentro del sistema nacional — Queretaro via manufactura aeroespacial, Nuevo Leon via exportacion manufacturera independiente del hub central.



# 9. Limitaciones
Las limitaciones del corpus empirico original se mantienen: incertidumbre de datos pre-1820, N pequeno en casos historicos (4 casos), bajo R2 en el caso Portugal (0.123), posible causalidad inversa en el caso digital, sesgo de seleccion de casos y sensibilidad a la eleccion del trigger en casos graduales.

Limitaciones adicionales del Modelo de Triple Resolucion: los Modulos Micro y Macro son marcos conceptuales con operacionalizacion parcial. Las variables RQ, RL, DI, DP y MG tienen criterios de medicion propuestos pero no han sido validadas empiricamente con series de datos estructuradas. El Indice de Soberania Atomica (ASI) se propone como hipotesis de trabajo. Umbrales de fase calibrados empiricamente con N=4,774 usuarios HackerEarth 2026: Fase 1 ASI<0.016 (mediana Basic), Fase 2 ASI 0.016-0.167 (mediana Intermediate), Fase 3 ASI 0.167-1.0, Fase 4 ASI≥1.0 (precision=1.0, validado). El Factor de Coherencia Ck tiene mecanismo neurologico verificado (Friston 2010) pero su operacionalizacion para el modelo no ha sido probada. El Composite Score Index Empresarial (CSIE) requiere aplicacion en caso real. Las series historicas de PIB estatal 1940-1993 son estimaciones construidas con Maddison Project como proxy — no datos directos del INEGI.



# 10. Criterios de Refutacion
RC1 — Velocidad Escalar: refutado si una tecnologia es adoptada sistematicamente mas rapido por empresas que por individuos (RC1a), o si emerge una tecnologia sin acceso individual que invierte la jerarquia TC_micro < TC_meso < TC_macro (RC1b). Condicion de aplicabilidad: el principio aplica a tecnologias digitales accesibles individualmente.

RC2 — Respuesta Inmunologica: refutado si se documenta sistematicamente que hubs incorporan capacidades de nodos perifericos sin adquirirlos — adaptando sus estructuras hacia el nodo en lugar de suprimirlo. La respuesta es condicional: se activa cuando el nodo compite en el mismo plano; se invierte cuando complementa una capacidad que el hub no puede replicar.

RC3 — Inextractabilidad Cualitativa: refutado si un hub neutraliza sistematicamente el efecto diferencial del conocimiento de un nodo mediante brain drain, reverse engineering o saturacion deliberada. La condicion no es extraccion directa sino neutralizacion del efecto diferencial.

RC4 — Umbral Minimo Dual: refutado si un leapfrog se sostiene con RQ o RL por debajo del umbral minimo operacional. El postulado no requiere equilibrio entre dimensiones — solo presencia de ambas por encima de su minimo respectivo.

RC5 — Secuencia de Expansion: refutado si la expropiacion directa produce estados mas estables que la absorcion silenciosa para la misma clase de nodo. La expropiacion como primera opcion ocurre cuando el tiempo es el recurso critico, no por error estrategico.

RC6 — Irreversibilidad: refutado si un Nodo Sombra revierte la satelizacion desde adentro del sistema sin trigger exogeno, con el hub operando normalmente y sin intervencion de actores externos. La reversion es tecnicamente posible pero practicamente inviable porque el hub tiene mas recursos para frenar la reestructura que el nodo para ejecutarla.



# 11. Protocolo de Diagnostico
El modelo es prescriptivo ademas de descriptivo. Cuatro pasos para aplicar la SNT v2.0 a cualquier sistema real.

Paso 1 — Clasificacion de nivel: recopilar datos de produccion del nodo. Verificar si la distribucion sigue ley de potencia (ajuste log-log, R2 > 0.7, p < 0.05). Clasificar en la taxonomia de cinco niveles segun posicion relativa en la distribucion.

Paso 2 — Calculo de gradientes: calcular w_ij para cada hub que extrae del nodo. Calcular el gradiente compuesto si hay multiples hubs. El error mas comun es medir solo el gradiente hacia el hub inmediato — el caso Tlaxcala muestra que el gradiente de largo alcance puede ser 8.3x mayor que el directo.

Paso 3 — Estimacion del horizonte de sucesos: ajustar la trayectoria historica. Si b > 0 (satelizacion), estimar t_horizon. Si b < 0 (convergencia), identificar el mecanismo y verificar su sostenibilidad.

Paso 4 — Identificacion de la dimension ortogonal: buscar dimensiones donde el hub no ha invertido en 5-10 anos, donde el nodo tiene ventaja inicial medible, y donde la dimension tiene potencial de preferential attachment. Verificar que no requiera infraestructura controlada por el hub. Disenar la intervencion: atacar la deficiencia critica al minimo, construir capacidad en la nueva dimension sin activar la respuesta inmunologica, ejecutar el leapfrog cuando la ventana este abierta.



# 12. Corpus de 721 Casos Reales — Hallazgos Definitivos

El corpus empirico v30 comprende 721 casos reconstruidos en su totalidad desde
fuentes primarias verificables (Maddison Project, INEGI, US Census, JHU COVID-19,
Open Exoplanet Catalogue, MacLulich/Elton, HackerEarth). Reemplaza el corpus previo
de 502 casos, retirado tras una auditoria que detecto ~188 valores de b sinteticos
(np.random.normal()) y una columna R2 con valores imposibles (hasta -7.332). Integridad
del corpus v30: R2 en [0,1] en todos los casos (0 negativos, 0 mayores que 1), cada b
reproducible desde scripts publicos en reconstruction_real/. El 89% de los casos son
estadisticamente significativos (p<0.05).

Distribucion por dominio (friccion, n, b_media): A Ciudades (media, 4), B Paises
Maddison (alta, 446, +0.092), C Regiones INEGI+US Census (alta, 24, +0.091), D Digital
(baja, 3, -1.364), E1 Invasion biologica (nula, 4, +2.891), E2 Depredador-presa (alta,
2, +0.145), E3 Parasito-huesped COVID (nula, 234, +0.912), F1-F3 Astronomico
(media/baja, 4). Total 721, b_media global +0.366.

Hallazgo 1 — La friccion institucional predice la satelizacion (resultado central):
Correlacion de Spearman entre el indice de friccion (ordinal 0-3 asignado a priori)
y b por caso, dominios sociales/biologicos (n=714): rho = -0.68, p = 2.5e-97. A mayor
friccion institucional, menor exponente de satelizacion.

Hallazgo 2 — Separacion de regimenes: los dominios biologicos sin friccion (E1+E3)
producen b_media = +0.95; los economicos con friccion (A+B+C) producen b_media = +0.09.
Mann-Whitney U = 103,538, p = 2.4e-74. Los sistemas sin freno institucional se
satalizan ~10x mas rapido. Este es el resultado empirico central del modelo y es mas
fuerte con datos reales que con los sinteticos previos.

Hallazgo 3 — Los triggers abruptos son mas rapidos que los graduales: ratio 5.9x,
Mann-Whitney U=24,802, p=1.91e-5 (n=486, excluyendo E2 y F4 por interdependencia
mutua). Resultado estable a traves de tres expansiones sucesivas del corpus (57 -> 114
-> 721 casos). Nota: el corpus de 57 casos sugeria que los triggers hibridos eran los
mas rapidos (p=0.0098); con el corpus completo ese resultado no se sostiene (artefacto
de N pequeno) y la jerarquia estable es abruptos > hibridos > graduales.

Hallazgo 4 — La soberania politica frena la satelizacion tanto como la
interdependencia ecologica: los pares de paises soberanos (b_media~+0.09) y los
sistemas depredador-presa (E2, b_media=+0.145) son estadisticamente indistinguibles —
dos mecanismos distintos que anclan b cerca de cero porque la satelizacion completa
destruiria al hub.

Hallazgo 5 — Regimenes de modelado: la ley de potencia es la mejor descripcion donde
la friccion es baja (epidemias E3: mejor en 6/8; invasion E1: b>1 consistente); en
alta friccion (paises) compiten exponencial (~49%) y lineal (~35%). El exponente b
sigue siendo una metrica descriptiva comparable entre dominios, no la afirmacion de
que la ley de potencia sea el unico modelo generativo en todos ellos.

# 13. Capa de Colapso Orbital Acoplado (ACO-A)

La Arquitectura de Colapso Orbital deja de ser un modulo aparte y se reformula como
una capa universal y transversal de la SNT: el colapso es un eje ortogonal que puede
activarse en cualquier sistema, de cualquier dominio, en cualquier punto de su
trayectoria. Lo demostramos con datos reales en cinco dominios — finanzas, historia,
cripto, biologia y astronomia — y mostramos que un solo principio (minima friccion)
genera distintos modos de colapso segun las condiciones de frontera.

## 13.1 Dos ejes ortogonales (b perpendicular a Delta)
Cada sistema es un par de coordenadas independientes. Eje 1 — Satelizacion:
R(t)=a*t^b, como evoluciona la dominancia mientras la relacion acoplada corre.
Eje 2 — Colapso: A(tau)=c*tau^Delta, con tau = tiempo desde la extincion funcional;
Delta mide la velocidad/forma de la absorcion una vez que el hub colapsa. El colapso
no espera a que termine el ciclo de satelizacion (reloj distinto, tau != t).
Prediccion falsable: entre casos con b y Delta medidos, corr(b, Delta) ~ 0. Primer
test (cripto emparejado, n=11): Spearman rho(b_subida, Delta_caida) = +0.009 (p=0.98)
— consistente con la ortogonalidad.

## 13.2 Capa de hazard h(tau): la inevitabilidad en forma falsable
"Ningun sistema es eterno" = h(tau) > 0 para todo sistema (probabilidad de colapso
nunca cero); refutable si se halla un sistema con hazard = 0. Primer hazard estimado
(cohorte cripto, n=41, extincion funcional = precio < 1% del maximo historico): 15
extinciones repartidas en todo el rango de edad (0.27-8.6 anos), sin periodo libre de
muerte; Kaplan-Meier decreciente; hazard positivo y creciente con la edad —
consistente con h(tau)>0. Caveats: sesgo de supervivencia (hazard real mayor),
confound edad/calendario, n limitado.

## 13.3 Taxonomia de modos de colapso (tres factores)
El modo lo gobiernan friccion x trigger x (hay piso/techo en la magnitud?):
Decaimiento Orbital Regulado (friccion alta -> ley de potencia suave o exponencial,
no acelera; testigos: cohorte 2008 R2=0.85-0.99, Roma/URSS, fulguracion solar
R2=0.975, TDE R2=0.84); Decaimiento Craquelado (friccion~0 + gradual -> fragmentacion
erratica; EOS R2=0.10-0.70); Caida-a-piso (friccion~0 + abrupto + con piso -> ley de
potencia a un piso residual; FTX R2=0.875); Acantilado Catastrofico (friccion~0 +
abrupto + sin piso -> super-exponencial; LUNA, 5.6 ordenes de magnitud en 11 dias);
Barrido Logistico (magnitud acotada -> curva S; Delta->Omicron k=0.22/dia).

## 13.4 Principio de Minima Friccion (unificador)
Todo colapso sigue la trayectoria que minimiza la friccion integrada (familia
variacional: Fermat, minima accion, minima disipacion). Equivale a un flujo gradiente
sobre un paisaje de estabilidad (la bola que sale de su valle). Version falsable: el
colapso realizado tiene menor friccion integrada que las trayectorias contrafactuales
(WaMu por via FDIC pre-arreglada = minima friccion -> 21 h; Lehman sin esa via ->
fragmentacion lenta, 30,681 h; rango ~1,460x, monotonico con el grado de intervencion
regulatoria).

## 13.5 Resultados con datos reales (cuatro de la hoja de ruta)
(1) Friccion operacionalizada: dentro del cohorte financiero 2008 (n=6), friccion del
canal de resolucion (ordinal 1-6) vs Delta: Spearman rho = -1.000, p<0.001 — mas
friccion, absorcion mas frontal y ordenada. (2) Ortogonalidad b perpendicular Delta:
cripto n=11, rho=+0.009 (§13.1). (3) Biologia sin techo: la ola Omicron en casos
absolutos (Sudafrica, JHU) decae exponencial suave (R2=0.96, e-fold ~22 d), NO
acantilado — la retroalimentacion epidemiologica es friccion intrinseca. (4) Hazard
h(tau)>0 (§13.2). Conexion con el hallazgo central: la friccion institucional predice
b (rho=-0.68) y tambien gobierna la forma de Delta — es la palanca de los dos ejes.
Caveats: evidencia correlacional, n chico en cripto, dominios que difieren en mas que
la friccion; se enmarca como hipotesis fuerte, no como prueba causal.

# 14. Dialogo con la Literatura
Barabasi y Albert (1999): la SNT extiende el preferential attachment cuantificando la velocidad de satelizacion mediante el exponente b y proponiendo una taxonomia de cinco niveles funcionales. Verificacion con INEGI confirma la distribucion predicha (b=-0.473, R2=0.838, p<0.001).

Watts y Strogatz (1998): la SNT agrega la dimension direccional del flujo de recursos al coeficiente de clustering. Dos nodos pueden estar a poca distancia de conexion pero en niveles jerarquicos radicalmente distintos.

Holland (1995): la SNT especifica la satelizacion como dinamica emergente recurrente con trayectoria matematicamente predecible dentro de los Sistemas Adaptativos Complejos.

Friston (2010): la SNT extiende el Principio de Energia Libre mas alla del cerebro individual hacia los sistemas sociales. La respuesta inmunologica del hub y el Factor de Coherencia Ck son manifestaciones del mismo principio a distintas escalas.

Brezis y Krugman (1993): la SNT extiende el leapfrogging tecnologico a tres escalas y formaliza las condiciones de fallo que el modelo original no desarrollo.



# 15. Conclusiones
## 15.1 Lo que la SNT demuestra
La satelizacion opera en tres escalas con dinamicas distintas no intercambiables. La taxonomia de cinco niveles es verificable con datos INEGI y sigue ley de potencia. El modelo binario subestimaba el grado de satelizacion de Tlaxcala en 9.3x. Los primeros casos de leapfrog exitoso dentro del sistema nacional mexicano estan documentados: Queretaro (b=-0.155) y Nuevo Leon (b=-0.058) convergiendo hacia CDMX mediante salto dimensional. Con el corpus real de 721 casos, la friccion institucional es el predictor dominante de b (rho=-0.68, p=2.5e-97) y gobierna ademas la forma del colapso (Delta): una sola variable une como dominas y como colapsas. La hipotesis de la proporcion aurea (H-phi) fue probada y refutada en 4 rondas y queda fuera de los claims.

## 15.2 Lo que la SNT no demuestra
Que el leapfrog sea siempre posible para cualquier nodo. El modelo formaliza las condiciones de viabilidad y los mecanismos de fallo pero no garantiza el exito cuando esas condiciones se cumplen. Los Modulos Micro y Macro requieren validacion empirica independiente.

## 15.3 Lineas de investigacion futura
Validacion del Modulo Micro con datos longitudinales de trayectorias individuales. Operacionalizacion del ASI con datos comportamentales. Extension de la matriz N-cuerpos a otros sistemas nacionales. Identificacion de mas casos de leapfrog exitoso en sistemas Meso. Formalizacion matematica del Principio de Transmision en Cascada con datos de perturbaciones exogenas (COVID-19, crisis financiera 2008).

## 15.4 La implicacion mayor
La implicacion mas importante no es teorica sino practica. Si la satelizacion sigue un algoritmo predecible con una taxonomia de fallos identificable, es intervenible. Para Tlaxcala: el 89.2% del gradiente no viene de Puebla sino de CDMX. Cualquier estrategia que solo ataque la relacion Tlaxcala-Puebla resuelve el 10.8% del problema. Para el Nodo Atomico: el leapfrog cognitivo — orquestar agentes de IA en lugar de ejecutar tareas lineales — es la primera dimension en la historia reciente donde la ventaja acumulada de los nodos dominantes no aplica directamente. La evidencia de HackerEarth 2026 sugiere que esa ventana esta abierta ahora.

El algoritmo de satelizacion es predecible. La taxonomia de fallos del leapfrog es conocida. Lo que sigue es una decision que ningun modelo puede tomar por el nodo.



# Referencias
Avey, J.B., Reichard, R.J., Luthans, F. y Mhatre, K.H. (2011). Meta-analysis of the impact of positive psychological capital on employee attitudes, behaviors, and performance. Human Resource Development Quarterly, 22(2), 127-152.

Barabasi, A.L. y Albert, R. (1999). Emergence of Scaling in Random Networks. Science, 286(5439), 509-512.

Bolt, J. y van Zanden, J.L. (2024). Maddison Project Database 2023. University of Groningen. https://www.rug.nl/ggdc/historicaldevelopment/maddison/

Brezis, E.S. y Krugman, P.R. (1993). Leapfrogging in International Competition. American Economic Review, 83(5), 1211-1219.

Costa, L.F., Palma, N. y Reis, J. (2015). The great escape? European Review of Economic History, 19(1), 1-22.

Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience, 11(2), 127-138. DOI: 10.1038/nrn2787

Gelderblom, O. (2013). Cities of Commerce. Princeton University Press.

Holland, J.H. (1995). Hidden Order: How Adaptation Builds Complexity. Addison-Wesley.

INEGI (2022). PIB per capita por entidad federativa. Sistema de Cuentas Nacionales de Mexico. https://www.inegi.org.mx/temas/pib/

OCDE (2020). Start-ups, Killer Acquisitions and Merger Control. DAF/COMP(2020)5.

Ringrose, D.R. (1973). Madrid and the Spanish Economy, 1560-1850. Journal of Economic History, 33(2), 284-314.

Strogatz, S.H. (2001). Exploring complex networks. Nature, 410(6825), 268-276.

Van der Wee, H. (1963). The Growth of the Antwerp Market and the European Economy. Martinus Nijhoff.

Watts, D.J. y Strogatz, S.H. (1998). Collective dynamics of small-world networks. Nature, 393(6684), 440-442.

Zainos Corona, E. (2026). Shadow Node Theory — Replication Package v2.5.0 (corpus real de 721 casos + capa de colapso ACO-A). Zenodo. https://doi.org/10.5281/zenodo.19446521

Thom, R. (1972). Stabilite structurelle et morphogenese. [catastrofe de pliegue]

Waddington, C.H. (1957). The Strategy of the Genes. [paisaje epigenetico]

Holling, C.S. (1973). Resilience and stability of ecological systems. Annual Review of Ecology and Systematics, 4, 1-23.

Lenton, T.M. et al. (2008). Tipping elements in the Earth's climate system. PNAS, 105(6), 1786-1793.

Fuentes de datos de la capa de colapso: Yahoo Finance (LUNA, FTT, EOS); NOAA SWPC GOES (rayos X solares); NASA IRSA / ZTF (TDE AT2019qiz); CoV-Spectrum / LAPIS (variantes SARS-CoV-2); SEC, FDIC, Federal Reserve, SIGTARP (cohorte 2008).

— Fractal Core Research — Pre-print v2.5.0 (marco v30) — Tlaxcala, Mexico — 2026 —