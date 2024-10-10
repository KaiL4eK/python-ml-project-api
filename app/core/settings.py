from pydantic import Field
from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    root_path: str = Field("/api", alias="API_ROOT")


class CelerySettings(BaseSettings):
    backend: str = Field(
        "redis://redis:6379/0",
        alias="CELERY_BROKER_URL",
    )
    broker: str = Field(
        "redis://redis:6379/0",
        alias="CELERY_RESULT_BACKEND",
    )
