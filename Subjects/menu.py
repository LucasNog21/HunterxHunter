from tkinter import *
from Subjects.abstract_window import Window
from User_menu.register_user import Register


class Menu(Window):
    def __init__(self, mestre, title, label_quants, label_names, button_quant, button_names):
        super().__init__(mestre, title, label_quants, label_names, button_quant, button_names)

        self.buttons_generate(self.open_file(Register))


if __name__ == "__main__":
    raiz = Tk()
    Menu(raiz, "Hunter Website", 0, 0, 1, "Registrar")
    raiz.mainloop()
