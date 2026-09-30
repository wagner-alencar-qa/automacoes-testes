Feature: Login no Sauce Demo

  Scenario: Login com sucesso
    Given que o usuário acessa a página de login
    When informa "standard_user" e "secret_sauce"
    Then deve ser redirecionado para a página de produtos

  Scenario: Login com credenciais inválidas
    Given que o usuário acessa a página de login
    When informa "locked_out_user" e "secret_sauce"
    Then deve visualizar mensagem de erro
