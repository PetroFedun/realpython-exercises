from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

# 1. Напишите программу, которая извлекает весь НТМ L-код веб-страницы
# http.j/olympus.realpython.org/profiles.

url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())

# 2. Используя Beautiful Soup, выделите список всех ссылок на странице -
# проведите поиск тегов HTML с именем а и получите значение атрибута
# href для каждого тега.

all_links = []
for a_tag in soup.find_all("a"):
    link = a_tag.get("href")
    all_links.append(link)

print(all_links)

# 3. Извлеките НТМL-код каждой страницы в списке - добавьте полный
# путь к файлу и выведите текст (без тегов HTML) на каждой странице,
# используя метод . get_text () из библиотеки Beautiful Soup.

for link in all_links:
    full_url = f"http://olympus.realpython.org{link}"
    response = requests.get(full_url)
    page_text = response.text
    page_soup = BeautifulSoup(page_text, "html.parser")
    text_without_tags = page_soup.get_text()
    
    print(f"URL: {full_url}\n")
    print(text_without_tags)
    print("=======================================")
