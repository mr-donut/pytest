from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPagesLocators:
    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")

    LOGIN_REGISTER = (By.CSS_SELECTOR, "#login_form")