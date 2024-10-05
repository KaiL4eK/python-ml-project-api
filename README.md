# Project README! Here we go!

<div align="center">

[![PythonSupported](https://img.shields.io/badge/python-3.9-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)

Awesome `python-ml-project-api` project!

This is sample ML Project API using [fastapi](https://fastapi.tiangolo.com/) and [celery](https://docs.celeryq.dev/en/stable/) based on [redis](https://redis.io/).

> In case of license issues with redis you can replace it with [dragonfly](https://github.com/dragonflydb/dragonfly).

</div>

- [Project README! Here we go!](#project-readme-here-we-go)
  - [Repository contents](#repository-contents)
  - [System requirements](#system-requirements)
  - [How to run server](#how-to-run-server)
    - [Local run](#local-run)

## Repository contents

- [docs](docs) - documentation of the project
- [reports](reports) - reports generated (as generated from notebooks)
  > Check if you need to ignore large reports or keep them in Git LFS
- [configs](configs) - configuration files directory
- [notebooks](notebooks) - directory for `jupyter` notebooks
- [tests](tests) - project tasts based on [pytest](https://docs.pytest.org/en/stable/)
- [scripts](scripts) - repository service scripts
  > These ones are not included into the pakckage if you build one - these scripts are only for usage with repository
- [python_ml_project_api](python_ml_project_api) - source files of the project
- [.editorconfig](.editorconfig) - configuration for [editorconfig](https://editorconfig.org/)
- [.gitignore](.gitignore) - the files/folders `git` should ignore
- [.pre-commit-config.yaml](.pre-commit-config.yaml) - [pre-commit](https://pre-commit.com/) configuration file
- [README.md](README.md) - the one you read =)
- [DEVELOPMENT.md](DEVELOPMENT.md) - guide for development team
- [Makefile](Makefile) - targets for `make` command
- [cookiecutter-config-file.yml](cookiecutter-config-file.yml) - cookiecutter project config log
- [poetry.toml](poetry.toml) - poetry local config
- [pyproject.toml](pyproject.toml) - Python project configuration
- [.env.example](.env.example) - Example of `.env` file, some rules:
  - > [!WARNING]
    > Don't store credential in examples, fill real credentials in `.env` file itself
  - Use longer names to understand relations between envs and services

## System requirements

- Python version: 3.9
- Operating system: Ubuntu or WSL
- Poetry version defined in [poetry.version](poetry.version)

> We tested on this setup - you can try other versions or operation systems by yourself!

## How to run server

### Docker run

- Create `.env` file from [`.env.example`](.env.example)
- Run app in docker mode
```bash
make app-docker-start-dev
```

> Dev mode (`-dev` suffix) contains `--reload` in script and override of volumes in compose so you can edit files on your machine and service inside container will reload

> Server is exposed on 8080 port

> Swagger URL http://127.0.0.1:8080/api/v1/docs

### Local run

> This way you can run server itself on your machine on port 5000

- Create `.env.local` file from [`.env.example`](.env.example)
  - It has to contain addresses of `localhost` instead of `redis` as we are going to connect outside Docker network
- Run locally main process
```bash
make app-start
```
- [Optionally] Run Redis and Worker processes in docker in another terminal
```bash
make app-docker-start-dev
```
