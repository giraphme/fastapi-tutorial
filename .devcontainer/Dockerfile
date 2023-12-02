FROM python:3.12

ENV PATH /root/.local/bin:$PATH

RUN apt-get update \
  && curl -sSL https://install.python-poetry.org | python - \
  && poetry config virtualenvs.create false

COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN poetry install
COPY . .
