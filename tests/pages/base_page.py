from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def find_all(self, by, value):
        return self.driver.find_elements(by, value)

    def wait_element(self, by, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, value)))

    def click(self, by, value):
        self.wait_for_clickable((by, value)).click()

    def type(self, by, value, text):
        self.wait_for_visible((by, value)).send_keys(text)

    def get_text(self, by, value):
        return self.wait_for_visible((by, value)).text
