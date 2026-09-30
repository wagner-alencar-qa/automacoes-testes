import pytest
from tests.transactions.login_transaction import LoginTransaction


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
def test_login_valido(driver):
    """
    [SMOKE, REGRESSION, E2E] Login com sucesso
    
    Funcionalidade: Login de usuário
    Cenário: Login com sucesso
    Justificativa: É pré-requisito para praticamente toda operação autenticada.
    """
    login = LoginTransaction(driver)
    login.realizar_login("standard_user", "secret_sauce")
    
    assert "inventory" in driver.current_url


@pytest.mark.regression
def test_login_invalido(driver):
    """
    [REGRESSION] Login com credenciais inválidas
    
    Funcionalidade: Login de usuário
    Cenário: Login com credenciais inválidas
    Justificativa: Valida regra de negócio e tratamento de erro.
    """
    login = LoginTransaction(driver)
    erro = login.login_invalido("locked_out_user", "secret_sauce")
    
    assert "locked out" in erro.lower() or "Epic sadface" in erro


@pytest.mark.regression
def test_login_usuario_bloqueado(driver):
    """
    [REGRESSION] Login com usuário bloqueado
    
    Funcionalidade: Login de usuário
    Cenário: Usuário bloqueado
    Justificativa: Validação de regra específica de autenticação.
    """
    login = LoginTransaction(driver)
    erro = login.login_invalido("locked_out_user", "secret_sauce")
    
    assert "locked out" in erro.lower()