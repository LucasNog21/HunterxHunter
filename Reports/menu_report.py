from tkinter import *
from Reports.Register_report import Report_register
from Reports.report import Report
from Subjects.menu import Menu
import pickle

class Menu_report(Menu):
    def __init__(self, master):
        super().__init__(master)
        self.file_name = "Pickle_files\list_reports.txt"
        self.list = []
        self.generate = False

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
        self.button_open_reports["command"] = lambda o=Report_register: self.open_file(o)
        self.button_open_reports.pack(side = "right")


    def button_generate(self):
        if self.generate == False:
            for report in self.list:
                self.button_frame = Frame(self.master)
                self.button_frame.pack()

                self.button = Button(self.button_frame, text=report.title, command=lambda r=report: self.open_report(r))
                self.button.pack(side="left")
        self.generate = True

    def open_report(self,report):
        root = Tk()
        Report(root,report.title, report.category, report.description, report.get_name())

    def exibition_report(self):
        self.update_register()
        self.button_generate() 

if __name__ == "__main__":
    root = Tk()
    Menu_report(root)
    root.mainloop()