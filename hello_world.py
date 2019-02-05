import tkinter as tk


class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack()
        self.master.title("Hello World..!!!")
        #self.master.resizable(False,False)
        # self.master.tk_setPalette(background='#eee')
        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) /2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) /2
        self.master.geometry("{}x{}".format(int(x),int(y)))
        self.master.config(menu=tk.Menu(self.master))

        tk.Label(self,text="This is my First GUI Program").pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
