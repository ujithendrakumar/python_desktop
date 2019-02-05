from tkinter import *

def doNothing():
    print("Ok Ok I won't")

root = Tk()

menu =Menu(root,tearoff=False)

root.config(menu=menu)

subMenu = Menu(menu,tearoff=False)

menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project....",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing)

editMenu = Menu(menu,tearoff=False)

menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo",command=doNothing)
editMenu.add_command(label="Redo",command=doNothing)

#=============== ToolBar=================
toolbar = Frame(root,bg="blue")

insertButt = Button(toolbar,text="Insert Mappings",command=doNothing)
insertButt.pack(side=LEFT,padx=29,pady=2)
printButt = Button(toolbar,text="Print",command=doNothing)
printButt.pack(side=RIGHT,padx=50,pady=0)
toolbar.pack(side=TOP,fill=X)
#========== Status Bar ========================
status = Label(root,text="This is Jithendra Kumar Project  Pratice",bd=1,relief=SUNKEN,anchor=W)

status.pack(side=BOTTOM,fill=X)
root.geometry("1024x720")
app = Frame(root)
app.master.title('Jithendra Kumar Testing Application')
root.mainloop()