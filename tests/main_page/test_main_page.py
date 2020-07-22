from page_objects.main_page import MainPage


class TestMainPage():
    def test_login_link_exist(self, browser):
        mp = MainPage(browser)
        mp.open()
        assert mp.login_link_exist(), 'Login link is not represented!'

    def test_can_open_login_page_from_main_page(self, browser):
        mp = MainPage(browser)
        mp.open()
        mp.enter_or_reister()
        assert '/accounts/login/' in mp.url, "Incorrect link"
