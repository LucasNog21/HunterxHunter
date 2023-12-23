from tkinter import *

class Report:
    def __init__(self, master ,title, category, description, name):
        self.master = master
        self.title = title
        self.category = category
        self.description = description
        self.name = name
        

        self.master.title("Relato")
        self.window = Frame(self.master)
        self.window["padx"] = 50
        self.window["pady"] = 10
        self.window.pack() 

        self.title_frame = Frame(self.window)
        self.title_frame.pack()
        self.title = Label(self.window, text = self.title)
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.top_frame = Frame(self.window)
        self.top_frame.pack()
        self.category_label = Label(self.top_frame, text = "Categoria: "+self.category, padx = 30)
        self.category_label.pack(side = LEFT)

        self.name_label = Label(self.top_frame, text ="Autor: "+self.name, padx = 30)
        self.name_label.pack(side = RIGHT)


        self.description_frame = Frame(self.window)
        self.description_frame.pack()

        self.text_label = Label(self.description_frame, text = self.description, width = 50, wraplength = 250, justify = "center")
        self.text_label.pack()
 


if __name__ == "__main__":
    root = Tk()
    Report(root, "Teste", "Desabafo", "Sei la qualquer coisa eu nao sei o que escrever esse é so um teste para ver como vai funcionar o negocio de mudar. Estou fazendo esse projeto de noite muito muito tarde e pelo menos ta um pouco bonito. fé", "Lucas")
    root.mainloop()
