class Pilha:
    def __init__(self, elementos=[]):
        if isinstance(elementos, list)==True:
            self.__elementos = elementos.copy()
            print(f"Pilha={self.__elementos} criada com sucesso.")
        else:
            self.__elementos = []
            print("Erro, argumento não é lista. Pilha iniciada vazia.")

    def len_pilha(self):
        print (f"Comprimento da pilha: {len(self.__elementos)}.")

    def empilhar(self, elemento):
        self.__elementos.append(elemento)

    def desempilhar(self):
        if len(self.__elementos)==0:
            print("Pilha vazia.")
        else:
            self.__elementos.pop()
            if len(self.__elementos)==0:
                print("Pilha esvaziada.")
            else:
                print(f"Pilha agora é: {self.__elementos}.")

    def get_pilha(self):
        print (f"Pilha é: {self.__elementos.copy()}.")
        
#a)
p1=Pilha([1, 7, 9])
p2=Pilha()

#b)
p1.len_pilha()
p2.len_pilha()

#c)
p3=Pilha(42)

#d)
p2.empilhar(4)
p2.empilhar(10)

#e)
p2.len_pilha()

#f)
p2.get_pilha()

#g)
p2.desempilhar()
p2.desempilhar()
p2.desempilhar()

