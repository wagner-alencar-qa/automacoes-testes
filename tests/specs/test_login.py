def test_login_valido(driver):
    from tests.transactions.login_transaction import LoginTransaction

    login = LoginTransaction(driver)
    login.realizar_login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_login_invalido(driver):
    from tests.transactions.login_transaction import LoginTransaction

    login = LoginTransaction(driver)
    erro = login.login_invalido("locked_out_user", "secret_sauce")

    assert "locked out" in erro.lower() or "Epic sadface" in erro