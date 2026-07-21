class Cliente:
    def __init__(self, nome: str, cpf: str, nome_social: str = ""):
        self.__nome = nome
        self.__cpf = cpf
        self.__nome_social = nome_social

    # Getters e Setters
    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_cpf(self) -> str:
        return self.__cpf

    def set_cpf(self, cpf: str):
        self.__cpf = cpf

    def get_nome_social(self) -> str:
        return self.__nome_social

    def set_nome_social(self, nome_social: str):
        self.__nome_social = nome_social

class Conta:
    def __init__(self, agencia: int, numero: int, clientes: list[Cliente], saldo: float=0):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo
        self.__clientes = clientes

    def saque(self, valor: float):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
          return "Saldo Insuficiente."

    def deposito(self, valor: float):
            self.__saldo += valor

    def resumo(self):
        print(f"Agencia: {self.__agencia}, CC: {self.__numero}, saldo = {self.__saldo}")
        for cli in self.__clientes:
         print(f"Correntista: {cli.get_nome()}, CPF: {cli.get_cpf()}")
        print("="*40)

    def adiciona_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def remove_cliente(self, cpf: str):
        for indice, cliente in enumerate(self.__clientes):
            if cliente.get_cpf() == cpf:
                self.__clientes.pop(indice)

    def imprime_clientes(self):
        for cli in self.__clientes:
            print(f"Nome: {cli.get_nome()} CPF: {cli.get_cpf()}")
        print("="*40)

    # Getters e Setters
    def get_agencia(self) -> int:
        return self.__agencia
    def set_agencia(self, agencia: int):
        self.__agencia = agencia
    def get_numero(self) -> int:
        return self.__numero
    def set_numero(self, numero: int):
        self.__numero = numero
    def get_saldo(self) -> int:
        return self.__saldo
    def set_agencia(self, saldo: int):
        self.__saldo = saldo
        
cliente1 = Cliente("Leoni", "0000000101")
cliente2 = Cliente("Carol", "0000000102")
cliente3 = Cliente("Rodrigo", "0000000103")
conta1 = Conta(123, 456, [cliente2, cliente3], 100000)
conta2 = Conta(890, 576, [cliente1], 50)

conta1.resumo()

