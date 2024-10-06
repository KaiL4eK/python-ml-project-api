import logging

from celery.states import PENDING

from app.celery import get_async_result
from app.celery.prediction.tasks import predict_task
from app.models.prediction import (
    PredictionDataInput,
    PredictionErrorData,
    PredictionResultData,
    PredictionResultResponse,
    PredictionStatus,
)
from python_ml_project_api.prediction import predict

logger = logging.getLogger(__name__)


def make_sync_predict(data: PredictionDataInput) -> PredictionResultData:
    data_np = data.get_np_array()
    predict_result = predict(data=data_np)
    return PredictionResultData(prediction=predict_result)


def start_async_predict(data: PredictionDataInput) -> str:
    # The data we transfer to worker has to be serializable
    # Se we just transform them into simple objects
    data_ser = data.model_dump()
    task_info = predict_task.delay(data=data_ser)
    return str(task_info.id)


def get_async_predict_status_or_result(task_id: str) -> PredictionResultResponse:
    result = get_async_result(task_id)
    response = PredictionResultResponse(status=PredictionStatus.RUNNING)

    if result.state == PENDING:
        # In case `task_if is incorrect` Celery still return PENDING state
        response.status = PredictionStatus.UNKNOWN
        return response

    if result.ready():
        if result.successful():
            result_raw_data = result.get()
            response.status = PredictionStatus.COMPLETED
            response.result = PredictionResultData(prediction=result_raw_data)
        else:
            response.status = PredictionStatus.FAILED
            response.error = PredictionErrorData(msg=result.traceback)

    return response
