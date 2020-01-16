from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPagesLocators:
    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")

    LOGIN_REGISTER = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators:
    ADD_LINK = (By.CSS_SELECTOR, "#add_to_basket_form.add-to-basket")

    BASKET_LINK = (By.CSS_SELECTOR, "#content_inner")