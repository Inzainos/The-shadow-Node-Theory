#!/usr/bin/env python3
"""
Friccion -> Delta: extension del test de la cohorte 2008 (n=6) a los 18 casos ACO.

El test original (`friction_operational.py`) asigno a los 6 casos financieros de
2008 un ordinal de friccion = "grado documentado de pre-arreglo regulatorio del
canal de resolucion" (1 = desordenado, sin canal; 6 = totalmente pre-arreglado)
y midio Spearman rho(F, Delta) = -1.000 (n=6, p ~ 0.11 dos colas — nunca
significativo).

Aqui se extiende el ordinal a los otros 12 casos ACO (H, I, T) usando el mismo
criterio: el canal de resolucion DOCUMENTADO de cada caso. Los canales son
hechos verificables (citados abajo); la asignacion del ordinal es post-hoc —
el autor debe validarla antes de tratarla como pre-registrada. El Delta de cada
caso es la `b` del corpus ACO v29 (exponente de absorcion, series committeadas).

Asignaciones nuevas (canal documentado):
  H01 URSS 1991        1  disolucion sin canal de resolucion pre-arreglado
  H02 Roma 476         1  abdicacion/saqueo, sin canal
  H03 Azteca 1521      1  conquista militar
  H04 Cartago 146 AC   1  destruccion militar
  I01 PanAm 1991       2  Chapter 11 con venta de activos a multiples compradores,
                          sin resultado unico pre-arreglado
  I02 Polaroid 2001    3  Chapter 11 con comprador unico (OEP) via tribunal
  I03 Kodak 2012       4  Chapter 11 (363): patentes a consorcio en subasta
                          supervisada por tribunal
  I04 Blockbuster 2010 4  subasta 363 con comprador unico (Dish)
  T01 Nokia 2013       6  venta privada totalmente negociada (acuerdo bilateral
                          anunciado 2013, cerrado 2015)
  T02 Compaq 2002      6  fusion amigable negociada
  T03 Sun 2010         6  adquisicion negociada
  T04 MySpace 2011     1  migracion de usuarios, sin canal formal de resolucion

Uso:
    python reconstruction_real/code/friction_aco_18.py
"""

import sys

import numpy as np
from scipy import stats

# (id, friccion, canal documentado, Delta = b del corpus ACO v29)
# Fricciones F01-F06: las del test original (friction_operational.py).
CASOS = [
    ("F01_Lehman_2008", 1, "Chapter 11 desordenado, sin resolucion", 0.2460),
    ("F02_BearStearns_2008", 5, "Fed-brokered (Maiden Lane)", 0.0433),
    ("F03_WashingtonMutual_2008", 6, "Receivership FDIC (P&A)", 0.0089),
    ("F04_Wachovia_2008", 3, "FDIC-assisted open-bank", 0.1527),
    ("F05_MerrillLynch_2008", 2, "Fusion privada presionada", 0.2165),
    ("F06_Chrysler_2009", 4, "Gestion estatal (TARP / 363)", 0.1376),
    ("H01_URSS_1991", 1, "Disolucion sin canal pre-arreglado", 0.3487),
    ("H02_Roma_476", 1, "Abdicacion/saqueo, sin canal", 0.4529),
    ("H03_Azteca_1521", 1, "Conquista militar", 0.6926),
    ("H04_Cartago_146AC", 1, "Destruccion militar", 0.3357),
    ("I01_PanAm_1991", 2, "Ch.11, activos a multiples compradores", 0.3624),
    ("I02_Polaroid_2001", 3, "Ch.11, comprador unico via tribunal", 0.4123),
    ("I03_Kodak_2012", 4, "Ch.11 363, patentes a consorcio en subasta", 1.2438),
    ("I04_Blockbuster_2010", 4, "Subasta 363, comprador unico (Dish)", 1.8059),
    ("T01_Nokia_2013", 6, "Venta privada negociada (Microsoft)", 1.8136),
    ("T02_Compaq_2002", 6, "Fusion amigable negociada (HP)", 0.1525),
    ("T03_SunMicrosystems_2010", 6, "Adquisicion negociada (Oracle)", 0.2075),
    ("T04_MySpace_2011", 1, "Migracion de usuarios, sin canal formal", 2.1947),
]


def spearman_perm(F, D, n_perm=100000, seed=20261018):
    """Spearman observado + p por permutacion (dos colas)."""
    rho_obs, _ = stats.spearmanr(F, D)
    rng = np.random.default_rng(seed)
    cont = 0
    D = np.asarray(D, float)
    for _ in range(n_perm):
        Dp = rng.permutation(D)
        r, _ = stats.spearmanr(F, Dp)
        if abs(r) >= abs(rho_obs) - 1e-12:
            cont += 1
    return rho_obs, cont / n_perm


def main():
    print("Friccion (pre-arreglo del canal) vs Delta — extension ACO n=18")
    print("Asignacion post-hoc de los 12 casos nuevos; el autor debe validarla.")
    print("=" * 74)
    print(f"{'caso':<26}{'F':>3}  {'Delta':>7}  canal documentado")
    for cid, f, canal, d in CASOS:
        print(f"{cid:<26}{f:>3}  {d:>7.4f}  {canal}")

    F = np.array([c[1] for c in CASOS], float)
    D = np.array([c[3] for c in CASOS], float)

    rho18, p18 = spearman_perm(F, D)
    print("\n--- Extension n=18 (todos los casos ACO) ---")
    print(f"Spearman rho(F, Delta) = {rho18:+.3f} | p permutacion (dos colas, "
          f"100k) = {p18:.4f}")

    F6 = F[:6]
    D6 = D[:6]
    rho6, _ = stats.spearmanr(F6, D6)
    print("\n--- Original n=6 (cohorte 2008, referencia) ---")
    print(f"Spearman rho(F, Delta) = {rho6:+.3f} (p ~ 0.11 dos colas, n=6)")

    # Descomposicion: cuanto aporta cada caso nuevo a la direccion original
    print("\n--- Descomposicion por dominio ---")
    for dom, mask in (("F (2008)", np.array([c[0].startswith("F") for c in CASOS])),
                      ("H (historico)", np.array([c[0].startswith("H") for c in CASOS])),
                      ("I (industrial)", np.array([c[0].startswith("I") for c in CASOS])),
                      ("T (tecnologico)", np.array([c[0].startswith("T") for c in CASOS]))):
        if mask.sum() >= 3:
            r, _ = stats.spearmanr(F[mask], D[mask])
            print(f"  {dom}: rho = {r:+.3f} (n={int(mask.sum())})")

    print("\n--- Lectura ---")
    print("La direccion original (mas friccion -> Delta menor, absorcion mas")
    print("front-loaded) se sostiene o no segun lo que diga el rho de n=18.")
    print("Casos notables a priori: Nokia (F=6, Delta=1.81) y Blockbuster")
    print("(F=4, Delta=1.81) van CONTRA la direccion; MySpace (F=1, Delta=2.19)")
    print("y los H (F=1, Delta 0.34-0.69) van a favor. El resultado es el que")
    print("es: post-hoc, n pequeno, y a validar por el autor antes de citarlo.")


if __name__ == "__main__":
    sys.exit(main())
