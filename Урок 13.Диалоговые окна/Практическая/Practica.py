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

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

open_button = tk.Button(button_frame, text="Открыть", command=open_file)
open_button.grid(row=0, column=0, padx=5)

save_button = tk.Button(button_frame, text="Сохранить", command=save_file)
save_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Очистить", command=clear_text)
clear_button.grid(row=0, column=2, padx=5)

root.mainloop()
