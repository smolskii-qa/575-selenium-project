from selenium.webdriver.common.by import By


class BasePageLocators():
    LINK_LOGIN = (By.CSS_SELECTOR, '#login_link')
    LINK_LOGIN_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BUTTON_VIEW_BASKET = (By.XPATH, '//a[@class="btn btn-default"][contains(., "View basket")]')


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_CONTENT = (By.CSS_SELECTOR, '#content_inner')


class MainPageLocators():
    LINK_LOGIN = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, '#login_form')
    FORM_REGISTER = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    MESSAGE_SUCCESS = (
        By.XPATH,
        '//div[@id="messages"]/div[contains(@class, "alert")][contains(., "has been added to your basket")]'
    )
    MESSAGE_BASKET_AMOUNT = (
        By.XPATH,
        '//div[@id="messages"]/div[contains(@class, "alert")][contains(., "Your basket total is now")]'
    )
    # Относительный локатор. Используется только для поиска внутри сообщений
    MESSAGE_STRONG_TEXT_RELATIVE = (By.TAG_NAME, 'strong')
