import tkinter as tk
from tkinter import PhotoImage
import random

def move_smiley():
    # Generate random coordinates within the window
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    smiley_width = smiley_button.winfo_width()
    smiley_height = smiley_button.winfo_height()

    x = random.randint(0, window_width - smiley_width)
    y = random.randint(0, window_height - smiley_height)

    smiley_button.place(x=x, y=y)

    # Optionally resize the window randomly
    new_width = random.randint(200, 500)
    new_height = random.randint(200, 500)
    root.geometry(f"{new_width}x{new_height}")

# Main window
root = tk.Tk()
root.title("Смайлик")
root.geometry("400x400")

# Load the smiley image
smiley_image = PhotoImage(file="smile.gif")  # Make sure the file exists in the working directory

# Create a button with the smiley image
smiley_button = tk.Button(root, image=smiley_image, command=move_smiley)
smiley_button.place(x=150, y=150)  # Initial position

root.mainloop()
