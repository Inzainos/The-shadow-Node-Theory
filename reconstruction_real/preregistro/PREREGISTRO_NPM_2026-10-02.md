# Pre-registro — capa ACO-A en el ecosistema npm

**Fecha:** 2026-10-02 · **Rama:** `claude/charming-brown-w9h8iu` · **Base:** `main` en `4cdee3b`
· **Autor de la teoría:** Elán Zainos Corona · **Análisis:** Claude Code (sesión del
repositorio), a pedido del autor.

Este documento se sube al repositorio **antes** de descargar cualquier dato de análisis.
El commit y su fecha en GitHub son el sello de tiempo. Todo lo que se reporte después
debe seguir estas reglas; cualquier cambio se anota en la sección **Desviaciones** del
informe de resultados, con motivo, y nunca en silencio.

## 0. Qué es esto y qué no es

Es una **aplicación independiente** de la capa ACO-A a un dominio nuevo, fuera del corpus
de 721 casos. No modifica el corpus, no modifica ninguna cifra publicada y no forma parte
de la release v2.6.1. Si los resultados resultan citables, se integran en una versión
posterior; si no, queda el registro de que se probó.

**Por qué este dominio.** Tres razones que ningún otro candidato reúne a la vez:

1. **Sin filtro de supervivencia.** La prueba pre-registrada de disparadores (2026-09-27)
   quedó sesgada porque el archivo WUP 2018 de la ONU solo lista aglomeraciones que
   llegaron a 300 mil habitantes en 2018, de modo que los traslados fracasados (Dodoma,
   Yamoussoukro) quedaron fuera. **El registro de npm conserva a los perdedores:** un
   paquete muerto sigue listado con su serie completa.
2. **Réplica cruzada de la ortogonalidad.** El criterio RC9 (b ⊥ Δ) solo se ha probado en
   cripto, donde 153 de 242 máximos cayeron en 2021 — un solo ciclo de mercado. Este
   dominio tiene otro reloj y otra dinámica.
3. **Primera prueba de la taxonomía de modos de colapso con n grande.** Hoy esa taxonomía
   descansa en casos testigo elegidos a mano (LUNA, FTX, EOS), que es el tipo de evidencia
   que la auditoría v32 castigó en otros apartados.

## 0.1 Ceguera declarada

El analista **no ha descargado ni visto** ninguna serie de descargas, ningún listado de
paquetes ni ningún aviso de vulnerabilidad usado en las pruebas de abajo.

Sí se hizo, antes de escribir este documento, una **inspección de esquema** de las cuatro
APIs, sobre paquetes conocidos y ajenos a cualquier muestra (`left-pad`, `express`,
`lodash`, `colors`, `moment`, `requests`, `event-stream`). Se verificó únicamente:

- qué campos devuelve `registry.npmjs.org` (`time.created`, `time.modified`, versiones,
  presencia del campo `deprecated`);
- que la serie de descargas es diaria, que el rango máximo por petición es de **18 meses**
  y que el primer día con datos del servicio es **2015-01-10**;
- que el endpoint de descargas acepta hasta **128 paquetes por petición** (`bulk`);
- que `replicate.npmjs.com/_all_docs` expone el listado completo (**4,446,242** paquetes
  al 2026-10-02) y sirve como marco de muestreo;
- que `api.osv.dev` devuelve avisos con fecha de publicación y severidad.

No se miró ningún valor de descargas, máximo, caída ni extinción. Las cifras de esquema
citadas arriba condicionan el diseño y por eso se declaran.

## 0.2 Reglas generales

1. **Se reporta todo resultado**, favorable o no, con el mismo detalle.
2. **α = 0.05.** Donde la hipótesis tiene dirección pre-especificada, la prueba principal
   es de una cola; también se reporta el p de dos colas.
