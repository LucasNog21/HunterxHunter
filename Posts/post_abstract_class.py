from tkinter import Tk, Label
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Exemplo de Imagem")

        # Carregando a imagem com o PIL
        self.imagem_pil = Image.open("Images\IMG_20221224_234029_938.jpg")
        self.imagem_tk = ImageTk.PhotoImage(self.imagem_pil)

        # Adicionando a imagem a um rótulo
        self.label = Label(master, image=self.imagem_tk)
        self.label.pack()

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()


