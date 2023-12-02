FROM python:3.12

ENV PATH /root/.local/bin:$PATH
WORKDIR /app

RUN apt-get update \
  && curl -sSL https://install.python-poetry.org | python - \
  && poetry config virtualenvs.create false

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock
RUN poetry install
COPY . .
