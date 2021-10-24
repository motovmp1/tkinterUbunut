# aula de tkinter python Joao ribeiro

from tkinter import *


menu_inicial = Tk()
menu_inicial.title("Primeira App Tkinter")

# geometry
menu_inicial.geometry("900x400+100+200")
menu_inicial.resizable(False, False)

def cmd_click(mensagem):
    print(mensagem)

# button on python
cmd = Button(menu_inicial, text="Executar", command= lambda: cmd_click("Nova mensagem lambda"))
cmd.pack()




menu_inicial.mainloop()