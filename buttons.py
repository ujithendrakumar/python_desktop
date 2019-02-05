import tkinter as tk
import AppKit
class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack(padx=20,pady=15)
        self.master.title("The Buttons GUI")
        self.master.bind('<Escape>',self.click_cancel)
        # self.master.geometry("1024x720")

        tk.Label(self,text="This is  Buttons Display").pack()
        tk.Button(self,text="OK",default="active",bg="green",fg="white",command=self.click_ok).pack(side='right')
        tk.Button(self, text="Cancel", default="active",bg="red",fg="white", command=self.click_cancel).pack(side='right')

        button_frame = tk.Frame(self)
        button_frame.pack(padx=20,pady=(0,15),anchor='e')

        tk.Button(button_frame,text="Ok",default="active",command=self.click_cancel).pack(side='right')
        tk.Button(button_frame, text="Cancel", command=self.click_cancel).pack(side='right')

    def click_ok(self):
        print("The User clicked 'OK'")

    def click_cancel(self):
        print("The User clicked 'Cancel'")
        self.master.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()