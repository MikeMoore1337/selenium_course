import pytest
import time
import math

from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():
#    @pytest.mark.xfail
    def test_answer1(self, browser):
        answer = math.log(int(time.time()))
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        time.sleep(5)
        input1 = browser.find_element_by_css_selector('.string-quiz__textarea')
        input1.send_keys(str(answer))
        button = browser.find_element_by_css_selector('.submit-submission')
        button.click()
        time.sleep(2)
        message = browser.find_element_by_css_selector('.smart-hints__hint')
        print('*****TEXT MESSAGE******\n' + message.text)
        assert "Correct!" == str(message.text)
#