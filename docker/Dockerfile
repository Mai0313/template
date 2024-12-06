ARG PYTHON_VERSION=3.10.14
FROM python:${PYTHON_VERSION}-slim as builder

LABEL maintainer="Wei Lee <mai@mai0313.com>" \
    org.label-schema.name="repo-template" \
    org.label-schema.vendor="Wei Lee" \
    org.label-schema.schema-version="1.0" \
    com.centurylinklabs.watchtower.stop-signal="SIGINT"

# Install git, Node.js, and other dependencies
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends git make curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install python packages
COPY ./docker/mirror/pip.conf /root/.pip/pip.conf
RUN git config --global http.sslVerify false && \
    python -m pip install --upgrade pip

########################################################################################

FROM builder as base
WORKDIR /base_env
COPY ./requirements.lock ./requirements.lock
RUN pip install -r ./requirements.lock && \
    pip cache purge

FROM builder as dev
WORKDIR /base_env
COPY ./requirements-dev.lock ./requirements-dev.lock
RUN pip install -r ./requirements-dev.lock && \
    pip cache purge

########################################################################################

FROM base as prod
WORKDIR /app
COPY . .
