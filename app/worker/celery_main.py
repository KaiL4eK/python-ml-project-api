import logging

from constants import CELERY_PREDICT_TASK_NAME
from settings import CelerySettings

from celery import Celery

logger = logging.getLogger(__name__)

settings = CelerySettings()

logger.info(settings)

app = Celery(
    "worker",
    backend=settings.backend,
    broker=settings.broker
)
app.conf.task_routes = {
    CELERY_PREDICT_TASK_NAME: {"queue": "predict"}
}

app.conf.update(task_track_started=True)
