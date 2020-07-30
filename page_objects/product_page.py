from page_objects.main_page import BasePage
from page_objects.mixin_page import PageHeaderMixin
from page_objects.product_page_locators import ProductPageLocators as PPL

from urllib.parse import urljoin


class ProductPage(PageHeaderMixin, BasePage):
    def __init__(self, driver, url_name="", title=None):
        """
        :param driver: from conftest.py
        :param url_name: if url_name was not passed, instance would be main catalogue! else open product page
        """
        super().__init__(driver=driver, page_path=urljoin('/catalogue/', url_name))
        self._url_name = url_name
        self._title = title

    def is_product_page(self):
        if not self._title or self._url_name:
            raise Exception('Instance of ProductPage is catalogue page or title was not passed!')
        return self.get_product_name() == self._title

    def get_product_name(self):
        return self.find_element(PPL.PRODUCT_NAME).text

    def get_product_price(self):
        return self.find_element(PPL.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        link = self.find_element(PPL.ADD_TO_BASKET_BUTTON)
        link.click()

    def is_product_added(self):
        assert self.is_element_present(PPL.SUCCESS_MESSAGE)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(PPL.ADD_TO_BASKET_BUTTON), "add to basket button is not present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(PPL.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapeared_success_message(self):
        assert self.is_disappeared(PPL.SUCCESS_MESSAGE)


if __name__ == "__main__":
    from selenium import webdriver
    browser = webdriver.Chrome()
    mp = ProductPage(driver=browser,
                     url_name="studyguide-for-counter-hack-reloaded_205")
    mp.open()
    print(mp.get_product_price())
    print(mp.get_current_page_path)

    browser.quit()