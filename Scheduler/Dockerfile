FROM python:3.7-alpine

WORKDIR $APP_PATH

COPY requirements.txt $APP_PATH

RUN apk add mysql-dev gcc alpine-sdk
RUN pip install -r requirements.txt
