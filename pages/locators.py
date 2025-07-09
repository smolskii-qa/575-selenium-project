from selenium.webdriver.common.by import By
from utils.translations import get_text


class BasePageLocators():
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, '.basket-mini span a.btn')
    ICON_USER = (By.CSS_SELECTOR, '.icon-user')
    LINK_LOGIN = (By.CSS_SELECTOR, '#login_link')
    LINK_LOGIN_INVALID = (By.CSS_SELECTOR, '#login_link_inc')


class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, '#content_inner')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')


class MainPageLocators():
    pass


class LoginPageLocators():
    BUTTON_REGISTER = (By.CSS_SELECTOR, 'form#register_form button.btn.btn-lg.btn-primary')
    FORM_LOGIN = (By.CSS_SELECTOR, '#login_form')
    FORM_REGISTER = (By.CSS_SELECTOR, '#register_form')
    INPUT_REGISTER_EMAIL = (By.CSS_SELECTOR, 'input#id_registration-email')
    INPUT_REGISTER_PASSWORD = (By.CSS_SELECTOR, 'input#id_registration-password1')
    INPUT_REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input#id_registration-password2')


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    # Относительный локатор. Используется только для поиска внутри сообщений
    MESSAGE_STRONG_TEXT_RELATIVE = (By.TAG_NAME, 'strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

    @staticmethod
    def get_message_basket_amount_locator(language):
        text = get_text('alert_basket_total', language)
        return (
            By.XPATH,
            f'//div[@id="messages"]/div[contains(@class, "alert")][contains(., "{text}")]'
        )

    @staticmethod
    def get_message_success_locator(language):
        text = get_text('alert_success_add_to_basket', language)
        return (
            By.XPATH,
            f'//div[@id="messages"]/div[contains(@class, "alert")][contains(., "{text}")]'
        )
