# Напишите программу exponent.py, которая получает от пользователя два числа
# и выводит результат возведения первого числа в степень, заданную вторым числом.
# Результат выполнения программы должен выглядеть примерно так (с вводом
# от пользователя):
# Enter а base: 1.2
# Enter an exponent: 3
# 1.2 to the power of 3 = 1.7279999999999998

base = input('Enter a base: ')
exponent = input('Enter an exponent: ')
print(f'{base} to the power of {exponent} = {float(base) ** float(exponent)}')
