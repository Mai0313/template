FROM python:3.9.15-slim

LABEL maintainer="Wei Lee <mai@mai0313.com>" \
    org.label-schema.name="app" \
    org.label-schema.vendor="Wei Lee" \
    org.label-schema.schema-version="1.0" \
    com.centurylinklabs.watchtower.stop-signal="SIGINT"

RUN apt-get -y update
RUN apt-get -y install ffmpeg libsm6 libxext6 libgl1 git

RUN python -m pip install --upgrade pip

WORKDIR /app
COPY . /app
EXPOSE 8080
RUN pip install -r requirements.txt
