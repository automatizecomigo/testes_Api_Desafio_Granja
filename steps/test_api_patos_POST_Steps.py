from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page, expect
import json

scenarios('../feature/api_patos_POST.feature')


@given("que a API de clientes está disponível")
def requisicao_API_patos_POST(browser: Page):
    # Acessar a URL da API
    browser.goto('http://127.0.0.1:8000/api/clientes/')



@when('fizer uma requisição POST para "/api/patos/"  deve ser retornada ultimo cadastro')
def lista_do_ultimo_pato_com_status_201_ok(browser: Page):

    cliente_data = {
        "nome": "pato_donalds_black",
        "filhos":"5",
        "mae":"1"

    }

    # Fazer a requisição POST
    response = browser.context.request.post(
        "http://127.0.0.1:8000/api/patos/",
        data=json.dumps(cliente_data),  # Enviar os dados como string JSON
        headers={"Content-Type": "application/json"}
    )

    assert response.status == 201, f"Erro na requisição, status: {response.status}"

    # Obter o último cliente cadastrado
    cliente_cadastrado = response.json()
    print(f"Último cliente cadastrado: {cliente_cadastrado}")


@then("a resposta deve ter o status 201")
def validar_resposta_status_201_ok(browser: Page):
    expect(browser.get_by_text('HTTP 201 Created', exact=True))
