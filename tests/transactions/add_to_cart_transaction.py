from guara.transaction import AbstractTransaction
from tests.pages.inventory_page import InventoryPage


class AddToCartTransaction(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = InventoryPage(driver)

    def do(self, item_id):
        self.page.add_item(item_id)
        self.page.open_cart()
        return self.driver.current_url
