#!/usr/bin/env bash

docker compose \
    -f docker/docker-compose.yaml \
    -f docker/docker-compose.dev.yaml \
    up --build
