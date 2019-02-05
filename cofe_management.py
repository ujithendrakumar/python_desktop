import  tkinter as tk
from tkinter import *
root = tk.Tk()


Tops = tk.Frame(root ,width=1350 ,height=100 ,bd=8 ,relief="raise").pack()

f1 = tk.Frame(root ,width=900 ,height=650 ,bd=8 ,relief="raise")
f1.pack(side=LEFT)
f2 = tk.Frame(root ,width=440 ,height=650 ,bd=8 ,relief="raise")
f2.pack(side=RIGHT)
# f1a = tk.Frame(f1, width=900, height=330, bd=8, relief="raise")
# f1a.pack(side=TOP)
# f2a = tk.Frame(f2, width=900, height=320, bd=8, relief="raise")
# f2a.pack(side=TOP)
# fb2 = tk.Frame(f2, width=440, height=50, bd=16, relief="raise")
# fb2.pack(side = BOTTOM)
root.mainloop()