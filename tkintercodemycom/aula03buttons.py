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

# -----------------------------------------
# buttons

def cmd_disable():
    button_2['state']= 'disabled'
    button_2['bg'] = '#ffb3b3'
    print("teste")

def reset_button():
    button_2['state']= 'normal'
    button_2['bg']= orig_color
    print("clear all")



label_space = Label(root, text='')
label_space.grid(row=0, column=1)

button_1 = Button(root, text="Executar", padx=30, pady=50, command=lambda: cmd_disable())
button_1.grid(row=3, column=3)


button_2 = Button(root, text="Executar", padx=30, pady=50)
button_2.grid(row=4, column=3)
orig_color = button_2.cget("background")


button_3 = Button(root, text="Reset", padx=50, pady=100, command=lambda: reset_button())
button_3.grid(row=3, column=4)



root.mainloop()
