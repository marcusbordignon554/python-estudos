import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ValorNegativoError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass


class ContaCorrente:
    def __init__(self, nome: str, limite: float):
        self.__nome = nome
        self.__limite = limite
        self.__data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__saldo = 0.0
        
    def depositar(self, valor: float):
        if valor < 0:
            raise ValorNegativoError("Depósito negativo não permitido.")
        self.__saldo += valor

    def sacar(self, valor: float):
        if valor < 0:
            raise ValorNegativoError("Saque negativo não permitido.")
        if valor > self.__saldo + self.__limite:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        self.__saldo -= valor

    def __str__(self):
        return (f"Nome: {self.__nome}\n"
                f"Data de criação: {self.__data_criacao}\n"
                f"Limite: R${self.__limite:.2f}\n"
                f"Saldo: R${self.__saldo:.2f}")


class AppContaCorrente:
    def __init__(self, master):
        self.master = master
        self.master.title("Conta Corrente")
        self.master.geometry("400x250")
        self.master.resizable(False, False)
        self.conta = None

        tk.Label(master, text="Nome:").pack()
        self.entry_nome = tk.Entry(master)
        self.entry_nome.pack()

        tk.Label(master, text="Limite:").pack()
        self.entry_limite = tk.Entry(master)
        self.entry_limite.pack()

        self.btn_criar = tk.Button(master, text="Criar", command=self.criar_conta)
        self.btn_criar.pack()

        self.label_info = tk.Label(master, text="", justify="left")
        self.label_info.pack()

        tk.Label(master, text="Valor:").pack()
        self.entry_valor = tk.Entry(master)
        self.entry_valor.pack()

        frame_botoes = tk.Frame(master)
        frame_botoes.pack()
        tk.Button(frame_botoes, text="Depositar", command=self.depositar).pack(side="left", padx=10)
        tk.Button(frame_botoes, text="Sacar", command=self.sacar).pack(side="left")

    def criar_conta(self):
        nome = self.entry_nome.get().strip()
        limite_texto = self.entry_limite.get().strip()
        if not nome or not limite_texto:
            messagebox.showerror("Erro", "Nome e limite são obrigatórios.")
            return
        try:
            limite = float(limite_texto)
            self.conta = ContaCorrente(nome, limite)
            self.label_info.config(text=str(self.conta))
        except ValueError:
            messagebox.showerror("Erro", "Limite deve ser um número.")


    def depositar(self):
        if not self.conta:
            messagebox.showerror("Erro", "Crie uma conta primeiro.")
            return
        try:
            valor = float(self.entry_valor.get())
            self.conta.depositar(valor)
            self.label_info.config(text=str(self.conta))
        except ValueError:
            self.entry_valor.delete(0, tk.END)
            messagebox.showerror("Erro", "Digite um valor numérico.")
        except ValorNegativoError as e:
            messagebox.showerror("Erro", str(e))

    def sacar(self):
        if not self.conta:
            messagebox.showerror("Erro", "Crie uma conta primeiro.")
            return
        try:
            valor = float(self.entry_valor.get())
            self.conta.sacar(valor)
            self.label_info.config(text=str(self.conta))
        except ValueError:
            self.entry_valor.delete(0, tk.END)
            messagebox.showerror("Erro", "Digite um valor numérico.")
        except (ValorNegativoError, SaldoInsuficienteError) as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AppContaCorrente(root)
    root.mainloop()
