import tkinter as tk
from tkinter import messagebox
import random

class JogoDasCores:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo das Cores")
        self.master.geometry("300x150")
        self.master.resizable(False, False)
        self.cores = ["red", "yellow", "blue", "green", "black", "white", "gray"]
        self.pontos = 0
        self.cor_esperada = ""
        self.btn_texto = tk.Button(master, text="Clique para iniciar", width=25, height=2, command=self.sortear)
        self.btn_texto.pack(pady=5)
        self.btn_texto.bind("<Button-3>", self.resetar_jogo)
        self.frame_cores = tk.Frame(master)
        self.frame_cores.pack()
        self.botoes_cores = []
        for cor in self.cores:
            btn = tk.Button(self.frame_cores, bg=cor, width=5, height=2)
            btn.config(command=lambda c=cor: self.verificar(c))
            btn.pack(side="left", padx=2)
            self.botoes_cores.append(btn)
            
        self.label_pontos = tk.Label(master, text="Pontos: 0", font=("Arial", 12))
        self.label_pontos.pack(pady=5)


    def sortear(self):
        cor_aleatoria = random.choice(self.cores)
        texto_aleatorio = random.choice(self.cores)
        self.cor_esperada = texto_aleatorio
        self.btn_texto.config(bg=cor_aleatoria, fg="black" if cor_aleatoria != "black" else "white", text=texto_aleatorio)

    def verificar(self, cor_clicada):
        if not self.cor_esperada:
            return
        if cor_clicada == self.cor_esperada:
            self.pontos += 1
        else:
            self.pontos -= 1
        self.label_pontos.config(text=f"Pontos: {self.pontos}")
        self.sortear()

    def resetar_jogo(self, event):
        self.pontos = 0
        self.cor_esperada = ""
        self.btn_texto.config(bg="SystemButtonFace", text="Clique para iniciar")
        self.label_pontos.config(text="Pontos: 0")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDasCores(root)
    root.mainloop()
