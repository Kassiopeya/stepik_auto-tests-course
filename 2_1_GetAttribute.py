from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"
# ссылка на задание https://stepik.org/lesson/165493/step/7

try:
    browser = webdriver.Chrome()
    browser.get(link)
    chest = browser.find_element_by_id("treasure")
    chest_contain = chest.get_attribute("valuex")
    x = chest_contain
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    # выбор чекбокса "I'm the robot"
    checkbox_amzarobot = browser.find_element_by_css_selector("[type='checkbox']")
    checkbox_amzarobot.click()
    # выбор радиобаттона "Robot rule"
    radio_choice = browser.find_element_by_css_selector("[value='robots']")
    radio_choice.click()
    # нажатие Submit
    submit_all = browser.find_element_by_css_selector("[type='submit']")
    submit_all.click()
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()
