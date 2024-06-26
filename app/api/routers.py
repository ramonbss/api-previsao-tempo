from fastapi import APIRouter, HTTPException
from app.services.api import API_TUITE_PREVISOES
from app.services.configuracoes import configurar_variaveis_ambiente_se_dentro_container

api_router = APIRouter()
api_tuite_previsoes = API_TUITE_PREVISOES()

configurar_variaveis_ambiente_se_dentro_container(api_tuite_previsoes)


@api_router.get("/tuitar_previsoes")
def previsao_de_tempo(cidade: str):
    try:
        resposta = api_tuite_previsoes.tuitar_previsao_do_tempo(cidade)
        return resposta
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
