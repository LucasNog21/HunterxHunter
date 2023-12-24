from tkinter import *
from tkinter import messagebox
import pickle

class Register:
    def __init__(self,master):
        self.master = master
        self.list = []
        self.file_name = ""
    
    def autenticate(self):
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
            instance = ''
            self.list.append(instance)
            pickle.dump(self.list, file)
            file.close()

    def update_register(self):
        self.list = []
        with open(self.file_name, 'rb') as file:
            while True:
                try:
                    self.list = pickle.load(file)

                except EOFError:
                    break

    def verify_register(self):

        if not self.list == []:
            for object in self.list:
                if object.atributte == self.atributte:
                    self.atributte_in = True
                    return object
            else:
                return False
        else:
            return False
    
    def delete_register(self):
        messagebox.showinfo("Registro deletado",f"Registro deletado com sucesso")
        with open(self.file_name, 'rb') as file:
            self.list = pickle.load(file)

        self.list = [obj for obj in self.list if object.atributte != self.user_name]

        with open(self.file_name, 'wb') as file:
            pickle.dump(self.list, file)
        self.master.destroy()