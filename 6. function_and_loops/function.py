# 1. Напишите функцию cube (), которая получает один числовой параметр
# и возвращает значение указанного числа в третьей степени. Протести­руйте функцию -
# вызовите cube() для нескольких разных чисел и вы­
# ведите результаты.

def cube(num):
    return num ** 3

print(cube(3)) # 27
print(cube(5)) # 125
print(cube(6)) # 216

# 2. Напишите функцию greet( ), которая получает один строковый параметр
# с именем name и выводит текст «Hello <name>!», где <name> заменяется
# значением параметра name.

def greet(name):
    print(f'Hello {name}!')

greet('Petro')