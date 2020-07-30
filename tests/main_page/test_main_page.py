from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from constants import LANGUAGES
import pytest


class TestMainPage:
    @pytest.mark.need_review_custom_scenarios
    @pytest.mark.parametrize('common_selector, element', MainPage.COMMON_PAGE_ELEMENTS)
    def test_common_elements_exists(self, browser, common_selector, element):
        page = MainPage(driver=browser)
        page.open()
        page.is_common_elements_present(common_selector, element)

    @pytest.mark.need_review_custom_scenarios
    def test_basket_link_exist(self, browser):
        mp = MainPage(driver=browser)
        mp.open()
        mp.basket_link_exist()

    @pytest.mark.need_review_custom_scenarios
    def test_guest_can_open_login_page_from_main_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_or_register_page()
        page = LoginPage(browser)
        page.is_page_registration_login_page()

    @pytest.mark.need_review_custom_scenarios
    @pytest.mark.parametrize('language', LANGUAGES)
    def test_can_change_language_from_main_page(self, browser, language):
        mp = MainPage(browser)
        mp.open()
        mp.change_language(language)
        mp.is_language_changed(language)
