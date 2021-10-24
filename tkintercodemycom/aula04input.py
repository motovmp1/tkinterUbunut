from tkinter import *


root = Tk()
root.title("App tkinter")


# -------------------------------
# gemometry
root.geometry("800x500")

# --------------------------------
# label
label_1 = Label(root, text="Hello  Tkinter")
label_1.pack()


def gray_text(event):
    if (e.get() == ''):
        print("empty")
        e.delete(0)
    else:
        print("text")
        e.delete(0, 'end')
        e['fg']= 'black'

e = Entry(root, foreground="gray")
e.pack()
e.insert(0, "insert your name here")
e.bind("<1>", gray_text)


root.mainloop()