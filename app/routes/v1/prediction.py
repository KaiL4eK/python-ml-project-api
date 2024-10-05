from fastapi import APIRouter, HTTPException

from app.models.prediction import (
    PredictionDataInput,
    PredictionResultResponse,
    PredictionStatus,
    PreditionStartSuccess,
)
from app.services.prediction import (
    get_async_predict_status_or_result,
    make_sync_predict,
    start_async_predict,
)

router = APIRouter()


@router.post("/synchronous")
def predict_sync(data: PredictionDataInput) -> PredictionResultResponse:
    if not data:
        raise HTTPException(status_code=404, detail="'data' argument invalid!")

    predict_data = make_sync_predict(data)

    return PredictionResultResponse(
        result=predict_data,
        status=PredictionStatus.COMPLETED,
    )


@router.post("/start")
def predict_start(data: PredictionDataInput) -> PreditionStartSuccess:
    if not data:
        raise HTTPException(status_code=404, detail="'data_input' argument invalid!")

    task_id = start_async_predict(data)

    return PreditionStartSuccess(task_id=task_id)


@router.get("/status/{task_id}")
def predict_status(task_id: str) -> PredictionResultResponse:
    response = get_async_predict_status_or_result(task_id)

    return response
