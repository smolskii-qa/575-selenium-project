from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALL_MESSAGES = (By.CSS_SELECTOR, '#messages .alert .alertinner')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    # Относительный локатор. Используется только для поиска внутри сообщений
    REL_MESSAGE_STRONG_TEXT = (By.TAG_NAME, 'strong')

# class="basket-mini pull-right hidden-xs"
#
#
# class ="price_color"
#
#
# class ="alert alert-safe alert-noicon alert-info  fade in"
# class ="alertinner " сообщение
#
#
# class ="alert alert-safe alert-noicon alert-success  fade in" strog
