FROM python:3.7-alpine

ENV APP_PATH /opt/apps/Scheduler

WORKDIR $APP_PATH

EXPOSE 8800

COPY requirements.txt $APP_PATH

RUN apk add mysql-dev gcc alpine-sdk
RUN pip install -r requirements.txt
