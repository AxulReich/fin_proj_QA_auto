from page_objects.base_page import BasePage
from page_objects.mixin_page import PageHeaderMixin
from page_objects.main_page_locators import MainPageLocators as MPL

import allure


class MainPage(PageHeaderMixin, BasePage):
    pass
    # @allure.step('Search product')
    # def search(self, search_text: str):
    #     self.find_element(MPL.search_field).send_keys(search_text)
    #     self.find_element(MPL.search_button).click()
    #
    # def enter_or_reister(self):
    #     self.find_element(MPL.login_link).click()
    #
    # def change_language(self, language='en-gb'):
    #     select = Select(self.find_element(MPL.drop_down_language_list))
    #     select.select_by_value(language)
    #     self.find_element(MPL.language_change_button).click()
    #
    # def got_to_main_page_by_oscar_label_link(self, language='en-gb'):
    #     self.find_element(MPL.get_oscar_label_main_page_link_selector(language)).click()


if __name__ == "__main__":
    pass
    # from selenium import webdriver
    # browser = webdriver.Chrome()
    # mp = MainPageHeader(driver=browser)
    # mp.open()
    # mp.change_language(language='ru')
    # mp.login_link_exist()