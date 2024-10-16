Feature: Geração de Relatórios

  Scenario: Gerar relatório em Excel
    Given que a API de relatórios está disponível
    When fizer uma requisição GET para "/api/reports/excel/"
    Then a resposta do relatório Excel deve ter o status 200

  Scenario: Gerar relatório em PDF
    Given que a API de relatórios está disponível
    When fizer uma requisição GET para "/api/reports/pdf/"
    Then a resposta do relatório PDF deve ter o status 200
