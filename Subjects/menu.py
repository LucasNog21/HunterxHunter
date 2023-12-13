from tkinter import *
import pickle

def printar():
    print("DEU CERTO")

def printar_agradecidamente():
    print("OBRIGAADOOOOOOOOOOOOOOOOOOOOOO")
class Menu:
    def __init__(self, mestre, title, button_quant, button_names, button_func):
        self.title = title
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

        for buttons in range(self.button_quant):

            self.c0 = Frame(self.mestre)
            self.c0.pack()
            self.botao = Button(self.c0, text = button_names[buttons])
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
    

if __name__ == "__main__":
    raiz = Tk()
    Menu(raiz,'teste',2,['Botao 1', 'Botao 2'], [printar, printar_agradecidamente])
    raiz.mainloop()
