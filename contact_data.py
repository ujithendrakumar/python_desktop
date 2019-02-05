import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk


class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master.title(" Contact Information Data Module ")
        self.master.geometry("1300x720")
        self.grid()
        self.large_font = ('Verdana', 30)
        self.small_font = ('Verdana', 14)

        image = Image.open("images/ujk.png")
        image = image.resize((214, 100), Image.ANTIALIAS)  # The (250, 250) is (width,height)
        photo = ImageTk.PhotoImage(image)
        label = Label(self,image=photo)
        label.image = photo  # keep a reference!
        label.grid(row=1,column=0,columnspan=2)

        # ===================== Frame 1=================================
        f1 = Frame(self)
        f1.grid(row=2,column=0,padx=5)

        #Label
        label1 = Label(f1,text=" Contact ID ",font=("Calibri",14,'normal'))
        label1.grid(row=2,column=0,padx=70)

        #Entry Fiedl
        contact_id = tk.StringVar(value='')
        inp1 = Entry(f1,textvariable=contact_id,font=self.small_font,width=20)
        inp1.grid(row=2,column=1)

        # Label
        label3 = Label(f1, text=" First Name ", font=("Calibri", 14, 'normal'))
        label3.grid(row=3, column=0, padx=70,pady=30)

        # Entry Fiedl
        first_name = tk.StringVar(value='')
        inp2 = Entry(f1, textvariable=first_name, font=self.small_font, width=20)
        inp2.grid(row=3, column=1)

        # Label
        label4 = Label(f1, text=" Last Name ", font=("Calibri", 14, 'normal'))
        label4.grid(row=4, column=0, padx=70)

        # Entry Fiedl
        last_name = tk.StringVar(value='')
        inp3 = Entry(f1, textvariable=last_name, font=self.small_font, width=20)
        inp3.grid(row=4, column=1)

        # Label
        label5 = Label(f1, text=" Mobile No ", font=("Calibri", 14, 'normal'))
        label5.grid(row=5, column=0, padx=70, pady=30)

        # Entry Fiedl
        mobile = tk.StringVar(value='')
        inp4 = Entry(f1, textvariable=mobile, font=self.small_font, width=20)
        inp4.grid(row=5, column=1)

        # Label
        label6 = Label(f1, text=" Address ", font=("Calibri", 14, 'normal'))
        label6.grid(row=6, column=0, padx=70)

        # Entry Fiedl
        address = tk.StringVar(value='')
        inp5 = Text(f1, height=6, width=30)
        inp5.grid(row=6, column=1)

        #label
        label7 = Label(f1, text=" Select Gender ", font=("Calibri", 14, 'normal'))
        label7.grid(row=7, column=0, padx=70, pady=30)
        """
        #COMBO BOX
        combo = Combobox(f1)
        combo['values'] = ('Select Gender ',"Male","Female")
        combo.current(0)  # set the selected item
        
        combo.grid(row=7, column=1)
        """
        f3 = Frame(f1)
        f3.grid(row=7, column=1, padx=5)
        tk.Radiobutton(f3,text="Male",padx=20,variable="v",value="male").grid(row=0, column=0,sticky=W)
        tk.Radiobutton(f3, text="FeMale", padx=20, variable="v", value="female").grid(row=0, column=1,sticky=W)
        #===================== Frame 2=================================
        f2 = Frame(self)
        f2.grid(row=2, column=1,padx=5)

        #Label
        label2 = Label(f2, text=" Search ", font=("Calibri", 14, 'normal'))
        label2.grid(row=2, column=3, padx=30)

        #Entry
        search_word = tk.StringVar(value='')
        ser1 = Entry(f2, textvariable=search_word, font=self.small_font, width=40)
        ser1.grid(row=2, column=4)
        #Test
        ser1 = Text(f2)
        ser1.grid(row=3, column=3,padx=30,pady=30,columnspan=2,sticky=W,rowspan=5)

        #========================== Buttons ====================================
        f4 = tk.Frame(self)
        f4.grid(row=3, column=0, padx=5,columnspan=4,pady=15)

        btn1 = tk.Button(f4,bg="green",text=" Add ",fg="white",pady=8,padx=30,font=("calibri bold",12))
        btn1.grid(row=0,column=0)

        btn2 = tk.Button(f4, bg="blue", text=" Update ", fg="white", pady=8, padx=30, font=("calibri bold", 12))
        btn2.grid(row=0, column=1)

        btn3 = tk.Button(f4, bg="red", text=" Delete ", fg="white", pady=8, padx=30, font=("calibri bold", 12))
        btn3.grid(row=0, column=2)

        btn4 = tk.Button(f4, bg="orange", text=" Clear ", fg="white", pady=8, padx=30, font=("calibri bold", 12))
        btn4.grid(row=0, column=3)

    # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(2, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    # root.grid_rowconfigure(0, weight=1)
    # root.grid_columnconfigure(0, weight=1)
    app.mainloop()
