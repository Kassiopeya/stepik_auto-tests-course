from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
# ссылка на задание https://stepik.org/lesson/228249/step/3

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element_by_id("num1").text
    b = browser.find_element_by_id("num2").text
    y = int(a) + int(b)
    value = str(y)

    dropdown = Select(browser.find_element_by_tag_name("select"))
    dropdown.select_by_visible_text(value)

    submit_button = browser.find_element_by_css_selector(".btn-default")
    submit_button.click()

finally:
    # успеваем скопировать код за 6 секунд
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()
