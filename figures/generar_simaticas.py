import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
out = Path('/home/deamon/The-shadow-Node-Theory/figures')
np.random.seed(0)
data = np.random.rand(10,10)
plt.imshow(data, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='correlación forma/tono')
plt.title('Tela simática - mapa de resonancia dominio')
plt.savefig(out/'tela_simática.png', dpi=150)
plt.close()
print('simática creada')
