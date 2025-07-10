FROM python:3.12-slim

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

ENV UV_PROJECT_ENVIRONMENT=/tmp/.venv

RUN uv sync --frozen

COPY . .

ENV PYTHONPATH="/app"

ENV PORT=8000

EXPOSE 8000

CMD ["litestar", "--app", "src.main:app", "run", "--host", "0.0.0.0", "--port", "8000"]
