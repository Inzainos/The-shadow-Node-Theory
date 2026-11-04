import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

out = Path('/home/deamon/The-shadow-Node-Theory/figures')
out.mkdir(exist_ok=True)

t = np.linspace(1,100,200)
for b, label in [(0.5,'Sublineal'),(1.0,'Lineal'),(1.5,'Superlineal')]:
    R = t**b
    plt.plot(t,R,label=f'b={b}')
plt.xlabel('t')
plt.ylabel('R(t)')
plt.title('Trayectorias R(t)=t^b')
plt.legend()
plt.savefig(out/'trayectorias_Rt.png', dpi=150)
plt.close()

# Campo phi esquemático
x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)
X,Y = np.meshgrid(x,y)
phi = X**2 + Y**2
plt.contourf(X,Y,phi, levels=20, cmap='viridis')
plt.colorbar(label='φ')
plt.title('Campo de fricción φ esquemático')
plt.savefig(out/'campo_phi.png', dpi=150)
plt.close()

print('Figuras generadas')
