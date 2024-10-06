from pydantic import Field
from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    root_path: str = Field("/api", alias="ML_API_SERVER_API_ROOT")


class CelerySettings(BaseSettings):
    backend: str = Field(
        "redis://redis:6379/0",
        alias="ML_API_SERVER_CELERY_BROKER_URL",
    )
    broker: str = Field(
        "redis://redis:6379/0",
        alias="ML_API_SERVER_CELERY_RESULT_BACKEND",
    )
