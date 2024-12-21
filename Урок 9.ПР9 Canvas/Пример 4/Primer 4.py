from tkinter import *
root = Tk()
c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_oval(50, 10, 150, 110, width=2)
c.create_oval(10, 120, 190, 190,
 fill='grey70', outline='white')

root.mainloop()