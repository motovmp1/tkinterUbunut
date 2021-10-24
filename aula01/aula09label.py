# aula de tkinter python Joao ribeiro

from tkinter import *


menu_inicial = Tk()
menu_inicial.title("Primeira App Tkinter")

# geometry
menu_inicial.geometry("900x400+100+200")
menu_inicial.resizable(False, False)


#Label em tkinter aqui nome
label_1 = Label(menu_inicial, text="Este primeiro label")
label_1.pack()

#Label em tkinter aqui nome
label_2 = Label(menu_inicial, text="Este primeiro label 2")
label_2.pack()


cmd_button = Button(menu_inicial, text="Executar")
cmd_button.pack()



menu_inicial.mainloop()