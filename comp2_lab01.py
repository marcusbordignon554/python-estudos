def calcular_combustivel(distancia:int, consumo:int) -> float:
    '''Calcula quantos litros de combustivel precisará para percorrer uma certa distancia.

    Parametros:
    distancia: Distancia em km do destino.
    consumo: Litros consumidos pelo carro por km percorrido.

    Retorna:
    A quantidade de litros de combustıvel necessária para completar a viagem.
    '''
    
    return distancia/consumo


def verifica_tarefa(tarefa:str, lista:str) -> bool:
    '''Verifica se uma tarefa especifica esta na lista.

    Parametros:
    tarefa: A tarefa que é verificada se está na lista.
    lista: É a lista de tarefas a serem completadas.

    Retorna:
    Se é True ou False se a tarefa está na lista.
    '''

    return tarefa in lista


def adiciona_item(lista:list[str], item:str) -> list[str]:
    '''Adiciona um item a uma lista de compras se já não estiver na lista.

    Parametros:
    lista: A lista de compras onde os itens são armazenados.
    item: O item a ser checado se esta na lista, e caso nao esteja, é adicionado à lista de compras.

    Retorna:
    A lista de compras atualizada. Se o item já estiver na lista, a lista é retornada sem ser alterada.
    '''
    if item in lista:
        return lista
    else:
        lista.append(item)
        return lista


def contar_palavras(lista: list[str]) -> dict[str, int]:
    '''Conta as palavras de uma lista de strings.

    Parametros:
    lista: É a lista de palavras onde vai ser checada quantas vezes uma palavra se repete.

    Retorna:
    Um dicionario com as palavras e o numero de vezes que elas se repetem.
    '''

    palavra=""
    dicionario={}

    for palavra in lista:
        if palavra in dicionario:
            dicionario[palavra]=dicionario[palavra]+1
        else:
            dicionario[palavra]=1

    return dicionario


def classificar_idade(idade:int) -> str:
    '''Classifica se a pessoa é Crianca, Adolescente, Adulto ou Idoso de acordo com a idade fornecida.

    Parametros:
    idade: A idade da pessoa.

    Retorna:
    A classificacao da pessoa de acordo com a idade fornecida.
    '''

    if idade<12:
        return "Criança"
    elif 12<=idade<=17:
        return "Adolescente"
    elif 18<=idade<=64:
        return "Adulto"
    else:
        return "Idoso"


def calcular_desconto(valor:int) -> float:
    '''Funcao que recebe o valor da compra e retorna o preco final da compra apos o desconto.

    Parametros:
    valor: É o valor inicial da compra.

    Retorna:
    O valor final da compra após o desconto.
    '''

    if valor <=100:
        valor=valor-(valor*0.05)
        print("R$ "+str(valor))
    elif 101<=valor<=500:
        valor=valor-(valor*0.1)
        print("R$ "+str(valor))
    elif 501<=valor<=1000:
        valor=valor-(valor*0.15)
        print("R$ "+str(valor))
    else:
        valor=valor-(valor*0.2)
        print("R$ "+str(valor))


def contagem_regressiva(numero:int) -> int and str:
    '''Funcao que faz uma contagem regressiva a partir de um numero fornecido pelo usuario e imprima os numeros de forma decrescente ate 1.

    Parametros:
    numero: E o número fornecido pelo usuário.

    Retorna:
    Uma string com a contagem até o numero 1, seguido da mensagem "Fim da contagem!"
    '''
    resultado = ""
    while numero>0:
        print(numero)
        numero-=1
    print("Fim da contagem!")


def classifica_estudantes(lista:float or int, corte:float or int) -> dict:
    '''Funcao que percorre a lista de notas e classifica os estudantes como aprovados ou reprovados com base em uma nota de corte.

    Parametros:
    lista: É a lista de notas dos estudantes.
    corte: É a nota de corte.

    Retorna:
    Uma biblioteca com o número de estudantes aprovados e reprovados.
    '''

    dicionario={"aprovado":0, "reprovado":0}
    
    for nota in lista:
        if nota<6.0:
            dicionario["reprovado"]+=1
        else:
            dicionario["aprovado"]+=1
            
    return dicionario

def verifica_acesso() -> None:
    '''Funcao que verifica se o visitante pode ou não acessar todas as atracoes com base na idade que ele digitar,
    além de perguntar ao usuario se ele deseja verificar o acesso para mais pessoas
    '''
    continuar="Sim"
    while continuar=="Sim":
    

        idade:int=int(input("Idade:")) #idade:int
        if idade >=18:
            print("Acesso permitido a todas as atrações.") #Retorna uma string
        else:
            print("Acesso restrito às atrações para menores de idade.") #Retorna uma string
    
        continuar:str=str(input("Continuar:")) #continuar:str


def verifica_senha() -> None:
    '''Função que solicita ao usuário que crie uma senha e verifica se ela atende ao critério de ter pelo menos 8 caracteres, pedindo uma senha nova
    até que uma senha válida seja fornecida ou até que o número máximo de tentativas seja alcançado.
    '''
    
    contador = 0
    while contador < 3:
        senha:str=input("Senha: ")  # senha:str
        if len(senha) < 8:
            contador += 1
            if contador < 3:  
                print("Senha inválida. A senha deve ter pelo menos 8 caracteres.") #Retorna uma string
        else:
            print("Senha aceita.") #Retorna uma string
            return
        
    print("Número máximo de tentativas excedido. Tente novamente mais tarde.") #Retorna uma string
            
