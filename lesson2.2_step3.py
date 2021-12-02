from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    #link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим сумму чисел
    x_el = browser.find_element_by_css_selector('h2 .nowrap:nth-of-type(2)')
    x = x_el.text
    y_el = browser.find_element_by_css_selector('h2 .nowrap:nth-of-type(4)')
    y = y_el.text
    s = str(int(x) + int(y))

    # Инициализируем новый объект с тегом "select"
    select = Select(browser.find_element_by_tag_name('select#dropdown'))
    # Ищем вариант суммы чисел из списка
    select.select_by_value(s)

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