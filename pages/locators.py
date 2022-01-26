from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form") 

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET=(By.CLASS_NAME, "btn.btn-lg.btn-primary")
    NAME_BOOK=(By.CSS_SELECTOR, ".product_main  h1")
    PRICE_BOOK=(By.CSS_SELECTOR,".product_main  h1+p")
    NAME_BOOK_AFTER_ADDED=(By.CSS_SELECTOR, ".alertinner strong")
    PRICE_BOOK_AFTER_ADDED=(By.CSS_SELECTOR, ".alertinner p strong")
    