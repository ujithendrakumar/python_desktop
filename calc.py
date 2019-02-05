from tkinter import  *
from tkinter import StringVar

cal = Tk()
cal.title('Jithendra Calculator Application')

def btnClick(number):
    global  operator
    operator = operator + number
    text_input.set(operator)
def btnClear():
    global  operator
    operator =''
    text_input.set("")

def btnEqulInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator =''


operator =""

text_input= StringVar()

txtDisplay = Entry(cal,font=('arial',20,'bold'),textvariable=text_input,justify="right",bd=30,insertwidth=4,bg="powder blue").grid(columnspan=4)

btn7 = Button(cal,font=('arial',20,'bold'),text="7" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("7")).grid(row=1,column=0)
btn8 = Button(cal,font=('arial',20,'bold'),text="8" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("8")).grid(row=1,column=1)
btn9 = Button(cal,font=('arial',20,'bold'),text="9" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("9")).grid(row=1,column=2)
btnadd = Button(cal,font=('arial',20,'bold'),text="+" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("+")).grid(row=1,column=3)


btn4 = Button(cal,font=('arial',20,'bold'),text="4" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("4")).grid(row=2,column=0)
btn5 = Button(cal,font=('arial',20,'bold'),text="5" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("5")).grid(row=2,column=1)
btn6 = Button(cal,font=('arial',20,'bold'),text="6" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("6")).grid(row=2,column=2)
btnsub = Button(cal,font=('arial',20,'bold'),text="-" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("-")).grid(row=2,column=3)

btn1 = Button(cal,font=('arial',20,'bold'),text="1" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("1")).grid(row=3,column=0)
btn2 = Button(cal,font=('arial',20,'bold'),text="2" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("2")).grid(row=3,column=1)
btn3 = Button(cal,font=('arial',20,'bold'),text="3" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("3")).grid(row=3,column=2)
btnMul = Button(cal,font=('arial',20,'bold'),text="*" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("*")).grid(row=3,column=3)

btn0 = Button(cal,font=('arial',20,'bold'),text="0" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("0")).grid(row=4,column=0)
btnClear = Button(cal,font=('arial',20,'bold'),text="c" ,bd=8,bg="powder blue",padx=16,pady=16,command=btnClear).grid(row=4,column=1)
btnEqual = Button(cal,font=('arial',20,'bold'),text="=" ,bd=8,bg="powder blue",padx=16,pady=16,command=btnEqulInput).grid(row=4,column=2)
btndiv = Button(cal,font=('arial',20,'bold'),text="/" ,bd=8,bg="powder blue",padx=16,pady=16,command=lambda: btnClick("/")).grid(row=4,column=3)

cal.tk_setPalette(background="black")
cal.resizable(False,False)
# cal.geometry("360x600")
cal.mainloop()