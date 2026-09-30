from guara.transaction import AbstractTransaction
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage
from tests.pages.inventory_page import InventoryPage


class CheckoutTransaction(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)

    def do(self, item_id, first_name, last_name, zip_code):
        return self.comprar_produto(item_id, first_name, last_name, zip_code)

    def comprar_produto(self, item_id, first_name, last_name, zip_code):
        self.inventory_page.add_item(item_id)
        self.inventory_page.open_cart()
        self.cart_page.checkout()
        self.checkout_page.fill_customer_data(first_name, last_name, zip_code)
        self.checkout_page.proximo()
        self.checkout_page.finish()
        return self.checkout_page.is_order_complete()
