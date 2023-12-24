from tkinter import *
from tkinter import messagebox
from Subjects.user import User
import pickle

class Register_user:
    def __init__(self, master, change, user_name, delete):

        self.master = master
        self.change = change
        self.user_name = user_name
        self.delete = delete
        self.list_users = []
        self.file_name = "Pickle_files\list_register.txt"

        if self.delete:
            self.verify_delete()

        else:

            self.window = Frame(self.master)
            self.window["padx"] = 100
            self.window["pady"] = 10
            self.window.pack()

            self.title = Label(self.window, text = "Registro")
            self.title["font"] = ("Arial", "10", "bold")
            self.title.pack()

            self.user_frame = Frame(self.master)
            self.user_frame.pack()
            self.user_label = Label(self.user_frame, text = "nome de usuario")
            self.user_label.pack(side = LEFT)
            self.user_entry = Entry(self.user_frame)
            self.user_entry.pack(side = LEFT)

            self.password_frame = Frame(self.master)
            self.password_frame.pack()
            self.password_label = Label(self.password_frame, text = "senha")
            self.password_label.pack(side = LEFT)
            self.password_entry = Entry(self.password_frame)
            self.password_entry.pack(side = LEFT)

            self.hunter_date_frame = Frame(self.master)
            self.hunter_date_frame.pack()
            self.hunter_date_label = Label(self.hunter_date_frame, text = "Data do exame hunter")
            self.hunter_date_label.pack(side = LEFT)
            self.hunter_date_entry = Entry(self.hunter_date_frame)
            self.hunter_date_entry.pack(side = LEFT)

            self.category_frame = Frame(self.master)
            self.category_frame.pack()
            self.category_label = Label(self.category_frame, text = "Categoria")
            self.category_label.pack(side = LEFT)
            self.category_entry= Entry(self.category_frame)
            self.category_entry.pack(side = LEFT)

            self.name_frame = Frame(self.master)
            self.name_frame.pack()
            self.name_label = Label(self.name_frame, text = "Nome")
            self.name_label.pack(side = LEFT)
            self.name_entry = Entry(self.name_frame)
            self.name_entry.pack(side = LEFT)

            self.date_frame = Frame(self.master)
            self.date_frame.pack()
            self.date_label = Label(self.date_frame, text = "Data de nascimento")
            self.date_label.pack(side = LEFT)
            self.date_entry = Entry(self.date_frame)
            self.date_entry.pack(side = LEFT)


            self.button_frame = Frame(self.master)
            self.button_frame.pack()
            self.button = Button(self.button_frame, text = "Autenticar")
            self.button["command"] = self.autenticate
            self.button.pack()



    def autenticate(self):
        self.username_in = False

        self.username = self.user_entry.get()
        self.password = self.password_entry.get()
        self.hunter_exam_date = self.hunter_date_entry.get()
        self.category = self.category_entry.get()
        self.name = self.name_entry.get()
        self.birth_date = self.date_entry.get()

        self.update_register()

        if self.change:
            self.delete_register()

        if self.verify_register() == False:

            try:
                self.register()
                messagebox.showinfo("Sucesso","Registro autenticado.")
                self.master.destroy()
            except FileNotFoundError:
                messagebox.showinfo("Arquivo inexistente",f"O arquivo {self.file_name} não foi encontrado.")

        else:
            messagebox.showinfo("Erro de autenticação", "nome de usuário já presente no arquivo")


    def verify_delete(self):
        self.master.destroy()
        self.delete_register()
        messagebox.showinfo("Uma pena","Conta deletada.")


    def register(self):
    
        with open(self.file_name, 'wb') as file:
            new_user = User(self.username, self.password, self.hunter_exam_date, self.category, self.name, self.birth_date)
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
        messagebox.showinfo("Registro deletado",f"Registro deletado com sucesso")
        with open(self.file_name, 'rb') as file:
            self.list_users = pickle.load(file)

        self.list_users = [user for user in self.list_users if user.username != self.user_name]

        with open(self.file_name, 'wb') as file:
            pickle.dump(self.list_users, file)
        self.master.destroy()



if __name__ == "__main__":
    raiz = Tk()
    Register_user(raiz)
    raiz.mainloop()