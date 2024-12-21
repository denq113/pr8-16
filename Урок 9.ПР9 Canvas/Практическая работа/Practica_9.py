from tkinter import *

root=Tk()

c = Canvas(root,width=200,height=200,bg = "white")
c.pack()
a = -10
b = 30

c.create_rectangle(50,70,160,180,fill = "aqua",width=0)

c.create_polygon(30,70,102,30,180,70,fill = "aqua",width=0)

c.create_oval(160,10,190,40,fill = "darkgoldenrod1",width=0)

for i in range (20,0,-1):
    a = a + 10
    b = b + 10
    c.create_arc(a, 290, b, 160,
                 start=160, extent=-70,
                 style=ARC, outline='green',
                 width=1)



root.mainloop()