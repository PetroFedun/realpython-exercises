import mechanicalsoup
# browser = mechanicalsoup.Browser()
# url = "http://olympus.realpython.org/login"
# page = browser.get(url)
# print(page.soup)
# 1. Используйте MechanicalSoup для предоставления правильного имени
# пользователя ("zeus") и пароля ("ThunderDude") форме авторизации,
# находящейся по адресу http.j/olympus.realpython.org/login.

browser = mechanicalsoup.Browser()
login_url = "http://olympus.realpython.org/login"
login_page = browser.get(login_url)
login_html = login_page.soup
form = login_html.form
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"
profiles_page = browser.submit(form, login_page.url)


# 2. Выведите заголовок текущей страницы, чтобы убедиться, что вы были
# перенаправлены на страницу /profiles.

title = profiles_page.soup.title
print(f"Title: {title.text}")

# 3. Используйте MechanicalSoup для возвращения к странице входа (верни­
# тесь к предыдущей странице).

login_page = browser.get(login_url)
login_title = login_page.soup.title
print(f"Title: {login_title.text}")

# 4. Введите в форме авторизации неправильное имя пользователя и пароль,
# а затем найдите в НТМL-коде возвращенной веб-страницы текст «Wгong
# username or password!~, чтобы убедиться в том, что попытка входа за­
# вершилась неудачей.

form = login_html.form
form.select("input")[0]["value"] = "wrong"
form.select("input")[1]["value"] = "password"
error_page = browser.submit(form, login_page.url)
if error_page.soup.text.find("Wrong username or password!") != -1:
    print("Login Failed.")
else:
    print("Login Successful.")
