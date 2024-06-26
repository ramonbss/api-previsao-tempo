import pytest
import requests_mock
from app.services.api import API_TUITE_PREVISOES


@pytest.fixture
def api():
    return API_TUITE_PREVISOES()


def testar_nome_servidor_openweather_preenchido(api):
    assert api.ENDPOINT_OPENWEATHER_API


def testar_nome_servidor_twitter_preenchido(api):
    assert api.ENDPOINT_TWITTER_API


def test_obter_previsoes_de_tempo_successo(api):
    cidade = "Salvador"
    with requests_mock.Mocker() as mocker:
        mocker.get(
            api.ENDPOINT_OPENWEATHER_API,
            json={
                "current": {"temp": 27, "weather": [{"description": "céu com nuvens"}]},
                "daily": [{"dt": 1608412800, "temp": {"day": 28}}],
            },
            status_code=200,
        )

        resposta = api.obter_previsoes_de_tempo(cidade)

        assert resposta["resultado"] is True
        assert "data" in resposta
        assert resposta["data"]["current"]["temp"] == 27


def test_obter_previsoes_de_tempo_falha(api):
    cidade = "CidadeInexistente"
    with requests_mock.Mocker() as mocker:
        mocker.get(
            api.ENDPOINT_OPENWEATHER_API,
            json={
                "detail": f"Erro ao obter previsão para a cidade: {cidade}",
                "status_code": 400,
            },
            status_code=400,
        )

        resposta = api.obter_previsoes_de_tempo(cidade)

        assert resposta["resultado"] is False
        assert "data" in resposta
        assert cidade in resposta["data"]["detail"]


def test_postar_tuite_successo(api):
    texto_tuite = "Tuite com as previsoes de tempo;"
    with requests_mock.Mocker() as mocker:
        mocker.post(
            api.ENDPOINT_TWITTER_API,
            json={"resultado": True, "data": "Tuite criado com sucesso!"},
            status_code=201,
        )

        resposta = api.postar_tuite(texto_tuite)

        assert resposta["resultado"] is True
        assert resposta["data"]["data"] == "Tuite criado com sucesso!"


def test_postar_tuite_falha(api):
    texto_tuite = "Tuite com falha"
    with requests_mock.Mocker() as mocker:
        mocker.post(
            api.ENDPOINT_TWITTER_API,
            json={
                "title": "Unauthorized",
                "type": "about:blank",
                "status": 401,
                "detail": "Unauthorized",
            },
            status_code=401,
        )

        resposta = api.postar_tuite(texto_tuite)

        assert resposta["resultado"] is False
        assert "data" in resposta


def test_tuitar_previsao_do_tempo_successo(api):
    cidade = "Salvador"
    with requests_mock.Mocker() as mocker:
        mocker.get(
            api.ENDPOINT_OPENWEATHER_API,
            json={
                "lat": -12.9822,
                "lon": -38.4813,
                "timezone": "America/Bahia",
                "current": {
                    "dt": 1714354666,
                    "temp": 27.85,
                    "clouds": 40,
                    "weather": [
                        {"id": 802, "main": "Nuvens", "description": "nuvens dispersas"}
                    ],
                },
                "daily": [
                    {"dt": 1714312800, "temp": {"day": 28.73}},
                    {"dt": 1714399201, "temp": {"day": 27.34}},
                    {"dt": 1714399202, "temp": {"day": 27.37}},
                    {"dt": 1714399203, "temp": {"day": 27.38}},
                    {"dt": 1714399204, "temp": {"day": 27.39}},
                    {"dt": 1714399205, "temp": {"day": 27.40}},
                ],
            },
        )

        mocker.post(
            api.ENDPOINT_TWITTER_API,
            json={"resultado": True, "data": "Tuite criado com sucesso!"},
        )

        resposta_tuitar_previsao = api.tuitar_previsao_do_tempo(cidade)

        assert resposta_tuitar_previsao["status_code"] == 201
        assert resposta_tuitar_previsao["mensagem"] == "Tuite criado com sucesso!"


def test_tuitar_previsao_do_tempo_falha(api):
    cidade = "CidadeInexistente"
    with requests_mock.Mocker() as mocker:
        mocker.get(
            api.ENDPOINT_OPENWEATHER_API,
            status_code=400,
            json={
                "detail": f"Erro ao obter previsão para a cidade: {cidade}",
                "status_code": 400,
            },
        )

        response = api.tuitar_previsao_do_tempo(cidade)

        assert response["status_code"] == 400
        assert "mensagem_erro" in response
