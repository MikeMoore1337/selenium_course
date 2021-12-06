import os
import time
from selenium import webdriver

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поля
    input1 = browser.find_element_by_css_selector('input[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input[name="email"]')
    input3.send_keys("example@email.com")

    # Загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector('[type="file"]')
    element.send_keys(file_path)

    # Кликаем Submit
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

except Exception as error:
   print(f'ERROR! Traceback: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
#