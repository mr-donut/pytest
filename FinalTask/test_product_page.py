from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import pytest

import time

@pytest.mark.skip
def test_guest_should_see_add_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = ProductPage(browser, link)
    page.open()

@pytest.mark.skip
def test_guest_should_see_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(2)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(5)
    page.should_be_message()
    page.compare_the_basket_price()
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = BasePage(browser, login_link)
    page.open()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.browser = browser
        self.page = LoginPage(browser, link)
        self.page.open()
        # time.sleep(2)
        self.page.register_new_user(str(email), str(password))
        self.page.should_be_authorized_user()


    def test_user_can_add_product_to_basket(browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        browser.implicitly_wait(2)
        page.should_be_message()
        page.compare_the_basket_price()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()