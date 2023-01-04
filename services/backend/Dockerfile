FROM python:3.10.4-slim-bullseye

ARG POSTGRES_USER \
    POSTGRES_SERVER \
    POSTGRES_DB \
    POSTGRESS_PASSWORD 

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.2.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.local/bin" \
    POSTGRES_USER=${POSTGRES_USER} \
    POSTGRESS_PASSWORD=${POSTGRESS_PASSWORD} \
    POSTGRES_DB=${POSTGRES_DB} \
    POSTGRES_SERVER=${POSTGRES_SERVER}

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    curl \
    make \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version

WORKDIR /code

COPY poetry.lock pyproject.toml /code/

COPY . /code/

RUN poetry install --without db




