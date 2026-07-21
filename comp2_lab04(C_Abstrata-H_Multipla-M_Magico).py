from abc import ABC, abstractmethod

class Pessoa(ABC):
    """Classe abstrata que representa uma pessoa genérica."""

    def __init__(self, nome: str, endereco: str, idade: int):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade

    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

    def set_endereco(self, endereco: str):
        self.__endereco = endereco

    def aniversario(self):
        self.__idade += 1

    def __str__(self) -> str:
        return f"Nome: {self.__nome}, Endereço: {self.__endereco}, Idade: {self.__idade}"

    def get_nome(self) -> str:
        return self.__nome


class PessoaFisica(Pessoa):
    """Representa uma pessoa física com CPF e estado civil."""

    def __init__(self, nome: str, endereco: str, idade: int, cpf: str, estado_civil: str):
        Pessoa.__init__(self, nome, endereco, idade)
        self.__cpf = cpf
        self.__estado_civil = estado_civil

    def get_id(self) -> str:
        return self.__cpf

    def set_estado_civil(self, estado_civil: str):
        self.__estado_civil = estado_civil

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PessoaFisica):
            return self.__cpf == other.__cpf
        return False

    def __str__(self) -> str:
        return f"{super().__str__()}, CPF: {self.__cpf}, Estado Civil: {self.__estado_civil}"

    def get_cpf(self) -> str:
        return self.__cpf


class PessoaJuridica(Pessoa):
    """Representa uma pessoa jurídica com CNPJ."""

    def __init__(self, nome: str, endereco: str, idade: int, cnpj: str):
        super().__init__(nome, endereco, idade)
        self.__cnpj = cnpj

    def get_id(self) -> str:
        return self.__cnpj

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PessoaJuridica):
            return self.__cnpj == other.__cnpj
        return False

    def __str__(self) -> str:
        return f"{super().__str__()}, CNPJ: {self.__cnpj}"

    def get_cnpj(self) -> str:
        return self.__cnpj


class Empregado(PessoaFisica):
    """Representa um empregado com salário."""

    def __init__(self, nome: str, endereco: str, idade: int, cpf: str, estado_civil: str, salario: float):
        PessoaFisica.__init__(self, nome, endereco, idade, cpf, estado_civil)
        self.__salario = salario

    def aumentar_salario(self, aumento: float):
        self.__salario += aumento

    def total_anual(self) -> float:
        return self.__salario * 13

    def __str__(self) -> str:
        return f"{super().__str__()}, Salário: R$ {self.__salario:.2f}"

    def get_salario(self) -> float:
        return self.__salario


class Empresa(PessoaJuridica):
    """Representa uma empresa com lista de empregados."""

    def __init__(self, nome: str, endereco: str, idade: int, cnpj: str, empregados: list = []):
        super().__init__(nome, endereco, idade, cnpj)
        self.__empregados = empregados

    def contratar(self, empregado: Empregado):
        if empregado in self.__empregados:
            print("Empregado já contratado!")
        else:
            self.__empregados.append(empregado)

    def demitir(self, empregado: Empregado):
        if empregado in self.__empregados:
            self.__empregados.remove(empregado)
        else:
            print("Empregado não pertence à empresa!")

    def __len__(self) -> int:
        return len(self.__empregados)

    def __str__(self) -> str:
        empregados_str = "\n".join([f"  - {emp.get_nome()}" for emp in self.__empregados])
        return f"{super().__str__()}\nEmpregados:\n{empregados_str if empregados_str else '  (nenhum)'}"


class EmpregadoPJ(Empregado, Empresa):
    """Representa um prestador PJ que é empregado e também empresa."""

    def __init__(self, nome: str, endereco: str, idade: int, cpf: str, estado_civil: str, salario: float, cnpj: str, contrato: str):
        Empregado.__init__(self, nome, endereco, idade, cpf, estado_civil, salario)
        Empresa.__init__(self, nome, endereco, idade, cnpj, [self])
        self.__contrato = contrato

    def get_id(self) -> str:
        return f"{self.get_cpf()} {self.get_cnpj()}"

    def __eq__(self, other: object) -> bool:
        return PessoaFisica.__eq__(self, other) or PessoaJuridica.__eq__(self, other)

    def __str__(self) -> str:
        return f"{Empregado.__str__(self)} | CNPJ: {self.get_cnpj()} | Contrato: {self.__contrato}"


empregado1 = Empregado("João", "Rua A", 30, "111", "Solteiro", 3000)
empregado2 = Empregado("Maria", "Rua B", 28, "222", "Casada", 3200)

empregado3 = Empregado("Carlos", "Rua C", 35, "111", "Divorciado", 3100)

prestador1 = EmpregadoPJ("Marcos", "Rua D", 40, "222", "Casado", 4000, "123456789", "Prestação de Serviços")

print(empregado1)
print(empregado2)
print(empregado3)
print(prestador1)

print(isinstance(empregado1, EmpregadoPJ))       
print(isinstance(empregado1, Empregado))         
print(isinstance(empregado1, PessoaFisica))      
print(isinstance(empregado1, Empresa))           
print(isinstance(empregado1, PessoaJuridica))    
print(isinstance(empregado1, Pessoa))            

print(Empregado.mro())

print(isinstance(prestador1, EmpregadoPJ))       
print(isinstance(prestador1, Empregado))         
print(isinstance(prestador1, PessoaFisica))      
print(isinstance(prestador1, Empresa))           
print(isinstance(prestador1, PessoaJuridica))    
print(isinstance(prestador1, Pessoa))            

print(EmpregadoPJ.mro())

print(empregado1 == empregado2)  
print(empregado1 == empregado3) 
print(empregado2 == prestador1)  

empresa = Empresa("Tech Ltda", "Rua Z", 10, "88888888")

print(len(empresa))

print(empresa)

empresa.contratar(empregado1)
empresa.contratar(empregado2)

print(len(empresa)) 

print(empresa)

empresa.demitir(empregado2)

print(len(empresa))  

print(empresa)

empresa.demitir(empregado2)

empresa.contratar(empregado3)  

empresa.contratar(prestador1)

print(len(empresa))  

print(empresa)

prestador1.set_endereco("Rua Nova")
prestador1.set_estado_civil("Viúvo")
prestador1.aniversario()
prestador1.aumentar_salario(500)

print(f"Salário anual do prestador1: R$ {prestador1.total_anual():.2f}")

print(empresa)
