from selenium import webdriver
import time
import math
#ссылка на задание https://stepik.org/lesson/184253/step/4

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    start_button = browser.find_element_by_css_selector(".btn-primary")
    start_button.click()
    time.sleep(2)
    # соглашаемся с сообщением
    confirm = browser.switch_to.alert
    confirm.accept()
    # ищем икс и отправляем игрек
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calculate(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    submit_button = browser.find_element_by_css_selector(".btn-primary")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()