FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH="/app"
ENV PORT=8000
EXPOSE 8000

CMD ["litestar", "--app", "src.main:app", "run", "--host", "0.0.0.0", "--port", "8000"]
