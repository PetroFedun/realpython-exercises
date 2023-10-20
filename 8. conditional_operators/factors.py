# Напишите программу которая запрашивает у пользователя положи­
# тельное целое число, а затем выводит список множителей этого числа. Пример
# запуска программы с выводом результата:
# Enter а positive integer: 12
# 1 is а factor of 12
# 2 is а factor of 12
# 3 is а factor of 12
# 4 is а factor of 12
# 6 is а factor of 12
# 12 is а f actor of 12

number = int(input('Enter а positive integer: '))

for d in range(1, number + 1):
  if number % d == 0:
      print(f'{d} is a factor of {number}')
