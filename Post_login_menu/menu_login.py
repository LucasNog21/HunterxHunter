from tkinter import *
from tkinter import messagebox
from Post_login_menu.register_treath import Treath_register
from User_menu.register_user import Register
import pickle

class Menu_login:
    def __init__(self, mestre, user_name):
        self.mestre = mestre
        self.user_name = user_name
        self.file_name = "Pickle_files\list_register.txt"
        self.file_name_treaths = "Pickle_files\list_treaths.txt"
        self.list_users = []
        self.list_treaths = []
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
        self.botao["command"] = self.exibition_users
        self.botao.pack()

        self.c3 = Frame(self.mestre)
        self.c3.pack()
        self.botao = Button(self.c3, text = "Registrar ameaças")
        self.botao["command"] = self.abrir_registro_ameaça
        self.botao.pack()

        self.c4 = Frame(self.mestre)
        self.c4.pack()
        self.botao = Button(self.c4, text = "Exibir ameaças")
        self.botao["command"] = self.exibition_treaths
        self.botao.pack()

        self.c5 = Frame(self.mestre)
        self.c5.pack()
        self.botao = Button(self.c5, text = "Mudar registro")
        self.botao["command"] = self.change_register
        self.botao.pack()


    def exibition_users(self):
        with open(self.file_name, 'rb') as file: 
            while True:
                try:
                    self.list_users = pickle.load(file)

                except EOFError:
                    break

        exibition = ''
        for user in self.list_users:
            if user and hasattr(user, 'username'):
                exibition += user.username + '\n'

    
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

    def exibition_treaths(self):
        with open(self.file_name_treaths, 'rb') as file: 
            while True:
                try:
                    self.list_treaths = pickle.load(file)

                except EOFError:
                    break
                
        exibition = ''
        for treath in self.list_treaths:
            if treath and hasattr(treath, 'specie'):
                exibition += treath.specie + '\n'

    
        self.top = Toplevel()
        self.top.title("Ameaças")

        self.widget1 = Frame(self.top)
        self.widget1["padx"] = 100
        self.widget1["pady"] = 10
        self.widget1.pack()
        self.msg = Label(self.widget1, text= exibition)
        self.msg.pack()
    
    def change_register(self):
        raiz_registro = Tk()
        Register(raiz_registro, True, self.user_name)
        raiz_registro.mainloop()



if __name__ == "__main__":
    raiz = Tk()
    Menu_login(raiz)
    raiz.mainloop()