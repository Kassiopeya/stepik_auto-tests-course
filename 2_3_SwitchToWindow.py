from selenium import webdriver
import time
import math

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
# ссылка на задание https://stepik.org/lesson/184253/step/6

try:
    browser.get(link)
    flying_button = browser.find_element_by_css_selector(".trollface")
    flying_button.click()
    #переключаемся в окно с конкретным названием
    browser.switch_to.window(browser.window_handles[1])
    # ищем икс и отправляем игрек
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calculate(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    submit_button = browser.find_element_by_css_selector(".btn-primary")
    submit_button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()