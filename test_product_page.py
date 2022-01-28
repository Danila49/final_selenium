from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest
from pages.basket_page import BasketPage


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

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page=ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()
@pytest.mark.skip  
def test_guest_cant_see_success_message(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page=ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page=ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket()
    basket_page=BasketPage(browser, browser.current_url)
    basket_page.is_emty_basket()
    basket_page.is_has_wrinting_empty_basket()
