from tkinter import *
from tkinter import messagebox
import pickle

class Menu_login:
    def __init__(self, mestre):
        self.mestre = mestre
        self.c1 = Frame(self.mestre)
        self.c1["padx"] = 100
        self.c1["pady"] = 10
        self.c1.pack()

        self.titulo = Label(self.c1, text = "Menu de autenticados")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.c2 = Frame(self.mestre)
        self.c2.pack()
        self.botao = Button(self.c2, text = "Exibir registros")
        self.botao["command"] = self.exibir_registros
        self.botao.pack()


    def exibir_registros(self):
        self.file_name = "HunterxHunter\list_register.txt"

        with open(self.file_name, 'rb') as file: 
            list_users = []
            while True:
                try:
                    user = pickle.load(file)
                    list_users.append(user)

                except EOFError:
                    break
                
        exibition = ''
        for user in list_users:
            if user and hasattr(user, 'name'):
                exibition += user.name + '\n'

    
        self.top = Toplevel()
        self.top.title("Dados do arquivo")

        self.widget1 = Frame(self.top)
        self.widget1["padx"] = 100
        self.widget1["pady"] = 10
        self.widget1.pack()
        self.msg = Label(self.widget1, text= exibition)
        self.msg.pack()

 

if __name__ == "__main__":
    raiz = Tk()
    Menu_login(raiz)
    raiz.mainloop()