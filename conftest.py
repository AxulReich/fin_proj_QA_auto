from logging import getLogger

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import IMPLICIT_WAIT, WINDOW_SIZE, LANGUAGES

Logger = getLogger('__name__')


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default="chrome",
        help="Choose browser: chrome or firefox")
    parser.addoption(
        '--language',
        action='store',
        default="en-gb",
        help="Choose page language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    page_language = request.config.getoption("language")
    browser = None
    if page_language in LANGUAGES:
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': page_language})
    else:
        raise pytest.UsageError("--language should be valid!")
    if browser_name.lower() == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name.lower() == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        print("Browser {} still is not implemented".format(browser_name))
        raise pytest.UsageError('--browser should be chrome or firefox!')

    browser.implicitly_wait(IMPLICIT_WAIT)
    browser.set_window_size(*WINDOW_SIZE)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture()
def test_email(request):
    try:
        params = request.param
        if params == 'free':
            return Faker().ascii_free_email()
        elif params == 'company':
            return Faker().ascii_company_email()
        else:
            raise NotImplementedError(f'incorrect request param: {params}')
            # Logger.warning(f'incorrect request param: {params}')
            # return Faker().email()
    except AttributeError:
        return Faker().email()
