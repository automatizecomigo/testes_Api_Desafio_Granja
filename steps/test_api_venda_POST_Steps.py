from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page, expect
import json

scenarios('../feature/api_venda_POST.feature')


@given("que a API de vendas  está disponível")
def requisicao_API_vendas_POST(browser: Page):
    # Acessar a URL da API
    browser.goto('http://127.0.0.1:8000/api/vendas/')



@when('fizer uma requisição POST para "/api/vendas/"  deve ser retornada ultimo cadastro')
def lista_da_ultima_venda_com_status_201_ok(browser: Page):
    venda_data = {
        "data_venda": "2024-11-16T15:55:43.864027Z",
        "cliente": 'Cliente object (5)',
        "patos": 'Pato object (1)'
    }

    # Fazer a requisição POST
    response = browser.context.request.post(
        "http://127.0.0.1:8000/api/vendas/",
        data=json.dumps(venda_data),  # Enviar os dados como string JSON
        headers={"Content-Type": "application/json"}
    )

    # Verifique o status da resposta
    assert response.status == 201, f"Erro na requisição, status: {response.status}, corpo: {response.text}"

    # Obter a última venda cadastrada
    venda_cadastrada = response.json()
    print(f"Última venda cadastrada: {venda_cadastrada}")


@then("a resposta deve ter o status 201")
def validar_resposta_status_201_ok(browser: Page):
    expect(browser.get_by_text('HTTP 201 Created', exact=True))
