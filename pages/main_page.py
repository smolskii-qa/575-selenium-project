from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LINK_LOGIN)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LINK_LOGIN), 'Login link is not presented'
