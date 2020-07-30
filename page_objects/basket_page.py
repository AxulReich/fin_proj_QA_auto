from page_objects.main_page import BasePage
from page_objects.mixin_page import PageHeaderMixin
from page_objects.basket_page_locators import BasketPageLocators as BPL


class BasketPage(PageHeaderMixin, BasePage):
    def __init__(self, driver, page_path='/basket/'):
        super().__init__(driver=driver, page_path=page_path)

    def should_be_empty_basket(self):
        assert self.is_not_element_present(BPL.ADDED_PRODUCT_LIST)

    def proceed_checout(self):
        self.find_element(BPL.PROCEED_CHECKOUT_BUTTON).click()

if __name__ == "__main__":
    from selenium import webdriver
    browser = webdriver.Chrome()
    mp = BasketPage(driver=browser)
    mp.open()