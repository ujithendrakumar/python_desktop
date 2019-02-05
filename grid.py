from  tkinter import *

root = Tk()
'''
label_1 = Label(root,text="Name")

label_2 = Label(root,text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0)
label_2.grid(row=1)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
c =  Checkbutton(root,text="Keep me loggeed in.")
button = Button(root,text="Login",bg="green",fg="white")

c.grid(columnspan=2)
button.grid(columnspan=2)
'''

# ============= Binding Functions to Layouts ==================

def printName(event):
    print('Hello my name is Jithendra Kumar ')

button_1 = Button(root,text="Print my Name ")
button_1.bind("<Button-1>",printName)
button_1.pack()

root.mainloop()