from tkinter import *
from Posts.post import Post
import webbrowser

class Post_register:
    def __init__(self, master):
        self.master = master
        self.master.title("Post")
        self.file_types = [("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.gif")]
        self.image_object = None

        self.window = Frame(self.master)
        self.window["padx"] = 100
        self.window["pady"] = 10
        self.window.pack()

        self.title = Label(self.window, text = "Registro de post")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.title_frame = Frame(self.master)
        self.title_frame.pack()
        self.title_label = Label(self.title_frame, text = "Titulo")
        self.title_label.pack(side = LEFT)
        self.title_entry = Entry(self.title_frame)
        self.title_entry.pack(side = LEFT)

        self.category_frame = Frame(self.master)
        self.category_frame.pack()
        self.category_label = Label(self.category_frame, text = "Categoria")
        self.category_label.pack(side = LEFT)
        self.category_entry = Entry(self.category_frame)
        self.category_entry.pack(side = LEFT)

        self.description_frame = Frame(self.master)
        self.description_frame.pack()
        self.description_label = Label(self.description_frame, text = "Descrição")
        self.description_label.pack(side = LEFT)
        self.description_entry = Entry(self.description_frame)
        self.description_entry.pack(side = LEFT)

        self.name_frame = Frame(self.master)
        self.name_frame.pack()
        self.name_label = Label(self.name_frame, text = "Nome")
        self.name_label.pack(side = LEFT)
        self.name_entry = Entry(self.name_frame)
        self.name_entry.pack(side = LEFT)

        self.image_frame = Frame(self.master)
        self.image_frame.pack()
        self.image_label = Label(self.image_frame, text = "file_image")
        self.image_label.pack(side = LEFT)
        self.image_entry = Entry(self.image_frame)
        self.image_entry.pack(side = LEFT)

        self.button_post_frame = Frame(self.master)
        self.button_post_frame.pack()
        self.button_post = Button(self.button_post_frame, text = "Postar")
        self.button_post["command"] = self.posting
        self.button_post.pack()

        self.button_frame = Frame(self.master)
        self.button_frame.pack()
        self.button_size = Button(self.button_frame, text = "redefinir imagem")
        self.button_size["command"] = self.open_link
        self.button_size.pack()
        

        self.button_import = Button(self.button_frame, text = "Importar imagem")
        self.button_import ["command"] = self.import_image
        self.button_import .pack()
    
    def open_link(self):
        link = "https://www.befunky.com/pt/criar/editor-de-fotos/"
        webbrowser.open(link)
    

    def posting(self):
        self.title = self.title_entry.get()
        self.category = self.category_entry.get()
        self.description = self.description_entry.get()
        self.name = self.name_entry.get()
        self.file_image = self.image_entry.get()

        self.open_post()


    def open_post(self):
        root = Tk()
        posts = Post(root, self.title, self.category, self.file_image, self.description, self.name)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    posts = Post_register(root)
    root.mainloop()