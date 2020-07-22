from page_objects.product_page import ProductPage


class TestProductPage():
    def test_login_link_exist(self, browser):
        pp = ProductPage(driver=browser)
        pp.open()
        assert pp.login_link_exist(), 'login link is not presented'

    def test_add_to_basket_exist(self, browser):
        pp = ProductPage(driver=browser)
        pp.open()
        assert pp.should_be_add_to_basket_button(), "Add to basket button is not presented!"
