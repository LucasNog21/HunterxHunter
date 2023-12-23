from tkinter import *
from tkinter import messagebox
from Reports.Register_report import Report_register
from Reports.report import Report
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

        self.button_generate()

    def button_generate(self):
        for report in self.list_reports:
            self.button_frame = Frame(self.master)
            self.button_frame.pack()

            self.button = Button(self.button_frame, text=report.title, command=lambda r=report: self.open_report(r))
            self.button.pack(side="left")

    
    def open_report(self,report):
        root = Tk()
        Report(root,report.title, report.category, report.description, report.get_name())


    def open_register_report(self):
        root = Tk()
        Report_register(root)
        root.mainloop()

    def update_report(self):
        self.list_reports = []
        with open(self.file_name, 'rb') as file:
            while True:
                try:
                    self.list_reports = pickle.load(file)

                except EOFError:
                    break

    def exibition_report(self):
        self.update_report()
        self.button_generate() 

if __name__ == "__main__":
    root = Tk()
    Menu_report(root)
    root.mainloop()