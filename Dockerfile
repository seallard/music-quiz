FROM python:3.12-alpine

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

RUN addgroup -S appgroup && adduser -S app_user -G appgroup
USER app_user

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
