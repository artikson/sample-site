FROM python:3.11-alpine AS compile-stage
RUN apk add  --no-cache linux-headers g++

COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-alpine
COPY --from=compile-stage /root/.local /root/.local
COPY . /app
WORKDIR /app

ENV PATH=/root/.local/bin:$PATH
CMD [ "uwsgi", "app.ini"]