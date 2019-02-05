from tkinter import *

root = Tk()
'''
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

buttton1 = Button(topFrame,text="Button One",fg='red')
buttton2 = Button(topFrame,text="Button Two",fg='blue')
buttton3 = Button(topFrame,text="Button Three",fg='green')
buttton4 = Button(topFrame,text="Button Four",fg='orange')

buttton1.pack()
buttton2.pack()
buttton3.pack()
buttton4.pack()

buttton1.pack(side=LEFT)
buttton2.pack(side=LEFT)
buttton3.pack(side=LEFT)
buttton4.pack(side=BOTTOM)
'''
#============== Flitering Widgets in Layouts =================
one =Label(root,text="Jithendra Kumar",bg="red",fg="white")
one.pack()


three =Label(root,text="Python Software Developer",bg="green",fg="white")
three.pack(side=LEFT,fill =Y)

two =Label(root,text="Ummadisingu",bg="blue",fg="white")
two.pack(fill =X)
four =Label(root,text="The Fastgrowing Developer",bg="orange",fg="white")
four.pack(fill =X)
root.mainloop()