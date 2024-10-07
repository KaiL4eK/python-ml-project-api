import logging

from celery import Celery
from celery.result import AsyncResult

from app.core.settings import CelerySettings

logger = logging.getLogger(__name__)

settings = CelerySettings()  # type: ignore[call-arg]

app = Celery(backend=settings.backend, broker=settings.broker)
# Don't forget to register your new tasks
#   Modules with name `tasks.py` are detected
app.autodiscover_tasks(["app.celery.prediction"])


def get_async_result(task_id: str) -> AsyncResult:
    result = app.AsyncResult(id=task_id)
    return result
