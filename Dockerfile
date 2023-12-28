FROM python:3.12

WORKDIR /app
RUN pip install poetry

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

RUN poetry install --compile

ENTRYPOINT poetry run gunicorn website.wsgi -b 0.0.0.0:$PORT
