from fastapi import APIRouter, HTTPException
from app.services.api import API_TUITE_PREVISOES

api_router = APIRouter()
api_tuite_previsoes = API_TUITE_PREVISOES()


@api_router.get("/tuitar_previsoes")
def previsao_de_tempo(cidade: str):
    try:
        resposta = api_tuite_previsoes.tuitar_previsao_do_tempo(cidade)
        return resposta
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
