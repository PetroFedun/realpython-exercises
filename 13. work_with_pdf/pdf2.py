import pathlib
from PyPDF2 import PdfWriter, PdfReader

pdf_path = pathlib.Path('/home/petro/Documents/js.pdf')
pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

# 1. Извлеките последнюю страницу из файла Pride_ and_Prejudice.pdf и со­
# храните ее в файле last_yage.pdf, находящемся в домашнем каталоге.

last_page = pdf_reader.pages[-1]
pdf_writer.add_page(last_page)
output_pdf_path = pathlib.Path('/home/petro/Documents/last_page.pdf')
with open(output_pdf_path, 'wb') as output_pdf_file:
    pdf_writer.write(output_pdf_file)

# 2. Извлеките из файла Pride_and_Prejudice.pdf все страницы с четными
# индексами (не номерами страниц!) и сохраните их в новом файле every_
# other_yage.pdf в домашнем каталоге.

num_pages = len(pdf_reader.pages)

for n in range(num_pages):
    if n % 2 == 0:
        page = pdf_reader.pages[n]
        pdf_writer.add_page(page)

with open(output_pdf_path, 'wb') as output_pdf_file:
    pdf_writer.write(output_pdf_file)

# 3. Разбейте файл Pride_and_Prejudice.pdf на два новых файла PDF. Пер­
# вый должен содержать первые 150 страниц, а второй - все оставшиеся
# страницы. Сохраните оба файла в домашнем каталоге с именами part_ 1.
# pdf и part_2.pdf.

part1_writer = PdfWriter()
part2_writer = PdfWriter()

part1_pages = pdf_reader.pages[:150]
part2_pages = pdf_reader.pages[150:]

for page in part1_pages:
    part1_writer.add_page(page)

for page in part2_pages:
    part2_writer.add_page(page)

part1_output_path = pathlib.Path('/home/petro/Documents/part_1.pdf')
with part1_output_path.open(mode="wb") as part1_output_file:
    part1_writer.write(part1_output_file)

part2_output_path = pathlib.Path('/home/petro/Documents/part_2.pdf')
with part2_output_path.open(mode="wb") as part2_output_file:
    part2_writer.write(part2_output_file)
