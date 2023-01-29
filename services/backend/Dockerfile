FROM python:3.10.4-slim-bullseye as base

ENV VIRTUAL_ENV="/opt/venv" \
    POETRY_HOME="$HOME/pypoetry" \
    PATH="$PATH:$HOME/pypoetry/bin"

RUN apt update && apt upgrade -y \
    && apt install --no-install-recommends -y \
    curl \
    make \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version

FROM base as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR="/var/cache/pypoetry"

RUN python -m venv $VIRTUAL_ENV

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install

FROM base as stage

ENV POSTGRES_USER=${POSTGRES_USER} \
    POSTGRESS_PASSWORD=${POSTGRESS_PASSWORD} \
    POSTGRES_DB=${POSTGRES_DB} \
    POSTGRES_SERVER=${POSTGRES_SERVER} \
    VIRTUAL_ENV="/opt/venv" \
    PATH="/home/user/pypoetry/bin:$PATH"

RUN apt update && apt install -y make

WORKDIR /usr/local/src/backlog-tracker

RUN adduser --debug user && chown -R user:user ./

USER user

COPY --from=builder --chown=user:user /pypoetry/ /home/user/pypoetry/

COPY --from=builder --chown=user:user $VIRTUAL_ENV $VIRTUAL_ENV

COPY --chown=user:user ./ ./
