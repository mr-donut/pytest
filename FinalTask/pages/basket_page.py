from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def go_to_basket_link(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_link.click()
        print("Зашли в корзину")
        return BasketPage(browser=self.browser, url=self.browser.current_url)

    def should_be_goods_absence(self):
        assert not self.is_element_present(*BasketPageLocators.PROCCED_LINK), "Basket not empty!"

    def basket_empty_message(self):
        language = self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
        message = self.browser.find_element(By.CSS_SELECTOR, "#content_inner p").text

        assert str("basket is empty") in message, "Basket is not empty."
        assert str("basket is empty") in message, "Basket is not empty." if language == str("en") else "Language of the page not English!"
