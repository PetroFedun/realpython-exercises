# Повторите пример из этого раздела с извлечением результата броска, но также
# включите текущее время его получения с веб-страницы. Это время можно по­
# лучить из части строки внутри тега <р>, следующего после результата броска
# в НТМL-коде страницы.Повторите пример из этого раздела с извлечением результата броска, но также
# включите текущее время его получения с веб-страницы. Это время можно по­
# лучить из части строки внутри тега <р>, следующего после результата броска
# в НТМL-коде страницы.

from time import sleep
import mechanicalsoup

my_browser = mechanicalsoup.Browser()
for i in range(0, 6):
    page = my_browser.get("http://olympus.realpython.org/dice")
    html_text = page.soup
    dice_result_tag = html_text.select("#result")
    dice_result = dice_result_tag[0].text
    time_tag = page.soup.select("#time")
    time = time_tag[0].text
    time = time[: time.find(" - ")]
    print(f"Rolled a '{dice_result}' on {time}")
    if i < 5: 
        sleep(10)
