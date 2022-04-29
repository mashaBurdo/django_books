from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

try:
    10/0
# если блоком try сгенерировано исключение
except Exception as e:
    # печатаем тип и текст ошибки на консоль
    print(type(e).__name__, e)
    # создаем драйвер чтобы можно было управлять браузером
    driver = webdriver.Chrome(service=Service("/usr/lib/chromium-browser/chromedriver"))
    # при помощи драйвера открываем поисковик гугл
    driver.get("https://www.google.com/")
    # получаем поле, в которое можно ввести запрос
    inputElement = driver.find_element(by=By.NAME, value="q")
    # вводим наш запрос (тип и текст ошибки)
    inputElement.send_keys(str(type(e).__name__)+' '+str(e), )
    # жмем enter чтобы получить результаты
    inputElement.send_keys(Keys.ENTER)

    # получаем html-тэги, в которых содержатся адреса сайтов с результатами
    cite_tags = driver.find_elements(by=By.TAG_NAME, value="cite")
    # итерируемся по этим сайтам
    for cite in cite_tags:
        # получаем ссылку на сайт
        cite_link = cite.text[:cite.text.find(' ')]
        # если это stackoverflow (там обычно самые толковые ответы)
        if cite_link == "https://ru.stackoverflow.com":
            # то заходим туда и видим ответ
            cite.click()
            # Ура! Теперь каждый раз, как только блоком try будет сгенерирована ошибка - в браузере с
            # сразу появится решение


