#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload --log-config config/log_config.yaml
