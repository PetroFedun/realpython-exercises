import sqlite3

# 1. Создайте новую базу данных, содержащую таблицу Roster. Таблица со­
# стоит из трех полей: Name, Species и Age. Столбцы Name и Species должны
# быть текстовыми, а столбец Age должен быть целочисленным полем.

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')

# 2. Заполните созданную таблицу следующими значениями:
               
data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

# 3. Обновите поле Name записи Jadzia Dax, чтобы оно содержало значение
# Ezri Dax.
               
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

# 4. Выведите значения Name и Age для всех строк данных, у которых поле
# Species содержит значение Bajoran.

cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
rows = cursor.fetchall()

for row in rows:
    print("Name:", row[0])
    print("Age:", row[1])

conn.commit()
conn.close()
