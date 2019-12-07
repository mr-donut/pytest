import pytest
from selenium import webdriver
import time
import math

def answer():
    return math.log(int(time.time()))
# print(answer())

@pytest.fixture(scope="function")
def browser():
    # print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
class TestSearch(object):
    def test_should_send_correct_answer(self, browser, link):
        l = {link}
        browser.get(l)
        browser.implicitly_wait(10)
        field = browser.find_element_by_css_selector(".textarea")
        field.send_keys(str(answer()))
        time.sleep(1)
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()
        time.sleep(5)
        x_element = browser.find_element_by_css_selector("pre.smart-hints__hint").text
        assert "Correct!" in x_element, 'не совпадает ответ!'
        print(x_element)