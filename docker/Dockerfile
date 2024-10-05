FROM python:3.9.0

# Disable buffering - instant show logs instantly
ENV PYTHONUNBUFFERED 1
# Disable writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Install system depdendencies
RUN apt-get update \
  # Additional dependencies
  && apt-get install -y make \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# If you have so many dependencies - better look into requirements installation
COPY poetry.lock pyproject.toml scripts/install_poetry.sh ./
RUN pip install --upgrade pip && \
    bash install_poetry.sh && \
    poetry config virtualenvs.create false && \
    poetry install --only main

COPY ./app/ ./
COPY ./python_ml_project_api/ ./python_ml_project_api/

# Find code from app directory
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Copy runtime scripts into root
COPY ./docker/scripts/ /

# Define port that is exposed
EXPOSE 8080
CMD uvicorn main:app --host 0.0.0.0 --port 8080
