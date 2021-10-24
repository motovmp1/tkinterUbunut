# aula de tkinter python Joao ribeiro

from tkinter import *
from tkinter import font


menu_inicial = Tk()
menu_inicial.title("Primeira App Tkinter")

# geometry
menu_inicial.geometry("900x400+100+200")
menu_inicial.resizable(False, False)


label_1 = Label(menu_inicial, 
                            text="Este e o label",
                            bg="yellow",
                            fg="red",
                            font="Arial 20 bold"
                            )
label_1.pack()


menu_inicial.mainloop()
