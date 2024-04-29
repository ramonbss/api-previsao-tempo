# Projeto de Integração OpenWeather e Twitter

Este projeto é uma aplicação FastAPI que utiliza as APIs do OpenWeatherMap e do Twitter para postar automaticamente previsões do tempo para uma cidade específica no Twitter.

## Pré-requisitos

Antes de iniciar, certifique-se de que os seguintes projetos estão clonados e em execução localmente, pois este projeto depende deles:

- **Twitter API**: [https://github.com/ramonbss/twitter-api](https://github.com/ramonbss/twitter-api)
- **OpenWeather API**: [https://github.com/ramonbss/openweather-api](https://github.com/ramonbss/openweather-api)

Ambos os projetos devem estar configurados e rodando nas portas especificadas (`8001` para OpenWeather e `8002` para Twitter).

## Configuração

1. Clone este repositório:
   ```
   git clone https://github.com/ramonbss/api-previsao-tempo.git
   ```
1. Navegue até o diretório do projeto:
   ```
   cd api-previsao-tempo
   ```
1. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

## Executando a Aplicação
Para iniciar o servidor FastAPI, execute o seguinte comando:
```
uvicorn app.main:app --port 8000
```

## Uso
Para postar uma previsão do tempo no Twitter, envie uma requisição `GET` para o endpoint `/tuitar_previsoe`s com o parâmetro cidade especificando o nome da cidade desejada:
```
curl http://localhost:8000/tuitar_previsoes?cidade="Sao Paulo"
```