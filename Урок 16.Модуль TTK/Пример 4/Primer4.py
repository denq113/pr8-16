from tkinter import *
from tkinter.ttk import *
root = Tk()
style = Style()
style.configure("G.TButton", foreground="green")
Button(text="First", style="G.TButton").pack()
Button(text="Second").pack()
root.mainloop()