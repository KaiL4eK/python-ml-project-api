#!/usr/bin/env bash

poetry run uvicorn app.main:app \
    --reload --port 5000 \
    --env-file .env.local \
    --reload-include python_ml_project_api/ \
    --use-colors \
    --log-config config/local/log_config.yaml
