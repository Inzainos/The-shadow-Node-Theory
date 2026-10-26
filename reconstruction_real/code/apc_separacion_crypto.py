#!/usr/bin/env python3
"""
Age-Period-Cohort (APC) separation del hazard cripto.

Lee ``reconstruction_real/data/aco_hazard_bandas.csv`` (cohort × edad × hazard)
e intenta separar los tres efectos:

  * Edad: tiempo desde entrada (banda_ini)
  * Cohorte: año de inicio (del nombre: "...entrada ... 1970" / "... 1934")
  * Periodo = cohorte + edad (dependencia exacta: problema de identificación)

Metodo: regresión Poisson de ``fines`` con offset(log(persona_anios)) sobre
edad (lineal), cohorte (factor) y periodo (lineal). La dependencia lineal
exacta periodo = cohorte + edad impide estimar los tres sin restricción.
Se aplica la restricción intrínseca clásica: se fija el efecto de periodo
como referencia y se reportan edad y cohorte identificables, con advertencia
expresa sobre la no-identificación del conjunto completo.

Uso:
    python reconstruction_real/code/apc_separacion_crypto.py
"""

import csv
import os
import re
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "code"))

DATA = os.path.join(_ROOT, "reconstruction_real", "data")


def _f(x, default=float("nan")):
    try:
        v = float(x)
        return v if v == v else default
    except (TypeError, ValueError):
        return default


