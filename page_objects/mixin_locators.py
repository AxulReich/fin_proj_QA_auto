from selenium.webdriver.common.by import By


class PageHeaderLocators:
    login_link = (By.CSS_SELECTOR, "#login_link")

    search_field = (By.ID, 'id_q')
    search_button = (By.CSS_SELECTOR, 'input.btn')

    drop_down_language_list = (By.CSS_SELECTOR, "select[name='language']")
    language_change_button = (By.XPATH, '//*[@id="language_selector"]/button')

    main_page_link = (By.CSS_SELECTOR, 'header>div.page_inner>div>div.col-sm-7.h1>a')

    basket_page_link = (By.CSS_SELECTOR, "span.btn-group>a")

    @staticmethod
    def get_drop_down_language_selector(language='en-gb'):
        return By.CSS_SELECTOR, f"option[value={language}]"

    @staticmethod
    def get_oscar_label_main_page_link_selector(language='en-gb'):
        return By.CSS_SELECTOR, f'a[href="/{language}/"]'

