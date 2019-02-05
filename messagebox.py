from tkinter import *

import tkinter.messagebox

root  = Tk()
tkinter.messagebox.showinfo("Window Title","Monkyes can live 300 Years")

answer= tkinter.messagebox.askquestion("Question 1","Do you like silly faces?")
answer2= tkinter.messagebox.askquestion("Question 2","Do you Love Your Mom?")
if answer == 'yes':
    print("Your absolutely Right !!")

if answer2 == 'yes':
    print("Wow, that was Great!!")
#========================= Graphics & Shapes ================

canvas = Canvas(root,width=200,height=400)
canvas.pack(padx=20,pady=10)

black_line = canvas.create_line(0,0,200,50,fill="green")

rectangle = canvas.create_rectangle(15,15,300,300,fill="red")
root.geometry("1024x720")
root.mainloop()