from tkinter import *
from PIL import Image, ImageTk
from Posts.post import Post
import webbrowser
from tkinter import filedialog
import os 

class Post_register:
    def __init__(self, master):
        self.master = master
        self.master.title("Exemplo de Imagem")

        self.c1 = Frame(self.master)
        self.c1["padx"] = 100
        self.c1["pady"] = 10
        self.c1.pack()

        self.titulo = Label(self.c1, text = "Registro de post")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.c2 = Frame(self.master)
        self.c2.pack()
        self.t2 = Label(self.c2, text = "Titulo")
        self.t2.pack(side = LEFT)
        self.l2 = Entry(self.c2)
        self.l2.pack(side = LEFT)

        self.c3 = Frame(self.master)
        self.c3.pack()
        self.t3 = Label(self.c3, text = "Categoria")
        self.t3.pack(side = LEFT)
        self.l3 = Entry(self.c3)
        self.l3.pack(side = LEFT)

        self.c5 = Frame(self.master)
        self.c5.pack()
        self.t5 = Label(self.c5, text = "Descrição")
        self.t5.pack(side = LEFT)
        self.l5 = Entry(self.c5)
        self.l5.pack(side = LEFT)

        self.c6 = Frame(self.master)
        self.c6.pack()
        self.t6 = Label(self.c6, text = "Nome")
        self.t6.pack(side = LEFT)
        self.l6 = Entry(self.c6)
        self.l6.pack(side = LEFT)

        self.c4 = Frame(self.master)
        self.c4.pack()
        self.botao = Button(self.c4, text = "Postar")
        self.botao["command"] = self.postar
        self.botao.pack()

        self.c5 = Frame(self.master)
        self.c5.pack()
        self.botao = Button(self.c5, text = "redefinir imagem")
        self.botao["command"] = self.open_link
        self.botao.pack()

        self.c6 = Frame(self.master)
        self.c6.pack()
        self.botao = Button(self.c6, text = "Importar imagem")
        self.botao["command"] = self.import_image
        self.botao.pack()
    
    def import_image(self):
        file_path = filedialog.askopenfilename()

        hunter = file_path.find("HunterxHunter")

        if hunter != -1:
            relative_path = file_path[hunter:]

        self.file_image = relative_path


    def open_link(self):
        link = "https://www.befunky.com/pt/criar/editor-de-fotos/"
        webbrowser.open(link)
    

    def postar(self):
        self.title = self.l2.get()
        self.category = self.l3.get()
        self.description = self.l5.get()
        self.name = self.l6.get()

        self.open_post()


    def open_post(self):
        raiz = Tk()
        posts = Post(raiz, self.title, self.category, self.file_image, self.description, self.name)
        raiz.mainloop()

if __name__ == "__main__":
    raiz = Tk()
    posts = Post_register(raiz)
    raiz.mainloop()


