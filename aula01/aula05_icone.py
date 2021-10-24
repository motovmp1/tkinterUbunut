try:
    import tkinter as tk
except:
    import tkinter as tk
    

    
app = tk.Tk()
app.title("Frame Window Size Frozen")


app.resizable(True, True)
app.minsize(width=600, height=400)
app.maxsize(width=800, height=500)
app.mainloop()