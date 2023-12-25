from tkinter import *
from tkinter import messagebox
from Post_login_menu.register_treath import Treath_register
from Post_login_menu.user_page import User_page
from Reports.menu_report import Menu_report
from Subjects.menu import Menu
import pickle

class Menu_login(Menu):
    def __init__(self, master, user_name):
        super().__init__(master)
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
        self.button_open_users["command"] = lambda o=Treath_register: self.open_file(o)
        self.button_open_users.pack(side = "right")

        self.button_frame_2 = Frame(self.master)
        self.button_frame_2.pack()
        self.button_exibition_treaths = Button(self.button_frame_2, text = "Exibir ameaças")
        self.button_exibition_treaths["command"] = self.exibition_treaths
        self.button_exibition_treaths.pack(side = "left")

        self.button_post_register = Button(self.button_frame_2, text = "Página de usuário")
        self.button_post_register["command"] = self.open_user_page
        self.button_post_register.pack(side = "right")

        self.button_frame_3 = Frame(self.master)
        self.button_frame_3.pack()
        self.button_report_treaths = Button(self.button_frame_3, text = "Menu de relatos")
        self.button_report_treaths["command"] = lambda o=Menu_report: self.open_file(o)
        self.button_report_treaths.pack(side = "left")

    def open_user_page(self):
        user_root = Tk()
        User_page(user_root, self.user_name)
        user_root.mainloop()

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
                exibition += "Usuário"+str(self.list_users.index(user)+1) + '\n' "Nome: " + user.name + '\n' " Usuário: " + user.username + '\n' " Categoria: " + user.category + '\n' " Data do exame: " + user.hunter_exam_date + '\n\n'

        self.open_window(exibition)

    def exibition_treaths(self):
        with open(self.file_name_treaths, 'rb') as file: 
            while True:
                try:
                    self.list_treaths = pickle.load(file)

                except EOFError:
                    break
                
        exibition = ''
        for treath in self.list_treaths:
            if treath and hasattr(treath, 'name'):
                exibition += "Ameaça"+str(self.list_treaths.index(treath)+1) + '\n' +"Nome: " + treath.name + '\n' + "Espécie:" + treath.specie + '\n' " Nível: "+ treath.get_level()  + '\n\n'

        self.open_window(exibition)
    
if __name__ == "__main__":
    root = Tk()
    Menu_login(root)
    root.mainloop()