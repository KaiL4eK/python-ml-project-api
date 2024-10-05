import numpy as np

from worker.prediction import predict

def make_sync_predict(data: np.ndarray) -> int:
    result_predict = predict(data=data)
    return result_predict


def predict_start(data: np.ndarray) -> str:
    task_info = predict.delay(data=data)
    return task_info.id
