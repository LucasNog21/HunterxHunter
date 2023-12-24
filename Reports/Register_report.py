from tkinter import *
from tkinter import messagebox
from Reports.data_report import Data_report
from Subjects.register import Register
import pickle

class Report_register(Register):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Post")
        self.list = []
        self.file_name = "Pickle_files\list_reports.txt"

        self.window = Frame(self.master)
        self.window["padx"] = 100
        self.window["pady"] = 10
        self.window.pack()

        self.title = Label(self.window, text = "Registro de relato")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.title_frame = Frame(self.master)
        self.title_frame.pack()
        self.title_label = Label(self.title_frame, text = "Titulo")
        self.title_label.pack(side = LEFT)
        self.title_entry = Entry(self.title_frame)
        self.title_entry.pack(side = LEFT)

        self.category_frame = Frame(self.master)
        self.category_frame.pack()
        self.category_label = Label(self.category_frame, text = "Categoria")
        self.category_label.pack(side = LEFT)
        self.category_entry = Entry(self.category_frame)
        self.category_entry.pack(side = LEFT)

        self.description_frame = Frame(self.master)
        self.description_frame.pack()
        self.description_label = Label(self.description_frame, text = "Descrição")
        self.description_label.pack(side = LEFT)
        self.description_entry = Entry(self.description_frame)
        self.description_entry.pack(side = LEFT)

        self.name_frame = Frame(self.master)
        self.name_frame.pack()
        self.name_label = Label(self.name_frame, text = "Nome")
        self.name_label.pack(side = LEFT)
        self.name_entry = Entry(self.name_frame)
        self.name_entry.pack(side = LEFT)


        self.button_report_frame = Frame(self.master)
        self.button_report_frame.pack()
        self.button_report = Button(self.button_report_frame, text = "Postar")
        self.button_report["command"] = self.autenticate
        self.button_report.pack()

    def autenticate(self):
        self.title = self.title_entry.get()
        self.category = self.category_entry.get()
        self.description = self.description_entry.get()
        self.name = self.name_entry.get()

        self.report_register()
        messagebox.showinfo("Sucesso","Registro autenticado.")
        self.master.destroy()    


    def report_register(self):
        self.update_register()
        with open(self.file_name, 'wb') as file:
            new_report = Data_report(self.title, self.category, self.description, self.name)
            self.list.append(new_report)
            pickle.dump(self.list, file)
            file.close()

if __name__ == "__main__":
    root = Tk()
    posts = Report_register(root)
    root.mainloop()