import time
from selenium import webdriver

browser = webdriver.Chrome()
# на этой ссылке скрипт успешно проходит
link = "http://suninjuly.github.io/registration1.html"
# на этой ссылке скрипт падает с ошибкой NoSuchElementException
#link = "http://suninjuly.github.io/registration2.html"

try:
    browser.get(link)
    time.sleep(1)
    # По плейсхолднеру можно найти так:
    # input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    # но не для этого задания
    input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
    input1.send_keys("1")
    input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
    input2.send_keys("2")
    input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
    input3.send_keys("3")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

# Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла