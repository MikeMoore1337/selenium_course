import math

# Функция для рассчёта формулы на сайте
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Используем атрибут .text для найденного элемента
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # Рассчитываем и указываем значение "y"
    input1 = browser.find_element_by_css_selector('input[type="text"]')
    input1.send_keys(y)

    # Отмечаем чекбокс I'm the robot
    option1 = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    option1.click()

    # Выбираем радиобаттон Robots rule
    option2 = browser.find_element_by_css_selector('[value="robots"]')
    option2.click()

    # Кликаем Submit
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

except Exception as error:
   print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#