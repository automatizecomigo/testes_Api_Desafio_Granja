from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page

scenarios('../feature/api_patos_GET.feature')


@given("que a API de Patos está disponível")
def requisicao_API_patos_GET(browser: Page):
    browser.goto('http://127.0.0.1:8000/api/patos/')


@when('fizer uma requisição GET para "/api/patos/" a lista de patos deve ser retornada')
def lista_de_patos_com_status_200_ok(context):
    # Criando um novo contexto de navegação para a requisição HTTP
    browser = context.browser
    with browser.new_context() as ctx:
        response = ctx.request.get("http://127.0.0.1:8000/api/patos/")

        assert response.status == 200, f"Erro na requisição, status: {response.status}"

        clientes = response.json()

        print(f"Lista de clientes retornada: {clientes}")

        assert len(clientes) > 0, "Nenhum cliente foi retornado."


@then("a resposta deve ter o status 200")
def validacao_de_status(browser: Page):
    expect(browser.get_by_text('HTTP 200 OK', exact=True))








