from datetime import datetime
import requests


class API:
    _SERVER = "http://localhost"
    ENDPOINT_OPENWEATHER_API = f"{_SERVER}:8001/previsao_de_tempo"
    ENDPOINT_TWITTER_API = f"{_SERVER}:8002/tuitar_temperatura"

    def obter_previsoes_de_tempo(self, cidade: str):
        url = f"{self.ENDPOINT_OPENWEATHER_API}?cidade={cidade}"
        resposta = requests.get(url)
        return self._retornar_resultado_servidor(resposta)

    def postar_tuite(self, texto_tuite: str):
        payload = {"texto": texto_tuite}

        resposta = requests.post(self.ENDPOINT_TWITTER_API, json=payload)
        return self._retornar_resultado_servidor(resposta)

    def _retornar_resultado_servidor(self, resposta_requests):
        return {
            "resultado": 200 <= resposta_requests.status_code < 300,
            "data": resposta_requests.json(),
        }

    def _retornar_erro(self, mensagem):
        return {"status_code": 400, "mensagem_erro": mensagem}

    def _retornar_sucesso(self, mensagem):
        return {"status_code": 201, "mensagem": mensagem}
