from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page

scenarios('../feature/api_venda_GET.feature')


@given("que a API de vendas está disponível")
def requisicao_API_clientes_GET(browser: Page):
    browser.goto('http://127.0.0.1:8000/api/vendas/')


@when('fizer uma requisição GET para "/api/vendas/" exibir a lista de vendas realizadas')
def lista_de_vendas_com_status_200_ok(context):
    # Criando um novo contexto de navegação para a requisição HTTP
    browser = context.browser
    with browser.new_context() as ctx:
        response = ctx.request.get("http://127.0.0.1:8000/api/vendas/")

        assert response.status == 200, f"Erro na requisição, status: {response.status}"

        vendas = response.json()

        print(f"Lista de clientes retornada: {vendas}")

        assert len(vendas) > 0, "Nenhum cliente foi retornado."


@then("a resposta deve ter o status 200")
def step_impl(browser: Page):
    expect(browser.get_by_text('HTTP 200 OK', exact=True))








