from selenium import webdriver
import time
import math
# ссылка на задание https://stepik.org/lesson/228249/step/6

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    time.sleep(1)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calculate(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    # выполнение JS скрипта для скролла страницы до видимости искомого элемента
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    submit = browser.find_element_by_css_selector("button[type='submit']")
    submit.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
