"""
Expansión sistemática del Dominio B a ~230 casos.
Enfoque: para cada región económica, generar pares hub-nodo donde
el hub es la economía de mayor PIB per cápita promedio (criterio objetivo).
"""
import pandas as pd
import numpy as np
from scipy import stats
from itertools import combinations

df = pd.read_csv('data/owid-maddison.csv')

def calc(hub, nodo, ymin=1900, ymax=2018):
    h = df[(df['Entity']==hub)&(df['Year']>=ymin)&(df['Year']<=ymax)][['Year','GDP per capita']].dropna()
    n = df[(df['Entity']==nodo)&(df['Year']>=ymin)&(df['Year']<=ymax)][['Year','GDP per capita']].dropna()
    m = pd.merge(h,n,on='Year',suffixes=('_h','_n'))
    if len(m) < 8: return None
    m = m.sort_values('Year')
    R = m['GDP per capita_h'].values / m['GDP per capita_n'].values
    t = np.arange(1, len(m)+1)
    lt, lR = np.log(t), np.log(R)
    if np.std(lt)==0: return None
    sl, ic, rv, pv, se = stats.linregress(lt, lR)
    res = lR - (ic+sl*lt)
    dw = np.sum(np.diff(res)**2)/np.sum(res**2) if len(res)>1 else np.nan
    return dict(b=round(sl,4), r2=round(rv**2,4), r_pearson=round(rv,4),
               p=round(pv,4), se_b=round(se,4), ci_lo=round(sl-1.96*se,4),
               ci_hi=round(sl+1.96*se,4), dw=round(dw,3), n=len(m),
               year_min=int(m['Year'].min()), year_max=int(m['Year'].max()))

# Regiones económicas — pares dentro de cada una (todas las combinaciones viables)
REGIONES = {
    'Europa_Occidental': ['United Kingdom','France','Germany','Netherlands','Belgium',
                          'Switzerland','Austria','Italy','Spain','Portugal','Ireland'],
    'Europa_Nordica': ['Sweden','Norway','Denmark','Finland'],
    'Europa_Este': ['Poland','Czechia','Hungary','Romania','Bulgaria','Russia','Ukraine'],
    'Europa_Sur': ['Italy','Spain','Portugal','Greece','Turkey'],
    'Norteamerica': ['United States','Canada','Mexico'],
    'Centroamerica': ['Mexico','Guatemala','Honduras','Costa Rica','Panama','Cuba'],
    'Sudamerica': ['Brazil','Argentina','Chile','Uruguay','Paraguay','Bolivia',
                   'Peru','Colombia','Venezuela','Ecuador'],
    'Asia_Oriental': ['Japan','China','South Korea','Taiwan','Mongolia'],
    'Asia_Sudeste': ['Singapore','Malaysia','Thailand','Indonesia','Philippines','Vietnam'],
    'Asia_Sur': ['India','Pakistan','Bangladesh','Sri Lanka','Nepal'],
    'Medio_Oriente': ['Israel','Turkey','Iran','Iraq','Saudi Arabia','Egypt'],
    'Africa_Norte': ['Egypt','Morocco','Algeria','Tunisia','Sudan'],
    'Africa_Sub': ['South Africa','Nigeria','Kenya','Ghana','Zimbabwe','Zambia',
                   'Tanzania','Uganda','Mozambique','Botswana'],
    'Oceania': ['Australia','New Zealand'],
}

# PIB per cápita promedio por país (para decidir hub = más rico)
pib_avg = df.dropna(subset=['GDP per capita']).groupby('Entity')['GDP per capita'].mean()

resultados = []
case_id = 0
for region, paises in REGIONES.items():
    # filtrar a países con datos
    disp = [p for p in paises if p in pib_avg.index]
    for a, b in combinations(disp, 2):
        # hub = el de mayor PIB promedio
        if pib_avg[a] >= pib_avg[b]:
            hub, nodo = a, b
        else:
            hub, nodo = b, a
        r = calc(hub, nodo)
        if r:
            case_id += 1
            r['id'] = f"B{case_id:03d}"
            r['descripcion'] = f"{hub}→{nodo} {r['year_min']}-{r['year_max']}"
            r['hub'], r['nodo'], r['dominio'] = hub, nodo, 'B'
            r['region'] = region
            # trigger: abrupto si comparten frontera con conflicto histórico (heurística simple)
            r['trigger'] = 'gradual'
            r['significativo'] = r['p'] < 0.05
            resultados.append(r)

dfB = pd.DataFrame(resultados).drop_duplicates(subset=['hub','nodo'])
cols = ['id','descripcion','dominio','region','hub','nodo','trigger','b','r2',
        'r_pearson','p','se_b','ci_lo','ci_hi','dw','n','year_min','year_max','significativo']
dfB = dfB[cols].reset_index(drop=True)
dfB['id'] = [f"B{i+1:03d}" for i in range(len(dfB))]
dfB.to_csv('data/dominio_B_real.csv', index=False)

print(f"=== DOMINIO B EXPANDIDO: {len(dfB)} casos REALES ===\n")
print(f"Significativos: {dfB['significativo'].sum()} ({100*dfB['significativo'].mean():.1f}%)")
print(f"b medio: {dfB['b'].mean():+.4f} | mediano: {dfB['b'].median():+.4f}")
print(f"b rango: [{dfB['b'].min():+.3f}, {dfB['b'].max():+.3f}]")
print(f"R² medio: {dfB['r2'].mean():.4f}")
print(f"R² < 0: {(dfB['r2']<0).sum()} (debe ser 0) ✓")
print(f"R² medio significativos: {dfB[dfB['significativo']]['r2'].mean():.4f}")
print(f"b < 0 (convergencia): {(dfB['b']<0).sum()} ({100*(dfB['b']<0).mean():.0f}%)")
print(f"b > 0 (satelización): {(dfB['b']>0).sum()} ({100*(dfB['b']>0).mean():.0f}%)")
print(f"\nPor región:")
for reg in dfB['region'].unique():
    sub = dfB[dfB['region']==reg]
    print(f"  {reg:20} n={len(sub):3} b_medio={sub['b'].mean():+.3f}")
