import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y = np.tan(x)

y[np.abs(np.cos(x)) < 0.05] = np.nan

plt.plot(x, y, 'g.-')
plt.title("Plot da Função Tangente")
plt.xticks(
    [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
    [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$']
)
plt.grid(True)
plt.show()
