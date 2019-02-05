import tkinter as tk
from tkinter import  *

class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.grid(padx=40,pady=50)
        self.master.title(" KM to Grams, Pounds & Ounes ")
        self.master.geometry("1024x200")
        def kg_to_grams_pounds_ounces():

            input_kg_val = float(input_kg.get())
            grams_res = input_kg_val * 1000
            grams.delete("1.0", END)
            grams.insert(END,grams_res)

            pounds_res = input_kg_val * 2.20462
            pounds.delete("1.0", END)
            pounds.insert(END, pounds_res)

            ounces_res = input_kg_val * 35.274
            ounces.delete("1.0", END)
            ounces.insert(END, ounces_res)

        # // Label
        lbl1 = Label(self,text="KG",font=('Calibri',15,"bold"))
        lbl1.grid(row=0,column=0)
        # //Entry
        vcmd = (self.register(self.callback))
        entry_value1 = StringVar()
        input_kg = Entry(self,textvariable=entry_value1, validate='all', validatecommand=(vcmd, '%P'))
        input_kg.insert(0, 'Please Enter Kg')
        input_kg.grid(row=0,column=1)
        # input_kg.focus_set()

        # Convert Button
        btn1 = Button(text=" Convert ",command=kg_to_grams_pounds_ounces,bg="green",fg="white")
        btn1.grid(row=0,column=2)

        #Dispaly Names
        gr_name = Label(self,text="Grams",font=('Calibri',15,"bold"))
        gr_name.grid(row=1,column=0)

        po_name = Label(self, text="Pounds",font=('Calibri',15,"bold"))
        po_name.grid(row=1, column=1)

        ou_name = Label(self, text="Ounces",font=('Calibri',15,"bold"))
        ou_name.grid(row=1, column=2)

        # Result Data Text Boxes
        grams = Text(self,width=30,height=1)
        grams.grid(row=2,column=0)

        pounds = Text(self, width=30, height=1)
        pounds.grid(row=2, column=1)


        ounces = Text(self, width=30, height=1)
        ounces.grid(row=2, column=2)

    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()