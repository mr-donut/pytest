import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")







@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin(object):
    def test_guest_should_see_oscar_link(self, browser, language):

        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector(".col-sm-7>a")
        # этот тест запустится 2 раза

    # def test_guest_should_see_navbar_element(self, browser, language):
          # этот тест тоже запустится дважды

# Напишем тест, который проверит, что для сайта с русским и английским языком будет отображаться ссылка на форму логина.
# Передадим в наш тест ссылки на русскую и английскую версию главной страницы сайта.
# В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться, и список значений параметра.
# В самом тесте наш параметр тоже нужно передавать в качестве аргумента.
# Обратите внимание, что внутри декоратора имя параметра оборачивается в кавычки, а в списке аргументов теста кавычки не нужны.