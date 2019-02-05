from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to JK  app")

lbl= Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=1)
combo = Combobox(window)
combo['values']= ('Select Option ',1, 2, 3, 4, 5, "Text")
combo.current(0) #set the selected item
combo.grid(column=0, row=2)
lbl2= Label(window, text="Hello", font=("Arial Bold", 50))
lbl2.grid(column=0, row=3)

txt = Entry(window,width=10)
txt.grid(column=1, row=3)
txt.focus_set()
def clicked():
    res = "Welcome to " + txt.get()
    lbl2.configure(text=res)

    # lbl2.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me",command=clicked)
btn.grid(column=0, row=4,padx=29,pady=20)

window.geometry('640x480')
window.mainloop()