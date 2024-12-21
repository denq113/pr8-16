from tkinter import *

def TextChange(event):
    Text['width'] = EntryUP.get()
    Text['height'] = EntryDown.get()

def collorChangeIn(event):
    Text['bg'] = 'white'

def collorChangeOut(event):
    Text['bg'] = 'lightgrey'

root = Tk()

frameUp = Frame()
frameDown = Frame()


f = Frame(frameUp)
f.pack(side=LEFT)

EntryUP = Entry(f, width=3)
EntryUP.pack()

EntryDown = Entry(f, width=3)
EntryDown.pack()

Button1 = Button(frameUp,text="Изменить")
Button1.pack(side = RIGHT)

Text = Text(frameDown,width=10,height=5,bg= "lightgrey")
Text.pack()

Button1.bind('<Button-1>',TextChange)
Button1.bind('<Return>',TextChange)

Text.bind('<FocusIn>',collorChangeIn)
Text.bind('<FocusOut>',collorChangeOut)

frameUp.pack(side = TOP)
frameDown.pack(side = BOTTOM)

root.mainloop()
