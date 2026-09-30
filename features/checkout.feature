Feature: Checkout no Sauce Demo

  Scenario: Compra completa com sucesso
    Given que o usuário está logado
    And adiciona um produto ao carrinho
    When conclui o checkout com dados válidos
    Then deve visualizar a confirmação da compra
