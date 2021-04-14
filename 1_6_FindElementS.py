from selenium import webdriver
import time
# ссылка на задание https://stepik.org/lesson/138920/step/7 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/huge_form.html"

try:
    browser.get(link)
    time.sleep(1)
    elements = browser.find_elements_by_css_selector("input[type='text']")
    for element in elements:
        element.send_keys("1")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла