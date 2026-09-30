"""""from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def acessar(self):
        self.driver.get("https://sua-url.com/login")

    def preencher_usuario(self, usuario):
        self.driver.find_element(By.ID, "username").send_keys(usuario)

    def preencher_senha(self, senha):
        self.driver.find_element(By.ID, "password").send_keys(senha)

    def clicar_login(self):
        self.driver.find_element(By.ID, "login").click()"""

from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def acessar(self):
        self.open("https://www.saucedemo.com")

    def preencher_usuario(self, usuario):
        self.wait_for_visible(self.USERNAME).send_keys(usuario)

    def preencher_senha(self, senha):
        self.find(*self.PASSWORD).send_keys(senha)

    def clicar_login(self):
        self.wait_for_clickable(self.LOGIN_BUTTON).click()

    def login(self, usuario, senha):
        self.acessar()
        self.preencher_usuario(usuario)
        self.preencher_senha(senha)
        self.clicar_login()

    def get_error_message(self):
        try:
            return self.wait_for_visible(self.ERROR_MESSAGE).text
        except Exception:
            return ""