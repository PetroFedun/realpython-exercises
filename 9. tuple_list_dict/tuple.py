# 1.Создайте литерал кортежа с именем cardinal_numbers, содержащий
# строки "first", "second" и "third" в указанном порядке.

cardinal_number = ('first', 'second', 'third')

# 2.Используя индексирование и print (), выведите строку с индексом 1 из
# cardinal_numbers.

print(cardinal_number[1])

# 3. В одной строке кода распакуйте значения из cardinal_numbers в три но­
# вые строки с именами position1, position2 и positionЗ. Затем выведите
# каждое значение в отдельной строке.

pos1, pos2, pos3 = cardinal_number
print(pos1)
print(pos2)
print(pos3)

# 4. Используя функцию tuple() и строковый литерал, создайте кортеж
# с именем my _name, содержащий буквы вашего имени.

my_name = tuple('Petro')

# 5. Проверьте, входит ли символ "х" в my_name, при помощи ключевого
# слова in.

'x' in my_name

# 6.Используя синтаксис сегментов, создайте новый кортеж, содержащий
# все буквы my_name, кроме первой.

new_tuple = my_name[1:]
print(new_tuple)
