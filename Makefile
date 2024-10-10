#* Variables
SHELL := /usr/bin/env bash
PYTHON ?= python3

#* Initialization
.PHONY: project-init
project-init: poetry-install tools-install mypy-install

.PHONY: poetry-install
poetry-install:
	poetry install -n

.PHONY: poetry-lock-update
poetry-lock-update:
	poetry lock --no-update

.PHONY: poetry-export
poetry-export:
	poetry lock -n && poetry export --without-hashes > requirements.txt

.PHONY: poetry-export-dev
poetry-export-dev:
	poetry lock -n && poetry export --with dev --without-hashes > requirements.dev.txt

#* Tools
.PHONY: tools-install
tools-install:
	poetry run pre-commit install --hook-type prepare-commit-msg --hook-type pre-commit

.PHONY: pre-commit-update
pre-commit-update:
	poetry run pre-commit autoupdate

.PHONY: pre-commit-run-all
pre-commit-run-all:
	poetry run pre-commit run --all-files

#* Notebooks
.PHONY: nbextention-toc-install
nbextention-toc-install:
	poetry run jupyter contrib nbextension install --user
	poetry run jupyter nbextension enable toc2/main

#* Tests
.PHONY: tests
tests:
	poetry run pytest -c pyproject.toml tests

#* Linting
.PHONY: mypy-install
mypy-install:
	poetry run mypy --install-types --non-interactive ./

.PHONY: mypy
mypy:
	poetry run mypy --config-file pyproject.toml ./

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	find . | grep -E "(.ipynb_checkpoints$$)" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: clean-all
clean-all: pycache-remove build-remove

#* Service targets
.PHONY: grep-todos
grep-todos:
	git grep -EIn "TODO|FIXME|XXX"

#* Application targets
.PHONY: app-start
app-start:
	bash scripts/app-local-start.sh

#* Docker targets
.PHONY: app-docker-build
app-docker-build:
	docker compose \
		--env-file .env \
		-f docker/docker-compose.yaml \
		build

.PHONY: app-docker-start
app-docker-start: app-docker-build
	docker compose \
		--env-file .env \
		-f docker/docker-compose.yaml \
		up

.PHONY: app-docker-start-dev
app-docker-start-dev: app-docker-build
	docker compose \
		--env-file .env \
		-f docker/docker-compose.yaml \
		-f docker/docker-compose.dev.yaml \
		up
