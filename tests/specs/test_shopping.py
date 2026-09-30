from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage
from tests.pages.inventory_page import InventoryPage
from tests.transactions.checkout_transaction import CheckoutTransaction
from tests.transactions.login_transaction import LoginTransaction


def test_adicionar_item_ao_carrinho(driver):
    LoginTransaction(driver).realizar_login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_item("sauce-labs-backpack")

    assert inventory_page.get_cart_badge_count() == 1


def test_fluxo_completo_de_compra(driver):
    LoginTransaction(driver).realizar_login("standard_user", "secret_sauce")

    checkout = CheckoutTransaction(driver)
    sucesso = checkout.comprar_produto(
        "sauce-labs-backpack",
        "Ana",
        "Silva",
        "01000-000",
    )

    assert sucesso is True
    assert "checkout-complete" in driver.current_url


def test_validar_carrinho_vazio(driver):
    LoginTransaction(driver).realizar_login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.open_cart()

    assert CartPage(driver).get_item_count() == 0


def test_validacao_checkout_sem_dados(driver):
    LoginTransaction(driver).realizar_login("standard_user", "secret_sauce")

    InventoryPage(driver).add_item("sauce-labs-backpack")
    InventoryPage(driver).open_cart()
    CartPage(driver).checkout()

    CheckoutPage(driver).proximo()

    assert "first-name" in driver.current_url or "error" in driver.page_source.lower()
