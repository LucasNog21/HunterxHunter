from tkinter import *
from tkinter import messagebox
from Post_login_menu.menu_login import Menu_login
import pickle

class Login:
    def __init__(self, master):
        self.master = master
        self.file_name = "Pickle_files\list_register.txt"
        self.list_users = []
        self.window = Frame(self.master)
        self.window["padx"] = 100
        self.window["pady"] = 10
        self.window.pack()

        self.title = Label(self.window, text = "Login")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.user_frame = Frame(self.master)
        self.user_frame.pack()
        self.user_label = Label(self.user_frame, text = "nome de usuario")
        self.user_label.pack(side = LEFT)
        self.user_entry = Entry(self.user_frame)
        self.user_entry.pack(side = LEFT)

        self.password_frame = Frame(self.master)
        self.password_frame.pack()
        self.password_label = Label(self.password_frame, text = "senha")
        self.password_label.pack(side = LEFT)
        self.password_entry = Entry(self.password_frame)
        self.password_entry.pack(side = LEFT)

        self.button_frame = Frame(self.master)
        self.button_frame.pack()
        self.button = Button(self.button_frame, text = "Autenticar")
        self.button["command"] = self.login
        self.button.pack()

    def login(self):
        self.username = self.user_entry.get()
        self.password = self.password_entry.get()
        self.username_in = False
        self.password_in = False
        
        self.update_read()
        self.verify_login()
                    
        if self.username_in and self.password_in:

            messagebox.showinfo("Sucesso","Seu login foi um sucesso")
            self.mestre.destroy()
            menu_login_root = Tk()
            Menu_login(menu_login_root, self.username)
            menu_login_root.mainloop()
        else:
            messagebox.showinfo("Falha no login","Usuário e/ou senha não presente(s) no arquivo. Tente novamente")
    
    def update_read(self):
        with open(self.file_name, 'rb') as file: 
            while True:
                try:
                    self.list_users = pickle.load(file)

                except EOFError:
                    break
        

    def verify_login(self):
        for user in self.list_users:
                if user.username == self.username:
                    self.username_in = True
                    if user.get_password() == self.password:
                        self.password_in = True


if __name__ == "__main__":
    root = Tk()
    Login(root)
    root.mainloop()