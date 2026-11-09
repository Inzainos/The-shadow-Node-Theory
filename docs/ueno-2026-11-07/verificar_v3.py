#!/usr/bin/env python3
"""Verificacion v3 del modelo Ueno (stdlib, sin dependencias externas).

Lee ~/workspace/snt-taxonomia/tabla-maestra-ueno-mef.csv y recomputa:
  - R(t) = ueno_total_usd_equiv / (total_sistema_usd_equiv - ueno_total_usd_equiv)
    para las 31 filas con R, comparada con la columna R_t del CSV, y tambien
    desde los componentes crudos (USD*6000 + Gs).
  - b (c) meseta dic 2025-sep 2026, n=10, origen dic 2024 (calendario).
  - b (e) serie completa feb 2024-sep 2026, n=31, origen feb 2024 (calendario).
  - b (c') meseta local, origen dic 2025: calendario vs secuencial, para la
    ventana v3 (n=10, con mar 2026) y, como control de metodo, para la
    ventana v2 (n=9, sin mar 2026) y la ventana v1 (n=8, sin ene ni mar 2026),
    cuyos valores de auditoria son: v1 secuencial -0.0120 / calendario
    -0.0046; v2 secuencial +0.0086 / calendario +0.0104.

Convencion de t (v2 Apendice A, modelo-ueno-resultados-v2.md:290-299):
t es el mes calendario (meses desde el origen, con huecos cuando falta el
PDF). La numeracion secuencial 1..n es la que v1/v2 aplicaron de hecho en
(c'), contra lo declarado: hallazgo H-1 de la auditoria.
"""
import csv
import math
import os

CSV = os.path.expanduser("~/workspace/snt-taxonomia/tabla-maestra-ueno-mef.csv")
FX = 6000


def month_index(fecha):
    y, m = int(fecha[:4]), int(fecha[5:7])
    return y * 12 + m


def t_from(fecha, origin_fecha):
    """Meses calendario desde el origen, t=1 en el mes de origen."""
    return month_index(fecha) - month_index(origin_fecha) + 1


def ols(xs, ys):
    """OLS y = log a + b * log x. Devuelve (b, a, R2, n)."""
    n = len(xs)
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    mx = sum(lx) / n
    my = sum(ly) / n
    sxx = sum((v - mx) ** 2 for v in lx)
    sxy = sum((lx[i] - mx) * (ly[i] - my) for i in range(n))
    b = sxy / sxx
    loga = my - b * mx
    a = math.exp(loga)
    ss_tot = sum((v - my) ** 2 for v in ly)
    ss_res = sum((ly[i] - (loga + b * lx[i])) ** 2 for i in range(n))
    r2 = 1.0 - ss_res / ss_tot
    return b, a, r2, n


def fit(rows, origin):
    """rows: lista de (fecha, R). t calendario desde origin."""
    xs = [t_from(f, origin) for f, _ in rows]
    ys = [r for _, r in rows]
    return ols(xs, ys), xs


def fit_seq(rows):
    xs = list(range(1, len(rows) + 1))
    ys = [r for _, r in rows]
    return ols(xs, ys), xs


