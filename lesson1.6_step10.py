from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('.first_block > .first_class.form-group > .first.form-control')
    input1.send_keys('Ivan')
    input2 = browser.find_element_by_css_selector('.first_block > .form-group.second_class > .form-control.second')
    input2.send_keys('Petrov')
    input3 = browser.find_element_by_css_selector('.form-control.third')
    input3.send_keys('example@email.com')
    input4 = browser.find_element_by_css_selector('.second_block > .first_class.form-group > .first.form-control')
    input4.send_keys('+79876543210')
    input5 = browser.find_element_by_css_selector('.second_block > .form-group.second_class > .form-control.second')
    input5.send_keys('Russia')
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert 'Congratulations! You have successfully registered!' == welcome_text

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
#