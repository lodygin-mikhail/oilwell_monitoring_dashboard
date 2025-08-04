FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем скрипты и данные (но данные монтируются через volumes)
COPY scripts/ ./scripts/