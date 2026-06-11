"""
Reconstrucción del Dominio B (países) para SNT — datos REALES Maddison.
Cada par hub-nodo tiene justificación histórica/económica documentada.
Pipeline: R(t) = GDP_pc_hub / GDP_pc_nodo, OLS log-log, R² real.
"""
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('data/owid-maddison.csv')

def calc_satelizacion(hub, nodo, year_min=1900, year_max=2018, trigger='gradual'):
    h = df[(df['Entity']==hub) & (df['Year']>=year_min) & (df['Year']<=year_max)][['Year','GDP per capita']].dropna()
    n = df[(df['Entity']==nodo) & (df['Year']>=year_min) & (df['Year']<=year_max)][['Year','GDP per capita']].dropna()
    merged = pd.merge(h, n, on='Year', suffixes=('_hub','_nodo'))
    if len(merged) < 5:
        return None
    merged = merged.sort_values('Year')
    merged['R'] = merged['GDP per capita_hub'] / merged['GDP per capita_nodo']
    merged['t'] = merged['Year'] - merged['Year'].min() + 1
    log_t = np.log(merged['t'].values)
    log_R = np.log(merged['R'].values)
    if np.std(log_t) == 0 or len(merged) < 5:
        return None
    slope, intercept, r_value, p_value, se = stats.linregress(log_t, log_R)
    residuals = log_R - (intercept + slope*log_t)
    dw = np.sum(np.diff(residuals)**2) / np.sum(residuals**2) if len(residuals)>1 else np.nan
    return {
        'b': round(slope,4), 'r2': round(r_value**2,4), 'r_pearson': round(r_value,4),
        'p': round(p_value,4), 'se_b': round(se,4),
        'ci_lo': round(slope-1.96*se,4), 'ci_hi': round(slope+1.96*se,4),
        'dw': round(dw,3), 'n': len(merged),
        'year_min': int(merged['Year'].min()), 'year_max': int(merged['Year'].max()),
        'trigger': trigger
    }

# ── PARES HUB-NODO DOCUMENTADOS ──────────────────────────────────────────────
# Criterio: hub = economía dominante regional/histórica; nodo = periferia vinculada
# trigger: abrupto (shock: guerra, independencia, crisis), gradual (convergencia lenta)
PARES = [
    # ── Europa Occidental: núcleo vs periferia ──
    ("United Kingdom","Spain","gradual"), ("United Kingdom","Portugal","gradual"),
    ("United Kingdom","Ireland","abrupto"), ("United Kingdom","Greece","gradual"),
    ("Germany","Poland","abrupto"), ("Germany","Czechia","abrupto"),
    ("Germany","Hungary","gradual"), ("Germany","Austria","gradual"),
    ("France","Italy","gradual"), ("France","Spain","gradual"),
    ("France","Portugal","gradual"), ("France","Morocco","abrupto"),
    ("France","Algeria","abrupto"), ("France","Tunisia","abrupto"),
    ("Netherlands","Belgium","gradual"), ("Netherlands","Indonesia","abrupto"),
    ("Italy","Greece","gradual"), ("Italy","Albania","abrupto"),
    ("Sweden","Finland","gradual"), ("Sweden","Norway","gradual"),
    ("Denmark","Iceland","gradual"), ("Switzerland","Italy","gradual"),
    ("Austria","Hungary","gradual"), ("Austria","Slovenia","gradual"),
    # ── Norteamérica ──
    ("United States","Mexico","gradual"), ("United States","Canada","gradual"),
    ("United States","Cuba","abrupto"), ("United States","Guatemala","gradual"),
    ("United States","Honduras","gradual"), ("United States","Puerto Rico","abrupto"),
    # ── Sudamérica: hubs regionales ──
    ("Brazil","Argentina","gradual"), ("Brazil","Uruguay","gradual"),
    ("Brazil","Paraguay","gradual"), ("Brazil","Bolivia","gradual"),
    ("Argentina","Uruguay","gradual"), ("Argentina","Paraguay","gradual"),
    ("Argentina","Chile","gradual"), ("Chile","Peru","gradual"),
    ("Chile","Bolivia","gradual"), ("Colombia","Ecuador","gradual"),
    ("Colombia","Venezuela","gradual"), ("Peru","Bolivia","gradual"),
    ("Venezuela","Colombia","abrupto"),
    # ── Asia Oriental ──
    ("Japan","South Korea","abrupto"), ("Japan","Taiwan","abrupto"),
    ("Japan","China","gradual"), ("Japan","Thailand","gradual"),
    ("Japan","Philippines","gradual"), ("Japan","Indonesia","gradual"),
    ("China","India","gradual"), ("China","Vietnam","gradual"),
    ("China","Mongolia","gradual"), ("China","Pakistan","gradual"),
    ("South Korea","Vietnam","gradual"), ("South Korea","Philippines","gradual"),
    ("Taiwan","Philippines","gradual"), ("Singapore","Malaysia","abrupto"),
    ("Singapore","Indonesia","gradual"), ("Hong Kong","China","gradual"),
    # ── Asia del Sur ──
    ("India","Pakistan","abrupto"), ("India","Bangladesh","abrupto"),
    ("India","Sri Lanka","gradual"), ("India","Nepal","gradual"),
    # ── Medio Oriente / Norte de África ──
    ("Turkey","Greece","gradual"), ("Turkey","Egypt","gradual"),
    ("Egypt","Sudan","gradual"), ("Israel","Egypt","abrupto"),
    ("Saudi Arabia","Egypt","gradual"), ("Iran","Iraq","abrupto"),
    # ── Europa del Este / ex-URSS ──
    ("Russia","Ukraine","abrupto"), ("Russia","Belarus","gradual"),
    ("Russia","Kazakhstan","gradual"), ("Russia","Georgia","abrupto"),
    ("Poland","Ukraine","gradual"), ("Poland","Lithuania","gradual"),
    ("Czechia","Slovakia","abrupto"), ("Hungary","Romania","gradual"),
    # ── África Subsahariana ──
    ("South Africa","Zimbabwe","abrupto"), ("South Africa","Mozambique","gradual"),
    ("South Africa","Botswana","gradual"), ("South Africa","Zambia","gradual"),
    ("Nigeria","Ghana","gradual"), ("Nigeria","Niger","gradual"),
    ("Kenya","Tanzania","gradual"), ("Kenya","Uganda","gradual"),
    ("Ghana","Burkina Faso","gradual"), ("Ivory Coast","Mali","gradual"),
    # ── Oceanía ──
    ("Australia","New Zealand","gradual"), ("Australia","Papua New Guinea","gradual"),
    ("New Zealand","Fiji","gradual"),
]

