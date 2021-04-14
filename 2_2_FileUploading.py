from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
#ссылка на задание https://stepik.org/lesson/228249/step/7?unit=200781

try:
    browser.get(link)
    # time.sleep(3)
    name = browser.find_element_by_name("firstname")
    name.send_keys("A")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("S")
    email = browser.find_element_by_name("email")
    email.send_keys("S")
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.dirname(__file__)
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    file_button = browser.find_element_by_id("file")
    file_button.send_keys(file_path)
    submit_button = browser.find_element_by_css_selector(".btn-primary")
    submit_button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()