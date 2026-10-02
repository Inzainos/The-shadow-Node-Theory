# Casos de uso — aplicaciones independientes de la SNT

Apartado para las aplicaciones de la Shadow Node Theory **fuera del corpus de 721
casos**. Son pruebas de la teoría contra datos que no formaban parte de su
construcción: ninguna modifica el corpus, ninguna toca una cifra publicada, y cada
una puede fallar sin arrastrar al resto.

Se separan del corpus a propósito. El corpus es el cuerpo de evidencia histórico de
la teoría, con su auditoría y su versionado; esto es el banco de pruebas. Un caso de
uso que sale negativo **se queda documentado aquí con su cifra**, porque un banco de
pruebas del que solo se publican los aciertos no sirve para nada.

---

## 0. Protocolo común, obligatorio

Todo caso de uso de este apartado cumple, sin excepciones:

1. **Pre-registro subido antes de descargar un solo byte de análisis.** El commit del
   pre-registro es anterior al primer dato, y se cita por su hash en el informe. Fija
   hipótesis, estadísticos, reglas de decisión, exclusiones y —esto es lo importante—
   **qué significaría cada desenlace posible**, para que ninguna lectura se acomode
   después.
2. **Ceguera declarada con honestidad.** Si el analista ya vio los datos, se dice
   ("ceguera: ninguna"). Simular una ceguera que no hubo es peor que no tenerla.
3. **Se reporta todo resultado**, favorable o no, incluidos los "no evaluable" y los
   "sin poder".
4. **Log obligatorio.** Todo script escribe su registro en `reconstruction_real/logs/`
   (no versionado, por tamaño).
5. **Provenance con SHA-256** de cada descarga y de cada salida versionada, en
   [`data/FUENTES.md`](data/FUENTES.md).
6. **Sección de Desviaciones** en cada informe, con lo que se hizo distinto al
   pre-registro y por qué.
7. **Semilla fija** en todo bootstrap y simulación (`20261002` en los casos de esta
   ronda).

---

## 1. Capa ACO-A en el ecosistema npm — **completado**

**Pregunta:** ¿la capa de colapso ACO-A (hazard positivo, ortogonalidad b ⊥ Δ, modos
de colapso) aparece en un dominio que la teoría nunca vio: 4.4 millones de paquetes
de software libre?

| Documento | Ruta |
|---|---|
| Pre-registro | [`reconstruction_real/preregistro/PREREGISTRO_NPM_2026-10-02.md`](reconstruction_real/preregistro/PREREGISTRO_NPM_2026-10-02.md) (commit `3ff9fca`) |
| Informe | [`reconstruction_real/audits/RESULTADOS_NPM_2026-10-02.md`](reconstruction_real/audits/RESULTADOS_NPM_2026-10-02.md) |
| Código | `reconstruction_real/code/npm_cohorte_aco.py`, `npm_pruebas_aco.py` |
| Datos | `reconstruction_real/data/npm_cohorte_aco.csv.gz`, `npm_hazard_bandas.csv` |

**Diseño.** Marco de muestreo de **4,446,361** paquetes del registro completo
(`replicate.npmjs.com/_all_docs`, paginado), muestreo sistemático de 1 en 370 con
semilla fija → 12,017 nombres, y una cadena de atrición fijada de antemano hasta
**450 paquetes** ajustables. Extinción funcional definida sobre la serie diaria de
descargas; severidad de vulnerabilidades por la etiqueta de OSV.

| Prueba | Resultado | Decisión |
|---|---|---|
| Positividad del hazard | 8 de 11 bandas de edad con fines; las bandas de 8, 9 y 10 años (n = 106, 71, 32) sin ninguno | **NO RESPALDADA** |
| Forma del hazard | Spearman(edad, h) = **−0.716**, p 2 colas = 0.013 | **NO RESPALDADA**, y significativamente **decreciente** |
| Ortogonalidad b ⊥ Δ | ρ = **+0.114**, IC 95% **[+0.016, +0.209]** sobre 450 pares | **RESPALDADA** por equivalencia |
| Abrupto contra anunciado | La regla selecciona **1 solo caso** | **NO EVALUABLE** |

**Lo que aportó a la teoría.** La ortogonalidad **RC9 deja de depender de un solo
dominio y un solo ciclo de mercado**: npm la respalda con el signo opuesto al de
cripto, que es la clase de confirmación que importa. En cambio el hazard creciente de
la v30 **no sobrevive** aquí: es el tercer dominio con una tercera forma, así que la
afirmación de un hazard universalmente creciente no se sostiene.

**Lo que aportó de método.** La codificación de fricción a priori salió **degenerada**
(0 paquetes de fundación, 3 corporativos) porque un muestreo aleatorio de un registro
completo está dominado por la cola larga. Queda anotado: para medir fricción en un
dominio así hace falta muestreo estratificado, no aleatorio simple.

---

## 2. Réplica internacional del ajuste rango-tamaño — **completado**

**Pregunta:** la retirada de la lectura de apego preferencial del Módulo de N-cuerpos
se apoyaba en 32 entidades mexicanas. ¿Es un hecho general o una peculiaridad de
n = 32? Otros países publican datos subnacionales abiertos con **miles** de unidades.

