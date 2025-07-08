from selenium.webdriver.common.by import By


class BasePageLocators():
    BUTTON_VIEW_BASKET = (By.XPATH, '//a[@class="btn btn-default"][contains(., "View basket")]')
    ICON_USER = (By.CSS_SELECTOR, '.icon-user')
    LINK_LOGIN = (By.CSS_SELECTOR, '#login_link')
    LINK_LOGIN_INVALID = (By.CSS_SELECTOR, '#login_link_inc')


class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, '#content_inner')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')


class MainPageLocators():
    LINK_LOGIN = (By.CSS_SELECTOR, '#login_link')


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
    MESSAGE_BASKET_AMOUNT = (
        By.XPATH,
        '//div[@id="messages"]/div[contains(@class, "alert")][contains(., "Your basket total is now")]'
    )
    MESSAGE_SUCCESS = (
        By.XPATH,
        '//div[@id="messages"]/div[contains(@class, "alert")][contains(., "has been added to your basket")]'
    )
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
