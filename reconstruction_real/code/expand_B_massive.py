"""Expansión masiva del dominio B con TODOS los pares regionales viables."""
import pandas as pd, numpy as np
from scipy import stats
from itertools import combinations

df = pd.read_csv('data/owid-maddison.csv')

def calc(hub, nodo, ymin=1900, ymax=2018):
    h = df[(df['Entity']==hub)&(df['Year']>=ymin)&(df['Year']<=ymax)][['Year','GDP per capita']].dropna()
    n = df[(df['Entity']==nodo)&(df['Year']>=ymin)&(df['Year']<=ymax)][['Year','GDP per capita']].dropna()
    m = pd.merge(h,n,on='Year')
    if len(m)<10: return None
    m=m.sort_values('Year')
    R = m['GDP per capita_x'].values/m['GDP per capita_y'].values
    t = np.arange(1,len(m)+1)
    lt,lR = np.log(t),np.log(R)
    if np.std(lt)==0: return None
    sl,ic,rv,pv,se = stats.linregress(lt,lR)
    res=lR-(ic+sl*lt)
    dw=np.sum(np.diff(res)**2)/np.sum(res**2) if len(res)>1 else np.nan
    return dict(b=round(sl,4),r2=round(rv**2,4),r_pearson=round(rv,4),p=round(pv,4),
                se_b=round(se,4),ci_lo=round(sl-1.96*se,4),ci_hi=round(sl+1.96*se,4),
                dw=round(dw,3),n=len(m),year_min=int(m['Year'].min()),year_max=int(m['Year'].max()))

# Regiones ampliadas con TODOS los países disponibles
REGIONES = {
    'Europa_Occidental':['United Kingdom','France','Germany','Netherlands','Belgium','Switzerland','Austria','Italy','Spain','Portugal','Ireland','Luxembourg'],
    'Europa_Nordica':['Sweden','Norway','Denmark','Finland','Iceland'],
    'Europa_Este':['Poland','Czechia','Hungary','Romania','Bulgaria','Russia','Ukraine','Slovakia','Croatia','Serbia','Slovenia'],
    'Europa_Sur':['Italy','Spain','Portugal','Greece','Turkey','Cyprus','Malta'],
    'Norteamerica':['United States','Canada','Mexico'],
    'Centroamerica':['Mexico','Guatemala','Honduras','Costa Rica','Panama','Cuba','El Salvador','Nicaragua','Dominican Republic'],
    'Sudamerica':['Brazil','Argentina','Chile','Uruguay','Paraguay','Bolivia','Peru','Colombia','Venezuela','Ecuador'],
    'Asia_Oriental':['Japan','China','South Korea','Taiwan','Mongolia'],
    'Asia_Sudeste':['Singapore','Malaysia','Thailand','Indonesia','Philippines','Vietnam','Cambodia','Myanmar','Laos'],
    'Asia_Sur':['India','Pakistan','Bangladesh','Sri Lanka','Nepal','Afghanistan'],
    'Medio_Oriente':['Israel','Turkey','Iran','Iraq','Saudi Arabia','Egypt','Jordan','Lebanon','Syria','Yemen'],
    'Africa_Norte':['Egypt','Morocco','Algeria','Tunisia','Sudan','Libya'],
    'Africa_Sub':['South Africa','Nigeria','Kenya','Ghana','Zimbabwe','Zambia','Tanzania','Uganda','Mozambique','Botswana','Ethiopia','Cameroon','Ivory Coast','Senegal','Angola'],
    'Oceania':['Australia','New Zealand','Fiji','Papua New Guinea'],
}

pib_avg = df.dropna(subset=['GDP per capita']).groupby('Entity')['GDP per capita'].mean()

resultados=[]
for region, paises in REGIONES.items():
    disp=[p for p in paises if p in pib_avg.index]
    for a,b in combinations(disp,2):
        hub,nodo = (a,b) if pib_avg[a]>=pib_avg[b] else (b,a)
        r=calc(hub,nodo)
        if r:
            r.update(hub=hub,nodo=nodo,dominio='B',region=region,trigger='gradual',
                     descripcion=f"{hub}→{nodo} {r['year_min']}-{r['year_max']}",
                     significativo=r['p']<0.05)
            resultados.append(r)

dfB=pd.DataFrame(resultados).drop_duplicates(subset=['hub','nodo']).reset_index(drop=True)
dfB['id']=[f"B{i+1:03d}" for i in range(len(dfB))]
cols=['id','descripcion','dominio','region','hub','nodo','trigger','b','r2','r_pearson','p','se_b','ci_lo','ci_hi','dw','n','year_min','year_max','significativo']
dfB[cols].to_csv('data/dominio_B_real.csv',index=False)
print(f"DOMINIO B EXPANDIDO: {len(dfB)} casos")
print(f"  Significativos: {dfB['significativo'].sum()} ({100*dfB['significativo'].mean():.0f}%)")
print(f"  b medio: {dfB['b'].mean():+.3f}, R²<0: {(dfB['r2']<0).sum()}")
