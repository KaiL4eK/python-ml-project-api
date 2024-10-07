#!/usr/bin/env bash

set -o errexit
set -o nounset

celery -A app.celery.app worker --loglevel=info
