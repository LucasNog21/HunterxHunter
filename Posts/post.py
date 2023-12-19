from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

class Post:
    def __init__(self, master , title, category, file_image, description, name):
        self.master = master
        self.master.geometry("1000x600") 
        self.title = title
        self.category = category
        self.file_image = file_image
        self.imagem_pil = Image.open(self.file_image)
        self.description = description
        self.name = name

        self.ttl = Label(self.master, text=self.title, font=("Helvetica", 16))
        self.ttl.pack(anchor = "n")

        self.top_frame = Frame(self.master)
        self.top_frame.pack()

        self.cty = Label(self.top_frame, text="Categoria: "+self.category, font=("Helvetica", 15))
        self.cty.pack(side = "left", padx = 5, anchor="w")

        self.nm = Label(self.top_frame, text="Autor: "+self.name, font=("Helvetica", 15))
        self.nm.pack(side = "right", padx = 100, anchor="e")


        self.imagem_tk = ImageTk.PhotoImage(self.imagem_pil)
        self.img = Label(self.master, image=self.imagem_tk)
        self.img.image = self.imagem_tk
        self.img.pack()

        self.dsc = Label(self.master, text=self.description, wraplength=400, justify="center", font=("Helvetica", 12))
        self.dsc.pack()


    
        self.update_window_size()


    def update_window_size(self):
        width = self.imagem_pil.width

        height = 1000

        # Define o tamanho da janela
        self.master.geometry(f"{width}x{height}")
        return width
    
    def open_image(self):

        self.img_frame = Frame(self.master)
        self.img_frame.pack()
        self.imagem_tk = ImageTk.PhotoImage(self.imagem_pil)
        self.img = Label(self.master, image=self.imagem_tk)
        self.img.image = self.imagem_tk
        self.img.place(relx=0.5,rely =0.45, anchor = "c")


if __name__ == "__main__":
    raiz = Tk()
    app = Post(raiz, "Teste", "Ameaça", "HunterxHunter\Images\image500x600.jpg", "Muito bacana", "Lucas")
    raiz.mainloop()