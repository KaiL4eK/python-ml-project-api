from time import sleep
import numpy as np
from celery import current_task

from models.prediction import PredictionStatus

from .celery_main import app


@app.task(acks_late=True)
def predict(data: np.array) -> int:
    stages = [
        "preprocessing",
        "make prediction",
        "postprocessing",
        "formatting"
    ]

    for i, stage in enumerate(stages):
        sleep(1)
        current_task.update_state(
            state=PredictionStatus.RUNNING,
            meta={
                "process_percent": (i+1)*25,
                "stage": stage
            }
        )
    return np.sum(data).astype(int)
