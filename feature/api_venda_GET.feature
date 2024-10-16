Feature: Gerenciamento de Vendas

  Scenario: Obter todos as Vendas realizadas
    Given que a API de vendas está disponível
    When fizer uma requisição GET para "/api/vendas/" exibir a lista de vendas realizadas
    Then a resposta deve ter o status 200