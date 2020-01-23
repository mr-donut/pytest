from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_should_see_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  #открываем страницу
        login_page = page.go_to_login_page()
        login_page.should_be_login_page() #выполняем метод страницы - переходим на страницу логина

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_goods_absence()
    page.basket_empty_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_goods_absence()
    page.basket_empty_message()