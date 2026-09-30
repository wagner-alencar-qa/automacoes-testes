from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_customer_data(self, first_name, last_name, zip_code):
        self.wait_for_visible(self.FIRST_NAME).send_keys(first_name)
        self.find(*self.LAST_NAME).send_keys(last_name)
        self.find(*self.ZIP_CODE).send_keys(zip_code)

    def proximo(self):
        self.wait_for_clickable(self.CONTINUE).click()

    def finish(self):
        self.wait_for_clickable(self.FINISH).click()

    def is_order_complete(self):
        return "THANK YOU FOR YOUR ORDER" in self.wait_for_visible(self.COMPLETE_HEADER).text.upper()

    def get_success_message(self):
        return self.wait_for_visible(self.COMPLETE_HEADER).text

    def get_error_message(self):
        return self.wait_for_visible(self.ERROR_MESSAGE).text
