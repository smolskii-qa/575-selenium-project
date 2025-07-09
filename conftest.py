from random import choices

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language', choices=['en', 'ru'])


@pytest.fixture(scope='session')
def language(request):
    return request.config.getoption('language')


@pytest.fixture()
def browser(request):
    options = Options()
    browser_language = request.config.getoption('language')
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    browser._language = browser_language
    yield browser
    browser.quit()
