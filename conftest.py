import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture()
def browser(request):
    options = Options()
    browser_language = request.config.getoption('language')
    options.add_experimental_option('prefs', {'intl.accept_languags': browser_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
