import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2.5, 5, 400)
h = np.where(u != 0, u**2 * (-2*u + 1/u**3), np.nan)

plt.plot(u, h)
plt.title('h(u) com descontinuidade em u = 0')
plt.grid(True)
plt.show()