| Documento | Ruta |
|---|---|
| Pre-registro | [`reconstruction_real/preregistro/PREREGISTRO_RANGO_TAMANO_2026-10-02.md`](reconstruction_real/preregistro/PREREGISTRO_RANGO_TAMANO_2026-10-02.md) (commit `5b97328`) |
| Informe | [`reconstruction_real/audits/RESULTADOS_RANGO_TAMANO_2026-10-02.md`](reconstruction_real/audits/RESULTADOS_RANGO_TAMANO_2026-10-02.md) |
| Código | `reconstruction_real/code/rango_tamano_internacional.py`, `rango_tamano_percapita.py`, `rango_tamano_diagnostico.py` |
| Datos | `reconstruction_real/data/rango_tamano_internacional.csv`, `rango_tamano_poder.csv`, `rango_tamano_percapita.csv`, `rango_tamano_diagnostico.csv` |

**Diseño.** Seis niveles territoriales, año 2021, PIB total: estados y municipios de
Brasil (IBGE SIDRA), NUTS1/2/3 de la Unión Europea (Eurostat) y las 32 entidades
mexicanas. De **27 a 5,570 unidades**. Cada nivel es una réplica independiente.

| Nivel | n | órdenes de magnitud | b | ΔAIC | Veredicto |
|---|---:|---:|---:|---:|---|
| Brasil, estados | 27 | 2.17 | −1.3735 | +51.5 | LOGNORMAL (fuerte) |
| México, entidades | 32 | 1.47 | −0.9240 | +40.9 | LOGNORMAL (fuerte) |
| UE, NUTS1 | 111 | 2.75 | −1.0933 | +263.5 | LOGNORMAL (fuerte) |
| UE, NUTS2 | 293 | 3.58 | −1.0244 | +815.0 | LOGNORMAL (fuerte) |
| UE, NUTS3 | 1,327 | 3.11 | −1.0466 | +4,868.5 | LOGNORMAL (fuerte) |
| **Brasil, municipios** | **5,570** | **4.66** | −1.3940 | **−914.6** | **POTENCIA (fuerte)** |

ΔAIC > 0 favorece a la lognormal. Secundaria per cápita: la lognormal gana **4 de 4**.

**Tres resultados, en orden de importancia:**

1. **La hipótesis pre-registrada falla.** Escribí "la lognormal gana en todos los
   niveles". Gana en cinco de seis. Los 5,570 municipios de Brasil favorecen la ley de
   potencia, y así queda escrito.
2. **La prueba de bondad de ajuste de Clauset nunca alcanza poder utilizable.** La
   tasa de falso "sobrevive" va de 96.8% (n = 27) a **42.6% (n = 5,570)**, siempre por
   encima del umbral del 20% fijado de antemano. Por regla pre-registrada, la prueba
   de distribución **no se interpretó en ningún nivel**. El 96.4% de México nunca fue
   una limitación mexicana: es la curva de poder del método.
3. **No es un artefacto de n, y tampoco del rango dinámico.** Con el rango de Brasil
   clavado en 4.66 órdenes, la potencia gana en **93–99% de 200 réplicas a todos los
   tamaños entre 27 y 2,785** (diagnóstico post hoc, etiquetado como tal). Pero los
   1,327 municipios mayores de Brasil y las 1,327 regiones NUTS3 comparten n, rango
   (3.05 contra 3.11), σ (1.05 contra 1.12) y b (−1.057 contra −1.047) y dan
   **veredictos opuestos y aplastantes** (−2,919 contra +4,868). La diferencia está en
   la curvatura de la curva rango-tamaño y **su causa no está identificada**.

**Lo que aportó a la teoría.** Refuerza la retirada del 2026-10-02 en vez de
reabrirla: si la forma depende de cómo se parte el territorio, **la forma no puede ser
evidencia de un mecanismo generador**, en ningún sentido. Y obliga a matizar la
afirmación de invariancia **para la forma de la distribución de tamaños** — no para el
eje de satelización ni para ACO-A, que esta prueba no toca.

**Lo que aportó de método.** Dos cosas reutilizables:

- **Los códigos "Extra-Regio" de Eurostat contaminan cualquier distribución de
  tamaños.** Son 16 por nivel NUTS, tienen la longitud de código correcta, y no son
  unidades territoriales: embajadas, plataformas marinas, buques. Incluidos, ocupan
  toda la cola baja e inflan el rango dinámico europeo de ~3 a 4.5 órdenes de
  magnitud, que es la cantidad decisiva del método de Clauset. Se excluyen con
  `es_region()`.
- **Una prueba de poder vale más que un p.** Sin la curva de poder, el p = 0.974 de
  México se habría leído como "la ley de potencia sobrevive".

---

## 3. Casos diferidos

No son casos fallidos ni, hoy, casos bloqueados por técnica: están **diferidos por
decisión del autor** hasta que las fuentes mexicanas de datos abiertos se estabilicen.

