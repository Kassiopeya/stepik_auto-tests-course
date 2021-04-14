from selenium import webdriver
import time

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

try:
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element_by_id("button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
