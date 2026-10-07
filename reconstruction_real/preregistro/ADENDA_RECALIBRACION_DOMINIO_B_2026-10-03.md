# Adenda de recalibración — el valor puntual del Dominio B

**Pre-registro base:** [`PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md`](PREREGISTRO_DOMINIO_B_PUNTUAL_2026-10-02.md)
(commit `05bc9ee`).
**Informe que esta adenda puede modificar:** [`../audits/RESULTADOS_DOMINIO_B_PUNTUAL_2026-10-02.md`](../audits/RESULTADOS_DOMINIO_B_PUNTUAL_2026-10-02.md).
**Escrita y subida ANTES de correr el script de recalibración.** Autorizada por el
autor el 2026-10-03.

---

## 1. Qué reserva cierra esta adenda, y por qué existe

La corrida del 2026-10-03 cerró el valor puntual del Dominio B en **33 de 156
estimables (21.2%)**, porque `ar1_inf` midió **7.1%** de falso positivo y la banda de
admisión pre-registrada es **[2.5%, 7.5%]**.

Ese cierre quedó con tres reservas escritas en la §6.1 del informe. **La primera es la
única que se puede cerrar midiendo**, y es la razón de esta adenda:

> La admisión es marginal. 7.1% está dentro de la banda por **0.4 puntos**. El intervalo
> de Wilson al 95% es **[5.5%, 9.2%]**, que **no está contenido en la banda**: su extremo
> superior la rebasa. Con otra semilla el método podría medir 7.6% y quedar fuera. Para
> cerrar esta reserva habría que recalibrar con N ≫ 2,000 y el pre-registro no lo fijó.

El pre-registro fijó `N_SIM = 2,000`. Con 733 casos en el estrato estimable, el error
Monte Carlo (±1.9 puntos) es **del mismo orden que el ancho de la banda** (5 puntos). La
decisión de admisibilidad está por tanto dominada por ruido de simulación, no por el
método. Eso es lo que esta adenda corrige, y **nada más**.

**Esto no es una hipótesis nueva.** Es la misma cantidad, el mismo estimador, la misma
regla, medidos con menos error. No se cambia ningún otro parámetro.

---

## 2. Qué se corre

| Parámetro | Pre-registro base | Esta adenda | Por qué |
|---|---|---|---|
| `N_SIM`, escenario de tamaño (`b = 0`) | 2,000 | **200,000** | Estrato estimable ≈ 70,000. Semiancho del IC95 ≈ **0.19 puntos**, contra 1.9. El ruido deja de decidir |
| `N_SIM`, escenarios de poder (`b = −0.30`, `b = −0.60`) | 2,000 | **20,000** | El poder no entra en la regla de admisión. Se aprieta para que la lectura "al menos 33" descanse en una cifra firme |
| Métodos | los doce | **los doce** | Para comprobar que ninguno de los otros once entra a la banda con más precisión |
| Estratificación | — | **por el caso real de origen** | La corregida en `68e7ec3`. No se vuelve a la defectuosa |
| Banda de admisión | `[0.025, 0.075]` | **igual, sin cambio** | Cambiarla después de ver un resultado sería acomodar la regla |
| `BOOT_SIM` | 199 | **199, sin cambio** | — |
| Semilla | `20261002` | **`20261003`**, declarada aquí | Estimación **independiente**, no una extensión de la corrida anterior |
| Datos | `data/maddison_mpd2020.csv` | **los mismos** | Sin descargas |

**Script:** `code/dominio_B_recalibracion.py`, con log. Reutiliza por importación los doce
métodos de `dominio_B_valor_puntual.py` sin copiarlos, para que no puedan divergir.
**El script original y sus salidas no se tocan**: la corrida pre-registrada queda como
está publicada, y esta recalibración vive en archivos propios.

### Por qué una semilla nueva y no una extensión

Extender la corrida anterior con la misma semilla daría un estimado que **contiene** al
7.1% como submuestra, y entonces el 7.1% no sería una observación independiente del
resultado. Con semilla nueva, el 7.1% y la cifra de esta adenda son **dos mediciones
independientes de la misma cantidad**, y su concordancia (o su falta) es información.

---

## 3. La regla de decisión, fijada aquí y antes de ver nada

**Qué estimado gobierna.** El de **200,000**. Mide exactamente la misma cantidad que el
de 2,000 con un error diez veces menor, y el único defecto del original era su
precisión. No se elige el más conveniente de los dos después de verlos.

**La regla de admisión no cambia:** un método es admisible si su tasa de falso positivo
**medida** en el estrato estimable cae en `[0.025, 0.075]`.

| Desenlace | Lectura, escrita antes de medir |
|---|---|
| `ar1_inf` dentro de la banda **y** su IC95 contenido en ella | **La reserva 1 se cierra.** El valor puntual **33 de 156 (21.2%)** queda firme, con las reservas 2 (tautología de la cota) y 3 (poder) intactas, que no se cierran midiendo más réplicas |
| `ar1_inf` dentro de la banda **pero** su IC95 todavía la rebasa | La reserva **no se cierra**. El valor puntual se mantiene por la regla, y se reporta que sigue siendo marginal con el error ya reducido al mínimo práctico |
| **`ar1_inf` por encima de 7.5%** | **`ar1_inf` deja de ser admisible.** Como ningún otro método está cerca —el segundo mejor midió 11.3%— el valor puntual **vuelve a NO declararse y se cierra como indecidible**, por la regla del pre-registro base. El 33 regresa a ser la cifra conservadora a citar, y el informe se reescribe otra vez, en esa dirección |
| `ar1_inf` por **debajo** de 2.5% | Tampoco admisible: sería un método conservador de más. Mismo desenlace que el anterior |
| Otro de los once entra a la banda | Se reporta. Si hay **más de uno** admisible, el valor puntual lo produce el de **mayor poder**, por la regla del pre-registro base |

**Se reporta en todos los casos:** las doce tasas con su IC95 de Wilson, el tamaño del
estrato, las dos tablas de poder, y la comparación explícita contra las cifras de la
corrida de 2,000. **Ningún desenlace se deja sin publicar**, y el que obliga a revertir
el cierre se publica igual que el que lo confirma.

---

## 4. Lo que esta adenda NO hace

- **No reestima ninguna `b`** ni toca el corpus.
- **No cambia la partición** 156 estimables / 290 no estimables, que sale de `n_eff < 3`
  y no depende de simulación.
- **No cierra la reserva 2.** El 33 coincide con la cota inferior publicada porque
  `ar1_inf` **es** el estimador de esa cota; eso es por construcción y ninguna cantidad
  de réplicas lo cambia.
- **No cierra la reserva 3.** `ar1_inf` seguirá siendo el menos potente de los doce, así
  que la cifra seguirá leyéndose **"al menos 33 de 156"** aunque la admisión quede firme.
- **No se traslada a ningún otro dominio.** La calibración se hace con la terna
  `(n, ρ, σ)` **de este dominio**; otro dominio necesita la suya, por Axioma 0.1
  ([`../../papers/marco_teorico.md:110`](../../papers/marco_teorico.md)).

---

*Fractal Core Research · Tlaxcala, México · 2026-10-03*
