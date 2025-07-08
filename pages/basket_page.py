from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    MESSAGE_EMPTY_BASKET = 'Your basket is empty.'

    def should_not_basket_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket has items, but shouldn\'t'

    def should_be_message_empty_basket(self):
        expected_message = self.MESSAGE_EMPTY_BASKET
        message = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text
        assert expected_message in message, f'Wrong message: {message}, but expected: {expected_message}'
