from tkinter import *
root = Tk()
c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_polygon(100, 10, 20, 90, 180, 90)
c.create_polygon(40, 110, 160, 110,
 190, 180, 10, 180,
 fill='orange', outline='black')


root.mainloop()
