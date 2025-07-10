import time
import pytest
from random import randint
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

link_with_quiz_in_alert = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def register(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        salt = randint(1, 999999)
        page.register_new_user(f'volodimir992{salt}@test.com', f'fgshsajucsa{salt}')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.add_to_basket()
        page.should_be_correct_product_name_in_success_message(product_name)
        page.should_be_correct_amount_in_basket_amount_message(product_price)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_basket()
    page.should_be_correct_product_name_in_success_message(product_name)
    page.should_be_correct_amount_in_basket_amount_message(product_price)


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_not_basket_have_items()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message_disappeared()
