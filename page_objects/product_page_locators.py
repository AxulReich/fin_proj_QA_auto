from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]//button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main>p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")

    @staticmethod
    def get_product_selector_by_title(title):
        return By.CSS_SELECTOR, f'a[title="{title}"]'

if __name__ == '__main__':
    from constants import PRODUCTS
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    browser = webdriver.Chrome()
    from page_objects.login_page import LoginPage
    bp = LoginPage(driver=browser)
    bp.open()
    bp.search(PRODUCTS[0][1])
    bp._driver.find_element(By.PARTIAL_LINK_TEXT, "The shellcoder's handbook").click()
    time.sleep(1000)
    bp._driver.quit()