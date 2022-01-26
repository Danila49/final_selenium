from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        self.is_element_click(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        self.solve_quiz_and_get_code()
        time.sleep(15)
        
       


    