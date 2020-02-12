import tkinter
from tkinter.ttk import Label, Combobox, Entry, Button

from logFinder.com.logfinder.util.LogFinderUtils import LogFinderUtils


class LogFinderInterface(object):

    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title("Log Finder")
        self.win.geometry("600x400")

    def buildInterface(self):
        self.selectEnvironment()
        self.selectFE_BE()
        self.insertClientCode()
        self.insertDate()
        self.buttonBar()
        self.win.mainloop()

    def selectEnvironment(self):
        Label(self.win, text="Ambiente: ").grid(column=0, row=0, padx=10)
        combo = Combobox(self.win)
        combo.grid(column=1, row=0)
        logFinderUtils = LogFinderUtils()
        env = logFinderUtils.readProperties('environments')
        combo['values'] = env[0][1].split(',')

    def selectFE_BE(self):
        Label(self.win, text="FE/BE: ").grid(row=0, column=2, padx=40)
        combo = Combobox(self.win)
        combo.grid(row=0, column=3)
        combo['values'] = "FE BE"

    def insertClientCode(self):
        Label(self.win, text="Postazione: ").grid(row=2, column=0, pady=20, padx=10)
        self.win.clientCode = Entry(self.win, width=23, textvariable=tkinter.StringVar)
        self.win.clientCode.grid(row=2, column=1, padx=20)

    def insertDate(self):
        Label(self.win, text="Data: ").grid(row=2, column=2, padx=40)
        self.win.date = Entry(self.win, width=23, textvariable=tkinter.StringVar)
        self.win.date.grid(row=2, column=3, padx=20)

    def buttonBar(self):
        Button(self.win, text="Invia").grid(row=3, column=0, padx=10)
        Button(self.win, text="Reset", command=self.resetForm).grid(row=3, column=1, padx=5)

    def resetForm(self):
        self.win.date.delete(0, tkinter.END)
        self.win.clientCode.delete(0, tkinter.END)
