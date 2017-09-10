FROM python:3-alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

RUN apk --update --no-cache add build-base linux-headers && pip install --no-cache-dir uwsgi && apk del build-base linux-headers

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:80", "--module", "app:app", "--processes", "1", "--threads", "8"]
