from tkinter import *
from tkinter import messagebox
from Reports.Register_report import Report_register
import pickle

class Menu_report:
    def __init__(self, master):
        self.master = master
        self.file_name = "Pickle_files\list_reports.txt"
        self.list_reports = []

        self.window = Frame(self.master)
        self.window["padx"] = 100
        self.window["pady"] = 10
        self.window.pack()

        self.title = Label(self.window, text = "Menu de relatos")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.button_frame_1 = Frame(self.master)
        self.button_frame_1.pack()

        self.button_exibition = Button(self.button_frame_1, text = "Exibir relatos")
        self.button_exibition["command"] = self.exibition_report
        self.button_exibition.pack(side = "left")

        self.button_open_reports = Button(self.button_frame_1, text = "Registrar relatos")
        self.button_open_reports["command"] = self.open_register_report
        self.button_open_reports.pack(side = "right")

    

if __name__ == "__main__":
    root = Tk()
    Menu_report(root)
    root.mainloop()