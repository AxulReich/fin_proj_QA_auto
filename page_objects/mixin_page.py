from selenium.webdriver.support.ui import Select
import allure
import pytest

from page_objects.base_page import BasePage
from page_objects.mixin_locators import PageHeaderLocators as PHL


class PageHeaderMixin(BasePage):
    """
    In this class implemented methods for interaction with page elements were included at all pages
    """
    COMMON_PAGE_ELEMENTS = [
        (PHL.login_link, 'login link)'),
        (PHL.drop_down_language_list, 'drop down language list'),
        (PHL.language_change_button, "language change button"),
        (PHL.search_field, "search field"),
        (PHL.search_button, 'search button'),
        (PHL.main_page_link, 'main page link')
    ]

    def is_common_elements_present(self, common_selector, element):
        assert self.is_element_present(common_selector), f"{element} is not represented!"

    def basket_link_exist(self):
        assert self.is_element_present(PHL.basket_page_link), "Basket link is not presented!"

    def is_language_changed(self, language):
        assert self.get_language == language, "link from drop-down language change menu referencing to incorrect page"

    @allure.step('Search product')
    def search(self, search_text: str):
        self.find_element(PHL.search_field).send_keys(search_text)
        self.find_element(PHL.search_button).click()

    def go_to_login_or_register_page(self):
        self.find_element(PHL.login_link).click()

    def go_to_basket_page(self):
        self.find_element(PHL.basket_page_link).click()

    def go_to_main_page(self, language='en-gb'):
        self.find_element(PHL.get_oscar_label_main_page_link_selector(language)).click()

    @allure.step('Change language')
    def change_language(self, language='en-gb'):
        select = Select(self.find_element(PHL.drop_down_language_list))
        select.select_by_value(language)
        self.find_element(PHL.language_change_button).click()


if __name__ == "__main__":
    from selenium import webdriver
    browser = webdriver.Chrome()
    mp = PageHeaderMixin(driver=browser)
    mp.open()

