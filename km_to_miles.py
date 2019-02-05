import tkinter as tk
from tkinter import  *

class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack()
        self.master.title(" Kilometers to Miles Converter ")
        self.master.config(background="black")

        # //Functions
        def km_to_miles_convert():
            miles = float(inp_val.get()) * 1.6
            res1.insert(END,miles)
            print(miles)
        # Button
        btn1 = Button(self,bg="orange",text="Exicute",command=km_to_miles_convert)
        btn1.grid(row=0,column=0)

        #Entry Field
        inp_val = StringVar()
        inp1 = Entry(self,width=30,textvariable=inp_val)
        inp1.grid(row=0,column=1)

        # Text Field
        res1 = Text(self,height=1,width=30)
        res1.grid(row=0,column=2)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()