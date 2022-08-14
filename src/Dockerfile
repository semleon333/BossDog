FROM python:3.9.12-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN apk add --update --no-cache gcc musl-dev libpq-dev
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools -r requirements.txt

COPY . .

EXPOSE 8000
