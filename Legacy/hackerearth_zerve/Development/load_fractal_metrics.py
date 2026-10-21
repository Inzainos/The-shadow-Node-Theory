import pandas as pd
import numpy as np
import logging
import sys
import os

# Crear directorio de logs si no existe (usando ruta relativa)
os.makedirs("docu", exist_ok=True)

# Configuración de logs
log_path = os.path.join("docu", "analisis_fractal_v3_adv.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - DEAMON-X - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_path, encoding='utf-8')
    ]
)

def calcular_vdr(df):
    """Calcula la Velocity of Dimensional Rotation (VDR).
    Distancia funcional entre herramientas distintas en la primera hora.
    """
    logging.info("Calculando Velocity of Dimensional Rotation (VDR)...")
    df = df.sort_values(['person_id', 'timestamp'])
    
    # Filtrar solo eventos con herramientas
    df_tools = df[df['prop_tool_name'].notna()].copy()
    
    # Identificar cambios de herramienta (rotaciones)
    df_tools['prev_tool'] = df_tools.groupby('person_id')['prop_tool_name'].shift(1)
    df_tools['rotacion'] = (df_tools['prop_tool_name'] != df_tools['prev_tool']) & df_tools['prev_tool'].notna()
    
    # Tiempo entre rotaciones
    df_tools['prev_ts'] = df_tools.groupby('person_id')['timestamp'].shift(1)
    df_tools['time_delta'] = (df_tools['timestamp'] - df_tools['prev_ts']).dt.total_seconds()
    
    # VDR = Sum(Rotaciones) / Avg(Time Delta entre rotaciones) en la primera hora
    # Simplificación: Rotaciones por hora de actividad real
    vdr_metrics = df_tools[df_tools['rotacion']].groupby('person_id').agg(
        num_rotaciones=('rotacion', 'sum'),
        avg_rotation_speed=('time_delta', 'mean')
    )
    
    # VDR alto = muchas rotaciones en poco tiempo
    vdr_metrics['VDR'] = vdr_metrics['num_rotaciones'] / (vdr_metrics['avg_rotation_speed'] / 60 + 1)
    return vdr_metrics[['VDR']]

def ejecutar_v3(ruta_archivo):
    logging.info("--- INICIANDO PROTOCOLO FRACTAL V3 (HackerEarth) ---")
    
    logging.info("Cargando matriz masiva para análisis de resonancia...")
    df = pd.read_csv(ruta_archivo)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed', utc=True)

    # 1. Análisis de Entropía Navegada
    # Columnas críticas con alta entropía (Nulls)
    cols_entropia = ['prop_credits_used', 'prop_user_id'] 
    logging.info("\n--- ANALISIS DE ENTROPIA NAVEGADA ---")
    
    # 2. Métricas Base
    user_metrics = df.groupby('person_id').agg(
        total_eventos=('event', 'count'),
        herramientas_unicas=('prop_tool_name', 'nunique'),
        total_creditos=('prop_credits_used', 'sum'),
        coder_agent_events=('prop_tool_name', lambda x: (x == 'Coder Agent').sum()),
        dias_activos=('timestamp', lambda x: x.dt.date.nunique()),
        primera_act=('timestamp', 'min'),
        ultima_act=('timestamp', 'max')
    )
    user_metrics['vida_util_dias'] = (user_metrics['ultima_act'] - user_metrics['primera_act']).dt.days
    user_metrics['pct_coder_agent'] = (user_metrics['coder_agent_events'] / user_metrics['total_eventos']) * 100

    # 3. Integración de VDR
    vdr_data = calcular_vdr(df)
    user_metrics = user_metrics.join(vdr_data, how='left').fillna({'VDR': 0})

    # 4. Cálculo de CSI con Factor de Resonancia (HackerEarth)
    logging.info("Calculando CSI con Factor de Resonancia...")
    def scale(series):
        if series.max() == series.min(): return series * 0
        return (series - series.min()) / (series.max() - series.min())

    s_tools = scale(user_metrics['herramientas_unicas'])
    s_retention = scale(user_metrics['vida_util_dias'])
    s_vdr = scale(user_metrics['VDR'])
    
    base_csi = (s_tools * 0.4 + s_retention * 0.3 + s_vdr * 0.3) * 100
    
    # Factor de Resonancia: 1.5x si Coder Agent > 50% y Créditos > Mediana
    p50_credits = user_metrics['total_creditos'].median()
    user_metrics['resonancia'] = (user_metrics['pct_coder_agent'] > 50) & (user_metrics['total_creditos'] > p50_credits)
    
    user_metrics['CSI_V3'] = base_csi
    user_metrics.loc[user_metrics['resonancia'], 'CSI_V3'] *= 1.5
    user_metrics['CSI_V3'] = user_metrics['CSI_V3'].clip(upper=100).round(2)

    # 5. Comparativa de Entropía (Elite vs Basic)
    # Hipótesis: El Élite tiene mayor % de datos no-nulos en vectores críticos (Usa la brújula)
    elite_ids = user_metrics[user_metrics['CSI_V3'] > 50].index
    basic_ids = user_metrics[user_metrics['CSI_V3'] <= 20].index
    
    df_elite = df[df['person_id'].isin(elite_ids)]
    df_basic = df[df['person_id'].isin(basic_ids)]
    
    logging.info(f"Densidad de Datos (No-Nulos) en Vectores Críticos:")
    for col in cols_entropia:
        d_elite = (df_elite[col].notna().sum() / len(df_elite)) * 100
        d_basic = (df_basic[col].notna().sum() / len(df_basic)) * 100
        logging.info(f"Columna {col}: Elite {d_elite:.2f}% vs Básico {d_basic:.2f}%")

    # 6. Resultados Crown Jewels
    top_elite = user_metrics.sort_values('CSI_V3', ascending=False).head(10)
    logging.info("\n--- TOP 10 ORQUESTADORES (HackerEarth) ---")
    logging.info("\n" + top_elite[['CSI_V3', 'VDR', 'resonancia', 'pct_coder_agent']].to_string())

    # Exportar
    ruta_csv = os.path.join("docu", "metricas_fractal_v3.csv")
    user_metrics.to_csv(ruta_csv)
    logging.info(f"Protocolo Fractal V3 finalizado. Exportado a: {ruta_csv}")
    
    logging.info("--- PROTOCOLO V3 FINALIZADO (HackerEarth) ---")
    return user_metrics

if __name__ == "__main__":
    nombre_archivo = "zerve_hackathon_dataset.csv"
    ejecutar_v3(nombre_archivo)

# Ejecutar directamente (no solo bajo __main__ para que funcione en Zerve)
user_metrics_fractal = ejecutar_v3("zerve_hackathon_dataset.csv")
print(user_metrics_fractal[['CSI_V3', 'VDR', 'resonancia', 'pct_coder_agent']].sort_values('CSI_V3', ascending=False).head(10).to_string())
