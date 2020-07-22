from page_objects.base_page import BasePage
from page_objects.login_page_locators import LoginPageLocators as LPL
import allure
import time


class LoginPage(BasePage):
    _page_path = '/accounts/login/'

    @allure.step('Register user')
    def registration(self, email: str, psw1: str, psw2: str):
        self.find_element(LPL.registration_email_form).send_keys(email)
        self.find_element(LPL.registration_password_form).send_keys(psw1)
        self.find_element(LPL.registration_password_confirm_form).send_keys(psw2)
        self.find_element(LPL.registration_confirm_button).click()
        self.wait_until_element_invisible(LPL.registration_confirm_button)