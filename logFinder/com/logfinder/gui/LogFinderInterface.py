import tkinter
from tkinter import messagebox
from tkinter.ttk import Label, Combobox, Entry, Button, Treeview

from logFinder.com.logfinder.businesslogic.LogFinderLogic import LogFinderLogic
from logFinder.com.logfinder.util.LogFinderUtils import LogFinderUtils


class LogFinderInterface(object):

    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title("Log Finder")
        self.win.geometry("1024x400")

    def buildInterface(self):
        self.selectEnvironment()
        self.selectServer()
        self.insertClientCode()
        self.insertDate()
        self.buttonBar()
        self.dataTable()
        self.win.mainloop()

    def selectEnvironment(self):
        Label(self.win, text="Ambiente: ").grid(column=0, row=0, padx=10)
        self.win.comboEnv = Combobox(self.win)
        self.win.comboEnv.grid(column=1, row=0)
        logFinderUtils = LogFinderUtils()
        env = logFinderUtils.readProperties('environments')
        self.win.comboEnv['values'] = env[0][1].split(',')

    def selectServer(self):
        Label(self.win, text="FE/BE: ").grid(row=0, column=2, padx=40)
        self.win.comboServer = Combobox(self.win)
        self.win.comboServer.grid(row=0, column=3)
        self.win.comboServer['values'] = "FE BE"

    def insertClientCode(self):
        Label(self.win, text="Postazione: ").grid(row=2, column=0, pady=20, padx=10)
        self.win.clientCode = Entry(self.win, width=23, textvariable=tkinter.StringVar)
        self.win.clientCode.grid(row=2, column=1, padx=20)

    def insertDate(self):
        Label(self.win, text="Data: ").grid(row=2, column=2, padx=40)
        self.win.date = Entry(self.win, width=23, textvariable=tkinter.StringVar)
        self.win.date.grid(row=2, column=3, padx=20)

    def buttonBar(self):
        Button(self.win, text="Invia", command=self.sendForm).grid(row=3, column=0, padx=10)
        Button(self.win, text="Reset", command=self.resetForm).grid(row=3, column=1, padx=5)

    def resetForm(self):
        self.win.date.delete(0, tkinter.END)
        self.win.clientCode.delete(0, tkinter.END)
        self.win.comboServer.delete(0, tkinter.END)
        self.win.comboEnv.delete(0, tkinter.END)

    def sendForm(self):
        env = self.win.comboEnv.get()
        server = self.win.comboServer.get()
        clientCode = self.win.clientCode.get()
        date = '*' + self.win.date.get() + '*'
        try:
            LogFinderLogic().connect_to_server(env, server, clientCode, date)
            messagebox.showinfo("LogFinder", "Connesso al server di " + env + " " + server)
        except Exception as e:
            messagebox.showerror("LogFinder", e)

    def dataTable(self):
        self.table = Treeview(columns="#0, #1")
        self.table.heading("#0", text="File")
        self.table.column("#0", minwidth=0, width=200, stretch=tkinter.NO)
        self.table.heading("#1", text="Macchina")
        self.table.column("#1", minwidth=0, width=200, stretch=tkinter.NO)
        self.table.grid(column=0, row=4, padx=10, pady=30)
