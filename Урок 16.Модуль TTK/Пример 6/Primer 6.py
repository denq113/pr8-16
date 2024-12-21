from tkinter import *
from tkinter.ttk import *
root = Tk()
Button(text="Hello World").pack(
 padx=40, pady=40,
 ipadx=20, ipady=20
)
st = Style()
st.map('TButton',
 foreground=[('!active', 'purple'),
 ('pressed', 'orange'),
 ('active', 'red')],
 background=[
 ('pressed', 'brown'),
 ('active', 'white')]
 )
root.mainloop()
