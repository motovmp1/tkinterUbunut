from tkinter import *


root = Tk()
root.title("App tkinter")


# -------------------------------
# gemometry
root.geometry("800x500")

# --------------------------------
# label
label_1 = Label(root, text="Hello  Tkinter")
label_1.grid(row=0, column=0)


label_2 = Label(root, text="Hello  second")
label_2.grid(row=1, column=0)

root.mainloop()
