from tkinter import *


# ---------------------------------
# meu widget
class FrameNome(Frame):

    def __init__(self, meumaster):
        super().__init__()
        self["height"] = 5
        self["width"] = 5
        self["bd"] = 1
        self["relief"] = SOLID
        self["padx"] = 10
        self["pady"] = 10
        
       


        label_nome = Label(self, text="Nome:")
        text_nome = Entry(self)
        label_nome.grid(row=1, column=0) 
        text_nome.grid(row=1, column=1)

# --------------------------------------------




# -----------------------------------------
# GUI
root = Tk()
root.title("App")

# geometry
root.geometry("900x400+100+200")
root.resizable(False, False)


frame_nome1 = FrameNome(root)
frame_nome1.place(x=10, y=10)







# -------------------------------------
# Mainloop
root.mainloop()