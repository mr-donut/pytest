from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest

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

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = BasePage(browser, login_link)
    page.open()