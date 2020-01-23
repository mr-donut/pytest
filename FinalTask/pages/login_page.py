from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPagesLocators
from selenium import webdriver
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        self.currrent_url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        assert self.browser.current_url, "login not in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.login_form = (By.CSS_SELECTOR, "#login_form")
        assert self.login_form, "Login form is Not exist!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.register_form = (By.CSS_SELECTOR, "#register_form")
        assert self.register_form, "Register form is not exist!"

    def register_new_user(self, email, password): #передаем 2 аргумента из вне
        # self.browser = webdriver.Chrome()
        # time.sleep(3)
        self.browser.find_element(*LoginPagesLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPagesLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPagesLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPagesLocators.REGISTER_BUTTON).click()