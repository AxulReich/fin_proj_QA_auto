from selenium.webdriver.common.by import By


class BasketPageLocators:
    ADDED_PRODUCT_LIST = (By.ID, '[id="basket_formset"]')
    PROCEED_CHECKOUT_BUTTON = (By.PARTIAL_LINK_TEXT, '/checkout/')