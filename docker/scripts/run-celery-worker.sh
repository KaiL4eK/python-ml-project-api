#!/usr/bin/env bash

set -o errexit
set -o nounset

celery -A app.worker.app worker --loglevel=info
