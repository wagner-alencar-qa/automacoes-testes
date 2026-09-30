from guara.transaction import AbstractTransaction
from tests.pages.checkout_page import CheckoutPage


class FinishOrderTransaction(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = CheckoutPage(driver)

    def do(self):
        self.page.finish()
        return self.page.get_success_message()
