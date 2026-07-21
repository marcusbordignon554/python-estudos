import tkinter as tk
from tkinter import font

class JogoDaForca(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Jogo da Forca")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.pack()
        self.palavra = self.carrega_palavra().lower()
        self.estado_palavra = tk.StringVar()
        self.letras_erradas = tk.StringVar()
        self.estado_palavra.set("-" * len(self.palavra))
        self.letras_erradas.set("")

        self.criar_widgets()

    def carrega_palavra(self):
        with open("palavra.txt", "r") as f:
            return f.read().strip()

    def criar_widgets(self):
        fonte = font.Font(family="Arial", size=16)
        self.label_titulo = tk.Label(self, text="Adivinhe a palavra", font=fonte)
        self.label_titulo.pack(pady=10)
        self.label_palavra = tk.Label(self, textvariable=self.estado_palavra, font=fonte)
        self.label_palavra.pack(pady=10)
        self.entrada = tk.Entry(self, font=fonte, width=2)
        self.entrada.pack(pady=10)
        self.entrada.bind("<Return>", self.verificar_letra)
        self.label_erros = tk.Label(self, textvariable=self.letras_erradas, font=fonte)
        self.label_erros.pack(pady=10)

    def verificar_letra(self, event):
        letra = self.entrada.get().lower().strip()
        if len(letra) == 1 and letra.isalpha():
            palavra_atual = list(self.estado_palavra.get())
            acertou = False
            for i, l in enumerate(self.palavra):
                if l == letra:
                    palavra_atual[i] = letra
                    acertou = True
            if acertou:
                self.estado_palavra.set("".join(palavra_atual))
            else:
                letras_atuais = self.letras_erradas.get()
                if letra not in letras_atuais:
                    self.letras_erradas.set(letras_atuais + letra)
        self.entrada.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDaForca(master=root)
    app.mainloop()
