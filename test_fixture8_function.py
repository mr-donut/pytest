import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.linuxmint
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.skip
    def test_guest_should_see_shop_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("a.dropdown-toggle")

    @pytest.mark.xfail
    def test_guest_should_see_favorite_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")

    @pytest.mark.regression
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("input.btn.btn-default")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_oscar_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".col-sm-7>a")

#Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
# pytest -s -v -m smoke test_fixture8_function.py  -прогнать один помеченый
# pytest -s -v -m "smoke and linuxmint" test_fixture8_function.py  -прогнать несколько помеченных
# pytest -v test_fixture8_function.py    -прогнать все
# pytest -rX -v test_fixture8_function.py    -прогнать все и показать отчет по помеченному reason=
#регистрировать метки явно перед использованием через файл pytest.ini в корневой директории вашего тестового проекта