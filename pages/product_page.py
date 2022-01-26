from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        self.is_element_click(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        self.solve_quiz_and_get_code()
        # time.sleep(120)
    
            
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
                  "Success message is presented, but should not be"
    
    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is should not be"


    