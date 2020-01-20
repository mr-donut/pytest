from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
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

    def register_new_user(self, email, password): #передаем 2 аргумента из вне?
        browser = webdriver.Chrome()
        # input_email = input("input your email \n")
        # input_password = input("input password, min.9 charaster \n")
        time.sleep(1)
        browser.find_element_by_css_selector("input#id_registration-email.form-control").send_keys(email)

        browser.find_element_by_css_selector("#id_registration-password1").send_keys(password)
        browser.find_element_by_css_selector("#id_registration-password2").send_keys(password)
        register_button = browser.find_element_by_css_selector('[name="registration_submit"]')
        register_button.click()