from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page, expect

scenarios('../feature/api_reports_GET.feature')


@given("que a API de relatórios está disponível")
def requisicao_API_relatorios_GET(browser: Page):
    # O cenário acessa a URL base da API de relatórios
    browser.goto('http://localhost:8000/api/reports/excel/')


@when('fizer uma requisição GET para "/api/reports/excel/"')
def requisicao_relatorio_excel(browser: Page):
    # Fazer a requisição GET para o relatório Excel
    response = browser.context.request.get("http://localhost:8000/api/reports/excel/")

    # Verifica se o arquivo baixado tem o formato Excel
    assert response.status == 200, f"Erro na requisição Excel, status: {response.status}"
    assert response.headers["Content-Type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", \
        f"Tipo de conteúdo inesperado para Excel: {response.headers['Content-Type']}"


@when('fizer uma requisição GET para "/api/reports/pdf/"')
def requisicao_relatorio_pdf(browser: Page):
    # Fazer a requisição GET para o relatório PDF
    response = browser.context.request.get("http://localhost:8000/api/reports/pdf/")

    # Verifica se o arquivo baixado tem o formato PDF
    assert response.status == 200, f"Erro na requisição PDF, status: {response.status}"
    assert response.headers["Content-Type"] == "application/pdf", \
        f"Tipo de conteúdo inesperado para PDF: {response.headers['Content-Type']}"


@then("a resposta do relatório Excel deve ter o status 200")
def validacao_relatorio_excel(browser: Page):
    # O formato do arquivo Excel foi validado no passo anterior
    pass


@then("a resposta do relatório PDF deve ter o status 200")
def validacao_relatorio_pdf(browser: Page):
    # O formato do arquivo PDF foi validado no passo anterior
    pass
