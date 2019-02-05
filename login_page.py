from tkinter import  *
import tkinter as tk

class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack(padx=20,pady=15)
        # self.master.tk_setPalette(background="#292929")
        tk.Message(self,text="Please authenticate with your username and password before continuing.",font="system 14 bold",justify='left',aspect='800').pack(pady=(15,0))

        # Username and password fields goes form here
        df = tk.Frame(self)
        df.pack(padx=20,pady=15,anchor='w')

        tk.Label(df,text=" Username : ").grid(row=0,column=0,sticky='w')

        self.username_input = tk.Entry(df,background="white",width='24')
        self.username_input.grid(row=0,column=1,sticky='w')
        self.username_input.focus_set()

        tk.Label(df,text=" Password : ").grid(row=1,column=0,sticky='w')

        self.password_input =  tk.Entry(df,background="white",width='24',show='*')
        self.password_input.grid(row=1,column=1,sticky='w')

        self.submit_button = tk.Button(df,text=" Login ",command=self.click_submit)
        self.submit_button.grid(row=2,column=1)
        # photo = PhotoImage(file="images/ujk.png")
        # lab = tk.Label(self, image=photo)
        # lab.pack()


    def click_cancel(self):
        print("user click Cancel")
        self.master.destroy()
    def click_submit(self,event=None):
        print("The user clicked Login: \n Username : {} \n Password : {} ".format(self.username_input.get(),self.password_input.get()))

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()

