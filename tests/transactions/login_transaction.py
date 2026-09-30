from guara.transaction import AbstractTransaction
from tests.pages.login_page import LoginPage


class LoginTransaction(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = LoginPage(driver)

    def do(self, usuario, senha):
        self.page.login(usuario, senha)
        return self.driver.current_url

    def realizar_login(self, usuario, senha):
        return self.do(usuario, senha)

    def login_invalido(self, usuario, senha):
        self.page.login(usuario, senha)
        return self.page.get_error_message()