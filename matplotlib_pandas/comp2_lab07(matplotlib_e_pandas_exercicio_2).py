import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-9, 9, 200)
y = x**2 - 9

x1 = x[y < 0]
y1 = y[y < 0]

x2 = x[y >= 0]
y2 = y[y >= 0]

plt.plot(x1, y1, 'r-', label='y < 0')
plt.plot(x2, y2, 'b-', label='y >= 0')
plt.legend()
plt.title(r'$y = x^2 - 9$')
plt.grid(True)
plt.show()
