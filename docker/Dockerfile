FROM python:3.10.14

LABEL maintainer="Wei Lee <mai@mai0313.com>" \
    org.label-schema.name="repo-template" \
    org.label-schema.vendor="Wei Lee" \
    org.label-schema.schema-version="1.0" \
    com.centurylinklabs.watchtower.stop-signal="SIGINT"

# Install git
RUN apt-get -y update && apt-get install -y \
    git \
    make \
    && rm -rf /var/lib/apt/lists/*
RUN git config --global http.sslVerify false

# Install python packages
COPY ./docker/mirror/pip.conf /root/.pip/pip.conf
RUN python -m pip install --upgrade pip

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt -U && pip cache purge
