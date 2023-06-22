# syntax=docker/dockerfile:1

FROM python:3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt
RUN venv/bin/pip install --no-cache-dir gunicorn pymysql

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP=microblog.py

RUN chown -R microblog:microblog ./
USER microblog
EXPOSE 5000

CMD ["./boot.sh"]