3. **Unidad de inferencia:** el paquete.
4. **Semilla fija:** `20261002` en toda aleatoriedad.
5. **Logs obligatorios** en `reconstruction_real/logs/` y **SHA-256** de cada archivo
   descargado, anotado en `data/FUENTES.md`.
6. **Censura:** la fecha de descarga de las series, anotada en el log.

---

## 1. Construcción de la cohorte

### 1.1 Marco de muestreo

`https://replicate.npmjs.com/_all_docs` (solo identificadores, sin documentos). Se recorre
el listado en streaming y se toma **una de cada k filas**, con el desplazamiento inicial
derivado de la semilla `20261002`, hasta obtener **12,000 nombres**. El muestreo es
sistemático y determinista: con la misma semilla y el mismo listado se reproduce.

No se almacena el listado completo (≈ 4.4 M filas) para no consumir disco innecesariamente;
se guarda la muestra resultante y su SHA-256.

### 1.2 Filtros de inclusión, en este orden

Se reporta la **atrición en cada paso**.

| # | Filtro | Motivo |
|---|---|---|
| 1 | `time.created` ≥ **2015-07-01** | El servicio de descargas empieza el 2015-01-10; se deja medio año de margen para que el inicio de la serie no esté truncado |
| 2 | `time.created` ≤ **2024-10-02** | Garantiza ≥ 24 meses de observación hasta el corte |
| 3 | El paquete no está despublicado (`unpublished` ausente) | Sin serie recuperable |
| 4 | Serie mensual con **≥ 24 meses** de datos | Mínimo para ajustar subida y caída |
| 5 | **≥ 1,000 descargas acumuladas en los primeros 180 días** | Umbral de actividad. Se mide en una ventana **temprana y predeterminada**, antes de que exista ningún máximo, para no condicionar el resultado |

**Sesgo declarado del filtro 5:** un paquete que arranca lento y alcanza su máximo mucho
después queda excluido. Es el análogo del filtro de supervivencia de WUP, pero en dirección
contraria (excluye arranques lentos, no finales fracasados) y se mide sobre una ventana
fijada de antemano. Se reporta cuántos paquetes caen por este filtro.

### 1.3 Agregación

**Totales mensuales.** Las descargas diarias de npm tienen estacionalidad semanal fuerte
(caída de fin de semana) que contaminaría cualquier ajuste log-log. El mes es la unidad.
`t = 1..n` meses desde el primer mes con datos.

### 1.4 Ajuste de exponentes

El mismo procedimiento del corpus: **MCO de log(y) contra log(t)** con `t = 1..n`
(`calc()` de `expand_B_massive.py`). Se reporta b, R², r de Pearson y p.

- **b_subida:** del primer mes de la serie al **máximo mensual**.
- **Δ_caída:** del máximo mensual al **mínimo posterior**.

Es el mismo método de `reconstruction_real/code/orthogonality_test.py`, trasladado de
precios diarios a descargas mensuales.

### 1.5 Extinción funcional (criterio ACO adaptado)

Un paquete está **funcionalmente extinto** cuando sus descargas mensuales caen por debajo
del **1% de su máximo mensual histórico** durante **≥ 6 meses consecutivos**. La fecha de
extinción es el **primer mes de esa racha**.

Es la traducción directa del criterio usado en la cohorte cripto (precio < 1% del máximo
histórico), con la racha de 6 meses añadida porque las descargas tienen más ruido que el
precio.

---

## 2. Punto 1 — Hazard h(τ) > 0

**Pregunta.** ¿"Ningún sistema es eterno" se sostiene en una tercera cohorte independiente,
y qué forma tiene el hazard?

**Diseño.** Nacimiento = `time.created`. Fin = extinción funcional (§1.5). Censura = fecha
de corte. Bandas de edad de **1 año**. Se reporta, por banda: en riesgo, fines, hazard
h = fines / en riesgo.

**H1a — Positividad.** Toda banda de edad con **≥ 30 en riesgo** tiene al menos un fin.
Una banda con 0 fines no refuta por sí sola (se reporta su cota superior 3/n) pero cuenta
como "sin evidencia de positividad" en esa banda.

