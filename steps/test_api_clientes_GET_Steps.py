from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page

scenarios('../feature/api_clientes_GET.feature')


@given("que a API de clientes está disponível")
def requisicao_API_clientes_GET(browser: Page):
    browser.goto('http://127.0.0.1:8000/api/clientes/')


@when('fizer uma requisição GET para "/api/clientes/" a lista de clientes deve ser retornada')
def lista_de_clientes_com_status_200_ok(context):
    # Criando um novo contexto de navegação para a requisição HTTP
    browser = context.browser
    with browser.new_context() as ctx:
        response = ctx.request.get("http://127.0.0.1:8000/api/clientes/")

        assert response.status == 200, f"Erro na requisição, status: {response.status}"

        clientes = response.json()

        print(f"Lista de clientes retornada: {clientes}")

        assert len(clientes) > 0, "Nenhum cliente foi retornado."


@then("a resposta deve ter o status 200")
def step_impl(browser: Page):
    expect(browser.get_by_text('HTTP 200 OK', exact=True))








