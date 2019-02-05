from tkinter import *

def doNothing():
    print("Ok Ok I won't")





root = Tk()

frame = Frame(root)

def cancelClick():
    root.destroy()

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu, tearoff=False)
editMenu = Menu(menu, tearoff=False)
viewMenu = Menu(menu, tearoff=False)
helpMenu = Menu(menu, tearoff=False)

menu.add_cascade(label="File",menu=subMenu)
menu.add_cascade(label="Edit",menu=editMenu)
menu.add_cascade(label="View",menu=viewMenu)
menu.add_cascade(label="Help",menu=helpMenu)

subMenu.add_command(label="New Project",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=cancelClick)


editMenu.add_command(label="Undo",command=doNothing)
editMenu.add_command(label="Redo",command=doNothing)
editMenu.add_command(label="Undo",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Copy",command=doNothing)
editMenu.add_command(label="Paste",command=doNothing)
editMenu.add_command(label="Select all",command=doNothing)


label_1 = Label(root,text="Diabeties Prediction",bg="green",fg="white")
label_1.config(font=('calibri',24),height=2)
label_1.pack(fill=X)

lable_2 = Label(root,text="Patient Name",bg="#000",fg="white")
lable_2.pack(fill=X)
entry_1 = Entry(root)

entry_1.pack()


status = Label(root,text="This is Jithendra Kumar Project  Pratice",bd=1,relief=SUNKEN,anchor=W)

status.pack(side=BOTTOM,fill=X)

root.geometry("1024x720")
frame.master.title(" Prediction")
root.mainloop()
