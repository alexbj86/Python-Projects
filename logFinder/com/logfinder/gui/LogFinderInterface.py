import tkinter
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from tkinter.ttk import Label, Combobox, Entry, Button, Treeview, Frame

from logFinder.com.logfinder.businesslogic.LogFinderLogic import LogFinderLogic
from logFinder.com.logfinder.util.LogFinderUtils import LogFinderUtils


class LogFinderInterface(object):

    def __init__(self):
        self.win = tkinter.Tk()
        self.win.resizable(width=tkinter.FALSE, height=tkinter.FALSE)
        self.win.title("Log Finder")
        self.win.geometry("800x450")
        self.top_frame = Frame(self.win, width=600)
        self.top_frame.grid(row=0, columnspan=3)

    def buildInterface(self):
        self.selectEnvironment()
        self.selectServer()
        self.insertClientCode()
        self.insertDate()
        self.buttonBar()
        self.win.mainloop()

    def selectEnvironment(self):
        Label(self.top_frame, text="Ambiente: ").grid(column=0, row=0, padx=10)
        self.top_frame.comboEnv = Combobox(self.top_frame)
        self.top_frame.comboEnv.grid(column=1, row=0)
        logFinderUtils = LogFinderUtils()
        env = logFinderUtils.readProperties('environments')
        self.top_frame.comboEnv['values'] = env[0][1].split(',')

    def selectServer(self):
        Label(self.top_frame, text="FE/BE: ").grid(row=0, column=2, padx=40)
        self.top_frame.comboServer = Combobox(self.top_frame)
        self.top_frame.comboServer.grid(row=0, column=3)
        self.top_frame.comboServer['values'] = "FE BE"

    def insertClientCode(self):
        Label(self.top_frame, text="Postazione: ").grid(row=2, column=0, pady=20, padx=10)
        self.top_frame.clientCode = Entry(self.top_frame, width=23, textvariable=tkinter.StringVar)
        self.top_frame.clientCode.grid(row=2, column=1, padx=20)

    def insertDate(self):
        Label(self.top_frame, text="Data: ").grid(row=2, column=2, padx=40)
        self.top_frame.date = Entry(self.top_frame, width=23, textvariable=tkinter.StringVar)
        self.top_frame.date.grid(row=2, column=3, padx=20)

    def buttonBar(self):
        Button(self.top_frame, text="Invia", command=self.sendForm).grid(row=3, column=0, padx=10)
        Button(self.top_frame, text="Reset", command=self.resetForm).grid(row=3, column=1, padx=5)

    def resetForm(self):
        self.top_frame.date.delete(0, tkinter.END)
        self.top_frame.clientCode.delete(0, tkinter.END)
        self.top_frame.comboServer.delete(0, tkinter.END)
        self.top_frame.comboEnv.delete(0, tkinter.END)

    def sendForm(self):
        env = self.top_frame.comboEnv.get()
        server = self.top_frame.comboServer.get()
        clientCode = self.top_frame.clientCode.get()
        date = '*' + self.top_frame.date.get() + '*'
        try:
            files = LogFinderLogic().get_list_files(clientCode, date, env, server)
            self.dataTable(files)
            messagebox.showinfo("LogFinder", "Connesso al server di " + env + " " + server)
        except Exception as e:
            messagebox.showerror("LogFinder", e)

    def dataTable(self, files):
        self.table = Treeview(self.win)
        self.table["columns"] = ("1", "2")
        self.table.column("1", minwidth=0, width=250, stretch=tkinter.NO)
        self.table.heading("1", text="File")
        self.table.column("2", minwidth=0, width=250, stretch=tkinter.NO)
        self.table.heading("2", text="Macchina")
        self.table.grid(row=1, column=0, padx=10, pady=30)
        for k in files.keys():
            for v in files.values():
                for l in v:
                    self.table.insert("", "end", values=(l, k))
        self.saveFileBtn()

    def saveFileBtn(self):
        Button(self.win, text="Download", command=self.chooseDir).grid(row=2, column=0, padx=10)

    def chooseDir(self):
        local_dir_name = askdirectory()
        print(local_dir_name)
        try:
            for s in self.table.selection():
                sel_rows = self.table.item(s).get('values')
                LogFinderLogic().download_file(sel_rows[0].strip(), sel_rows[1], local_dir_name)
                messagebox.showinfo("LogFinder", "Download completato")
        except Exception as e:
            messagebox.showerror("LogFinder", e)
        # print(self.table.item(s).get('values'))
