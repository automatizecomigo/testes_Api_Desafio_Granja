Feature: Gerenciamento de Clientes

  Scenario: Obter todos os clientes
    Given que a API de clientes está disponível
    When fizer uma requisição GET para "/api/clientes/" a lista de clientes deve ser retornada
    Then a resposta deve ter o status 200




