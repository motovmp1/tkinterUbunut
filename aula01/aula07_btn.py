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
cmd1 = Button(menu_inicial, text="Executar", command= lambda: cmd_click("Nova mensagem lambda"))
cmd1.pack()


# tkinker aceita commandos diretos na linha - nao preciso de uma funcao
cmd2 = Button(menu_inicial, text="Print", command= lambda: print("Nova mensagem print"))
cmd2.pack()





menu_inicial.mainloop()