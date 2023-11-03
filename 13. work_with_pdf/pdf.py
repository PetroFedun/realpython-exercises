import pathlib
from PyPDF2 import PdfReader

# 1. В папке practice_files главы 14 присутствует файл PDF с именем zen.pdf.
# Создайте экземпляр PdfFileReader для этого файла PDF.

pdf_path = pathlib.Path('/home/petro/Documents/js.pdf')

# 2. Используя экземпляр PdfFileReader из упражнения 1, выведите общее
# количество страниц в файле PDF.

pdf = PdfReader(str(pdf_path))
print(len(pdf.pages))

# 3. Выведите текст первой страницы файла PDF из упражнения 1.

first_page = pdf.pages[0]
text = first_page.extract_text()
print(text)
