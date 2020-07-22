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


class BasePage():
    _base_url = BASE_URL
    _page_path = None

    def __init__(self, browser: WebDriver):
        """
        :param browser: from conftest.py
        """
        self._browser = browser
        # self.url = url
        # self.browser.implicitly_wait(timeout)

    @property
    def url(self):
        return self._browser.current_url

    @property
    def source(self):
        return self._browser.page_source

    def open(self):
        url = urljoin(self._base_url, self._page_path)
        with allure.step(f'open {url}'):
            self._browser.get(url)
        # self._browser.get(self.url)

    def is_element_present(self, locator: tuple) -> bool:
        """
        method for check if element is present
        :param locator: css - (By.CSS_SELECTOR, css locator), id - (By.ID, css id locator),
                        xpath - (By.XPATH, xpath locator)
        :return: True / False
        """
        try:
            self._browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, locator: tuple) -> WebElement:
        """
        method to find element on the page
        :param locator: css - (By.CSS_SELECTOR, css locator), id - (By.ID, css id locator),
                        xpath - (By.XPATH, xpath locator)
        :return: object selenium WebElement
        """
        try:
            element = self._browser.find_element(*locator)
            return element
        except NoSuchElementException:
            raise AssertionError(f'Element with {locator} is not presented!')

    def wait_until_element_invisible(self, locator: tuple, timeout=EXPLICIT_WAIT):
        try:
            WebDriverWait(self._browser, timeout).until(
                EC.invisibility_of_element_located(locator),
                "Element with locator {1}: {2} still visible".format(*locator))
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
            WebDriverWait(self._browser, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self,  locator: tuple) -> bool:
        try:
            WebDriverWait(self._browser, EXPLICIT_WAIT, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True