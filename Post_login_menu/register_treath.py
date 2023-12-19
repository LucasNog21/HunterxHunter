from tkinter import *
from tkinter import messagebox
from Subjects.treath import Treath
import pickle

class Treath_register:
    def __init__(self, mestre):
        self.mestre = mestre
        self.file_name_treaths = "HunterxHunter\Pickle_files\list_treaths.txt"
        self.list_treaths = []
        self.c1 = Frame(self.mestre)
        self.c1["padx"] = 100
        self.c1["pady"] = 10
        self.c1.pack()

        self.titulo = Label(self.c1, text = "Registro de ameaça")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.c2 = Frame(self.mestre)
        self.c2.pack()
        self.t2 = Label(self.c2, text = "nome da ameaça")
        self.t2.pack(side = LEFT)
        self.l2 = Entry(self.c2)
        self.l2.pack(side = LEFT)

        self.c3 = Frame(self.mestre)
        self.c3.pack()
        self.t3 = Label(self.c3, text = "Espécie da ameaça")
        self.t3.pack(side = LEFT)
        self.l3 = Entry(self.c3)
        self.l3.pack(side = LEFT)

        self.c4 = Frame(self.mestre)
        self.c4.pack()
        self.t4 = Label(self.c4, text = "Nível da ameaça")
        self.t4.pack(side = LEFT)
        self.l4 = Entry(self.c4)
        self.l4.pack(side = LEFT)

        self.c5 = Frame(self.mestre)
        self.c5.pack()
        self.t5 = Label(self.c5, text = "Ameaça utiliza nen: S/N")
        self.t5.pack(side = LEFT)
        self.l5 = Entry(self.c5)
        self.l5.pack(side = LEFT)


        self.c4 = Frame(self.mestre)
        self.c4.pack()
        self.botao = Button(self.c4, text = "Registrar")
        self.botao["command"] = self.autenticar
        self.botao.pack()
    
    def autenticar(self):
        self.name = self.l2.get()
        self.specie = self.l3.get()
        self.level = self.l4.get()
        self.nen = self.l5.get()
        self.specie_in = False    

        self.update_register()
        self.verify_register()
        if self.verify_register() == False:

            try:
                self.registrar(self.file_name_treaths, self.specie, self.level)
                messagebox.showinfo("Sucesso","ameaça registrada.")
            except FileNotFoundError:
                messagebox.showinfo("Arquivo inexistente",f"O arquivo {self.file_name_treaths} não foi encontrado.")


    def registrar(self, file_name, specie, level):
        with open(file_name, 'wb') as file:
            treath = Treath(specie, level)
            self.list_treaths.append(treath)
            pickle.dump(self.list_treaths, file)
            file.close()
    

    def update_register(self):
        with open(self.file_name_treaths, 'rb') as file: 
            while True:
                try:
                    self.list_treaths = pickle.load(file)
    
                except EOFError:
                    break

    def verify_register(self):

        if not self.list_treaths == []:
            for treath in self.list_treaths:
                if treath.specie == self.specie:
                    self.specie_in = True
                    return treath
            else:
                return False
        else:
            return False
        
if __name__ == "__main__":
    raiz = Tk()
    Treath_register(raiz)
    raiz.mainloop()