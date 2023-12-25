from tkinter import *
from User_menu.register_user import Register_user
from Subjects.menu import Menu
from User_menu.login import Login

class Website(Menu):
    def __init__(self,master):
        super().__init__(master)
        self.master.title("HunterxHunter")
        self.window = Frame(self.master, background = "#D8EEEB")
        self.window["padx"] = 100
        self.window["pady"] = 10
        self.window.pack()

        self.title = Label(self.window, text = "Bem vindo ao Hunter Website\n ", background = "#D8EEEB")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.button_frame = Frame(self.master, background = "#D8EEEB")
        self.button_frame.config(bg = "#D8EEEB")
        self.button_frame.pack()

        self.register_button = Button(self.button_frame, text = "Registro", background = "gray")
        self.register_button["command"] = self.open_register
        self.register_button.pack(side = "left", padx = 30)

        self.login_button = Button(self.button_frame, text = "Login", background = "gray")
        self.login_button["command"] = lambda o=Login: self.open_file(o)
        self.login_button.pack(side = "right", padx = 30)


    def open_register(self):
        self.master = Tk()
        Register_user(self.master, False, None, False)
        self.master.mainloop()


if __name__ == "__main__":
    root = Tk()
    Website(root)
    root.mainloop()