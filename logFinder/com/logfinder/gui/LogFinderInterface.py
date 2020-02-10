import tkinter
from tkinter.ttk import Label, Combobox

from logFinder.com.logfinder.util.LogFinderUtils import LogFinderUtils

class LogFinderInterface(object):

    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title("Log Finder")
        self.win.geometry("600x400")


    def buildInterface(self):
        lblEnv = Label(self.win, text="Ambiente: ")
        lblEnv.grid(column=0, row=0)
        combo = Combobox(self.win)
        combo.grid(column=1, row=0)
        logFinderUtils = LogFinderUtils()
        env = logFinderUtils.readProperties('environments')
        combo['values'] = env[0][1].split(',');
        self.win.mainloop()

