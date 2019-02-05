import  tkinter as tk
from tkinter import *

class CafeManagement(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack()
        self.master.geometry('13x750+0+0')
        self.master.title(" Cafe Management System ")
        self.master.config(background="black")

        Tops = tk.Frame(self,width=1350,height=100,bd=8,relief="raise")
        Tops.pack()
        f1 = tk.Frame(root, width=900, height=650, bd=8, relief="raise")
        f1.pack(side=LEFT)
        f2 = tk.Frame(root, width=440, height=650, bd=8, relief="raise")
        f2.pack(side=RIGHT)
        # f1a = tk.Frame(f1, width=900, height=330, bd=8, relief="raise")
        # f1a.pack(side=TOP)
        # f2a = tk.Frame(f2, width=900, height=320, bd=8, relief="raise")
        # f2a.pack(side=TOP)
        # fb2 = tk.Frame(f2, width=440, height=50, bd=16, relief="raise")
        # fb2.pack(side = BOTTOM)
if __name__ == '__main__':
    root = tk.Tk()
    myapp = CafeManagement(root)
    myapp.mainloop()