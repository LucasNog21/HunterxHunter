from tkinter import *
from tkinter import messagebox
from Subjects.user import User
import pickle

class Register:
    def __init__(self, mestre, change, user_name):
        self.mestre = mestre
        self.change = change
        self.user_name = user_name
        self.list_users = []
        self.file_name = "HunterxHunter\Pickle_files\list_register.txt"
        self.c1 = Frame(self.mestre)
        self.c1["padx"] = 100
        self.c1["pady"] = 10
        self.c1.pack()

        self.titulo = Label(self.c1, text = "Registro")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.c2 = Frame(self.mestre)
        self.c2.pack()
        self.t2 = Label(self.c2, text = "nome de usuario")
        self.t2.pack(side = LEFT)
        self.l2 = Entry(self.c2)
        self.l2.pack(side = LEFT)

        self.c3 = Frame(self.mestre)
        self.c3.pack()
        self.t3 = Label(self.c3, text = "senha")
        self.t3.pack(side = LEFT)
        self.l3 = Entry(self.c3)
        self.l3.pack(side = LEFT)

        self.c4 = Frame(self.mestre)
        self.c4.pack()
        self.t4 = Label(self.c4, text = "Data do exame hunter")
        self.t4.pack(side = LEFT)
        self.l4 = Entry(self.c4)
        self.l4.pack(side = LEFT)

        self.c5 = Frame(self.mestre)
        self.c5.pack()
        self.t5 = Label(self.c5, text = "Categoria")
        self.t5.pack(side = LEFT)
        self.l5 = Entry(self.c5)
        self.l5.pack(side = LEFT)

        self.c6 = Frame(self.mestre)
        self.c6.pack()
        self.t6 = Label(self.c6, text = "Nome")
        self.t6.pack(side = LEFT)
        self.l6 = Entry(self.c6)
        self.l6.pack(side = LEFT)

        self.c7 = Frame(self.mestre)
        self.c7.pack()
        self.t7 = Label(self.c7, text = "Data de nascimento")
        self.t7.pack(side = LEFT)
        self.l7 = Entry(self.c7)
        self.l7.pack(side = LEFT)


        self.c4 = Frame(self.mestre)
        self.c4.pack()
        self.botao = Button(self.c4, text = "Autenticar")
        self.botao["command"] = self.autenticar
        self.botao.pack()
    
    

    def autenticar(self):
        self.username_in = False
        self.username = self.l2.get()
        self.password = self.l3.get()
        self.hunter_exam_date = self.l4.get()
        self.category = self.l5.get()
        self.name = self.l6.get()
        self.birth_date = self.l7.get()

        self.update_register()

        if self.change:
            print("Chegou aqui")  
            self.delete_register()

    
        if self.verify_register() == False:

            try:
                self.registrar(self.username, self.password, self.hunter_exam_date, self.category, self.name, self.birth_date)
                messagebox.showinfo("Sucesso","Registro autenticado.")
            except FileNotFoundError:
                messagebox.showinfo("Arquivo inexistente",f"O arquivo {self.file_name} não foi encontrado.")

        else:
            messagebox.showinfo("Erro de autenticação", "nome de usuário já presente no arquivo")


    def registrar(self, username, password, hunter_exam_date, category, name, birth_date):
       
        with open(self.file_name, 'wb') as file:
            new_user = User(username, password, hunter_exam_date, category, name, birth_date )
            self.list_users.append(new_user)
            pickle.dump(self.list_users, file)
            file.close()

    def update_register(self):
         self.list_users = []
         with open(self.file_name, 'rb') as file:
            while True:
                try:
                    self.list_users = pickle.load(file)

                except EOFError:
                    break

    def verify_register(self):

        if not self.list_users == []:
            for user in self.list_users:
                if user.username == self.username:
                    self.username_in = True
                    return user
            else:
                return False
        else:
            return False
    
    def delete_register(self):
        with open(self.file_name, 'rb') as file:
            self.list_users = pickle.load(file)

        self.list_users = [user for user in self.list_users if user.username != self.user_name]

        with open(self.file_name, 'wb') as file:
            pickle.dump(self.list_users, file)



if __name__ == "__main__":
    raiz = Tk()
    Register(raiz)
    raiz.mainloop()