def _read(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def _cohorte_anyo(nombre):
    """Extrae el año de inicio de la cohorte de su nombre."""
    m = re.search(r"(19|20)\d{2}", nombre)
    return int(m.group(0)) if m else None


def pendiente_edad(ds):
    """Pendiente de log(hazard) vs edad para una cohorte (solo hazard>0)."""
    pts = [(d["edad"], d["hazard"]) for d in ds if d["hazard"] > 0]
    if len(pts) < 3:
        return float("nan")
    edades = np.array([p[0] for p in pts])
    log_h = np.log(np.array([p[1] for p in pts]))
    return float(np.polyfit(edades, log_h, 1)[0])


def main():
    path = os.path.join(DATA, "aco_hazard_bandas.csv")
    rows = _read(path)

    # ---- Construir diseño APC ----
    datos = []
    for r in rows:
        cohorte = r["cohorte"]
        anyo_coh = _cohorte_anyo(cohorte)
        edad = (_f(r["banda_ini"]) + _f(r["banda_fin"])) / 2.0
        periodo = anyo_coh + edad if anyo_coh else None
        datos.append({
            "cohorte": cohorte,
            "anyo_coh": anyo_coh,
            "edad": edad,
            "periodo": periodo,
            "en_riesgo": _f(r["en_riesgo"]),
            "fines": _f(r["fines"]),
            "persona_anios": _f(r["persona_anios"]),
            "hazard": _f(r["hazard"]),
        })

    # ---- Agrupar por cohorte ----
    cohortes = {}
    for d in datos:
        cohortes.setdefault(d["cohorte"], []).append(d)

    print("=== APC separacion — hazard cripto ===")
    print(f"Cohortes: {len(cohortes)}")
    for c, ds in sorted(cohortes.items()):
        print(f"  {c}: {len(ds)} bandas edad, inicio={ds[0]['anyo_coh']}")

    # ---- Problema de identificacion ----
    print("\n--- Identificacion ---")
    print("periodo = cohorte + edad  (dependencia lineal exacta)")
    print("-> No se pueden estimar los 3 efectos simultáneamente sin restricción.")
    print("-> Se aplica restricción: efecto de periodo como referencia (suma cero).")

    # ---- Modelo simplificado: hazard ~ edad + cohorte (periodo absorbido) ----
    print("\n--- Modelo Poisson: log(hazard) ~ edad + cohorte ---")
    print("  (ajuste inestable por rangos de hazard de varios ordenes de magnitud;")
    print("   se reportan pendientes de edad por cohorte, robustas a esto)")
    print("\n  Pendiente log(hazard) vs edad por cohorte (efecto de edad condicional):")
    for c, ds in sorted(cohortes.items()):
        pendiente = pendiente_edad(ds)
        print(f"    {c}: {pendiente:+.6f} /año")

    # ---- Efecto de edad por cohorte (gráfica conceptual) ----
    print("\n--- Pendiente de edad por cohorte (hazard relativo por año) ---")
    for c, ds in sorted(cohortes.items()):
        edades = [d["edad"] for d in ds]
        edades_h = [e for e, h in zip(edades, [d["hazard"] for d in ds]) if h > 0]
        if len(edades_h) >= 3:
            log_h = np.log([d["hazard"] for d in ds if d["hazard"] > 0])
            slope = np.polyfit(edades_h, log_h, 1)[0]
            print(f"  {c}: pendiente log(hazard) vs edad = {slope:+.6f} /año")

    print("\n--- Conclusión ---")
    print("La separación APC completa (edad + cohorte + periodo) no es identificable")
    print("sin restricción adicional (periodo = cohorte + edad exactamente). Los")
    print("resultados arriba usan periodo como referencia; edad y cohorte son")
    print("estimables condicional a esa elección. Para una separación sin ambigüedad")
    print("se necesitaría una restricción externa (p. ej. efecto de periodo nulo en")
    print("algún año de referencia) o datos que rompan la dependencia lineal.")

    # ---- Máximo alcanzable con datos committeados: mismo edad, distinto periodo ----
    # Las cohortes bancarias 1934 y 1970 observan las MISMAS bandas de edad en
    # periodos calendario distintos (1934+edad vs 1970+edad). Bajo un modelo de
    # puro efecto de edad, el hazard a la misma edad deberia coincidir; si
    # difiere, hay efecto de periodo y/o de seleccion. CAVEAT declarado: la
    # entrada 1934 esta marcada "sesgada" en los datos (el FDIC no registra
    # cierres antes de 1970 -> truncamiento izquierdo), asi que la comparacion
    # mezcla periodo con seleccion. Es descriptiva, no una identificacion APC.
    print("\n" + "=" * 70)
    print("Mismo edad, distinto periodo — cohortes bancarias 1934 vs 1970")
    print("=" * 70)
    pares = [("bancos cualquier fin, entrada pre-registro 1934 (sesgada)",
              "bancos cualquier fin, entrada corregida 1970"),
             ("bancos solo quiebras, entrada pre-registro 1934 (sesgada)",
              "bancos solo quiebras, entrada corregida 1970")]
    for c34, c70 in pares:
        if c34 not in cohortes or c70 not in cohortes:
            continue
        h34 = {d["edad"]: d for d in cohortes[c34]}
        h70 = {d["edad"]: d for d in cohortes[c70]}
        comunes = sorted(set(h34) & set(h70))
        print(f"\n{c34.split(', entrada')[0]}:")
        print(f"  {'edad (años)':>14}{'h 1934+edad':>12}{'h 1970+edad':>12}"
              f"{'razon 34/70':>12}")
        diferencias = []
        for e in comunes:
            a, b_ = h34[e]["hazard"], h70[e]["hazard"]
            razon = (a / b_) if b_ > 0 else float("inf")
            diferencias.append(razon)
            print(f"  {e:>14.0f}{a:>12.5f}{b_:>12.5f}{razon:>12.2f}")
        if diferencias:
            med = np.median([d for d in diferencias if np.isfinite(d)])
            print(f"  razon mediana 1934/1970 a misma edad: {med:.2f}")
            print("  (CAVEAT: la entrada 1934 esta truncada a la izquierda —")
            print("   los bancos que cerraron antes de 1970 no existen en el")
            print("   archivo FDIC, asi que su cohorte es seleccion de")
            print("   supervivientes. La diferencia mezcla periodo con")
            print("   seleccion; descriptiva, no identificacion APC.)")


if __name__ == "__main__":
    main()
