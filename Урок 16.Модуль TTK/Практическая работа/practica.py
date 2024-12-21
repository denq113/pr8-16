import tkinter as tk
from tkinter import ttk

# Function to change the canvas color
def change_color(event):
    selected_color = color_combobox.get()
    canvas.config(bg=selected_color)

# Main window
root = tk.Tk()
root.title("Combobox и холст")
root.geometry("300x300")

# Combobox with color options
colors = ["blue", "yellow", "green", "red", "white"]
color_combobox = ttk.Combobox(root, values=colors)
color_combobox.current(0)  # Set the default selected value
color_combobox.pack(pady=10)

# Bind the color selection event
color_combobox.bind("<<ComboboxSelected>>", change_color)

# Canvas to display the selected color
canvas = tk.Canvas(root, width=200, height=200, bg=colors[0])
canvas.pack(pady=10)

root.mainloop()
