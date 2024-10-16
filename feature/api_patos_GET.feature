Feature: Gerenciamento de Patos

  Scenario: Obter todos os Patos cadastrados
    Given que a API de Patos está disponível
    When fizer uma requisição GET para "/api/patos/" a lista de patos deve ser retornada
    Then a resposta deve ter o status 200