def main():
    with open(CSV, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        data = list(reader)

    print(f"filas totales (sin cabecera): {len(data)}")
    print(f"filas marcadas 'MEF PDF': {sum(1 for r in data if r['fuente'] == 'MEF PDF')}")
    print(f"filas marcadas 'sin PDF': {sum(1 for r in data if r['fuente'] == 'sin PDF')}")

    # --- R(t) fila por fila ---
    rows_r = []  # (fecha, R_csv, R_recalc_equiv, R_recalc_crudos)
    max_diff = 0.0
    max_diff_crudo = 0.0
    for r in data:
        if not r["R_t"]:
            continue
        u_eq = float(r["ueno_total_usd_equiv"])
        t_eq = float(r["total_sistema_usd_equiv"])
        r_equiv = u_eq / (t_eq - u_eq)
        r_csv = float(r["R_t"])
        # componentes crudos: USD*6000 + Gs (FX 6000 por fila, segun tabla)
        u_crudo = float(r["ueno_usd_mef"]) * FX + float(r["ueno_gs_mef"])
        t_crudo = float(r["total_sistema_usd_mef"]) * FX + float(r["total_sistema_gs_mef"])
        r_crudo = u_crudo / (t_crudo - u_crudo)
        rows_r.append((r["fecha"], r_csv, r_equiv, r_crudo))
        max_diff = max(max_diff, abs(r_equiv - r_csv))
        max_diff_crudo = max(max_diff_crudo, abs(r_crudo - r_csv))

    print(f"\nmeses con R_t en CSV: {len(rows_r)}")
    print(f"diferencia maxima R_equiv vs R_csv: {max_diff:.6f}")
    print(f"diferencia maxima R_crudos vs R_csv: {max_diff_crudo:.6f}")
    for fecha, r_csv, r_eq, r_cr in rows_r:
        flag = "" if abs(r_eq - r_csv) < 0.00005 and abs(r_cr - r_csv) < 0.00005 else "  <-- DIFERENCIA"
        print(f"  {fecha}  csv={r_csv:.4f}  equiv={r_eq:.6f}  crudos={r_cr:.6f}{flag}")

    serie = [(f, rc) for f, rc, _, _ in rows_r]
    d = dict(serie)
    print(f"\nR mar 2026: {d['2026-03']:.4f} (csv {d['2026-03']:.4f})")
    print(f"R nov 2025: {d['2025-11']:.4f}  -> mar 2026 supera nov 2025: {d['2026-03'] > d['2025-11']}")
    print(f"R dic 2024 (cruce Roche-R): {d['2024-12']:.4f}; R nov 2024: {d['2024-11']:.4f}")

    # --- Meseta dic 2025 - sep 2026 ---
    meseta = [(f, r) for f, r in serie if "2025-12" <= f <= "2026-09"]
    print(f"\nmeseta dic25-sep26: n={len(meseta)} meses: {[f for f, _ in meseta]}")
    print(f"rango meseta: min={min(r for _, r in meseta):.4f} max={max(r for _, r in meseta):.4f}")

    (b_c, a_c, r2_c, n_c), xs_c = fit(meseta, "2024-12")
    print(f"(c) meseta origen dic24 calendario: b={b_c:.4f} a={a_c:.4f} R2={r2_c:.4f} n={n_c} t={xs_c}")
    (b_c_nov, a_c_nov, r2_c_nov, _), _ = fit(meseta, "2024-11")
    print(f"(c) meseta origen nov24 calendario (sensibilidad): b={b_c_nov:.4f} a={a_c_nov:.4f} R2={r2_c_nov:.4f}")

    # --- (c') local, calendario vs secuencial ---
    (b_cp_cal, a_cp_cal, r2_cp_cal, _), xs_cp = fit(meseta, "2025-12")
    (b_cp_seq, a_cp_seq, r2_cp_seq, _), xs_seq = fit_seq(meseta)
    print(f"(c') v3 meseta origen local dic25 CALENDARIO: b={b_cp_cal:.4f} a={a_cp_cal:.4f} R2={r2_cp_cal:.4f} n={len(meseta)} t={xs_cp}")
    print(f"(c') v3 meseta origen local dic25 SECUENCIAL: b={b_cp_seq:.4f} a={a_cp_seq:.4f} R2={r2_cp_seq:.4f} n={len(meseta)} t={xs_seq}")
    print(f"(c') v3 calendario == secuencial: {xs_cp == xs_seq} (sin huecos en dic25-sep26 con mar 2026 presente)")

    # Controles de metodo: ventanas v2 (n=9, sin mar 2026) y v1 (n=8, sin ene/mar 2026)
    meseta_v2 = [(f, r) for f, r in meseta if f != "2026-03"]
    (b2_cal, _, r2_2cal, _), _ = fit(meseta_v2, "2025-12")
    (b2_seq, _, r2_2seq, _), _ = fit_seq(meseta_v2)
    print(f"(c') CONTROL v2 n=9 calendario: b={b2_cal:.4f} R2={r2_2cal:.4f} (auditoria: +0.0104 / R2 0.0226)")
    print(f"(c') CONTROL v2 n=9 secuencial: b={b2_seq:.4f} R2={r2_2seq:.4f} (auditoria: +0.0086 / R2 0.0132; valor publicado en v2)")
    meseta_v1 = [(f, r) for f, r in meseta if f not in ("2026-01", "2026-03")]
    (b1_cal, _, r2_1cal, _), _ = fit(meseta_v1, "2025-12")
    (b1_seq, _, r2_1seq, _), _ = fit_seq(meseta_v1)
    print(f"(c') CONTROL v1 n=8 calendario: b={b1_cal:.4f} R2={r2_1cal:.4f} (auditoria: -0.0046 / R2 0.005)")
    print(f"(c') CONTROL v1 n=8 secuencial: b={b1_seq:.4f} R2={r2_1seq:.4f} (auditoria: -0.0120 / R2 0.0296; valor publicado en v1)")

    # --- Serie completa ---
    (b_e, a_e, r2_e, n_e), xs_e = fit(serie, "2024-02")
    print(f"\n(e) completa origen feb24 calendario: b={b_e:.4f} a={a_e:.4f} R2={r2_e:.4f} n={n_e} t_max={max(xs_e)}")
    print(f"(e) t calendario serie completa: {xs_e}")

    # --- Discrepancia mar 2026 (auditoria §2.8) ---
    # El componente USD "235M" es el USD de Ueno de mar 2026, exacto en el
    # CSV: 235,381,762 USD (no 235,000,000 redondeados). A FX 6.000 son
    # Gs 1,412,290,572,000, que es la cifra de la auditoria (+Gs 1.412.290M).
    tesoro_gs = 3721013013754
    balance_gs = 3163975000000
    usd_mar26 = None
    for r in data:
        if r["fecha"] == "2026-03":
            usd_mar26 = float(r["ueno_usd_mef"])
    print(f"\ndiscrepancia mar 2026 solo Gs: {tesoro_gs - balance_gs:,} Gs")
    print(f"USD mar 2026 exacto (CSV fila 2026-03): {usd_mar26:,.0f} USD")
    print(f"USD mar 2026 sin conciliar a FX 6000: {usd_mar26 * 6000:,.0f} Gs")
    print(f"discrepancia total en equivalentes (Gs + USD*6000): {(tesoro_gs - balance_gs) + usd_mar26 * 6000:,.0f} Gs")

    # --- Resumen para v3 ---
    print("\n=== RESUMEN v3 ===")
    print(f"R_mar2026={d['2026-03']:.4f}")
    print(f"b_meseta_c_origen_dic24={b_c:.4f} R2={r2_c:.4f} n={n_c}")
    print(f"b_meseta_cprima_calendario={b_cp_cal:.4f} R2={r2_cp_cal:.4f} n={len(meseta)}")
    print(f"b_meseta_cprima_secuencial={b_cp_seq:.4f} R2={r2_cp_seq:.4f} n={len(meseta)}")
    print(f"b_completa_e={b_e:.4f} a={a_e:.4f} R2={r2_e:.4f} n={n_e}")
    print(f"max_diff_R={max_diff:.6f}")


if __name__ == "__main__":
    main()
