# Напишите программу first _letter.py, которая запрашивает у пользователя ввод
# с приглашением "Tell me your password: ".Затем программа определяет первую
# букву пользовательского ввода, преобразует ее к верхнему регистру и выводит ее.
# Например, если пользователь ввел "no", программа должна выдать следующий
# результат:
# The first letter you entered was: N

password = input('Tell me your password: ')
upper_password = password.upper()
print('The first letter you entered was: ' + upper_password[0])