**H1b — Forma (afirmación de la v30).** El hazard **crece** con la edad:
Spearman(edad de banda, h) > 0, una cola. Respaldada si p < 0.05.

> **Estado previo de H1b, declarado antes de correr:** la v30 afirmaba hazard creciente.
> En la cohorte cripto salió creciente (ρ = +0.881, p = 0.002) pero **confundido con el
> calendario**. En la cohorte de bancos FDIC **no se sostuvo** (ρ = +0.050, p = 0.38;
> forma de bañera). Esta es la tercera cohorte y decide si la forma es
> **dominio-dependiente**, que es la lectura actual del repositorio.

**Secundaria.** Fin alternativo = **retiro** (campo `deprecated` presente en la última
versión, o paquete despublicado), contado como fin además de la extinción funcional.

**Confusión edad/calendario, declarada de antemano.** Igual que en cripto, los paquetes
nacidos temprano llegan a edades altas en años recientes. Se reporta la **distribución de
años calendario de las extinciones** junto al hazard, para que el lector juzgue. La
separación edad-periodo-cohorte queda fuera de alcance y se declara pendiente.

---

## 3. Punto 2 — Ortogonalidad b ⊥ Δ

**Pregunta.** ¿La velocidad de subida y la forma de la caída son independientes en un
dominio distinto de cripto?

**Criterios de admisión del par (b_subida, Δ_caída).** Serie de **≥ 24 meses**; máximo con
**≥ 6 meses antes y ≥ 6 meses después**; **≥ 6 puntos** en cada ajuste. Es la traducción
mensual de los criterios de la prueba cripto (200 días de serie, 120 días a cada lado del
pico, 20 puntos por ajuste).

**H2.** Ortogonalidad.

**Criterio de equivalencia** (idéntico al de la prueba cripto):

| Resultado | Decisión |
|---|---|
| IC 95% de Spearman (Fisher) **dentro de [−0.3, +0.3]** | **Respaldada** |
| **\|ρ\| ≥ 0.3** con p < 0.05 | **Refutada** |
| Cualquier otro caso | Indeterminada |

**Secundarias.** (a) Pearson sobre los exponentes. (b) Spearman parcial controlando el
máximo mensual en log10 (el tamaño podría inducir correlación espuria en ambos ejes).

---

## 4. Punto 3 — Modos de colapso: disparador abrupto contra anunciado

**Pregunta.** ¿La taxonomía ACO-A predice la forma de la caída? La taxonomía dice que
fricción ≈ 0 + disparador abrupto + sin piso → **Precipicio Catastrófico** (caída
pronunciada), mientras que fricción alta + anunciado → **Decaimiento Orbital Regulado**
(caída suave).

**Codificación del disparador, fijada aquí, antes de ver ninguna serie.**

| Clase | Regla |
|---|---|
| **Abrupto** | Existe un aviso en OSV para ese paquete en npm con severidad **CVSS ≥ 7.0**, cuya fecha de publicación cae en la ventana **[máximo − 3 meses, máximo + 6 meses]** |
| **Anunciado** | El campo `deprecated` está presente en la última versión publicada, **y** no hay aviso OSV con CVSS ≥ 7.0 en esa ventana |
| **Sin clasificar** | Todo lo demás. **Se excluye de este punto** y se reporta cuántos son |

Un paquete que cumpla ambas reglas se clasifica como **abrupto** (la vulnerabilidad manda
sobre la deprecación).

**Emparejamiento.** Cada caso abrupto se empareja 1:1, por vecino más cercano sin
reemplazo, con un caso anunciado que tenga:

- máximo mensual dentro de **±0.5 en log10**, y
- edad al máximo dentro de **±12 meses**.

Los abruptos sin pareja dentro de esas tolerancias se reportan como no emparejados y se
excluyen de la prueba principal.

