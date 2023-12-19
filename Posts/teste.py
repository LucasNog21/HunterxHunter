import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Selecionar Arquivo")

        # Entrada para exibir o caminho do arquivo
        self.entry_path = tk.Entry(self.master, width=40)
        self.entry_path.pack(pady=10)

        # Botão para abrir a caixa de diálogo de seleção de arquivo
        self.button_browse = tk.Button(self.master, text="Selecionar Arquivo", command=self.selecionar_arquivo)
        self.button_browse.pack(pady=10)

    def selecionar_arquivo(self):
        # Abre a caixa de diálogo de seleção de arquivo
        caminho_do_arquivo = filedialog.askopenfilename()

        # Atualiza a entrada com o caminho do arquivo selecionado
        self.entry_path.delete(0, tk.END)  # Limpa a entrada
        self.entry_path.insert(0, caminho_do_arquivo)  # Insere o novo caminho

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()