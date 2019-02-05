#=================== Mouse Click Events ===============================
from tkinter import  *

root = Tk()
"""
def leftClick(event):
    print('Left Side Print')


frame = Frame(root,height = 250, width = 300)

frame.bind("<Button-1>",leftClick)
frame.pack()
"""
#=================== Using Classs ======================================

class myClass():
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text="Print Message ",command=self.printMessage )
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame,text="Quit",command=frame.quit)
        self.quitButton.pack(side =LEFT)

    def printMessage(self):
        print("Print Button Exicuted")


b = myClass(root)

root.mainloop()
