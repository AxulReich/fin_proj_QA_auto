from page_objects.main_page import BasePage
from page_objects.product_page_locators import ProductPageLocators as PPL


class ProductPage(BasePage):
    _page_path = '/catalogue/'

    def should_be_add_to_basket_button(self):
        self.is_element_present(PPL.add_to_basketbutton)
    
