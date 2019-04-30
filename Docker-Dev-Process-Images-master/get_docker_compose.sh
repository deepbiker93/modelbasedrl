#!/bin/bash

DOCKER_COMPOSE_VERSION=1.23.0
DOCKER_COMPOSE_PATH=${HOME}/bin/docker-compose

curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o ${DOCKER_COMPOSE_PATH}
chmod u+x ${DOCKER_COMPOSE_PATH}
docker-compose --version

