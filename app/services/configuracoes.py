import os
from app.services.api import API_TUITE_PREVISOES


def configurar_variaveis_ambiente_se_dentro_container(
    api_tuite_previsoes: API_TUITE_PREVISOES,
):
    servidor_openweather = os.getenv("SERVIDOR_OPENWEATHER")
    servidor_twitter = os.getenv("SERVIDOR_TWITTER")

    if servidor_openweather:
        api_tuite_previsoes.setar_servidor_openweather(servidor_openweather)

    if servidor_twitter:
        api_tuite_previsoes.setar_servidor_twitter(servidor_twitter)
