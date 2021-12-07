import math
# Функция для рассчёта формулы на сайте
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
import time
from selenium import webdriver

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

    # Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # Решаем капчу
    x_el = browser.find_element_by_css_selector('span#input_value')
    x = x_el.text
    y = calc(x)

    # Вводим ответ в поле
    input1 = browser.find_element_by_css_selector('input[type="text"]')
    input1.send_keys(y)

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