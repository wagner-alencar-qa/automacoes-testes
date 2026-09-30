import pytest
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage
from tests.pages.inventory_page import InventoryPage
from tests.transactions.checkout_transaction import CheckoutTransaction
from tests.transactions.login_transaction import LoginTransaction


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
def test_adicionar_item_ao_carrinho(driver):
    """
    [SMOKE, REGRESSION, E2E] Adicionar item ao carrinho
    
    Funcionalidade: Carrinho de Compras
    Cenário: Adicionar item ao carrinho
    Justificativa: Etapa obrigatória da jornada de compra.
    """
    LoginTransaction(driver).realizar_login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_item("sauce-labs-backpack")
    
    assert inventory_page.get_cart_badge_count() == 1


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
def test_fluxo_completo_de_compra(driver):
    """
    [SMOKE, REGRESSION, E2E] Compra de produto com sucesso
    
    Funcionalidade: Processo de Compra
    Cenário: Compra de produto com sucesso
    Justificativa: Fluxo principal de geração de valor do produto.
    Se falhar, o sistema está comprometido.
    """
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


@pytest.mark.regression
def test_validar_carrinho_vazio(driver):
    """
    [REGRESSION] Acessar carrinho sem itens
    
    Funcionalidade: Carrinho Vazio
    Cenário: Acessar carrinho sem itens
    Justificativa: Validação de comportamento alternativo.
    """
    LoginTransaction(driver).realizar_login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_cart()
    
    assert CartPage(driver).get_item_count() == 0


@pytest.mark.regression
def test_validacao_checkout_sem_dados(driver):
    """
    [REGRESSION] Checkout sem preencher dados
    
    Funcionalidade: Validação do Checkout
    Cenário: Checkout sem preencher dados
    Justificativa: Validação negativa do formulário.
    """
    LoginTransaction(driver).realizar_login("standard_user", "secret_sauce")
    
    InventoryPage(driver).add_item("sauce-labs-backpack")
    InventoryPage(driver).open_cart()
    CartPage(driver).checkout()
    
    CheckoutPage(driver).proximo()
    
    assert "first-name" in driver.current_url or "error" in driver.page_source.lower()


@pytest.mark.regression
def test_remover_item_do_carrinho(driver):
    """
    [REGRESSION] Remover item do carrinho
    
    Funcionalidade: Carrinho de Compras
    Cenário: Remover item do carrinho
    Justificativa: Funcionalidade importante, porém não essencial para Smoke.
    """
    LoginTransaction(driver).realizar_login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_item("sauce-labs-backpack")
    inventory_page.remove_item("sauce-labs-backpack")
    
    assert inventory_page.get_cart_badge_count() == 0


@pytest.mark.regression
def test_logout_com_sucesso(driver):
    """
    [REGRESSION, E2E] Logout com sucesso
    
    Funcionalidade: Logout
    Cenário: Logout com sucesso
    Justificativa: Normalmente representa o encerramento correto da sessão do usuário.
    """
    LoginTransaction(driver).realizar_login("standard_user", "secret_sauce")
    
    # Simulating logout via menu
    from selenium.webdriver.common.by import By
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()
    
    assert "login" in driver.current_url or driver.current_url.endswith("/")
