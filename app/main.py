import logging

from fastapi import FastAPI

from app.core.settings import ServerSettings
from app.routes.v1 import api as api_v1

logger = logging.getLogger(__name__)

settings = ServerSettings()  # type: ignore[call-arg]

app = FastAPI(root_path=settings.root_path)
app.mount("/v1", api_v1)
