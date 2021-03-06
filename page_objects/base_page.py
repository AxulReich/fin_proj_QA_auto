from logging import getLogger
from urllib.parse import urljoin

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import BASE_URL, EXPLICIT_WAIT

Logger = getLogger(__name__)


class BasePage:
    _base_url = BASE_URL

    # _page_path = None

    def __init__(self, driver: WebDriver, page_path=None):
        """
        :param driver: from conftest.py
        """
        self._driver = driver
        self._page_path = page_path

    @property
    def url(self) -> str:
        return self._driver.current_url

    @property
    def get_language(self) -> str:
        return self.url.split('/')[3]

    @property
    def get_current_page_path(self):
        return self.url.split('/')[4:]

    # @classmethod
    # def create_from_current_page(cls):


    def open(self):
        url = urljoin(self._base_url, self._page_path)
        with allure.step(f'open {url}'):
            self._driver.get(url)

    def is_element_present(self, locator: tuple) -> bool:
        """
        method for check if element is present
        :param locator: css - (By.CSS_SELECTOR, css locator), id - (By.ID, css id locator),
                        xpath - (By.XPATH, xpath locator)
        :return: True / False
        """
        return len(self._driver.find_elements(*locator)) > 0

    def find_element(self, locator: tuple) -> WebElement:
        """
        method to find element on the page
        :param locator: css - (By.CSS_SELECTOR, css locator), id - (By.ID, css id locator),
                        xpath - (By.XPATH, xpath locator)
        :return: object selenium WebElement
        """
        try:
            element = self._driver.find_element(*locator)
            return element
        except NoSuchElementException:
            raise AssertionError(f'Element with {locator} is not presented!')

    def wait_until_element_invisible(self, locator: tuple, timeout=EXPLICIT_WAIT):
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.invisibility_of_element_located(locator))
        except TimeoutException as e:
            raise AssertionError(e)

    def is_not_element_present(self, locator: tuple, timeout=EXPLICIT_WAIT) -> bool:
        """
        Check that element is not present
        :param timeout: time to wait until element is
        :param locator:
        :return:
        """
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self._driver, EXPLICIT_WAIT, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True


if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    browser = webdriver.Chrome()
    bp = BasePage(driver=browser)
    bp.open()
    print(bp.get_language)
    print(bp.get_current_page_path)
    # bp.find_element((By.CSS_SELECTOR, 'h3>a[href="/en-gb/catalogue/the-age-of-the-pussyfoot_89/"]')).click()
    # print(bp.wait_until_element_invisible((By.CSS_SELECTOR, 'h3>a[href="/en-gb/catalogue/the-age-of-the-pussyfoot_89/"]')))
