from tkinter import *
from User_menu.register_user import Register
from User_menu.login import Login

class Website:
    def __init__(self,mestre):
        self.mestre = mestre
        self.c1 = Frame(self.mestre)
        self.c1["padx"] = 100
        self.c1["pady"] = 10
        self.c1.pack()

        self.titulo = Label(self.c1, text = "Bem vindo ao Hunter Website\n ")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.c2 = Frame(self.mestre)
        self.c2.pack()
        self.botao_registro = Button(self.c2, text = "Registro")
        self.botao_registro["command"] = self.abrir_registro
        self.botao_registro.pack()

        self.c3 = Frame(self.mestre)
        self.c3.pack()
        self.botao_login = Button(self.c3, text = "Login")
        self.botao_login["command"] = self.abrir_login
        self.botao_login.pack()


    def abrir_registro(self):
        raiz_registro = Tk()
        Register(raiz_registro, False, None)
        raiz_registro.mainloop()

    def abrir_login(self):
        raiz_login = Tk()
        Login(raiz_login)
        raiz_login.mainloop()

if __name__ == "__main__":
    raiz = Tk()
    Website(raiz)
    raiz.mainloop()