| Caso | Qué probaría | Estado |
|---|---|---|
| **Satelización económica de la ZEE mexicana** | El eje **b** de la SNT sobre empleo y actividad por municipio, con la Ciudad de México como hub | **Diferido por decisión del autor** |
| **N-cuerpos municipal** | La matriz de N-cuerpos al nivel municipal mexicano, en vez de las 32 entidades | **Diferido por decisión del autor** |

### Historia del acceso, medida y fechada

La causa técnica cambió entre mediciones, así que queda el registro de las dos para no
repetir el diagnóstico ni arrastrar una nota vieja:

| Fecha | Medición |
|---|---|
| 2026-10-02, mañana | Los CDN mexicanos (INEGI, IMSS, `datos.gob.mx`) respondían con un bloqueo **del lado del origen**: Akamai, `errors.edgesuite.net`. No era el proxy de la sesión — las APIs internacionales (Eurostat, IBGE, ONS, Banco Mundial) respondían sin problema |
| 2026-10-02, tarde | **El bloqueo de Akamai ya no aparece.** El servidor de INEGI contesta directo (`Microsoft-IIS/10.0`, 0.76 s). Lo que sigue dando 403 es la API CKAN de `datos.gob.mx` |

**Advertencia de método que vale más que el estado de la red.** INEGI devuelve
**HTTP 200 con una página de error** para cualquier ruta inexistente: 2,263 bytes de
HTML con el título "Página no encontrada". Un script que confíe en el código de estado
registrará descargas exitosas que no contienen datos. Hay que verificar el
`Content-Type` y el contenido, no el código. Este error ya se cometió una vez en esta
sesión.

Con el transporte abierto, lo que falta para correr estos dos casos no es red: son
rutas reales del directorio de INEGI, que exigen exploración y no adivinanza. El autor
decidió esperar; se desbloquea también si el archivo se aporta a mano.

---

## 4. Lo que los casos de uso le han hecho a la teoría

| Afirmación de la SNT | Antes de los casos de uso | Después |
|---|---|---|
| Ortogonalidad b ⊥ Δ (RC9) | Verificada solo en cripto (n = 11) | **Respaldada también en npm** (450 pares, ρ = +0.114, IC [+0.016, +0.209]), con el signo opuesto |
| Hazard de colapso creciente con la edad (v30) | Afirmada | **No sobrevive en npm** (ρ = −0.716, p = 0.013): tercer dominio, tercera forma |
| Positividad del hazard | Afirmada | **No respaldada en npm**: tres bandas de edad sin ningún fin |
| La jerarquía económica subnacional evidencia apego preferencial | Retirada con n = 32 | **Retirada y reforzada** con seis niveles y hasta 5,570 unidades |
| Invariancia de la forma de la distribución de tamaños | Afirmada | **Hay que matizarla**: mismo n, mismo rango, mismo σ, mismo b, veredictos opuestos entre Brasil y la UE |
| Gradiente compuesto de Tlaxcala (9.3×) | Verificado | **Sin cambio.** No depende de la forma de la distribución |

Tres de seis filas son negativas. Eso es el apartado funcionando como debe.

---

## 5. Cómo se propone un caso de uso nuevo

Para que un dominio sirva como caso de uso de la SNT tiene que cumplir las cinco:

1. **Datos abiertos y reproducibles**, con URL estable y hash. Nada de capturas, nada
   de datos que no se puedan volver a descargar.
2. **Fuera del corpus.** Si el dominio ya está en los 721 casos, no es una prueba
   independiente.
3. **Un eje de la teoría identificable de antemano**: satelización (`b`), colapso
   (`Δ`, hazard, modos), o la forma de la distribución. Un caso que no sabe qué eje
   prueba no prueba nada.
4. **n suficiente para el estadístico elegido, estimado antes de correr.** La lección
   del caso 2 es que esto hay que calcularlo, no suponerlo: una prueba sin poder
   produce un "no se descarta" que no significa nada.
5. **Falsable.** Tiene que existir un resultado posible que contradiga a la teoría, y
   tiene que estar escrito en el pre-registro antes de verlo.
6. **Por dominio.** El marco establece que **cada dominio tiene sus propios valores, y
   cada área dentro de un dominio también, y cada una es independiente** — Axioma 0.1
   (*"cada eje tenga definición operativa por dominio... no entra en ningún ajuste para
   ese dominio"*) y Axioma 2 (*"modos propios, no una frecuencia universal idéntica
   para todo"*). Entre dominios **solo** se admiten tres cosas: réplica independiente
   del mismo procedimiento, refutación de una afirmación universal por contraejemplo, y
   conteo de resultados independientes sin convertirlos en un estadístico único. **No**
   se admite ordenar dominios en una escala compartida ni leer la diferencia entre
   dominios como medición de la variable que los distingue. Ese error ya se cometió dos
   veces: en la prueba de fricción del 2026-09-27 y en la de deriva del 2026-10-02
   (auditoría: `reconstruction_real/audits/AUDITORIA_REGLA_POR_DOMINIO_2026-10-02.md`).

El orden de trabajo es siempre el mismo: pre-registro → commit → descarga → análisis
con log → informe con desviaciones → `FUENTES.md` → `CHANGELOG.md`.

---

*Fractal Core Research · Tlaxcala, México*
