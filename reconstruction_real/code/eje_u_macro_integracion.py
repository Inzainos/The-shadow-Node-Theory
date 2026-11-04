#!/usr/bin/env python3
"""
Integración indicadores macro con casos crypto para eje u.
Genera un índice macro global anual promedio y lo une a series crypto.
"""
import pandas as pd
import hashlib
from pathlib import Path

BASE = Path('/home/deamon/The-shadow-Node-Theory')
MACRO_DIR = BASE / 'data' / 'cripto' / 'macro'
BINANCE_CSV = BASE / 'data' / 'binance_cierres_diarios.csv.gz'
CASOS_CSV = BASE / 'data' / 'cripto' / 'casos_binance.csv'
OUT_DIR = BASE / 'reconstruction_real' / 'data'

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def build_macro_index():
    # promedios globales por año desde IMF y World Bank
    imf = pd.read_csv(MACRO_DIR / 'imf_indicators.csv')
    wb = pd.read_csv(MACRO_DIR / 'worldbank_indicators.csv')
    imf_agg = imf.groupby('year').agg({
        'gdp_growth_pct':'mean',
        'inflation_avg_pct':'mean',
        'unemployment_pct':'mean',
        'current_account_pct_gdp':'mean'
    }).reset_index()
    wb_agg = wb.groupby('year').agg({
        'gdp_growth_pct':'mean',
        'inflation_cpi_pct':'mean',
        'unemployment_pct':'mean',
        'gdp_per_capita_usd':'mean'
    }).reset_index()
    macro = pd.merge(imf_agg, wb_agg, on='year', suffixes=('_imf','_wb'), how='outer')
    macro['macro_index'] = (
        macro['gdp_growth_pct_imf'].fillna(0) -
        macro['inflation_avg_pct'].fillna(0) -
        macro['unemployment_pct_imf'].fillna(0)
    )
    return macro[['year','macro_index']]

def load_crypto(pairs):
    df = pd.read_csv(BINANCE_CSV, compression='gzip')
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['year'] = df['fecha'].dt.year
    results=[]
    for pair in pairs:
        sub = df[df['par']==pair].copy()
        if sub.empty:
            continue
        # serie anual de close
        annual = sub.groupby('year')['close'].last()
        macro = build_macro_index()
        merged = pd.merge(annual, macro, on='year', how='left')
        # correlación simple
        if len(merged)>=3:
            corr = merged['close'].corr(merged['macro_index'])
        else:
            corr = float('nan')
        results.append({'coin_pair':pair,'n_years':len(merged),'corr_macro_close':corr})
    return pd.DataFrame(results)

def main():
    casos = pd.read_csv(CASOS_CSV)
    pairs = casos['coin_pair'].tolist()
    out = load_crypto(pairs)
    out_path = OUT_DIR / 'eje_u_crypto_macro_corr.csv'
    out.to_csv(out_path, index=False)
    print(f'Escrito {out_path}')
    print(out.head(10))

if __name__=='__main__':
    main()
