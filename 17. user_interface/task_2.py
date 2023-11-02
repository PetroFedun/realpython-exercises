import tkinter as tk

# 1.Используя Tkinter в интерактивном окне IDLE, создайте окно с виджетом
# Label, в котором выводится текст "GUis are great ! ".

root = tk.Tk()
root.title("Simple GUI")
label = tk.Label(root, text="GUIs are great!")
label.pack()
root.mainloop()

# 2.Повторите упражнение 1 с текстом "Python rocks!".

root = tk.Tk()
root.title("Simple GUI")
label = tk.Label(root, text="Python rocks!")
label.pack()
root.mainloop()

# 3.Повторите упражнение 1 с текстом "Engage!".

root = tk.Tk()
root.title("Simple GUI")
label = tk.Label(root, text="Engage!")
label.pack()
root.mainloop()
