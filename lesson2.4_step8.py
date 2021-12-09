import time
import math
# Функция для рассчёта формулы на сайте
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Дожидаемся, когда цена дома уменьшится до $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    # Говорим Selenium проверять в течение 12 секунд и как только цена станет $100, кликаем Book
    button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()

    # Решаем уравнение
    x_el = browser.find_element_by_css_selector('span#input_value')
    x = x_el.text
    y = calc(x)

    # Вводим ответ в поле
    input1 = browser.find_element_by_css_selector('input[type="text"]')
    input1.send_keys(y)

    # Кликаем Submit
    button = browser.find_element_by_css_selector('button#solve')
    button.click()

except Exception as error:
   print(f'ERROR! Traceback: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
#