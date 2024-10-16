Feature: Gerenciamento de Patos

  Scenario: Obter todos os patos
    Given que a API de clientes está disponível
    When fizer uma requisição POST para "/api/patos/"  deve ser retornada ultimo cadastro
    Then a resposta deve ter o status 201