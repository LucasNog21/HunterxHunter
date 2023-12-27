from tkinter import *
import pickle

class Menu:
    def __init__(self, master):
        self.master = master
        self.list = []

    def update_register(self):
        self.list = []
        with open(self.file_name, 'rb') as file:
            while True:
                try:
                    self.list = pickle.load(file)

                except EOFError:
                    break

    def open_window(self, exibition):
        self.top = Toplevel()
        self.top.title("Dados do arquivo")

        self.widget1 = Frame(self.top)
        self.widget1["padx"] = 100
        self.widget1["pady"] = 10
        self.widget1.pack()
        self.msg = Label(self.widget1, text= exibition)
        self.msg.pack()
    
    def open_file(self, obj):
        self.master = Tk()
        obj(self.master)
        self.master.mainloop()

if __name__ == "__main__":
    root = Tk()
    Menu(root)
    root.mainloop()



