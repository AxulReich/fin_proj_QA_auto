from page_objects.base_page import BasePage
from page_objects.mixin_page import PageHeaderMixin
from page_objects.login_page_locators import LoginPageLocators as LPL
import allure


class LoginPage(PageHeaderMixin, BasePage):
    def __init__(self, driver, page_path='/accounts/login/'):
        """
        :param driver:
        :param url_name: if url_name was not passed instance open main catalogue! else open product page
        """
        super().__init__(driver)
        self._page_path = page_path

    @allure.step('enter user')
    def login_user(self, email: str, psw: str):
        self.find_element(LPL.login_email_address_form).send_keys(email)
        self.find_element(LPL.login_password_form).send_keys(psw)
        self.find_element(LPL.login_confirm_button).click()
        self.wait_until_element_invisible(LPL.login_form)

    @allure.step('Register user')
    def guest_registration(self, email: str, psw1: str, psw2: str):
        self.find_element(LPL.registration_email_form).send_keys(email)
        self.find_element(LPL.registration_password_form).send_keys(psw1)
        self.find_element(LPL.registration_password_confirm_form).send_keys(psw2)
        self.find_element(LPL.registration_confirm_button).click()
        self.wait_until_element_invisible(LPL.registration_form)

    def is_page_registration_login_page(self):
        assert '/accounts/login/' in self.url, "Incorrect link!"


if __name__ == "__main__":
    from constants import REGISTERED_USERS
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    browser = webdriver.Chrome()
    bp = LoginPage(driver=browser)
    bp.open()
    bp.guest_registration(email="fsffaef@ssef.com", psw1='fwewfAEwf6', psw2='fwewfAEwf6')
    time.sleep(100)