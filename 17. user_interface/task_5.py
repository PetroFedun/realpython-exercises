# 1. Напишите программу, которая выводит одну кнопку с цветом фона по
# умолчанию и черным текстом "Click me". Когда пользователь щелкнет
# на кнопке, ее фон должен окрашиваться в цвет, случайным образом вы­
# бранный из следующего списка:
# ["red", "orange", "yellow","blue", "green", "indigo", "violet"]

import random
import tkinter as tk


def change_bg_color():
    color = random.choice(
        ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]
    )
    button["bg"] = color


window = tk.Tk()
button = tk.Button(text="Click me", command=change_bg_color)
button.pack()
window.mainloop()

# 2. Напишите программу, моделирующую бросок игрального кубика. В про­
# грамме должна быть одна кнопка с текстом "Roll". Когда пользователь
# щелкает на кнопке, должно выводиться случайное цел.:ое число от 1 до 6.

import random
import tkinter as tk


def roll():
    lbl_result["text"] = str(random.randint(1, 6))


window = tk.Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

btn_roll = tk.Button(text="Roll", command=roll)
lbl_result = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

window.mainloop()
