import math
# Функция для рассчёта формулы на сайте
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
import time

try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Считаем значение для переменной x и мат.функцию от x
    x_el = browser.find_element_by_css_selector('span#input_value')
    x = x_el.text
    y = calc(x)

    # Скроллим страницу вниз
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Вводим ответ в поле
    input1 = browser.find_element_by_css_selector('input[type="text"]')
    input1.send_keys(y)

    # Выбираем  checkbox "I'm the robot"
    option1 = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    option1.click()

    # Переключаем radiobutton "Robots rule!"
    option2 = browser.find_element_by_css_selector('[id="robotsRule"]')
    option2.click()

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