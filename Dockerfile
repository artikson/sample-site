FROM python:3.11-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN apk add --no-cache gcc libc-dev linux-headers && \
    pip install -r requirements.txt

CMD [ "uwsgi", "app.ini" ]