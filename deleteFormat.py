import os
import tkinter as tk
from tkinter import filedialog

def delete_files():
    folder_path = filedialog.askdirectory()
    file_format = entry.get()
    format_count = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_format):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                # Получаем формат файла (расширение)
                file_extension = os.path.splitext(file)[1]
                # Увеличиваем счетчик для данного формата
                format_count[file_extension] = format_count.get(file_extension, 0) + 1
    label.config(text="Файлы с форматом {} удалены".format(file_format))
    # Выводим информацию о количестве разных форматов
    format_info = "Форматы файлов удалены в папке:\n"
    for format, count in format_count.items():
        format_info += "{}: {}\n".format(format, count)
    format_label.config(text=format_info)

def count_formats():
    folder_path = filedialog.askdirectory()
    format_count = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            format_count[file_extension] = format_count.get(file_extension, 0) + 1
    format_info = "Форматы файлов в папке:\n"
    for format, count in format_count.items():
        format_info += "{}: {}\n".format(format, count)
    label.config(text=format_info)

# Создаем графический интерфейс с помощью tkinter
root = tk.Tk()
root.title("Удаление файлов")
root.geometry("350x250")

# Создаем кнопку "Узнать количество форматов в папке" и привязываем к ней функцию count_formats
count_button = tk.Button(root, text="Узнать количество форматов в папке", command=count_formats)
count_button.pack()

# Создаем метку для отображения выбранной папки
folder_label = tk.Label(root, text="")
folder_label.pack()

# Создаем метку и поле ввода для формата файла
format_label = tk.Label(root, text="Формат файла:")
format_label.pack()
entry = tk.Entry(root)
entry.pack()

# Создаем кнопку "Удалить" и привязываем к ней функцию delete_files
delete_button = tk.Button(root, text="Удалить", command=delete_files)
delete_button.pack()

# Создаем метку для вывода информации
label = tk.Label(root, text="")
label.pack()

root.mainloop()