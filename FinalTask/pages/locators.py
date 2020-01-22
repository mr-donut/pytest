from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPagesLocators:
    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")

    LOGIN_REGISTER = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators:
    ADD_LINK = (By.CSS_SELECTOR, "#add_to_basket_form.add-to-basket")

    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1)")
    #"div.alert.alert-safe.alert-noicon.alert-success.fade.in div.alertinner"

class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")

    PROCCED_LINK = (By.CSS_SELECTOR, ".btn-primary.btn-block")