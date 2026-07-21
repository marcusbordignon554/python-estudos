import random
import pickle

class CifraCesar:
    """Classe que implementa a Cifra de César para criptografia e descriptografia de arquivos."""
    CARACTERES:str="ABCDEFGHIJKLMNOPQRSTUWXYZ#$&*@().:,!?[]=+-%abcdefghijklmnopqrstuvwxyz"

    @classmethod
    def __cripto_caractere(cls, caractere:str, chave:int)->str:
        """Criptografa um único caractere utilizando a chave informada."""
        if caractere in cls.CARACTERES:
            idx = cls.CARACTERES.index(caractere)
            novo_idx = (idx + chave) % len(cls.CARACTERES)
            return cls.CARACTERES[novo_idx]
        return caractere

    @classmethod
    def __decripto_caractere(cls,caractere:str,chave:int)->str:
        """Descriptografa um único caractere utilizando a chave informada."""
        if caractere in cls.CARACTERES:
            idx = cls.CARACTERES.index(caractere)
            novo_idx = (idx - chave) % len(cls.CARACTERES)
            return cls.CARACTERES[novo_idx]
        return caractere

    @classmethod
    def cripto_arquivo(cls,nome_arquivo:str,chave:int=0)->int:
        """Criptografa um arquivo texto utilizando a Cifra de César."""
        if not nome_arquivo:
            nome_arquivo=input("Digite o nome do arquivo: ")

        try:
            with open(nome_arquivo,'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
            return None

        n = len(cls.CARACTERES)
        if chave==0 or not (-n < chave < n):
            chave=random.choice([i for i in range(-n+1, n) if i != 0])

        nome_saida=nome_arquivo.replace('.txt', '') + '_cripto.txt'

        with open(nome_saida, 'w', encoding='utf-8') as arquivo_saida:
            for caractere in conteudo:
                arquivo_saida.write(cls.__cripto_caractere(caractere, chave))

        return chave

    @classmethod
    def decripto_arquivo(cls,nome_arquivo:str,chave:int=0,sobrescrever:bool=False)->int:
        """Descriptografa um arquivo criptografado utilizando a Cifra de César."""
        n=len(cls.CARACTERES)
        if chave == 0 or not (-n < chave < n):
            print("Erro: chave inválida para descriptografar.")
            return None

        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo=arquivo.read()
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
            return None

        if sobrescrever:
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_saida:
                for caractere in conteudo:
                    arquivo_saida.write(cls.__decripto_caractere(caractere, chave))
        else:
            nome_saida=nome_arquivo.replace('.txt', '') + '_decripto.txt'
            with open(nome_saida, 'w', encoding='utf-8') as arquivo_saida:
                for caractere in conteudo:
                    arquivo_saida.write(cls.__decripto_caractere(caractere, chave))

        return chave

if __name__ == "__main__":
    chave_cripto = CifraCesar.cripto_arquivo('teste.txt')
    print(f"Chave usada: {chave_cripto}")

    import pickle
    with open('chave_cripto.dump', 'wb') as f:
        pickle.dump(chave_cripto, f)

    with open('chave_cripto.dump', 'rb') as f:
        chave_decripto = pickle.load(f)

    CifraCesar.decripto_arquivo('teste_cripto.txt', chave_decripto)
    print("Arquivo descriptografado!")
