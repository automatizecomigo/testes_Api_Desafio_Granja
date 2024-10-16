Feature: Gerenciamento de Clientes

  Scenario: Obter todos os clientes
    Given que a API de clientes está disponível
    When fizer uma requisição POST para "/api/clientes/"  deve ser retornada ultimo cadastro
    Then a resposta deve ter o status 201