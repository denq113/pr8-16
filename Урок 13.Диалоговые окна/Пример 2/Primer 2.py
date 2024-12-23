from tkinter import *
from tkinter import filedialog as fd
def insert_text():
 file_name = fd.askopenfilename()
 f = open(file_name)
 s = f.read()
 text.insert(1.0, s)
 f.close()
def extract_text():
 file_name = fd.asksaveasfilename(
 filetypes=(("TXT files", "*.txt"),
 ("HTML files", "*.html;*.htm"),
 ("All files", "*.*")))
 f = open(file_name, 'w')
 s = text.get(1.0, END)
 f.write(s)
 f.close()
root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=1, column=1, sticky=W)
root.mainloop()
