import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
csv_path = Path('/home/deamon/The-shadow-Node-Theory/legacy/v2.7.5.1/reconstruction_real/data/eje_u_dimcor_crypto_por_caso.csv')
df = pd.read_csv(csv_path)
out = Path('/home/deamon/The-shadow-Node-Theory/figures')
plt.figure(figsize=(8,6))
plt.hist(df['d2_mean'].dropna(), bins=20, edgecolor='black')
plt.title('Distribución D2 Cripto 60 pares')
plt.xlabel('Dimensión de Correlación D2')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig(out/'crypto_d2_hist.png', dpi=150)
plt.close()
print('crypto figura creada')
