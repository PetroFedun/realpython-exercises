from urllib.request import urlopen

# 1. Напишите программу, которая извлекает весь код HTML веб-страницы
# по адресу http:j/olympus.realpython.org/profiles/dionysus.

url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")

# 2. Используйте строковый метод . find () для вывода текста, следующего за
# Name: и Favorite Color: (не включая начальные пробелы или завершающие
# теги HTML, которые могут присутствовать в той же строке).

for tag in ["Name: ", "Favorite Color: "]:
    tag_start = html_text.find(tag) + len(tag)
    tag_end = html_text[tag_start:].find("<")
    print(html_text[tag_start : tag_start + tag_end].strip(" \n"))

# 3. Повторите предыдущее упражнение с регулярными выражениями . В конце
# каждого шаблона следует поставить знак < (начало тега HTML) или символ
# новой строки, а из полученного текста надо убрать все лишние пробелы
# и символы новой строки при помощи строкового метода . strip().

import re

for tag in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
    match_results = re.search(tag, html_text)
    result = re.sub(".*: ", "", match_results.group())
    print(result.strip(" \n<"))
