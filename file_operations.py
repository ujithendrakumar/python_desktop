from tkinter import  *

root = Tk()

fw = open('sample.txt','w')
fw.write('Hello \nThis is Jithendra Kumar Ummadisingu\n')
fw.write(("I am a Python Software Engineer\n "))
fw.close()


fr = open('sample.txt','r')
text =fr.read()
print(text)
fr.close()

#=============== Exception Handeling ==========


while True:
    try:
        number =int(input("Please enter your favourite House Number?\n "))
        print(18/number)
        break
    except ValueError:
        print("Make sure and Enter a number")
    except ZeroDivisionError:
        print("Don't pick Zero ")
    except:
        break
    finally:
        print("Loop ends ..! ")




root.mainloop()
