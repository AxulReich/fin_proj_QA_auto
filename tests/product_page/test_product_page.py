from page_objects.product_page import ProductPage
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.basket_page import BasketPage
from page_objects.product_page_locators import ProductPageLocators as PPL
from constants import PRODUCTS, REGISTERED_USERS
import pytest


class TestProductPage():
    @pytest.mark.need_review_custom_scenarios
    @pytest.mark.parametrize('common_selector, element', ProductPage.COMMON_PAGE_ELEMENTS)
    def test_common_elements_exists(self, browser, common_selector, element):
        pp = ProductPage(driver=browser)
        pp.open()
        pp.is_common_elements_present(common_selector, element)

    @pytest.mark.need_review_custom_scenarios
    def test_basket_link_exist(self, browser):
        pp = ProductPage(driver=browser)
        pp.open()
        pp.basket_link_exist()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product = PRODUCTS[0]
        user = REGISTERED_USERS[0]

        page = MainPage(browser)
        page.open()
        page.go_to_login_or_register_page()

        page = LoginPage(browser)
        page.login_user(email=user[0], psw=user[1])

        page.search(product[1])
        page.find_element(PPL.get_product_selector_by_title(product[1])).click()

        page = ProductPage(driver=browser, url_name=product[0], title=product[1])
        page.add_product_to_basket()
        page.is_product_added()

    @pytest.mark.need_review_custom_scenarios
    @pytest.mark.parametrize('product_url_name, product_title', PRODUCTS)
    def test_guest_can_add_product_to_basket(self, browser, product_url_name, product_title):
        page = MainPage(browser)
        page.open()
        page.search(product_title)
        page.find_element(PPL.get_product_selector_by_title(product_title)).click()

        page = ProductPage(driver=browser, url_name=product_url_name, title=product_title)
        page.add_product_to_basket()
        page.is_product_added()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(driver=browser)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(driver=browser)
        page.should_be_empty_basket()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(driver=browser)
        page.open()
        page.go_to_login_or_register_page()
        page = LoginPage(driver=browser)
        page.is_page_registration_login_page()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        product = PRODUCTS[0]

        page = MainPage(browser)
        page.open()
        page.search(product[1])
        page.find_element(PPL.get_product_selector_by_title(product[1])).click()

        page = ProductPage(driver=browser, url_name=product[0], title=product[1])
        page.add_product_to_basket()
        page.is_product_added()