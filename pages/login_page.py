from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_REGISTER_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.INPUT_REGISTER_PASSWORD)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.INPUT_REGISTER_CONFIRM_PASSWORD)
        register_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)

        email_input.click()
        email_input.send_keys(email)
        password_input.click()
        password_input.send_keys(password)
        password_confirm_input.click()
        password_confirm_input.send_keys(password)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.does_url_have_substring('login'), 'URL doesnt have substring "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), 'Register form is not presented'
