from page_objects.login_page import LoginPage
import pytest


class TestLoginPage():
    def test_login_link_exist(self, browser):
        lp = LoginPage(driver=browser)
        lp.open()
        assert lp.login_link_exist(), 'login link is not presented'

    @pytest.mark.parametrize(
        'test_email, pwd', [
            pytest.param('free', 'xxxXXX1234', id='free email'),
            pytest.param('company', 'xxxXXX1234', id='Company email'),
        ], indirect=['test_email']
    )
    def test_valid_login(self, browser, test_email, pwd):
        lp = LoginPage(driver=browser)
        lp.open()
        lp.registration(test_email, pwd, pwd)




