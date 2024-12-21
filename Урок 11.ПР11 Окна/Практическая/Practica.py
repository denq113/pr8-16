import tkinter as tk
from tkinter import *

def add_shape():
    def draw():
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())

        if shape_type.get() == 1:  # Rectangle
            canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
        elif shape_type.get() == 2:  # Oval
            canvas.create_oval(x1, y1, x2, y2, outline="black", width=2)

        shape_window.destroy()

    shape_window = Toplevel(root)
    shape_window.title("Фигура")

    # Coordinate inputs
    Label(shape_window, text="x1:").grid(row=0, column=0)
    entry_x1 = Entry(shape_window)
    entry_x1.grid(row=0, column=1)

    Label(shape_window, text="y1:").grid(row=1, column=0)
    entry_y1 = Entry(shape_window)
    entry_y1.grid(row=1, column=1)

    Label(shape_window, text="x2:").grid(row=2, column=0)
    entry_x2 = Entry(shape_window)
    entry_x2.grid(row=2, column=1)

    Label(shape_window, text="y2:").grid(row=3, column=0)
    entry_y2 = Entry(shape_window)
    entry_y2.grid(row=3, column=1)

    # Shape selection
    shape_type = IntVar(value=1)
    Radiobutton(shape_window, text="Прямоугольник", variable=shape_type, value=1).grid(row=4, column=0, columnspan=2, sticky="w")
    Radiobutton(shape_window, text="Овал", variable=shape_type, value=2).grid(row=5, column=0, columnspan=2, sticky="w")

    # Draw button
    Button(shape_window, text="Нарисовать", command=draw).grid(row=6, column=0, columnspan=2)

# Main window
root = tk.Tk()
root.title("Прямоовал")

# Canvas
canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Add shape button
add_shape_button = Button(root, text="Добавить фигуру", command=add_shape)
add_shape_button.pack()

root.mainloop()
