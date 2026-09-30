from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def checkout(self):
        self.wait_for_clickable(self.CHECKOUT_BUTTON).click()

    def continue_shopping(self):
        self.wait_for_clickable(self.CONTINUE_SHOPPING).click()

    def get_item_count(self):
        items = self.find_all(*self.CART_ITEMS)
        return len(items)
