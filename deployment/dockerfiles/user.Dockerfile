FROM python:3.8.3-buster

ENV PYTHONBUFFERED=1 DEBIAN_FRONTEND=noninteractive

RUN mkdir /app
WORKDIR /app

COPY ./user/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
