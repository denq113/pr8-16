from tkinter import *
from tkinter.ttk import *
root = Tk()
b = Button(text="Hello")
b.pack()
t = Text(width=10, height=5)
t.pack()
print(root.__class__)
print(b.__class__)
print(t.__class__)
root.mainloop()