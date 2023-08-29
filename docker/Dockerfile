# Etapa de construcción
FROM python:3.9-alpine AS build

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# Etapa de ejecución
FROM python:3.9-alpine

WORKDIR /app

# Copia solo lo necesario desde la etapa de construcción
COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=build /app/ /app/

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]