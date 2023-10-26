import pathlib

# 1. Создайте новый объект Path для файла с именем myfile.txt в папке
# my_folder/, находящейся в домашнем каталоге вашего компьютера. При­
# свойте этот объект Path переменной с именем file_path.

file_path = pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder/file.txt')

# 2. Проверьте, существует ли файл/каталог для пути, присвоенного file_path.

print(file_path.exists())

# 3. Выведите имя для пути, присвоенного file_path. Программа должна вывести my_file.txt.

print(file_path.name)

# 4. Выведите имя родительского каталога для пути, присвоенного file_path.
# Программа должна вывести my_folder.

print(file_path.parent.name)

# 5.Создайте в домашней папке новый каталог с именем my_folder2/.

pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder2').mkdir()

# 6.Создайте в my_folder2/ три файла:
# • file1.txt
# • file2.txt
# • image 1.png

pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder2/file1.txt').touch()
pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder2/file2.txt').touch()
pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder2/image1.png').touch()

# 7. Переместите файл image1.png в новый каталог images/, находящийся в каталоге my_folder2/.

pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder2/images/').mkdir()
pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder2/image1.png').replace(pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder2/images/image1.png'))

# 8.Удалите фaйл file1.txt.

pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder2/file1.txt').unlink()

# 9.Удалите каталог my_folder/.

folder = pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/my_folder2')

for item in folder.iterdir():
    if item.is_file():
        item.unlink()
    elif item.is_dir():
        for subitem in item.iterdir():
            subitem.unlink()
        item.rmdir()

folder.rmdir()

# 10. ЗАДАЧА: ПЕРЕМЕЩЕНИЕ ВСЕХ ГРАФИЧЕСКИХ ФАЙЛОВ В НОВЫЙ КАТАЛОГ
# В папке practice_files располагается вложенная папка с именем documents/. Она
# содержит несколько файлов и вложенных папок. Некоторые файлы хранят
# графические изображения - они имеют расширения .png, .gif или .jpg.
# Создайте в папке practice_files подпапку с именем images/, переместите в нее все
# графические файлы. Когда это будет сделано, в новой папке должны находиться четыре файла:
# • image1.png
# • image2.gif
# • imageЗ.png
# • image4jpg

documents_dir = pathlib.Path('/home/petro/practice_files/documents')
images_dir = pathlib.Path('/home/petro/practice_files/documents/images')
images_dir.mkdir(exist_ok=True)

for path in documents_dir.rglob("*.*"):
    if path.suffix.lower() in [".png", ".jpg", ".gif"]:
        path.replace(images_dir / path.name)

# 11. Запишите следующий текст в файл starships.txt, хранящийся в вашем домашнем каталоге:
# Discovery
# Enterprise
# Defiant
# Voyager
# Каждое слово должно располагаться в отдельной строке.

path = pathlib.Path('/home/petro/realpython-exercises/12. work_with_file/starships.txt')

with path.open(mode="w", encoding="utf-8") as file:
    text = file.write("Discovery\nEnterprise\nDefiant\nVoyager")

# 12. Прочитайте файл starhips.txt, созданный в упражнении 11, и выведите
# каждую строку текста в файле. В выводе не должно быть лишних пустых строк между словами.

with path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    print(text)

# 13. Прочитайте файл starhips.txt и выведите слова, начинающиеся с буквы D

with path.open(mode="r", encoding="utf-8") as file:
    for starship in file.readlines():
        if starship.startswith("D"):
            print(starship, end="")

