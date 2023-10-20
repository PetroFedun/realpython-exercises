# 1. Создайте список food, содержащий два элемента: "rice" и "beans".

food = ['rice', 'beans']

# 2. Присоедините к food строку "broccoli" методом .append().

food.append('broccoli')

# 3. Добавьте в food строки "bread" и "pizza" при помощи метода . extend ().

food.extend(['bread', 'pizza'])

# 4. Выведите первые два элемента списка food, используя функцию print()
# и синтаксис сегментов.

print(food[:2])

# 5. Выведите последний элемент food, используя функцию print() 
# и син­таксис сегментов.

print(food[-1])

# 6. Создайте список breakfast из строки "eggs, fruit,
# orange juice" при помощи строкового метода. split( ).

breakfast = 'eggs, fruit, orange juice'
breakfast_list = breakfast.split(', ')
print(breakfast_list)

# 7. Убедитесь в том, что breakfast содержит три элемента, при помощи
# функции len ()

len(breakfast_list)

# 8. Создайте генератором списка новый список lengths, содержащий длины
# всех строк из списка breakfast.

lengths = [len(p) for p in breakfast_list]

print(lengths)

# 9. Создайте кортеж data, содержащий два значения . Первым значением
# должен быть кортеж (1, 2), а вторым - кортеж (З, 4).

date = ((1,2), (3,4))

# 10. Напишите цикл for, который перебирает data и выводит сумму каждого
# вложенного кортежа. Результат должен выглядеть примерно так:
# Row 1 sum: 3
# Row 2 sum: 7

for q, d in enumerate(date, start=1):
    print(f'Row {q} sum: {sum(d)}')

# 11.Создайте список [ 4, З, 2, 1] и присвойте его переменной numbers.

number = [4, 3, 2, 1]

# 12.Создайте копию списка numbers с использованием записи [ : ].

copy_number = number

# 13.Отсортируйте список numbers в числовом порядке методом . sort ().

number.sort()
print(number)
