from tkinter import *
from tkinter import messagebox
from Post_login_menu.register_treath import Treath_register

import pickle

class Menu_login:
    def __init__(self, mestre):
        self.mestre = mestre
        self.file_name = "Pickle_files\list_register.txt"
        self.file_name_treaths = "Pickle_files\list_treaths.txt"
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

        self.c3 = Frame(self.mestre)
        self.c3.pack()
        self.botao = Button(self.c3, text = "Registrar ameaças")
        self.botao["command"] = self.abrir_registro_ameaça
        self.botao.pack()

        self.c4 = Frame(self.mestre)
        self.c4.pack()
        self.botao = Button(self.c4, text = "Exibir ameaças")
        self.botao["command"] = self.exibir_ameaças
        self.botao.pack()


    def exibir_registros(self):
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

    def abrir_registro_ameaça(self):
        raiz_registro = Tk()
        Treath_register(raiz_registro)
        raiz_registro.mainloop()

    def exibir_ameaças(self):
        with open(self.file_name_treaths, 'rb') as file: 
            list_treaths = []
            while True:
                try:
                    treath = pickle.load(file)
                    list_treaths.append(treath)

                except EOFError:
                    break
                
        exibition = ''
        for treath in list_treaths:
            if treath and hasattr(treath, 'specie'):
                exibition += treath.specie + " nivel " + treath.get_level() +'\n'

    
        self.top = Toplevel()
        self.top.title("Ameaças")

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