import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.2)
f1 = x
f2 = x**2
f3 = x**3

plt.plot(x, f1, 'r--', linewidth=1.5, label='f(x) = x')
plt.plot(x, f2, 'bs', markersize=2.5, label='f(x) = x²')
plt.plot(x, f3, 'g^', markersize=2, label='f(x) = x³')
plt.legend()
plt.title("Três Funções")
plt.grid(True)
plt.savefig("grafico_funcoes.png")
plt.show()
