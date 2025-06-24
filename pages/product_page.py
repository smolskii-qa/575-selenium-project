from .base_page import BasePage
from .locators import ProductPageLocators

MESSAGE_SUCCESS_ADD = 'has been added to your basket'
MESSAGE_BASKET_PRICE = 'Your basket total is now'


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_all_messages(self):
        messages = self.browser.find_elements(*ProductPageLocators.ALL_MESSAGES)
        assert messages, 'Can\'t find messages'
        return messages

    def get_target_message(self, target):
        messages = self.get_all_messages()
        message = next((m.text for m in messages if target in m.text), None)
        assert message, 'Can\'t find target message'
        return message

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_correct_product_name_message(self):
        product_name = self.get_product_name()
        message = self.get_target_message(MESSAGE_SUCCESS_ADD)
        assert product_name in message, 'Wrong name in message about adding product to cart'

    def should_be_correct_cost_message(self):
        product_cost = self.get_product_price()
        message = self.get_target_message(MESSAGE_BASKET_PRICE)
        assert product_cost in message, 'Wrong cost in message about basket'
