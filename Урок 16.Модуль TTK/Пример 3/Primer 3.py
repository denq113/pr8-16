from tkinter import *
from tkinter import ttk
root = Tk()
b_tk = Button(text="Hello Tk")
b_ttk = ttk.Button(text="Hello Ttk")
b_tk.config(background="#b00",
 foreground="#fff")
style = ttk.Style()
style.configure("TButton",
 background="#0b0",
 foreground="#fff")
b_tk.pack(padx=10, pady=10)
b_ttk.pack(padx=10, pady=10)
root.mainloop()
