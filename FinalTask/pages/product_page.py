from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_to_basket(self):
        add_link = self.browser.find_element(*ProductPageLocators.ADD_LINK)
        add_link.click()

    def should_be_goods_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_LINK), "Goods link is not presented"

    def should_be_message(self):
        product_name = self.browser.find_element(By.CSS_SELECTOR, ".col-sm-6.product_main").text #div.col-sm-6:nth-child(2)
        message_product_name = self.browser.find_element(By.CSS_SELECTOR, ".alertinner strong").text
        assert str(message_product_name) in str(product_name), \
            "Message not matched with product name"

    def compare_the_basket_price(self):
        message_basket_price = self.browser.find_element(By.CSS_SELECTOR, ".alertinner p strong").text
        basket_price = self.browser.find_element(By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs").text
        assert str(message_basket_price) in str(basket_price), \
            "Message not matched with product name"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

#   Теперь в этом же классе реализуем метод ............, в котором будем перехватывать исключение.
#   В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
#   Чтобы перехватывать исключение, нужна конструкция try/except:
#   def is_element_present(self, how, what):
#       try:
#           self.browser.find_element(how, what)
#       except (имя исключения):
#           return False
#       return True
#   Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:
#   from selenium.common.exceptions import имя_исключения