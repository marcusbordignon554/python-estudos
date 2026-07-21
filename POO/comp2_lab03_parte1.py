class Pessoa:

    __universidade = 'UFRJ'

    @classmethod
    def get_universidade(cls) -> str:
        return cls.__universidade

    @classmethod
    def set_universidade(cls, universidade: str):
        cls.__universidade = universidade
        print(f"Universidade {cls.__universidade} cadastrada com sucesso.")

    def __init__(self, nome: str, matricula: str):
        self.__nome = nome
        self.__matricula = matricula

    def get_nome(self) -> str:
        return self.__nome

    def get_matricula(self) -> str:
        return self.__matricula

    def exibir_infos(self):
        print(f"Universidade: {Pessoa.get_universidade()}; Nome: {self.__nome}; Matricula: {self.__matricula}")


class Professor(Pessoa):
    """Representa um professor universitário."""

    def __init__(self, nome: str, matricula: str, departamento: str):
        super().__init__(nome, matricula)
        self.__departamento = departamento

    def get_departamento(self) -> str:
        return self.__departamento

    def set_departamento(self, departamento: str):
        self.__departamento = departamento
        print(f"Departamento {self.__departamento} cadastrado com sucesso.")

    def exibir_infos(self):
        super().exibir_infos()
        print(f"Departamento: {self.__departamento}")


class Aluno(Pessoa):
    """Representa um aluno universitário."""

    def __init__(self, nome: str, matricula: str, disciplinas: list = []):
        super().__init__(nome, matricula)
        self.__disciplinas = disciplinas

    def get_disciplinas(self) -> list:
        return self.__disciplinas

    def inscrever(self, disciplina: str):
        if disciplina not in self.__disciplinas:
            self.__disciplinas.append(disciplina)
            print(f"Item {disciplina} inscrito nas disciplinas com sucesso.")
        else:
            print(f"Aluno já inscrito na disciplina {disciplina}")

    def trancar(self, disciplina: str):
        if disciplina in self.__disciplinas:
            self.__disciplinas.remove(disciplina)
            print("Item trancado com sucesso.")
            if self.__disciplinas == []:
                print("Nenhuma disciplina atual.")
            else:
                print(f"Disciplinas atuais: {self.__disciplinas}")
        else:
            print(f"Aluno não está inscrito na disciplina {disciplina}.")

    def exibir_infos(self):
        super().exibir_infos()
        print(f"Disciplinas: {self.__disciplinas}")


class AlunoGraduacao(Aluno):
    """Representa um aluno universitário com seu curso de graduação."""

    def __init__(self, nome: str, matricula: str, curso: str, disciplinas: list = []):
        super().__init__(nome, matricula, disciplinas)
        self.__curso = curso

    def get_curso(self) -> str:
        return self.__curso

    def set_curso(self, curso: str):
        self.__curso = curso
        print(f"Curso {self.__curso} cadastrado com sucesso.")

    def exibir_infos(self):
        super().exibir_infos()
        print(f"Curso: {self.__curso}")


class AlunoPosGraduacao(Aluno):
    """Representa um aluno universitário de pós-graduação com sua área de atuação."""

    def __init__(self, nome: str, matricula: str, area: str, disciplinas: list = []):
        super().__init__(nome, matricula, disciplinas)
        self.__area_pesquisa = area

    def get_area(self) -> str:
        return self.__area_pesquisa

    def set_area(self, area: str):
        self.__area_pesquisa = area
        print(f"Área de pesquisa {self.__area_pesquisa} cadastrada com sucesso.")

    def exibir_infos(self):
        super().exibir_infos()
        print(f"Área de pesquisa: {self.__area_pesquisa}")


prof1=Professor("Albert","31090100","Instituto de Computacao")
aluno1=AlunoGraduacao("Brígida","125000001","BCMT")
aluno2=AlunoGraduacao("Cleiton","125000003","Estatística",["Computacao 2"])
aluno3=AlunoGraduacao("Dulce","125000003","Ciencias Atuariais",["Computacao 2", "Calculo Numérico"])
aluno4=AlunoPosGraduacao("Eric","225000001","Engenharia de Software",["Inteligencia Computacional"])
prof1.exibir_infos()
aluno1.exibir_infos()
aluno2.exibir_infos()
aluno3.exibir_infos()
aluno4.exibir_infos()
aluno1.inscrever("Computacao 2")
aluno1.inscrever("Computacao 2")
aluno3.trancar("Calculo Numérico")
aluno2.trancar("Calculo Numérico")
prof1.exibir_infos()
aluno1.exibir_infos()
aluno2.exibir_infos()
aluno3.exibir_infos()
aluno4.exibir_infos()    
 
        
