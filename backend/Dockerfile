FROM python:3.10.12-alpine3.18

LABEL maintainer="Pratik"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /backend


RUN apk add --no-cache \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev git

RUN pip install -U pip
RUN pip install psycopg2


COPY data/ data/
WORKDIR /backend
COPY . /backend

RUN pip install --no-cache-dir -r requirements/dev.txt


CMD python3 manage.py runserver 0.0.0.0:8000