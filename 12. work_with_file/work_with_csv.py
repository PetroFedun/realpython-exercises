import csv
import pathlib

# 1. Напишите программу, которая записывает следующий список списков
# в файл numbers.csv в вашем домашнем каталоге:

numbers = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15] 
]

file_path = pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/number.cvs')

with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(numbers)

# 2. Напишите программу, которая читает числа в файле numbers.csv из
# упражнения 1 в список списков целых чисел с именем numbers. Выведите
# прочитанный список списков. Результат должен выглядеть так:
# [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

numbers = []

with file_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(num) for num in row]
        numbers.append(int_row)

print(numbers)

# 3.Напишите программу, которая записывает следующий список словарей
# в фaйл favorite_colors.csv в вашем домашнем каталоге:
# favorite_colors = [
# {"name": "Joe", "favorite_color": "Ыuе"},
# {"name": "Anne", "favorite_color": "green"},
# {"name": "Bailey", "favorite_color": "red"},

favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]

file_path = pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/favorite_colors.csv')

with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "favorite_color"])
    writer.writeheader()
    writer.writerows(favorite_colors)

# 4. Напишите программу, которая читает данные из фaйлafavonte_colors.csv
# (см. упражнение 3) в список cлoвapeйfavonte_colors. Выведите список
# словарей. Результат должен выглядеть примерно так:
# [{"name": "Joe", "favorite_color": "Ыuе"},
# {"name": "Anne", "favorite_color": "green"},
# {"name": "Bailey", "favorite_color": "red"}]

favorite_colors = []

with file_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        favorite_colors.append(row)

print(favorite_colors)

# 5. ЗАДАЧА: СОЗДАНИЕ СПИСКА РЕКОРДОВ
# В папке practice_files находится файл CSV scores.csv с данными об игроках и их показателях. Первые несколько строк файла выглядят так:
# name, score
# LLCoolDave,23
# LLCoolDave,27
# red,12
# LLCoolDave,26
# tom123,26
# Напишите программу, которая читает данные из файла CSV и создает новый
# файл high_scores.csv, в котором каждая строка содержит имя игрока и его наи­ более высокий результат.
# Выходной файл CSV должен выглядеть примерно так:
# name,high_score
# LLCoolDave,27
# red,12
# tom123,26
# О_О,22
# Misha46,25
# Empiro,23
# МаххТ,25
# L33tH4x,42
# johnsmith,30

scores_csv_path = pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/scores.csv')

with scores_csv_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    scores = [row for row in reader]

high_scores = {}

for item in scores:
    name = item["name"]
    score = int(item["score"])
    if name not in high_scores:
        high_scores[name] = score
    else:
        if score > high_scores[name]:
            high_scores[name] = score

output_csv_file = pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/high_scores.csv')

with output_csv_file.open(mode="w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "high_score"])
    writer.writeheader()
    for name in high_scores:
        row_dict = {"name": name, "high_score": high_scores[name]}
        writer.writerow(row_dict)
