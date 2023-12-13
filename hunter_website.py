from tkinter import *
from Subjects.abstract_window import Window
from User_menu.register_user import Register
from Subjects.menu import Menu

if __name__ == "__main__":
    raiz = Tk()
    Hunter_website = Menu(raiz, "Hunter Website", 0, 0, 1, "Registrar")
    raiz.mainloop()