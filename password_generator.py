import tkinter as tk
from tkinter import  *
import random
import string
import time
import urllib.request,urllib.error

class PasswordGenerator(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack()
        self.master.geometry('1024x720')
        self.master.title("Password Generator")
        # self.check_internet_connection()

        net_connect = Label(self,text="Internet Connection ",font=("Calibri Bold", 14),fg="white",bg="grey",padx=0,pady=5)
        net_connect.pack(side="right",fill=Y)

        net_connect.configure(text=self.check_internet_connection())

        # loop_value = 1
        # while loop_value == 1:
        #     net_connect.configure(text=self.check_internet_connection())
        #     time.sleep(5)


        master_lable = Label(self,text="Random Password Generator ",font=("Arial Bold", 30),fg="white",bg="red",padx=20,pady=10)
        master_lable.pack(side=TOP,fill =X)
        lbl = Label(self,text="Enter no of Charcters",font=("Arial Bold", 15))
        lbl.pack()

        text = Entry(self,width=50, textvariable="input_text")
        text.pack()
        text.focus_set()

        def callback():
            text_box.insert(INSERT, '');
            text_inp  = int(text.get())
            str_var =  self.randomStringDigits(text_inp)

            text_box.insert(END,str_var)

        frame2 = Frame(self)
        frame2.pack(padx=50,pady=10)
        b = Button(frame2, text="Generate", width=10, command=callback,padx=50,pady=10,fg="white",bg="green")
        b.pack()
        lbl2 = Label(self,text="Your Generated Password Here ").pack()
        text_box = Text(self,height=10,width=80,font=("Arial Bold", 16))
        text_box.pack(side=LEFT)

    def randomStringDigits(self,stringLength=15):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

    def check_internet_connection(self):
        loop_value = 1
        while loop_value == 1:
            # print ("test 1")
            try:
                urllib.request.urlopen("http://www.google.com")
                # loop_value = 0

                print("Internet Connected")
                return "connect"
            except urllib.error.URLError as e:
                # print("test 3")
                print(e.reason)

                print("Network currently down.")
                return "disconnect"
            # time.sleep(5)
if __name__ == '__main__':
    root = tk.Tk()
    myapp = PasswordGenerator(root)
    myapp.mainloop()