# Períodos clave (algunos pares con shock específico usan ventana de evento)
VENTANAS_EVENTO = {
    ("Japan","South Korea"): (1910,2018),    # ocupación 1910 + posguerra
    ("India","Pakistan"): (1947,2018),       # partición
    ("Russia","Ukraine"): (1991,2018),       # post-soviético
    ("Czechia","Slovakia"): (1993,2018),     # disolución
    ("Germany","Poland"): (1945,2018),       # posguerra
    ("United States","Cuba"): (1959,2018),   # revolución
    ("Singapore","Malaysia"): (1965,2018),   # separación
}

resultados = []
for i, (hub, nodo, trig) in enumerate(PARES):
    ymin, ymax = VENTANAS_EVENTO.get((hub,nodo), (1900,2018))
    r = calc_satelizacion(hub, nodo, ymin, ymax, trig)
    if r:
        r['id'] = f"B{i+1:03d}"
        r['descripcion'] = f"{hub}→{nodo} {r['year_min']}-{r['year_max']}"
        r['hub'] = hub
        r['nodo'] = nodo
        r['dominio'] = 'B'
        r['significativo'] = r['p'] < 0.05
        resultados.append(r)

dfB = pd.DataFrame(resultados)
cols = ['id','descripcion','dominio','hub','nodo','trigger','b','r2','r_pearson',
        'p','se_b','ci_lo','ci_hi','dw','n','year_min','year_max','significativo']
dfB = dfB[cols]
dfB.to_csv('data/dominio_B_real.csv', index=False)

print(f"=== DOMINIO B RECONSTRUIDO: {len(dfB)} casos REALES ===\n")
print(f"Significativos (p<0.05): {dfB['significativo'].sum()} ({100*dfB['significativo'].mean():.1f}%)")
print(f"b medio: {dfB['b'].mean():+.4f}")
print(f"b mediano: {dfB['b'].median():+.4f}")
print(f"b rango: [{dfB['b'].min():+.3f}, {dfB['b'].max():+.3f}]")
print(f"R² medio: {dfB['r2'].mean():.4f}  (todos entre 0-1 ✓)")
print(f"R² < 0: {(dfB['r2']<0).sum()} (debe ser 0)")
print(f"b < 0 (convergencia): {(dfB['b']<0).sum()} ({100*(dfB['b']<0).mean():.0f}%)")
print(f"b > 0 (satelización): {(dfB['b']>0).sum()} ({100*(dfB['b']>0).mean():.0f}%)")

# Por trigger
print(f"\nPor tipo de trigger:")
for trig in ['abrupto','gradual']:
    sub = dfB[dfB['trigger']==trig]
    print(f"  {trig}: n={len(sub)}, b_medio={sub['b'].mean():+.3f}")

print(f"\nEjemplos significativos:")
for _, r in dfB[dfB['significativo']].head(12).iterrows():
    print(f"  {r['id']}: {r['descripcion']:38} b={r['b']:+.3f} R²={r['r2']:.3f} p={r['p']:.4f}")
PYEOF
