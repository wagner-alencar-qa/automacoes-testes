from tests.pages.login_page import LoginPage


class LoginTransaction:
    def __init__(self, driver):
        self.page = LoginPage(driver)

    def realizar_login(self, usuario, senha):
        self.page.login(usuario, senha)

    def login_invalido(self, usuario, senha):
        self.page.login(usuario, senha)
        return self.page.get_error_message()