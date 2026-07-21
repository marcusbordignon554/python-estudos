import numpy as np
#1

def gera_matriz(a: float, b: float, m: int, n: int):
    valores = np.linspace(a, b, n)
    if len(valores) < m * m:
        print("Não é possível construir")
        return None
    return valores[:m*m].reshape((m, m))


#2
def linha(M, i):
    if len(M.shape) != 2:
        print("Isto não é uma matriz")
        return None
    if i < 0 or i >= M.shape[0]:
        print("Não existe esta linha")
        return None
    return M[i]

def coluna(M, i):
    if len(M.shape) != 2:
        print("Isto não é uma matriz")
        return None
    if i < 0 or i >= M.shape[1]:
        print("Não existe esta coluna")
        return None
    return M[:, i]


#3
def funcao3a(a, b, n):
    x = np.linspace(a, b, n)
    y = x**2 - 9
    return x, y

def funcao3b(a, b, n):
    x, y = funcao3a(a, b, n)
    booleano = y >= 0
    return x, y, booleano

def funcao3c(a, b, n):
    _, y, booleano = funcao3b(a, b, n)
    positivos = y[booleano]
    negativos = y[~booleano]
    return positivos, negativos

#4
def polinomio(x, a):
    expoentes = np.arange(len(a))
    potencias = x ** expoentes
    resultado = np.sum(a * potencias)
    return np.int64(resultado)

#5
from scipy.linalg import solve as scipy_solve

def solve(A, b):
    A = np.array(A)
    b = np.array(b)
    if A.ndim != 2 or b.ndim != 1 or A.shape[0] != b.shape[0]:
        return None, None
    m, n = A.shape
    if m == n:
        try:
            x = scipy_solve(A, b)
            det_A = np.linalg.det(A)
            return x, det_A
        except:
            return None, None
    else:
        try:
            A_T = A.T
            A_pseudo = np.linalg.inv(A_T @ A) @ A_T
            print("A_pseudoinv.shape=", A_pseudo.shape)
            print("b.shape=", b.shape)
            x = A_pseudo @ b
            return x, None
        except:
            return None, None
        
#6 ?????
