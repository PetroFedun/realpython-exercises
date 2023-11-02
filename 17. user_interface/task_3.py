import tkinter as tk

# 1. Напишите программу, которая выводит виджет Button шириной 50 тек­
# стовых единиц и высотой 25 текстовых единиц. Виджет должен иметь
# белый фон с синим текстом "Click here".

window = tk.Tk()
button = tk.Button(
    width=50, height=25, bg="white", fg="blue", text="Click here"
)
button.pack()
window.mainloop()

# 2. Напишите программу для вывода виджета Entry шириной 40 текстовых
# единиц, с белым фоном и черным текстом. Используйте метод . insert()
# для вставки в виджет Entry текста "What is your name?"

window = tk.Tk()
entry = tk.Entry(width=40)
entry.insert(0, "What is your name?")
entry.pack()
window.mainloop()
