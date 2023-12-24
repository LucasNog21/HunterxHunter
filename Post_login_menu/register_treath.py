from tkinter import *
from tkinter import messagebox
from Subjects.treath import Treath
from Subjects.register import Register
import pickle

class Treath_register(Register):
    def __init__(self, master):
        super().__init__(master)
        self.file_name = "Pickle_files\list_treaths.txt"
        self.list = []
        self.window = Frame(self.master)
        self.window["padx"] = 100
        self.window["pady"] = 10
        self.window.pack()

        self.title = Label(self.window, text = "Registro de ameaça")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.name_frame = Frame(self.master)
        self.name_frame.pack()
        self.name_label = Label(self.name_frame, text = "nome da ameaça")
        self.name_label.pack(side = LEFT)
        self.name_entry = Entry(self.name_frame)
        self.name_entry.pack(side = LEFT)

        self.specie_frame = Frame(self.master)
        self.specie_frame.pack()
        self.specie_label = Label(self.specie_frame, text = "Espécie da ameaça")
        self.specie_label.pack(side = LEFT)
        self.specie_entry = Entry(self.specie_frame)
        self.specie_entry.pack(side = LEFT)

        self.level_frame = Frame(self.master)
        self.level_frame.pack()
        self.level_label = Label(self.level_frame, text = "Nível da ameaça")
        self.level_label.pack(side = LEFT)
        self.level_entry = Entry(self.level_frame)
        self.level_entry.pack(side = LEFT)

        self.button_frame = Frame(self.master)
        self.button_frame.pack()
        self.button_register = Button(self.button_frame, text = "Registrar")
        self.button_register["command"] = self.autenticate
        self.button_register.pack()
    
    def autenticate(self):
        self.name = self.name_entry.get()
        self.specie = self.specie_entry.get()
        self.level = self.level_entry.get()
        self.name_in = False    

        self.update_register()

        if self.verify_register() == False:

            try:
                self.register()
                messagebox.showinfo("Sucesso","ameaça registrada.")
                self.master.destroy()
            except FileNotFoundError:
                messagebox.showinfo("Arquivo inexistente",f"O arquivo {self.file_name} não foi encontrado.")
        
        else: 
            messagebox.showinfo("Falha", "Registro de ameaça já existente")


    def register(self):
        with open(self.file_name, 'wb') as file:
            treath = Treath(self.name, self.specie, self.level)
            self.list.append(treath)
            pickle.dump(self.list, file)
            file.close()
    

    def verify_register(self):

        if not self.list == []:
            for treath in self.list:
                if treath.name == self.name:
                    self.name_in = True
                    return treath
            else:
                return False
        else:
            return False
        
if __name__ == "__main__":
    root = Tk()
    Treath_register(root)
    root.mainloop()