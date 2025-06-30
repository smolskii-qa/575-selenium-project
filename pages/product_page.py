from .base_page import BasePage
from .locators import ProductPageLocators

MESSAGE_SUCCESS_ADD = 'has been added to your basket'
MESSAGE_BASKET_PRICE = 'Your basket total is now'


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_correct_product_name_in_success_message(self):
        product_name = self.get_product_name()
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS)
        message_value = message.find_element(*ProductPageLocators.MESSAGE_STRONG_TEXT_RELATIVE).text
        assert message_value == product_name, 'Wrong name in message about adding product to cart'

    def should_be_correct_amount_in_basket_amount_message(self):
        product_cost = self.get_product_price()
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_AMOUNT)
        message_value = message.find_element(*ProductPageLocators.MESSAGE_STRONG_TEXT_RELATIVE).text
        assert message_value == product_cost, 'Wrong cost in message about basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS)


