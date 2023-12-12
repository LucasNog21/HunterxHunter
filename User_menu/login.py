from tkinter import *
from tkinter import messagebox
from Post_login_menu.menu_login import Menu_login
import pickle

class Login:
    def __init__(self, mestre):
        self.mestre = mestre
        self.file_name = "Pickle_files\list_register.txt"
        self.c1 = Frame(self.mestre)
        self.c1["padx"] = 100
        self.c1["pady"] = 10
        self.c1.pack()

        self.titulo = Label(self.c1, text = "Login")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.c2 = Frame(self.mestre)
        self.c2.pack()
        self.t2 = Label(self.c2, text = "Nome de usuario")
        self.t2.pack(side = LEFT)
        self.l2 = Entry(self.c2)
        self.l2.pack(side = LEFT)

        self.c3 = Frame(self.mestre)
        self.c3.pack()
        self.t3 = Label(self.c3, text = "Senha")
        self.t3.pack(side = LEFT)
        self.l3 = Entry(self.c3)
        self.l3.pack(side = LEFT)

        self.c4 = Frame(self.mestre)
        self.c4.pack()
        self.botao = Button(self.c4, text = "Autenticar")
        self.botao["command"] = self.logar
        self.botao.pack()

    def logar(self):
        self.username = self.l2.get()
        self.password = self.l3.get()
        self.username_in = False
        self.password_in = False

        with open(self.file_name, 'rb') as file: 
            list_users = []
            while True:
                try:
                    user = pickle.load(file)
                    list_users.append(user)

                except EOFError:
                    break
        
            for user in list_users:
                if user.username == self.username:
                    self.username_in = True
                    if user.get_password() == self.password:
                        self.password_in = True

            if self.username_in and self.password_in:

                messagebox.showinfo("Sucesso","Seu login foi um sucesso")
                self.mestre.destroy()
                raiz_menu_login = Tk()
                Menu_login(raiz_menu_login)
                raiz_menu_login.mainloop()
            else:
                messagebox.showinfo("Falha no login","Usuário e/ou senha não presente(s) no arquivo. Tente novamente")

def abrir_menu(self):
        raiz_menu = Tk()
        Menu_login(raiz_menu, self.username, self.password)
        raiz_menu.mainloop()


if __name__ == "__main__":
    raiz = Tk()
    Login(raiz)
    raiz.mainloop()