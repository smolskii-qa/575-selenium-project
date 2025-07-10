from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_button.click()

    def get_product_name(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_correct_product_name_in_success_message(self, expected_name):
        message = self.browser.find_element(*ProductPageLocators.get_message_success_locator(self.language))
        message_value = message.find_element(*ProductPageLocators.MESSAGE_STRONG_TEXT_RELATIVE).text
        assert message_value == expected_name, 'Wrong name in message about adding product to cart'

    def should_be_correct_amount_in_basket_amount_message(self, expected_amount):
        message = self.browser.find_element(*ProductPageLocators.get_message_basket_amount_locator(self.language))
        message_value = message.find_element(*ProductPageLocators.MESSAGE_STRONG_TEXT_RELATIVE).text
        assert message_value == expected_amount, 'Wrong cost in message about basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.get_message_success_locator(self.language)), \
            'Success message is presented, but should not be'

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.get_message_success_locator(self.language)), \
            'Message is not disappeared, but should be'
