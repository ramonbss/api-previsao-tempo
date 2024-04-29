import pytest
import requests_mock
from app.services.api import API


@pytest.fixture
def api():
    return API()


def test_obter_previsoes_de_tempo_success(api):
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


def test_obter_previsoes_de_tempo_failure(api):
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
