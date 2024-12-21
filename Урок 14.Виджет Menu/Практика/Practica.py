import tkinter as tk
from tkinter import messagebox, filedialog

def open_file():
    try:
        file_path = filedialog.askopenfilename(title="Открыть файл")
        if not file_path:
            raise FileNotFoundError("Файл не выбран.")
        with open(file_path, 'r') as file:
            text_field.delete("1.0", tk.END)
            text_field.insert(tk.END, file.read())
    except FileNotFoundError as e:
        messagebox.showinfo("Ошибка", str(e))

def save_file():
    try:
        file_path = filedialog.asksaveasfilename(title="Сохранить файл")
        if not file_path:
            raise FileNotFoundError("Файл не сохранён.")
        with open(file_path, 'w') as file:
            file.write(text_field.get("1.0", tk.END))
    except FileNotFoundError as e:
        messagebox.showinfo("Ошибка", str(e))

def clear_text():
    if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите очистить текст?"):
        text_field.delete("1.0", tk.END)

# Main window
root = tk.Tk()
root.title("Работа с файлами")

# Text field
text_field = tk.Text(root, wrap="word", width=50, height=20)
text_field.pack(padx=10, pady=10)

# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

# Context menu for text field
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Очистить", command=clear_text)

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

text_field.bind("<Button-3>", show_context_menu)  # Right-click to show context menu

root.mainloop()
