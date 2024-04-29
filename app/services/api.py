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

    def tuitar_previsao_do_tempo(self, cidade: str):
        resposta_obter_previsao = self.obter_previsoes_de_tempo(cidade)
        if not resposta_obter_previsao["resultado"]:
            return self._retornar_erro(resposta_obter_previsao["data"])
        previsoes = resposta_obter_previsao["data"]
        texto_tuite = self._criar_texto_tuite(previsoes, cidade)

        resposta_postar_tuite = self.postar_tuite(texto_tuite)
        if not resposta_postar_tuite["resultado"]:
            return self._retornar_erro(resposta_postar_tuite["data"])
        return self._retornar_sucesso("Tuite criado com sucesso!")

    def _criar_texto_tuite(self, retorno_api_openweather, cidade: str):

        temperatura_atual = retorno_api_openweather["current"]["temp"]
        descricao_do_clima = retorno_api_openweather["current"]["weather"][0][
            "description"
        ]
        tuite = f"{temperatura_atual}°C e {descricao_do_clima} em {cidade} na data {datetime.now().strftime('%d/%m')}. "
        tuite += "Previsão próximos dias: "

        for dia in retorno_api_openweather["daily"][1:6]:
            temp_dia = dia["temp"]["day"]
            data = datetime.fromtimestamp(dia["dt"]).strftime("%d/%m")
            tuite += f"{temp_dia}°C on {data}, "

        tuite = tuite.rstrip(", ")
        return tuite

    def _retornar_resultado_servidor(self, resposta_requests):
        return {
            "resultado": 200 <= resposta_requests.status_code < 300,
            "data": resposta_requests.json(),
        }

    def _retornar_erro(self, mensagem):
        return {"status_code": 400, "mensagem_erro": mensagem}

    def _retornar_sucesso(self, mensagem):
        return {"status_code": 201, "mensagem": mensagem}
