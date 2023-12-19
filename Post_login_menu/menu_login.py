from tkinter import *
from tkinter import messagebox
from Post_login_menu.register_treath import Treath_register
from User_menu.register_user import Register
from Posts.post_register import Post_register
import pickle

class Menu_login:
    def __init__(self, master, user_name):
        self.master = master
        self.user_name = user_name
        self.file_name = "Pickle_files\list_register.txt"
        self.file_name_treaths = "Pickle_files\list_treaths.txt"
        self.list_users = []
        self.list_treaths = []
        self.window = Frame(self.master)
        self.window["padx"] = 100
        self.window["pady"] = 10
        self.window.pack()

        self.title = Label(self.window, text = "Menu de autenticados")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.button_frame_1 = Frame(self.master)
        self.button_frame_1.pack()

        self.button_exibition = Button(self.button_frame_1, text = "Exibir registros")
        self.button_exibition["command"] = self.exibition_users
        self.button_exibition.pack(side = "left")

        self.button_open_users = Button(self.button_frame_1, text = "Registrar ameaças")
        self.button_open_users["command"] = self.open_treath_register
        self.button_open_users.pack(side = "right")

        self.button_frame_2 = Frame(self.master)
        self.button_frame_2.pack()
        self.button_exibition_treaths = Button(self.button_frame_2, text = "Exibir ameaças")
        self.button_exibition_treaths["command"] = self.exibition_treaths
        self.button_exibition_treaths.pack(side = "left")

        self.button_change_register = Button(self.button_frame_2, text = "Mudar registro")
        self.button_change_register["command"] = self.change_register
        self.button_change_register.pack(side ="right")

        self.button_frame_3 = Frame(self.master)
        self.button_frame_3.pack()
        self.button_post_register = Button(self.button_frame_3, text = "Post")
        self.button_post_register["command"] = self.open_post_register
        self.button_post_register.pack()

    def open_post_register(self):
        register_root = Tk()
        Post_register(register_root)
        register_root.mainloop()


    def exibition_users(self):
        with open(self.file_name, 'rb') as file: 
            while True:
                try:
                    self.list_users = pickle.load(file)

                except EOFError:
                    break

        exibition = ''
        for user in self.list_users:
            if user and hasattr(user, 'username'):
                exibition += user.username + '\n'

    
        self.top = Toplevel()
        self.top.title("Dados do arquivo")

        self.widget1 = Frame(self.top)
        self.widget1["padx"] = 100
        self.widget1["pady"] = 10
        self.widget1.pack()
        self.msg = Label(self.widget1, text= exibition)
        self.msg.pack()

    def open_treath_register(self):
        register_root = Tk()
        Treath_register(register_root)
        register_root.mainloop()

    def exibition_treaths(self):
        with open(self.file_name_treaths, 'rb') as file: 
            while True:
                try:
                    self.list_treaths = pickle.load(file)

                except EOFError:
                    break
                
        exibition = ''
        for treath in self.list_treaths:
            if treath and hasattr(treath, 'specie'):
                exibition += treath.specie + '\n'

    
        self.top = Toplevel()
        self.top.title("Ameaças")

        self.widget1 = Frame(self.top)
        self.widget1["padx"] = 100
        self.widget1["pady"] = 10
        self.widget1.pack()
        self.msg = Label(self.widget1, text= exibition)
        self.msg.pack()
    
    def change_register(self):
        register_root = Tk()
        Register(register_root, True, self.user_name)
        register_root.mainloop()



if __name__ == "__main__":
    root = Tk()
    Menu_login(root)
    root.mainloop()