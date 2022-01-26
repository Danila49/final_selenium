from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest



@pytest.mark.parametrize('link', ["0", "1", "2","3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    link=f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer{link}"
    page=ProductPage(browser,link)
    page.open()
    name_book=browser.find_element(*ProductPageLocators.NAME_BOOK).text
    price_book=browser.find_element(*ProductPageLocators.PRICE_BOOK).text
    page.add_product_to_basket()
    name_book_after_add=browser.find_element(*ProductPageLocators.NAME_BOOK_AFTER_ADDED).text
    price_book_after_add=browser.find_element(*ProductPageLocators.PRICE_BOOK_AFTER_ADDED).text
    assert name_book==name_book_after_add, "name book is different"
    assert price_book==price_book_after_add, "price book is different"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page=ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()
  
def test_guest_cant_see_success_message(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page=ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page=ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message()


