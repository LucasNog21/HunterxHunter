from tkinter import *
import pickle
from User_menu.register_user import Register
from User_menu.login import Login

class Window:
    def __init__(self, mestre, title, label_quants, label_names, button_quant, button_names):
        self.title = title
        self.label_quants = label_quants
        self.label_names = label_names
        self.list_entrys = []
        self.button_quant = button_quant
        self.button_names = button_names
        self.file_name = "Pickle_files\list_register.txt"
        self.file_name_treaths = "Pickle_files\list_treaths.txt"
        self.list_users = []
        self.list_treaths = []

        self.mestre = mestre
        self.c1 = Frame(self.mestre)
        self.c1["padx"] = 100
        self.c1["pady"] = 10
        self.c1.pack()

        self.titulo = Label(self.c1, text = self.title)
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

    def label_generate(self):
        for labels in range(self.label_quants):
            self.c2 = Frame(self.mestre)
            self.c2.pack()
            self.t2 = Label(self.c2, text = self.label_names[labels])
            self.t2.pack(side = LEFT)
            self.l2 = Entry(self.c2)
            self.l2.pack(side = LEFT)
            self.entrys.append(self.l2)

    def autenticate(self):
        for entrys in self.list_entrys:
            self.label_names[entrys] = entrys



    def buttons_generate(self, button_func):
        for buttons in range(self.button_quant):

            self.c0 = Frame(self.mestre)
            self.c0.pack()
            self.botao = Button(self.c0, text = self.button_names[buttons])
            self.botao["command"] = button_func[buttons]
            self.botao.pack()
            
    def open_file(self,Object):
        raiz = Tk()
        Object(raiz)
        raiz.mainloop()

    def exibition(self,list_elements, title, attribute):
        with open(self.file_name, 'rb') as file: 
            while True:
                try:
                    list_elements = pickle.load(file)

                except EOFError:
                    break

        exibition = ''
        for element in list_elements:
            if element and hasattr(element, attribute):
                exibition += element.attribute + '\n'

    
        self.top = Toplevel()
        self.top.title(title)

        self.widget1 = Frame(self.top)
        self.widget1["padx"] = 100
        self.widget1["pady"] = 10
        self.widget1.pack()
        self.msg = Label(self.widget1, text= exibition)
        self.msg.pack()

if __name__ == '__main__':
    raiz = Tk()
    Janela = Window(raiz,0,0,0,0,0,0)
    Janela.mainloop()
    