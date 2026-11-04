import matplotlib.pyplot as plt
from pathlib import Path
out = Path('/home/deamon/The-shadow-Node-Theory/figures')
labels = ['LOO Dominio','LOO Tono','Balanceada Dominio','Balanceada Tono']
values = [50.7,66.2,55.6,63.8]
plt.bar(labels, values)
plt.ylabel('Exactitud %')
plt.title('Tela de incertidumbre - métricas LOO')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(out/'tela_incertidumbre.png', dpi=150)
plt.close()
print('tela creada')
