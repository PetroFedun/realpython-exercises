# 1.Выведите строку, внутри которой используется двойная кавычка.

print('One old man say "This is bullshit"')

# 2.Выведите строку, внутри которой используется апостроф.

print("can't")

# 3.Выведите многострочный текст с сохранением пробелов.

print('''Lorem Ipsum is simply dummy text of the printing and typesetting industry.
      Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
      when an unknown printer took a galley of type and scrambled it to make a type specimen book.''')

# 4.Выведите строку, которая определяется в многострочном формате, но
# выводится в одной строке.

print("Lorem Ipsum is simply dummy text of the printing and typesetting industry. \
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \
when an unknown printer took a galley of type and scrambled it to make a type specimen book.")

# 5.Создайте строку и выведите ее длину при помощи функции len ()

print(len('Some random text'))

# 6.Создайте две строки, выполните их конкатенацию и выведите получен­
# ную строку.

print('Petro' + 'Fedun')

# 7. Создайте две строки, воспользуйтесь конкатенацией для добавления
# пробела между ними и выведите результат.

print('Petro' + ' ' + 'Fedun')

# 8. Выведите строку "zing", используя синтаксис срезов для определения
# правильного диапазона символов в строке "bazinga ".

print('bazinga'[2:6])

# 9. Напишите программу, которая преобразует следующие строки к нижне­
# му регистру: "Animals", "Badger", "Нопеу Вее", "Honey Badger". Каждый
# результат преобразования должен выводиться с новой строки.

print('Animals'.lower())
print('Badger'.lower())
print('Ноnеу Вее'.lower())

# 10. Повторите упражнение 9, но преобразуйте каждую строку к верхнему
# регистру, а не к нижнему.

print('Animals'.upper())
print('Badger'.upper())
print('Ноnеу Вее'.upper())

# 11. Напишите программу, которая удаляет пропуски из следующих строк,
# а затем выводит полученные результаты:

string1 = '     Filet Mignon'
string2 = 'Brisket     '
string3 = '  Cheeseburger    '

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

# 12. Напишите программу, которая выводит результат вызова . start-
# swith ( "Ье") для каждой из следующих строк:

str1 = 'Becomes'
str2 = 'becomes'
str3 = 'BEAR'
str4 = 'bEautiful'

print(str1.startswith('be'))
print(str2.startswith('be'))
print(str3.startswith('be'))
print(str4.startswith('be'))

# 13. Используя строки из упражнения 4, напишите программу, которая ис­
# пользует строковые методы для изменения каждой строки, чтобы вызов
# . startswith( "Ье") возвращал True для всех строк.

str1 = str1.lower()
str2 = str2.lower()
str3 = str3.lower()
str4 = str4.lower()

print(str1.startswith('be'))
print(str2.startswith('be'))
print(str3.startswith('be'))
print(str4.startswith('be'))

# 14. Напишите программу, которая получает ввод от пользователя и воспро­
# изводит его на экране.

prompt = input('Write anything here: ')
print(prompt)

# 15. Напишите программу, которая получает ввод от пользователя и выводит
# его в нижнем регистре.

response = input('What should i shout? ')
shouted_response = response.upper()
print(shouted_response)

# 16. Напишите программу, которая получает ввод от пользователя и выводит
# количество содержащихся в нем символов.

rando_user_str = input('Enter your string: ')
print(len(rando_user_str))

# 17. Создайте строку, содержащую целое число. Преобразуйте строку в целое
# число вызовом int(). Чтобы убедиться в том, что новый объект дей­
# ствительно является числом, умножьте его на другое число и выведите
# результат.

random_str = '12'
random_str = int(random_str)
print(random_str * 12)

# 18. Повторите предыдущее упражнение, но используйте число с плавающей
# точкой и функцию float ( )

random_num = '12'
random_str = float(random_str)
print(random_str * 12)

# 19. Создайте строку и целое число. Выведите их рядом друг с другом одной
# командой print при помощи str( ).

string_1 = 'Aaaa'
number1 = 10
print(string_1 + str(number1))

# 20. Напишите программу, которая дважды вызывает input () для получения
# двух чисел от пользователя, перемножает эти числа и выводит результат.
# Если пользователь вводит 2 и 4, программа должна вывести следующий
# текст:
# The product of 2 and 4 is 8.0.

num_1 = input('Enter your first number here: ')
num_2 = input('Enter your second number here: ')
print('The product of ' + str(num_1) + ' and ' + str(num_2) + ' is ' + str(float(num_1) * float(num_2)))

# 21. Создайте переменную с плавающей точкой weight, содержащую значение
# 0. 2, и строковый объект animal со значением "newt". Выведите следующую
# строку с этими переменными, используя только конкатенацию строк:
# 0.2 kg is the weight of the newt.

weight = 0.2
animal = 'newt'
print(str(weight) + ' kg is the weight of the ' + str(animal))

# 22. Выведите ту же строку с использованием метода . format () и пустых
# заполнителей {}.

print('{} kg is the weight of the {}'.format(weight, animal))

# 23. Выведите ту же строку с использованием синтаксиса f-строк.

print(f'{weight} kg is the weight of the {animal}')

# 24. В одной строке кода выведите результат вызова. find() для поиска под­
# строки "а" в строке "ААА". Результат должен быть равен -1.

a = 'AAA'
print(a.find('a'))

# 25. Замените каждое вхождение символа "s" на "х" в строке "Somebody said
# something to Samantha."

somebody = 'Somebody said something to Samantha'
print(somebody.replace('s', 'x'))

# 26. Напишите программу, которая запрашивает у пользователя ввод функ­ цией input()
# и выводит результат вызова .find() для поиска конкретной
# буквы во введенном тексте.

text = input('Write some text here: ')
find_letter = input('Write letter which need to find: ')
print(text.find(find_letter))
