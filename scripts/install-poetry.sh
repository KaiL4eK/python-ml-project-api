#!/usr/bin/env bash

poetry_version=$(cat poetry.version)

echo "Installing poetry==$poetry_version"

pip install poetry==$poetry_version
