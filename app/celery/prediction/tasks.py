from time import sleep

import numpy as np
from celery import Task

from app.celery import app
from app.models.prediction import PredictionStatus
from python_ml_project_api.prediction import predict


# bind=True - adds `self` argument to reach task instance
@app.task(acks_late=True, bind=True, track_started=True)
def predict_task(self: Task, data: dict[str, float]) -> int:
    stages = ["preprocessing", "make prediction", "postprocessing", "formatting"]

    for i, stage in enumerate(stages):
        sleep(5)
        # Optional, you can access it through result.info property
        self.update_state(
            # .value - to make it serializable
            state=PredictionStatus.RUNNING.value,
            meta={
                "process_percent": (i + 1) * 25,
                "stage": stage,
            },
        )
    data_np = np.array([data["feature1"], data["feature2"]])
    predict_result = predict(data_np)
    return predict_result
