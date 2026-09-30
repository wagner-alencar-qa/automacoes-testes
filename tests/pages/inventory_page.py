from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class InventoryPage(BasePage):
    PRODUCT_SORT = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_item(self, item_id):
        by, value = By.ID, f"add-to-cart-{item_id}"
        self.wait_for_clickable((by, value)).click()

    def remove_item(self, item_id):
        by, value = By.ID, f"remove-{item_id}"
        self.wait_for_clickable((by, value)).click()

    def open_cart(self):
        self.wait_for_clickable(self.CART_LINK).click()

    def get_cart_badge_count(self):
        try:
            return int(self.wait_for_visible(self.CART_BADGE).text)
        except Exception:
            return 0

    def sort_by(self, option_value):
        by, value = self.PRODUCT_SORT
        dropdown = self.wait_for_visible((by, value))
        dropdown.click()
        option_by, option_value_expr = By.XPATH, f"//option[@value='{option_value}']"
        self.wait_for_clickable((option_by, option_value_expr)).click()
