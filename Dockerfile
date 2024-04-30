FROM python:3.12-alpine
WORKDIR /api_integracao

COPY ./requirements.txt /api_integracao/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./tests /api_integracao/tests
COPY ./app /api_integracao/app

EXPOSE 8000

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]