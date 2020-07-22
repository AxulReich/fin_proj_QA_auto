from page_objects.base_page import BasePage
from page_objects.main_page_locators import MainPageLocators as MPL
import allure


class MainPage(BasePage):
    @allure.step('Search product')
    def search(self, search_text: str):
        self.find_element(MPL.search_field).send_keys(search_text)
        self.find_element(MPL.search_button).click()

    def enter_or_reister(self):
        self.find_element(MPL.login_link).click()



if __name__ == "__main__":
    from selenium import webdriver
    browser = webdriver.Chrome()
    mp = MainPage(driver=browser)
    mp.open()
    print(mp.login_link_exist())