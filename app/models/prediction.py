
from typing import Optional
from pydantic import BaseModel
from enum import Enum

import numpy as np


def PredictionDataInput(BaseModel):
    feature1: float
    feature2: float

    def get_np_array(self):
        return np.array(
            [
                [
                    self.feature1,
                    self.feature2,
                ]
            ]
        )


def PredictionResultData(BaseModel):
    prediction: int


def PredictionErrorData(BaseModel):
    msg: str



def PreditionStartSuccess(BaseModel):
    task_id: str


def PredictionStatus(Enum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"



def PredictionResultResponse(BaseModel):
    result: Optional[PredictionResultData]
    error: Optional[PredictionErrorData]
    status: PredictionStatus
