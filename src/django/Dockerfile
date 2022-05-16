FROM alpine

ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN apk add --update --no-cache gcc musl-dev python3 python3-dev libpq-dev\
  && python -m ensurepip\
  && pip3 install --no-cache --upgrade pip setuptools -r requirements.txt

COPY . .

EXPOSE 8000
