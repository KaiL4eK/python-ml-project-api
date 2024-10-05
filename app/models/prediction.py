from enum import Enum

import numpy as np
from pydantic import BaseModel, Field


class PredictionDataInput(BaseModel):
    feature1: float = Field(examples=[1.0])
    feature2: float = Field(examples=[2.0])

    def get_np_array(self):
        return np.array(
            [
                [
                    self.feature1,
                    self.feature2,
                ],
            ],
        )


class PredictionResultData(BaseModel):
    prediction: int


class PredictionErrorData(BaseModel):
    msg: str


class PreditionStartSuccess(BaseModel):
    task_id: str


class PredictionStatus(Enum):
    UNKNOWN = "UNKNOWN"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class PredictionResultResponse(BaseModel):
    result: PredictionResultData | None = None
    error: PredictionErrorData | None = None
    status: PredictionStatus
