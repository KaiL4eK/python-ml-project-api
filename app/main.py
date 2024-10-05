import os
import logging
from threading import Thread
from typing import Dict

from fastapi import FastAPI

from app.worker.celery_main import app as celery_app
from settings import ServerSettings
from app.routes.v1 import api as api_v1



log = logging.getLogger(__name__)

settings = ServerSettings()

app = FastAPI(root_path=settings.root_path)

app.mount("/v1", api_v1)
