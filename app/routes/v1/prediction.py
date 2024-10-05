from fastapi import APIRouter, HTTPException

from models.prediction import PredictionDataInput, PredictionResultResponse, PredictionStatus, PredictionResultData
from services.prediction import make_sync_predict

router = APIRouter()


@router.post(
    "/sync",
    response_model=PredictionResultResponse,
)
def predict_sync(data: PredictionDataInput):
    if not data:
        raise HTTPException(status_code=404, detail="'data_input' argument invalid!")

    data_np = data.get_np_array()
    predict_value = make_sync_predict(data_np)

    return PredictionResultResponse(
        result=PredictionResultData(
            prediction=predict_value
        ),
        status=PredictionStatus.COMPLETED
    )



# @router.post("/start")
# def predict_start(data: PredictionDataInput) -> PreditionStartSuccess:
#     if not data:
#         raise HTTPException(status_code=404, detail="'data_input' argument invalid!")

#     data_np = data.get_np_array()


#     return {"task_id": ...}


# @router.get("/status/{task_id}")
# def predict_status(task_id: str) -> PredictionResultResponse:
