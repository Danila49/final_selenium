from .base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def is_emty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ID_PRODUCT_IN_BASKET), \
            "In basket has product"
    
    def is_has_wrinting_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.WRITING_EMPTY_BASKET), \
            "writing empty basket doesn't have"