**H3.** Δ_caída es **mayor en magnitud** (caída más pronunciada) en los abruptos que en los
anunciados: Wilcoxon de una cola sobre las diferencias emparejadas.

**Decisión.** *Respaldada* si p < 0.05 y la mediana de la diferencia va en la dirección
predicha. *No respaldada* en otro caso. *Contraria* si el p de dos colas < 0.05 con la
diferencia en sentido opuesto.

**Secundarias.** (a) Sin emparejar, Mann-Whitney entre los dos grupos. (b) Descriptivo:
R² del ajuste de potencia en cada grupo (la taxonomía predice **peor** ajuste de potencia
en el modo craquelado y **mejor** en el regulado). (c) Conteo de paquetes cuya caída se
detiene en un piso no nulo (candidatos a **Detenido en Piso**), definido como: mínimo
posterior al máximo ≥ 1% del máximo y estable ±50% durante ≥ 6 meses.

---

## 5. Fricción a priori — **solo descriptivo, no es hipótesis**

Se codifica, antes de ver los datos, con la organización dueña del repositorio declarado en
los metadatos:

| Fricción | Criterio |
|---|---|
| alta (3) | Organización de fundación: `apache`, `eclipse`, `openjs-foundation`, `cncf`, `nodejs`, `gnome`, `mozilla` |
| media (2) | Organización corporativa: `microsoft`, `google`, `facebook`, `aws`, `vercel`, `shopify`, `ibm`, `oracle`, `netflix` |
| baja (1) | Cualquier otra organización |
| nula (0) | Cuenta de usuario individual, o sin repositorio declarado |

> **Por qué no es hipótesis.** La prueba pre-registrada del 2026-09-27 encontró que la
> fricción **no ordena b** entre dominios (ρ = −0.131, permutación exacta p = 0.39), y el
> repositorio ya no sostiene esa afirmación fuera del contraste epidemias contra el resto.
> Construir una hipótesis principal sobre un mecanismo no respaldado sería un error.
> La codificación se incluye **solo** para describir la composición de la cohorte y para
> que un análisis futuro pueda retomarla si el mecanismo se rehabilita.

---

## 6. Salidas previstas

- `reconstruction_real/code/npm_cohorte_aco.py` — descarga y construcción de la cohorte, con log.
- `reconstruction_real/code/npm_pruebas_aco.py` — los tres puntos, con log.
- `reconstruction_real/data/npm_cohorte_aco.csv.gz` — una fila por paquete: nombre, nacimiento,
  máximo mensual, mes del máximo, b_subida, Δ_caída, R² de cada ajuste, fecha de extinción,
  clase de disparador, fricción a priori.
- `reconstruction_real/data/npm_hazard_bandas.csv` — hazard por banda de edad.
- `reconstruction_real/audits/RESULTADOS_NPM_2026-10-02.md` — informe con la tabla
  hipótesis → resultado → decisión y la sección **Desviaciones**.
- SHA-256 de cada descarga en `data/FUENTES.md`.

## 7. Fuentes

| Fuente | Uso |
|---|---|
| `https://replicate.npmjs.com/_all_docs` | Marco de muestreo (4,446,242 paquetes al 2026-10-02) |
| `https://registry.npmjs.org/{paquete}` | Nacimiento, versiones, `deprecated`, repositorio |
| `https://api.npmjs.org/downloads/range/{inicio}:{fin}/{paquetes}` | Serie de descargas (máx. 18 meses y 128 paquetes por petición; datos desde 2015-01-10) |
| `https://api.osv.dev/v1/query` | Avisos de vulnerabilidad con fecha y severidad |

Las cuatro se consultaron el 2026-10-02 solo para verificar su esquema (§0.1). Antes de
usarlas para el análisis se revisan sus términos de uso y se respeta el límite de
peticiones que declaren.

---

*Fractal Core Research · Tlaxcala, México · 2026-10-02*
