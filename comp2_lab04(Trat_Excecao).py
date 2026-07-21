class NumeroParError(Exception):
    """Cria uma classe de exceção para resultados pares."""
    def __init__(self, msg: str = "Resultado da divisão não pode ser par."):
        super().__init__(msg)


class NumeradorZeroError(Exception):
    """Cria uma classe de exceção para numerador igual a zero."""
    def __init__(self, msg: str = "Numerador não pode ser 0."):
        super().__init__(msg)


def div(x:float,y:float)->float:
    """Faz a divisão de um número float por outro."""
    try:
        if x==0:
            raise NumeradorZeroError()
        resultado=x/y
        if resultado%2==0:
            raise NumeroParError()
        else:
            return resultado

    except NumeradorZeroError as e:
        print(f"Exceção: {type(e).__name__} - {e}")

    except NumeroParError as e:
        print(f"Exceção: {type(e).__name__} - {e}")

    except ZeroDivisionError as e:
        print(f"Exceção: {type(e).__name__} - Denominador não pode ser 0.")

    except ValueError as e:
        print(f"Exceção: {type(e).__name__} - Valor só pode ser numérico.")

    except TypeError as e:
        print(f"Exceção: {type(e).__name__} - Valor só pode ser numérico.")

    
def testar_div()->None:
    """Testa a função div() com valores inputados pelo usuário."""
    try:
        nm1=float(input("Digite o primeiro número: "))
        nm2=float(input("Digite o segundo número: "))
        return div(nm1,nm2)

    except ZeroDivisionError as e:
        print(f"Exceção: {type(e).__name__} - Denominador não pode ser 0.")

    except ValueError as e:
        print(f"Exceção: {type(e).__name__} - Valor só pode ser numérico.")


def incrementar(lista:list,incremento:int):
    """Incrementa o objeto incremento aos elementos da lista."""
    try:
        if not isinstance(lista,list):
            raise TypeError("O primeiro parâmetro deve ser uma lista.")
        if not isinstance(incremento,int):
            raise TypeError("O segundo parâmetro deve ser um inteiro.")
        for i in range(len(lista)):
            lista[i] += incremento

    except TypeError as e:
        print(f"Exceção: {type(e).__name__} - Valores da lista só podem ser numéricos para serem incrementados.")
        return None
    else:
        return lista
    finally:
        print("Função incrementar() concluída!")

