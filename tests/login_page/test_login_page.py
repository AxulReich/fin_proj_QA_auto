from page_objects.login_page import LoginPage
from constants import REGISTERED_USERS
import pytest


class TestLoginPage():
    @pytest.mark.need_review_custom_scenarios
    @pytest.mark.parametrize('common_selector, element', LoginPage.COMMON_PAGE_ELEMENTS)
    def test_common_elements_exists(self, browser, common_selector, element):
        lp = LoginPage(driver=browser)
        lp.open()
        lp.is_common_elements_present(common_selector, element)

    @pytest.mark.need_review_custom_scenarios
    def test_basket_link_exist(self, browser):
        lp = LoginPage(driver=browser)
        lp.open()
        lp.basket_link_exist()

    @pytest.mark.need_review_custom_scenarios
    @pytest.mark.parametrize(
        'test_email, pwd', [
            pytest.param('free', 'xxxXXX1234', id='free email'),
            pytest.param('company', 'xxxXXX1234', id='Company email'),
        ], indirect=['test_email']
    )
    def test_valid_registration(self, browser, test_email, pwd):
        lp = LoginPage(driver=browser)
        lp.open()
        lp.guest_registration(test_email, pwd, pwd)

    @pytest.mark.need_review_custom_scenarios
    @pytest.mark.parametrize('test_email, pwd', REGISTERED_USERS)
    def test_valid_login(self, browser, test_email, pwd):
        lp = LoginPage(driver=browser)
        lp.open()
        lp.login_user(test_email, pwd)



