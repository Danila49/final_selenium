from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest



@pytest.mark.parametrize('link', ["0", "1", "2","3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.xfail(reason="fixing this bug right now")
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
    