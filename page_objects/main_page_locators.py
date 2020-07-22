from selenium.webdriver.common.by import By


class MainPageLocators:
    login_link = (By.CSS_SELECTOR, "#login_link")

    search_field = (By.ID, 'id_q')
    search_button = (By.CSS_SELECTOR, 'input.btn')




