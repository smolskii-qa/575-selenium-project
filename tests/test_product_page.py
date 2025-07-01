import time
import pytest

from pages.product_page import ProductPage

# link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
link_without_quiz = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/']


@pytest.mark.parametrize(
    'link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        # pytest.param(
        #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        #   marks=pytest.mark.xfail),
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ]
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(3)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_name_in_success_message()
    page.should_be_correct_amount_in_basket_amount_message()
    time.sleep(3)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_without_quiz)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_without_quiz)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_without_quiz)
    page.open()
    page.add_to_basket()
    page.should_be_success_message_disappeared()
