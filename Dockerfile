# syntax=docker/dockerfile:1

###########
# BASE
###########

FROM python:3.12-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # PIP
    \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # POETRY
    \
    POETRY_VERSION=1.3.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    # PATH
    \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

###########
# BUILDER
###########

FROM base as builder
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

RUN --mount=type=cache,target=/root/.cache \
    curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN --mount=type=cache,target=/root/.cache \
    poetry install --without=dev --no-ansi --no-root --no-interaction

#############
# PRODUCTION
#############

FROM base

COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH
COPY . /app/
WORKDIR /app
ENTRYPOINT gunicorn website.wsgi -b 0.0.0.0:$PORT