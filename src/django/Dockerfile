FROM alpine

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN apk add --update --no-cache gcc musl-dev python3 python3-dev libpq-dev\
  && ln -sf python3 /usr/bin/python\
  && python3 -m ensurepip\
  && pip3 install --no-cache --upgrade pip setuptools\
  && pip3 install --no-cache --upgrade -r requirements.txt

COPY . .

EXPOSE 8000
