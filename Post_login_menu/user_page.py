from calendar import c
from tkinter import *
from User_menu.register_user import Register

class User_page:
    def __init__(self, master, user_name):
        self.master = master
        self.user_name = user_name
        self.master.title("Página de usuário")
        self.window = Frame(self.master, background = "#D8EEEB")
        self.window["padx"] = 100
        self.window["pady"] = 10
        self.window.pack()

        self.title = Label(self.window, text = "Usuário\n ", background = "#D8EEEB")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.button_frame_1 = Frame(self.master)
        self.button_frame_1.pack()

        self.button_change_register = Button(self.button_frame_1, text = "Mudar registro")
        self.button_change_register["command"] = self.change_register
        self.button_change_register.pack(side ="left")

        self.button_delete_register = Button(self.button_frame_1, text = "deletar registro")
        self.button_delete_register["command"] = self.delete_register
        self.button_delete_register.pack(side ="right")




    def delete_register(self):
        register_root = Tk()
        Register(register_root, False, self.user_name, True)
        register_root.mainloop()


    def change_register(self):
        register_root = Tk()
        Register(register_root, True, self.user_name, False)
        register_root.mainloop()