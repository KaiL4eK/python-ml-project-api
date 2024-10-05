#!/usr/bin/env bash

export PYTHONPATH=${PYTHONPATH}:"$(pwd)/app"
poetry run uvicorn main:app \
    --reload --port 5000 \
    --env-file .env \
    --reload-include python_ml_project_api/ \
    --use-colors
