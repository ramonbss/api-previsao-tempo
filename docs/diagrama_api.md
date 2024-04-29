```mermaid
graph TD
    client[("Client\n(Requisição HTTP)")]
    api[("/tuitar_previsoes\n(FastAPI Endpoint)")]
    sdk_openweather[("OpenWeather SDK\n/previsao_de_tempo")]
    sdk_twitter[("Twitter SDK\n/tuitar_temperatura")]
    openweather[("OpenWeather API")]
    twitter[("Twitter API")]

    client --> api
    api --> sdk_openweather
    api --> sdk_twitter
    sdk_openweather --> openweather
    sdk_twitter --> twitter

```    