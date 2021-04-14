from selenium import webdriver
import time
import math
#ссылка на задание https://stepik.org/lesson/165493/step/5

link = "http://suninjuly.github.io/math.html"
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
    radiobutton.click()
    submit = browser.find_element_by_css_selector("button[type='submit']")
    submit.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()