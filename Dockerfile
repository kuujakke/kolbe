FROM python:3-alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk --update --no-cache add build-base linux-headers postgresql-dev && \
pip install --no-cache-dir uwsgi && \
pip install --no-cache-dir -r requirements.txt\
&& apk del build-base linux-headers

COPY . /usr/src/app

EXPOSE 5000

ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:80", "--wsgi-file", "application.py", "--processes", "1", "--threads", "8", "--master"]
