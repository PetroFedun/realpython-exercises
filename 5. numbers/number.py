# 1. Напишите программу, которая создает две переменные, numl и num2. При­
# свойте каждой целочисленный литерал 25000000 - с разделителями-под­
# черкиваниями и без. Выведите numl и num2 в разных строках.

num1 = 25000000
num2 = 25000_000
print(num1)
print(num2)

# 2. Напишите программу, которая присваивает литерал с плавающей точкой
# 175000. 0 переменной num с использованием экспоненциальной записи,
# после чего выводит num в интерактивном окне.

num = 175e3
print(num)

# 3. В интерактивном окне IDLE попробуйте найти наименьший показатель
# степени N, для которого 2e<N> (где <N> замените вашим числом) воз­вращает inf.

n = 2e308
print(n)

# 4. Напишите программу, которая предлагает пользователю ввести число,
# а затем выводит его округленным до двух цифр. Выполнение вашей про­
# граммы должно выглядеть примерно так:
# Enter а number: 5.432
# 5.432 rounded to 2 decimal places is 5.43

rounded_number = input('Enter a number: ')
print(f'{rounded_number} rounded to 2 decimal places is {round(float(rounded_number), 2)}')

# 5. Напишите программу, которая предлагает пользователю ввести число,
# а затем выводит абсолютное значение этого числа. Выполнение вашей
# программы должно выглядеть примерно так:
# Enter а number: -10
# The absolute value of -10 is 10.0

absolute_number = input('Enter a number: ')
print(f'The absolute value of {absolute_number} is {abs(int(absolute_number))}')

# 6. Напишите программу, которая предлагает пользователю ввести два чис­ла, используя
# input () дважды, а затем сообщает, является ли разность
# этих двух чисел целым числом. Выполнение вашей программы должно
# выглядеть примерно так:
# Enter а number: 1.5
# Enter another number: .5
# The difference between 1.5 and .5 is an integer? True!

num_1 = input('Enter a number: ')
num_2 = input('Enter another number: ')
print(f'The difference between {num_1} and {num_2} is an integer? {(float(num_1) + float(num2)).is_integer()}!')

# 7. Если пользователь вводит два числа, разность которых не является целым
# числом, вывод должен выглядеть примерно так:
# Enter а number: 1.5
# Enter another number: 1.0
# The difference between 1.5 and 1.0 is an integer? False!

num_1 = input('Enter a number: ')
num_2 = input('Enter another number: ')
print(f'The difference between {num_1} and {num_2} is an integer? {(float(num_1) + float(num2)).is_integer()}!')

# 8. Выведите результат вычисления з
# 3 ** .125 в формате с фиксированной
# точкой с тремя знаками в дробной части.

print(f'{3 ** .125:.3f}')

# 9. Выведите число 150000 как денежную сумму с разделением групп раз­
# рядов запятыми. Денежные суммы должны выводиться с двумя знаками
# в дробной части.

print(f'{150000:.2f}')

# 10. Выведите результат 2 / 10 в процентах без дробной части (то есть должно
# выводиться значение 20%).

print(f'{2/10:.0%}')
