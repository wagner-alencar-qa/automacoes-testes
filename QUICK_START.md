# 🚀 Guia Rápido - Como Usar a Refatoração

## 1️⃣ Adicionar um Novo Teste

### Passo 1: Criar a Page (se não existir)

```python
# tests/pages/my_new_page.py
from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class MyNewPage(BasePage):
    MY_BUTTON = (By.ID, "my-button-id")
    MY_INPUT = (By.NAME, "my-input")
    
    def click_my_button(self):
        self.wait_for_clickable(self.MY_BUTTON).click()
    
    def enter_text(self, text):
        self.type(self.MY_INPUT[0], self.MY_INPUT[1], text)
```

### Passo 2: Criar a Transaction

```python
# tests/transactions/my_transaction.py
from guara.transaction import AbstractTransaction
from tests.pages.my_new_page import MyNewPage

class MyTransaction(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = MyNewPage(driver)
    
    def do(self, param1, param2):
        """Executa a ação de negócio."""
        self.page.click_my_button()
        self.page.enter_text(param1)
        return self.driver.current_url
```

### Passo 3: Criar o Teste

```python
# tests/specs/test_my_feature.py
import pytest
from tests.transactions.my_transaction import MyTransaction

@pytest.mark.smoke
@pytest.mark.regression
def test_my_scenario(driver):
    """[SMOKE, REGRESSION] Descrição do cenário"""
    result = MyTransaction(driver).do("param1", "param2")
    
    assert "expected" in result
```

---

## 2️⃣ UI Mudou? Siga Estes Passos

**Cenário:** O ID do botão mudou de `"login-button"` para `"btn-signin"`

### ❌ ERRADO - Procurar em todos os testes
```bash
# grep -r "login-button" tests/  # Encontra em 50 testes!
```

### ✅ CERTO - Alterar apenas na Page
```python
# tests/pages/login_page.py
class LoginPage(BasePage):
    LOGIN_BUTTON = (By.ID, "btn-signin")  # ← Alteração única
```

✨ **Boom!** Todos os 50 testes funcionam novamente.

---

## 3️⃣ Usar Asserções Customizadas

```python
from tests.assertions.custom_assertions import CustomAssertions

def test_example(driver):
    login = LoginTransaction(driver)
    login.realizar_login("user", "pass")
    
    # ✅ Asserções customizadas (mais legíveis)
    CustomAssertions.assert_page_loaded(driver, "inventory")
    
    # Vs.
    
    # ❌ Assert Selenium bruto (menos claro)
    assert "inventory" in driver.current_url
```

---

## 4️⃣ Usar a Fixture Application (Guará)

```python
def test_with_guara_fluent_api(app):
    """Exemplo com fluent API BDD."""
    app \
        .given("usuario precisa estar autenticado") \
        .when(LoginTransaction, "standard_user", "secret_sauce") \
        .then(lambda result: assert "inventory" in result)
```

---

## 5️⃣ Rodando Testes por Categoria

```bash
# Apenas Smoke (rápido - CI/CD)
pytest -m smoke -v

# Apenas Regression (completo - antes de merge)
pytest -m regression -v

# Apenas E2E (jornadas - pré-produção)
pytest -m e2e -v

# Teste específico
pytest tests/specs/test_login.py::test_login_valido -v

# Com relatório HTML
pytest -m smoke -v --html=report.html
```

---

## 6️⃣ Estrutura de um Teste Bem Escrito

```python
import pytest
from tests.transactions.my_transaction import MyTransaction
from tests.assertions.custom_assertions import CustomAssertions

@pytest.mark.smoke          # ← Tag de classificação
@pytest.mark.login          # ← Tag de funcionalidade
def test_login_success(driver):
    """
    [SMOKE, REGRESSION, E2E] Login com sucesso
    
    Funcionalidade: Autenticação
    Cenário: Login com credenciais válidas
    Justificativa: Pré-requisito para toda operação.
    """
    # SETUP
    transaction = MyTransaction(driver)
    
    # ACTION
    result = transaction.do("param1", "param2")
    
    # ASSERT
    CustomAssertions.assert_page_loaded(driver, "inventory")
    assert result is True
```

---

## 7️⃣ Debug - Elemento Não Encontrado?

**Se receber `TimeoutException`:**

1. Verifique o seletor CSS/ID na página
2. Aumente timeout na Page:

```python
class LoginPage(BasePage):
    def get_error_message(self):
        return self.wait_element(By.CSS_SELECTOR, "[data-test='error']", timeout=20).text
```

3. Ou ajuste globalmente em `tests/config/settings.py`:

```python
EXPLICIT_WAIT = 20  # Default era 10
```

---

## 8️⃣ Padrão Page + Transaction (Resumo)

| Camada | Responsabilidade | Exemplo |
|--------|-----------------|---------|
| **Page** | Seletores + interação com UI | `LoginPage.login(user, pass)` |
| **Transaction** | Fluxo de negócio | `LoginTransaction.do(user, pass)` |
| **Test** | Apenas setup, ação e asserção | `LoginTransaction(...).do(...)` |

✅ **Page:** "Como clickar o botão?"
✅ **Transaction:** "O que fazer para fazer login?"
✅ **Test:** "Login funciona?"

---

## 9️⃣ Checklist Antes de Commitar

- [ ] Todas as Pages usam `BasePage` como herança
- [ ] Todos os Transactions estendem `AbstractTransaction`
- [ ] Todos os Transactions implementam `do()` method
- [ ] Testes usam `@pytest.mark` com tags apropriadas
- [ ] Nenhum `find_element` direto no teste
- [ ] Nenhum hardcoded URL (usar `settings.py`)
- [ ] Testes passam com `pytest -m smoke`

---

## 🔟 Estrutura de Pastas (Copie e Cole)

```bash
# Copie para nova feature
mkdir -p tests/transactions
mkdir -p tests/pages
mkdir -p tests/specs
mkdir -p tests/assertions
mkdir -p tests/config
mkdir -p tests/fixtures
```

---

**Dúvidas? Releia os exemplos acima! 🎯**
