FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv

RUN uv sync --frozen

COPY src ./src

CMD ["uv", "run", "python", "src/scraper/main.py"]