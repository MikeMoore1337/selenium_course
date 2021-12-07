import math
# Функция для рассчёта формулы на сайте
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
import time
from selenium import webdriver

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

    # Переключаемся на новую вкладку
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
