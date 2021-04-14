from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
# ссылка на задание https://stepik.org/lesson/181384/step/8?unit=156009

try:
    # в течение 15сек проверяем каждые 0.5сек, пока значение цены станет 100 долларов
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,"price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()
    # скроллим страницу до видимости кнопки Submit
    submit = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    # вычисляем и отправляем решение уравнения
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calculate(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    submit.click()

finally:
    # успеваем скопировать код за 1 секунду
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()