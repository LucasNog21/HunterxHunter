from tkinter import *

class Menu:
    def __init__(self):
        self.file_name = "Pickle_files\list_register.txt"
        self.file_name_treaths = "Pickle_files\list_treaths.txt"
        self.list_users = []
        self.list_treaths = []
    
    def open_file(self,Object):
        raiz = Tk()
        Object(raiz)
        raiz.mainloop()

    def update_file(self):
        pass

